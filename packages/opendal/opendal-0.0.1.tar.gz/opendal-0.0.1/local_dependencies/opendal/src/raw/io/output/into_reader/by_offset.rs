// Copyright 2022 Datafuse Labs.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

use std::cmp;
use std::future::Future;
use std::io;
use std::io::Error;
use std::io::ErrorKind;
use std::io::SeekFrom;
use std::pin::Pin;
use std::sync::Arc;
use std::task::Context;
use std::task::Poll;

use futures::future::BoxFuture;
use futures::ready;
use futures::AsyncRead;
use tokio::io::ReadBuf;

use crate::raw::*;
use crate::*;

/// Convert given reader into seekable reader by offset.
///
/// # Notes
///
/// This operation is not zero cost. If the accessor already returns a
/// seekable reader, please don't use this.
pub fn by_offset(acc: Arc<dyn Accessor>, path: &str, offset: u64) -> OffsetReader {
    OffsetReader {
        acc,
        path: path.to_string(),
        offset,
        size: None,
        cur: 0,
        state: State::Idle,
        last_seek_pos: None,
        sink: Vec::new(),
    }
}

/// OffsetReader that can do seek on non-seekable reader.
pub struct OffsetReader {
    acc: Arc<dyn Accessor>,
    path: String,

    offset: u64,
    size: Option<u64>,
    cur: u64,
    state: State,

    /// Seek operation could return Pending which may lead
    /// `SeekFrom::Current(off)` been input multiple times.
    ///
    /// So we need to store the last seek pos to make sure
    /// we always seek to the right position.
    last_seek_pos: Option<u64>,
    /// sink is to consume bytes for seek optimize.
    sink: Vec<u8>,
}

enum State {
    Idle,
    Stating(BoxFuture<'static, Result<RpStat>>),
    Sending(BoxFuture<'static, Result<(RpRead, output::Reader)>>),
    Reading(output::Reader),
}

/// Safety: State will only be accessed under &mut.
unsafe impl Sync for State {}

impl OffsetReader {
    fn read_future(&self) -> BoxFuture<'static, Result<(RpRead, output::Reader)>> {
        let acc = self.acc.clone();
        let path = self.path.clone();
        let op = OpRead::default().with_range(BytesRange::new(
            Some(self.offset + self.cur),
            self.size.map(|v| v - self.cur),
        ));

        let fut = async move { acc.read(&path, op).await };

        Box::pin(fut)
    }

    fn stat_future(&self) -> BoxFuture<'static, Result<RpStat>> {
        let acc = self.acc.clone();
        let path = self.path.clone();

        let fut = async move { acc.stat(&path, OpStat::default()).await };

        Box::pin(fut)
    }
}

impl output::Read for OffsetReader {
    fn poll_read(&mut self, cx: &mut Context<'_>, buf: &mut [u8]) -> Poll<io::Result<usize>> {
        match &mut self.state {
            State::Idle => {
                if let Some(size) = self.size {
                    if self.cur >= size {
                        return Poll::Ready(Ok(0));
                    }
                }

                self.state = State::Sending(self.read_future());
                self.poll_read(cx, buf)
            }
            State::Sending(fut) => {
                let (rp, r) = ready!(Pin::new(fut).poll(cx))?;
                let meta = rp.into_metadata();

                self.size = Some(meta.content_length() + self.cur);
                self.state = State::Reading(r);
                self.poll_read(cx, buf)
            }
            State::Reading(r) => match ready!(Pin::new(r).poll_read(cx, buf)) {
                Ok(n) if n == 0 => {
                    // Reset state to Idle after all data has been consumed.
                    self.state = State::Idle;
                    Poll::Ready(Ok(0))
                }
                Ok(n) => {
                    self.cur += n as u64;
                    Poll::Ready(Ok(n))
                }
                Err(e) => {
                    self.state = State::Idle;
                    Poll::Ready(Err(e))
                }
            },
            State::Stating(_) => {
                // It's impossible for us to go into this state while
                // poll_read. We can just drop this future.
                self.state = State::Idle;
                self.poll_read(cx, buf)
            }
        }
    }

    fn poll_seek(&mut self, cx: &mut Context<'_>, pos: SeekFrom) -> Poll<io::Result<u64>> {
        match &mut self.state {
            State::Idle => {
                if let Some(last_pos) = self.last_seek_pos {
                    self.cur = last_pos;
                    self.last_seek_pos = None;
                    return Poll::Ready(Ok(self.cur));
                }

                let (base, amt) = match pos {
                    SeekFrom::Start(n) => (0, n as i64),
                    SeekFrom::End(n) => {
                        if let Some(size) = self.size {
                            (size as i64, n)
                        } else {
                            // We don't know the length yet, we need to stat.
                            self.state = State::Stating(self.stat_future());
                            return self.poll_seek(cx, pos);
                        }
                    }
                    SeekFrom::Current(n) => (self.cur as i64, n),
                };

                let n = match base.checked_add(amt) {
                    Some(n) if n >= 0 => n as u64,
                    _ => {
                        return Poll::Ready(Err(Error::new(
                            ErrorKind::InvalidInput,
                            "invalid seek to a negative or overflowing position",
                        )))
                    }
                };

                self.cur = n;
                self.last_seek_pos = None;
                Poll::Ready(Ok(self.cur))
            }
            State::Sending(_) => {
                // It's impossible for us to go into this state while
                // poll_seek. We can just drop this future.
                self.state = State::Idle;
                self.poll_seek(cx, pos)
            }
            State::Reading(r) => {
                let seek_pos = if let Some(last_pos) = self.last_seek_pos {
                    last_pos
                } else {
                    let (base, amt) = match pos {
                        SeekFrom::Start(n) => (0, n as i64),
                        SeekFrom::End(n) => {
                            if let Some(size) = self.size {
                                (size as i64, n)
                            } else {
                                // We don't know the length yet, we need to stat.
                                self.state = State::Stating(self.stat_future());
                                return self.poll_seek(cx, pos);
                            }
                        }
                        SeekFrom::Current(n) => (self.cur as i64, n),
                    };

                    match base.checked_add(amt) {
                        Some(n) if n >= 0 => n as u64,
                        _ => {
                            return Poll::Ready(Err(Error::new(
                                ErrorKind::InvalidInput,
                                "invalid seek to a negative or overflowing position",
                            )))
                        }
                    }
                };
                self.last_seek_pos = Some(seek_pos);

                if seek_pos == self.cur {
                    self.last_seek_pos = None;
                    return Poll::Ready(Ok(self.cur));
                }

                if seek_pos > self.cur && seek_pos - self.cur < 1024 * 1024 {
                    // 212992 is the default read mem buffer of archlinux.
                    // Ideally we should make this congiurable.
                    //
                    // TODO: make this value configurable
                    let consume = cmp::min((seek_pos - self.cur) as usize, 212992);
                    self.sink.reserve(consume);

                    let mut buf = ReadBuf::uninit(self.sink.spare_capacity_mut());
                    unsafe { buf.assume_init(consume) };

                    // poll_read will update pos, so we don't need to
                    // update again.
                    let n = ready!(Pin::new(r).poll_read(cx, buf.initialized_mut()))?;
                    assert!(n > 0, "consumed bytes must be valid");

                    self.cur += n as u64;
                } else {
                    // If we are trying to seek to far more away.
                    // Let's just drop the reader.
                    self.state = State::Idle;
                }

                // Make sure the pos is absolute from start.
                self.poll_seek(cx, SeekFrom::Start(seek_pos))
            }
            State::Stating(fut) => {
                let rp = ready!(Pin::new(fut).poll(cx))?;

                self.size = Some(rp.into_metadata().content_length() - self.offset);
                self.state = State::Idle;
                self.poll_seek(cx, pos)
            }
        }
    }

    fn poll_next(&mut self, cx: &mut Context<'_>) -> Poll<Option<io::Result<bytes::Bytes>>> {
        match &mut self.state {
            State::Idle => {
                if let Some(size) = self.size {
                    if self.cur >= size {
                        return Poll::Ready(None);
                    }
                }

                self.state = State::Sending(self.read_future());
                self.poll_next(cx)
            }
            State::Sending(fut) => {
                let (rp, r) = ready!(Pin::new(fut).poll(cx))?;
                let meta = rp.into_metadata();

                self.size = Some(meta.content_length() + self.cur);
                self.state = State::Reading(r);
                self.poll_next(cx)
            }
            State::Reading(r) => match ready!(Pin::new(r).poll_next(cx)) {
                Some(Ok(bs)) => {
                    self.cur += bs.len() as u64;
                    Poll::Ready(Some(Ok(bs)))
                }
                Some(Err(err)) => {
                    self.state = State::Idle;
                    Poll::Ready(Some(Err(err)))
                }
                None => {
                    self.state = State::Idle;
                    Poll::Ready(None)
                }
            },
            State::Stating(_) => {
                // It's impossible for us to go into this state while
                // poll_next. We can just drop this future.
                self.state = State::Idle;
                self.poll_next(cx)
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use std::io::SeekFrom;

    use async_trait::async_trait;
    use bytes::Bytes;
    use futures::AsyncRead;
    use futures::AsyncReadExt;
    use futures::AsyncSeekExt;
    use rand::prelude::*;
    use sha2::Digest;
    use sha2::Sha256;

    use super::*;
    use crate::Result;

    // Generate bytes between [4MiB, 16MiB)
    fn gen_bytes() -> (Bytes, usize) {
        let mut rng = thread_rng();

        let size = rng.gen_range(4 * 1024 * 1024..16 * 1024 * 1024);
        let mut content = vec![0; size];
        rng.fill_bytes(&mut content);

        (Bytes::from(content), size)
    }

    #[derive(Debug, Clone, Default)]
    struct MockReadService {
        data: Bytes,
    }

    impl MockReadService {
        fn new(data: Bytes) -> Self {
            Self { data }
        }
    }

    #[async_trait]
    impl Accessor for MockReadService {
        async fn read(&self, _: &str, args: OpRead) -> Result<(RpRead, output::Reader)> {
            let bs = args.range().apply_on_bytes(self.data.clone());

            Ok((
                RpRead::new(bs.len() as u64),
                Box::new(MockReader {
                    inner: futures::io::Cursor::new(bs.into()),
                }) as output::Reader,
            ))
        }

        async fn stat(&self, _: &str, _: OpStat) -> Result<RpStat> {
            Ok(RpStat::new(
                ObjectMetadata::new(ObjectMode::FILE).with_content_length(self.data.len() as u64),
            ))
        }
    }

    #[derive(Debug, Clone, Default)]
    struct MockReader {
        inner: futures::io::Cursor<Vec<u8>>,
    }

    impl output::Read for MockReader {
        fn poll_read(&mut self, cx: &mut Context, buf: &mut [u8]) -> Poll<io::Result<usize>> {
            Pin::new(&mut self.inner).poll_read(cx, buf)
        }

        fn poll_next(&mut self, cx: &mut Context<'_>) -> Poll<Option<io::Result<Bytes>>> {
            let mut bs = vec![0; 4 * 1024];
            let n = ready!(Pin::new(&mut self.inner).poll_read(cx, &mut bs)?);
            if n == 0 {
                Poll::Ready(None)
            } else {
                Poll::Ready(Some(Ok(Bytes::from(bs[..n].to_vec()))))
            }
        }
    }

    #[tokio::test]
    async fn test_read_all() -> anyhow::Result<()> {
        let (bs, _) = gen_bytes();
        let acc = Arc::new(MockReadService::new(bs.clone()));

        let mut r = Box::new(by_offset(acc, "x", 0)) as output::Reader;

        let mut buf = Vec::new();
        r.read_to_end(&mut buf).await?;
        assert_eq!(bs.len(), buf.len(), "read size");
        assert_eq!(
            format!("{:x}", Sha256::digest(&bs)),
            format!("{:x}", Sha256::digest(&buf)),
            "read content"
        );

        let n = r.seek(SeekFrom::Start(0)).await?;
        assert_eq!(n, 0, "seek position must be 0");

        let mut buf = Vec::new();
        r.read_to_end(&mut buf).await?;
        assert_eq!(bs.len(), buf.len(), "read twice size");
        assert_eq!(
            format!("{:x}", Sha256::digest(&bs)),
            format!("{:x}", Sha256::digest(&buf)),
            "read twice content"
        );

        Ok(())
    }

    #[tokio::test]
    async fn test_read_part() -> anyhow::Result<()> {
        let (bs, _) = gen_bytes();
        let acc = Arc::new(MockReadService::new(bs.clone()));

        let mut r = Box::new(by_offset(acc, "x", 4096)) as output::Reader;

        let mut buf = Vec::new();
        r.read_to_end(&mut buf).await?;
        assert_eq!(bs.len() - 4096, buf.len(), "read size");
        assert_eq!(
            format!("{:x}", Sha256::digest(&bs[4096..])),
            format!("{:x}", Sha256::digest(&buf)),
            "read content"
        );

        let n = r.seek(SeekFrom::Start(0)).await?;
        assert_eq!(n, 0, "seek position must be 0");

        let mut buf = Vec::new();
        r.read_to_end(&mut buf).await?;
        assert_eq!(bs.len() - 4096, buf.len(), "read twice size");
        assert_eq!(
            format!("{:x}", Sha256::digest(&bs[4096..])),
            format!("{:x}", Sha256::digest(&buf)),
            "read twice content"
        );

        let n = r.seek(SeekFrom::Start(1024)).await?;
        assert_eq!(1024, n, "seek to 1024");

        let mut buf = vec![0; 1024];
        r.read_exact(&mut buf).await?;
        assert_eq!(
            format!("{:x}", Sha256::digest(&bs[4096 + 1024..4096 + 2048])),
            format!("{:x}", Sha256::digest(&buf)),
            "read after seek 1024"
        );

        let n = r.seek(SeekFrom::Current(1024)).await?;
        assert_eq!(3072, n, "seek to 3072");

        let mut buf = vec![0; 1024];
        r.read_exact(&mut buf).await?;
        assert_eq!(
            format!("{:x}", Sha256::digest(&bs[4096 + 3072..4096 + 3072 + 1024])),
            format!("{:x}", Sha256::digest(&buf)),
            "read after seek to 3072"
        );

        Ok(())
    }
}
