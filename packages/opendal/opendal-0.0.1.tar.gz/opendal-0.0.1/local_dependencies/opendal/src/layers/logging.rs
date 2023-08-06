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

use std::fmt::Debug;
use std::io;
use std::io::Read;
use std::pin::Pin;
use std::sync::Arc;
use std::task::Context;
use std::task::Poll;

use async_trait::async_trait;
use bytes::Bytes;
use futures::AsyncRead;
use log::debug;
use log::log;
use log::trace;
use log::Level;

use crate::raw::*;
use crate::*;

/// LoggingLayer will add logging for OpenDAL.
///
/// # Logging
///
/// - OpenDAL will log in structural way.
/// - Every operation will start with a `started` log entry.
/// - Every operation will finish with the following status:
///   - `finished`: the operation is successful.
///   - `errored`: the operation returns an expected error like `NotFound`.
///   - `failed`: the operation returns an unexpected error.
///
/// # Todo
///
/// We should migrate to log's kv api after it's ready.
///
/// Tracking issue: <https://github.com/rust-lang/log/issues/328>
///
/// # Examples
///
/// ```
/// use anyhow::Result;
/// use opendal::layers::LoggingLayer;
/// use opendal::Operator;
/// use opendal::Scheme;
///
/// let _ = Operator::from_env(Scheme::Fs)
///     .expect("must init")
///     .layer(LoggingLayer::default());
/// ```
#[derive(Debug, Copy, Clone)]
pub struct LoggingLayer {
    error_level: Option<Level>,
    failure_level: Option<Level>,
}

impl Default for LoggingLayer {
    fn default() -> Self {
        Self {
            error_level: Some(Level::Warn),
            failure_level: Some(Level::Error),
        }
    }
}

impl LoggingLayer {
    /// Setting the log level while expected error happened.
    ///
    /// For example: accessor returns ObjectNotFound.
    ///
    /// `None` means disable the log for error.
    pub fn with_error_level(mut self, level: Option<Level>) -> Self {
        self.error_level = level;
        self
    }

    /// Setting the log level while unexpected failure happened.
    ///
    /// For example: accessor returns Unexpected network error.
    ///
    /// `None` means disable the log for failure.
    pub fn with_failure_level(mut self, level: Option<Level>) -> Self {
        self.failure_level = level;
        self
    }
}

impl Layer for LoggingLayer {
    fn layer(&self, inner: Arc<dyn Accessor>) -> Arc<dyn Accessor> {
        let meta = inner.metadata();
        Arc::new(LoggingAccessor {
            scheme: meta.scheme(),
            inner,

            error_level: self.error_level,
            failure_level: self.failure_level,
        })
    }
}

#[derive(Clone, Debug)]
struct LoggingAccessor {
    scheme: Scheme,
    inner: Arc<dyn Accessor>,

    error_level: Option<Level>,
    failure_level: Option<Level>,
}

static LOGGING_TARGET: &str = "opendal::services";

impl LoggingAccessor {
    #[inline]
    fn err_status(&self, err: &Error) -> &'static str {
        if err.kind() == ErrorKind::Unexpected {
            "failed"
        } else {
            "errored"
        }
    }

    #[inline]
    fn err_level(&self, err: &Error) -> Option<Level> {
        if err.kind() == ErrorKind::Unexpected {
            self.failure_level
        } else {
            self.error_level
        }
    }
}

#[async_trait]
impl Accessor for LoggingAccessor {
    fn inner(&self) -> Option<Arc<dyn Accessor>> {
        Some(self.inner.clone())
    }

    fn metadata(&self) -> AccessorMetadata {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} -> started",
            self.scheme,
            Operation::Metadata
        );
        let result = self.inner.metadata();
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} -> finished: {:?}",
            self.scheme,
            Operation::Metadata,
            result
        );

        result
    }

    async fn create(&self, path: &str, args: OpCreate) -> Result<RpCreate> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} -> started",
            self.scheme,
            Operation::Create,
            path
        );

        self.inner
            .create(path, args.clone())
            .await
            .map(|v| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> finished",
                    self.scheme,
                    Operation::Create,
                    path
                );
                v
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} -> {}: {err:?}",
                        self.scheme,
                        Operation::Create,
                        path,
                        self.err_status(&err)
                    )
                }
                err
            })
    }

    async fn read(&self, path: &str, args: OpRead) -> Result<(RpRead, output::Reader)> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} range={} -> started",
            self.scheme,
            Operation::Read,
            path,
            args.range()
        );

        self.inner
            .read(path, args.clone())
            .await
            .map(|(rp, r)| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} range={} -> got reader",
                    self.scheme,
                    Operation::Read,
                    path,
                    args.range()
                );
                (
                    rp,
                    Box::new(LoggingReader::new(
                        self.scheme,
                        Operation::Read,
                        path,
                        args.range().size(),
                        r,
                        self.failure_level,
                    )) as output::Reader,
                )
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} range={} -> {}: {err:?}",
                        self.scheme,
                        Operation::Read,
                        path,
                        args.range(),
                        self.err_status(&err)
                    )
                }
                err
            })
    }

    async fn write(&self, path: &str, args: OpWrite, r: input::Reader) -> Result<RpWrite> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} size={:?} -> started",
            self.scheme,
            Operation::Write,
            path,
            args.size()
        );

        let reader = LoggingReader::new(
            self.scheme,
            Operation::Write,
            path,
            Some(args.size()),
            r,
            self.failure_level,
        );
        let r = Box::new(reader) as input::Reader;

        self.inner
            .write(path, args.clone(), r)
            .await
            .map(|v| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} size={:?} -> written",
                    self.scheme,
                    Operation::Write,
                    path,
                    args.size()
                );
                v
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} size={:?} -> {}: {err:?}",
                        self.scheme,
                        Operation::Write,
                        path,
                        args.size(),
                        self.err_status(&err)
                    )
                }
                err
            })
    }

    async fn stat(&self, path: &str, args: OpStat) -> Result<RpStat> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} -> started",
            self.scheme,
            Operation::Stat,
            path
        );

        self.inner
            .stat(path, args.clone())
            .await
            .map(|v| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> finished: {v:?}",
                    self.scheme,
                    Operation::Stat,
                    path
                );
                v
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} -> {}: {err:?}",
                        self.scheme,
                        Operation::Stat,
                        path,
                        self.err_status(&err)
                    );
                }
                err
            })
    }

    async fn delete(&self, path: &str, args: OpDelete) -> Result<RpDelete> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} -> started",
            self.scheme,
            Operation::Delete,
            path
        );

        self.inner
            .delete(path, args.clone())
            .await
            .map(|v| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> finished",
                    self.scheme,
                    Operation::Delete,
                    path
                );
                v
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} -> {}: {err:?}",
                        self.scheme,
                        Operation::Delete,
                        path,
                        self.err_status(&err)
                    );
                }
                err
            })
    }

    async fn list(&self, path: &str, args: OpList) -> Result<(RpList, ObjectPager)> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} -> started",
            self.scheme,
            Operation::List,
            path
        );

        self.inner
            .list(path, args)
            .await
            .map(|(rp, v)| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> start listing dir",
                    self.scheme,
                    Operation::List,
                    path
                );
                let streamer =
                    LoggingPager::new(self.scheme, path, v, self.error_level, self.failure_level);
                (rp, Box::new(streamer) as ObjectPager)
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} -> {}: {err:?}",
                        self.scheme,
                        Operation::List,
                        path,
                        self.err_status(&err)
                    );
                }
                err
            })
    }

    fn presign(&self, path: &str, args: OpPresign) -> Result<RpPresign> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} -> started",
            self.scheme,
            Operation::Presign,
            path
        );

        self.inner
            .presign(path, args)
            .map(|v| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> finished: {v:?}",
                    self.scheme,
                    Operation::Presign,
                    path
                );
                v
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} -> {}: {err:?}",
                        self.scheme,
                        Operation::Presign,
                        path,
                        self.err_status(&err)
                    );
                }
                err
            })
    }

    async fn create_multipart(
        &self,
        path: &str,
        args: OpCreateMultipart,
    ) -> Result<RpCreateMultipart> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} -> started",
            self.scheme,
            Operation::CreateMultipart,
            path
        );

        self.inner
            .create_multipart(path, args.clone())
            .await
            .map(|v| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> finished",
                    self.scheme,
                    Operation::CreateMultipart,
                    path
                );
                v
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} -> {}: {err:?}",
                        self.scheme,
                        Operation::CreateMultipart,
                        path,
                        self.err_status(&err)
                    );
                }
                err
            })
    }

    async fn write_multipart(
        &self,
        path: &str,
        args: OpWriteMultipart,
        r: input::Reader,
    ) -> Result<RpWriteMultipart> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} upload_id={} part_number={:?} size={:?} -> started",
            self.scheme,
            Operation::WriteMultipart,
            path,
            args.upload_id(),
            args.part_number(),
            args.size()
        );

        let r = LoggingReader::new(
            self.scheme,
            Operation::Write,
            path,
            Some(args.size()),
            r,
            self.failure_level,
        );
        let r = Box::new(r);

        self.inner
            .write_multipart(path, args.clone(), r)
            .await
            .map(|v| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} upload_id={} part_number={:?} size={:?} -> written",
                    self.scheme,
                    Operation::WriteMultipart,
                    path,
                    args.upload_id(),
                    args.part_number(),
                    args.size()
                );
                v
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                       "service={} operation={} path={} upload_id={} part_number={:?} size={:?} -> {}: {err:?}",
                        self.scheme,
                        Operation::WriteMultipart,
                        path,
                        args.upload_id(),
                        args.part_number(),
                        args.size(),
                        self.err_status(&err)
                    );
                }
                err
            })
    }

    async fn complete_multipart(
        &self,
        path: &str,
        args: OpCompleteMultipart,
    ) -> Result<RpCompleteMultipart> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} upload_id={} -> started",
            self.scheme,
            Operation::CompleteMultipart,
            path,
            args.upload_id(),
        );

        self.inner
            .complete_multipart(path, args.clone())
            .await
            .map(|v| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} upload_id={} -> finished",
                    self.scheme,
                    Operation::CompleteMultipart,
                    path,
                    args.upload_id()
                );
                v
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} upload_id={} -> {}: {err:?}",
                        self.scheme,
                        Operation::CompleteMultipart,
                        path,
                        args.upload_id(),
                        self.err_status(&err)
                    );
                }
                err
            })
    }

    async fn abort_multipart(
        &self,
        path: &str,
        args: OpAbortMultipart,
    ) -> Result<RpAbortMultipart> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} upload_id={} -> started",
            self.scheme,
            Operation::AbortMultipart,
            path,
            args.upload_id()
        );

        self.inner
            .abort_multipart(path, args.clone())
            .await
            .map(|v| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} upload_id={} -> finished",
                    self.scheme,
                    Operation::AbortMultipart,
                    path,
                    args.upload_id()
                );
                v
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} upload_id={} -> {}: {err:?}",
                        self.scheme,
                        Operation::AbortMultipart,
                        path,
                        args.upload_id(),
                        self.err_status(&err)
                    );
                }
                err
            })
    }

    fn blocking_create(&self, path: &str, args: OpCreate) -> Result<RpCreate> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} -> started",
            self.scheme,
            Operation::BlockingCreate,
            path
        );

        self.inner
            .blocking_create(path, args)
            .map(|v| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> finished",
                    self.scheme,
                    Operation::BlockingCreate,
                    path
                );
                v
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} -> {}: {err:?}",
                        self.scheme,
                        Operation::BlockingCreate,
                        path,
                        self.err_status(&err)
                    );
                }
                err
            })
    }

    fn blocking_read(&self, path: &str, args: OpRead) -> Result<(RpRead, output::BlockingReader)> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} range={} -> started",
            self.scheme,
            Operation::BlockingRead,
            path,
            args.range(),
        );

        self.inner
            .blocking_read(path, args.clone())
            .map(|(rp, r)| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} range={} -> got reader",
                    self.scheme,
                    Operation::BlockingRead,
                    path,
                    args.range(),
                );
                let r = BlockingLoggingReader::new(
                    self.scheme,
                    Operation::BlockingRead,
                    path,
                    args.range().size(),
                    r,
                    self.failure_level,
                );
                (rp, Box::new(r) as output::BlockingReader)
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} range={} -> {}: {err:?}",
                        self.scheme,
                        Operation::BlockingRead,
                        path,
                        args.range(),
                        self.err_status(&err)
                    );
                }
                err
            })
    }

    fn blocking_write(
        &self,
        path: &str,
        args: OpWrite,
        r: input::BlockingReader,
    ) -> Result<RpWrite> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} size={:?} -> started",
            self.scheme,
            Operation::BlockingWrite,
            path,
            args.size()
        );

        let reader = BlockingLoggingReader::new(
            self.scheme,
            Operation::BlockingWrite,
            path,
            Some(args.size()),
            r,
            self.failure_level,
        );
        let r = Box::new(reader) as input::BlockingReader;

        self.inner
            .blocking_write(path, args.clone(), r)
            .map(|v| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} size={:?} -> written",
                    self.scheme,
                    Operation::BlockingWrite,
                    path,
                    args.size()
                );
                v
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} size={:?} -> {}: {err:?}",
                        self.scheme,
                        Operation::BlockingWrite,
                        path,
                        args.size(),
                        self.err_status(&err)
                    );
                }
                err
            })
    }

    fn blocking_stat(&self, path: &str, args: OpStat) -> Result<RpStat> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} -> started",
            self.scheme,
            Operation::BlockingStat,
            path
        );

        self.inner
            .blocking_stat(path, args)
            .map(|v| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> finished: {v:?}",
                    self.scheme,
                    Operation::BlockingStat,
                    path
                );
                v
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} -> {}: {err:?}",
                        self.scheme,
                        Operation::BlockingStat,
                        path,
                        self.err_status(&err)
                    );
                }
                err
            })
    }

    fn blocking_delete(&self, path: &str, args: OpDelete) -> Result<RpDelete> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} -> started",
            self.scheme,
            Operation::BlockingDelete,
            path
        );

        self.inner
            .blocking_delete(path, args)
            .map(|v| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> finished",
                    self.scheme,
                    Operation::BlockingDelete,
                    path
                );
                v
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} -> {}: {err:?}",
                        self.scheme,
                        Operation::BlockingDelete,
                        path,
                        self.err_status(&err)
                    );
                }
                err
            })
    }

    fn blocking_list(&self, path: &str, args: OpList) -> Result<(RpList, BlockingObjectPager)> {
        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} -> started",
            self.scheme,
            Operation::BlockingList,
            path
        );

        self.inner
            .blocking_list(path, args)
            .map(|(rp, v)| {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> got dir",
                    self.scheme,
                    Operation::BlockingList,
                    path
                );
                let li = BlockingLoggingPager::new(
                    self.scheme,
                    path,
                    v,
                    self.error_level,
                    self.failure_level,
                );
                (rp, Box::new(li) as BlockingObjectPager)
            })
            .map_err(|err| {
                if let Some(lvl) = self.err_level(&err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} -> {}: {err:?}",
                        self.scheme,
                        Operation::BlockingList,
                        path,
                        self.err_status(&err)
                    );
                }
                err
            })
    }
}

/// `LoggingReader` is a wrapper of `BytesReader`, with logging functionality.
struct LoggingReader<R> {
    scheme: Scheme,
    path: String,
    op: Operation,

    size: Option<u64>,
    has_read: u64,
    failure_level: Option<Level>,

    inner: R,
}

impl<R> LoggingReader<R> {
    fn new(
        scheme: Scheme,
        op: Operation,
        path: &str,
        size: Option<u64>,
        reader: R,
        failure_level: Option<Level>,
    ) -> Self {
        Self {
            scheme,
            op,
            path: path.to_string(),

            size,
            has_read: 0,

            inner: reader,
            failure_level,
        }
    }
}

impl<R> Drop for LoggingReader<R> {
    fn drop(&mut self) {
        if let Some(size) = self.size {
            if size == self.has_read {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} has_read={} -> consumed reader fully",
                    self.scheme,
                    self.op,
                    self.path,
                    self.has_read
                );

                return;
            }
        }

        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} has_read={} -> dropped reader",
            self.scheme,
            self.op,
            self.path,
            self.has_read
        );
    }
}

impl output::Read for LoggingReader<output::Reader> {
    fn inner(&mut self) -> Option<&mut output::Reader> {
        Some(&mut self.inner)
    }

    fn poll_read(&mut self, cx: &mut Context<'_>, buf: &mut [u8]) -> Poll<io::Result<usize>> {
        match self.inner.poll_read(cx, buf) {
            Poll::Ready(res) => match res {
                Ok(n) => {
                    self.has_read += n as u64;
                    trace!(
                        target: LOGGING_TARGET,
                        "service={} operation={} path={} has_read={} -> {}: {}B",
                        self.scheme,
                        self.op,
                        self.path,
                        self.has_read,
                        self.op,
                        n
                    );
                    Poll::Ready(Ok(n))
                }
                Err(err) => {
                    if let Some(lvl) = self.failure_level {
                        log!(
                            target: LOGGING_TARGET,
                            lvl,
                            "service={} operation={} path={} has_read={} -> failed: {err:?}",
                            self.scheme,
                            self.op,
                            self.path,
                            self.has_read,
                        )
                    }
                    Poll::Ready(Err(err))
                }
            },
            Poll::Pending => {
                trace!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} has_read={} -> pending",
                    self.scheme,
                    self.op,
                    self.path,
                    self.has_read
                );
                Poll::Pending
            }
        }
    }

    fn poll_next(&mut self, cx: &mut Context<'_>) -> Poll<Option<io::Result<Bytes>>> {
        match self.inner.poll_next(cx) {
            Poll::Ready(res) => match res {
                Some(Ok(bs)) => {
                    self.has_read += bs.len() as u64;
                    trace!(
                        target: LOGGING_TARGET,
                        "service={} operation={} path={} has_read={} -> {}: {}B",
                        self.scheme,
                        self.op,
                        self.path,
                        self.has_read,
                        self.op,
                        bs.len()
                    );
                    Poll::Ready(Some(Ok(bs)))
                }
                Some(Err(err)) => {
                    if let Some(lvl) = self.failure_level {
                        log!(
                            target: LOGGING_TARGET,
                            lvl,
                            "service={} operation={} path={} has_read={} -> failed: {err:?}",
                            self.scheme,
                            self.op,
                            self.path,
                            self.has_read,
                        )
                    }
                    Poll::Ready(Some(Err(err)))
                }
                None => Poll::Ready(None),
            },
            Poll::Pending => {
                trace!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} has_read={} -> pending",
                    self.scheme,
                    self.op,
                    self.path,
                    self.has_read
                );
                Poll::Pending
            }
        }
    }
}

impl<R: input::Read> AsyncRead for LoggingReader<R> {
    fn poll_read(
        mut self: Pin<&mut Self>,
        cx: &mut Context<'_>,
        buf: &mut [u8],
    ) -> Poll<io::Result<usize>> {
        match Pin::new(&mut self.inner).poll_read(cx, buf) {
            Poll::Ready(res) => match res {
                Ok(n) => {
                    self.has_read += n as u64;
                    trace!(
                        target: LOGGING_TARGET,
                        "service={} operation={} path={} has_read={} -> {}: {}B",
                        self.scheme,
                        self.op,
                        self.path,
                        self.has_read,
                        self.op,
                        n
                    );
                    Poll::Ready(Ok(n))
                }
                Err(err) => {
                    if let Some(lvl) = self.failure_level {
                        log!(
                            target: LOGGING_TARGET,
                            lvl,
                            "service={} operation={} path={} has_read={} -> failed: {err:?}",
                            self.scheme,
                            self.op,
                            self.path,
                            self.has_read,
                        )
                    }
                    Poll::Ready(Err(err))
                }
            },
            Poll::Pending => {
                trace!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} has_read={} -> pending",
                    self.scheme,
                    self.op,
                    self.path,
                    self.has_read
                );
                Poll::Pending
            }
        }
    }
}

/// `BlockingLoggingReader` is a wrapper of `BlockingBytesReader`, with logging functionality.
struct BlockingLoggingReader<R> {
    scheme: Scheme,
    path: String,
    op: Operation,

    size: Option<u64>,
    has_read: u64,

    inner: R,
    failure_level: Option<Level>,
}

impl<R> BlockingLoggingReader<R> {
    fn new(
        scheme: Scheme,
        op: Operation,
        path: &str,
        size: Option<u64>,
        reader: R,
        failure_level: Option<Level>,
    ) -> Self {
        Self {
            scheme,
            op,
            path: path.to_string(),

            size,
            has_read: 0,
            inner: reader,
            failure_level,
        }
    }
}

impl<R> Drop for BlockingLoggingReader<R> {
    fn drop(&mut self) {
        if let Some(size) = self.size {
            if size == self.has_read {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} has_read={} -> consumed reader fully",
                    self.scheme,
                    self.op,
                    self.path,
                    self.has_read
                );

                return;
            }
        }

        debug!(
            target: LOGGING_TARGET,
            "service={} operation={} path={} has_read={} -> dropped reader",
            self.scheme,
            self.op,
            self.path,
            self.has_read
        );
    }
}

impl output::BlockingRead for BlockingLoggingReader<output::BlockingReader> {
    fn inner(&mut self) -> Option<&mut output::BlockingReader> {
        Some(&mut self.inner)
    }

    fn read(&mut self, buf: &mut [u8]) -> io::Result<usize> {
        match self.inner.read(buf) {
            Ok(n) => {
                self.has_read += n as u64;
                trace!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} has_read={} -> {}: {}B",
                    self.scheme,
                    self.op,
                    self.path,
                    self.has_read,
                    self.op,
                    n
                );
                Ok(n)
            }
            Err(err) => {
                if let Some(lvl) = self.failure_level {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} has_read={} -> failed: {err:?}",
                        self.scheme,
                        self.op,
                        self.path,
                        self.has_read,
                    );
                }
                Err(err)
            }
        }
    }

    fn next(&mut self) -> Option<io::Result<Bytes>> {
        match self.inner.next() {
            Some(Ok(bs)) => {
                self.has_read += bs.len() as u64;
                trace!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} has_read={} -> {}: {}B",
                    self.scheme,
                    self.op,
                    self.path,
                    self.has_read,
                    self.op,
                    bs.len()
                );
                Some(Ok(bs))
            }
            Some(Err(err)) => {
                if let Some(lvl) = self.failure_level {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} has_read={} -> failed: {err:?}",
                        self.scheme,
                        self.op,
                        self.path,
                        self.has_read,
                    )
                }
                Some(Err(err))
            }
            None => None,
        }
    }
}

impl<R: input::BlockingRead> Read for BlockingLoggingReader<R> {
    fn read(&mut self, buf: &mut [u8]) -> io::Result<usize> {
        match self.inner.read(buf) {
            Ok(n) => {
                self.has_read += n as u64;
                trace!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} has_read={} -> {}: {}B",
                    self.scheme,
                    self.op,
                    self.path,
                    self.has_read,
                    self.op,
                    n
                );
                Ok(n)
            }
            Err(err) => {
                if let Some(lvl) = self.failure_level {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} has_read={} -> failed: {err:?}",
                        self.scheme,
                        self.op,
                        self.path,
                        self.has_read,
                    );
                }
                Err(err)
            }
        }
    }
}

struct LoggingPager {
    scheme: Scheme,
    path: String,
    finished: bool,
    inner: ObjectPager,
    error_level: Option<Level>,
    failure_level: Option<Level>,
}

impl LoggingPager {
    fn new(
        scheme: Scheme,
        path: &str,
        inner: ObjectPager,
        error_level: Option<Level>,
        failure_level: Option<Level>,
    ) -> Self {
        Self {
            scheme,
            path: path.to_string(),
            finished: false,
            inner,
            error_level,
            failure_level,
        }
    }
}

impl Drop for LoggingPager {
    fn drop(&mut self) {
        if self.finished {
            debug!(
                target: LOGGING_TARGET,
                "service={} operation={} path={} -> consumed dir fully",
                self.scheme,
                Operation::List,
                self.path
            );
        } else {
            debug!(
                target: LOGGING_TARGET,
                "service={} operation={} path={} -> dropped dir",
                self.scheme,
                Operation::List,
                self.path
            );
        }
    }
}

impl LoggingPager {
    #[inline]
    fn err_status(&self, err: &Error) -> &'static str {
        if err.kind() == ErrorKind::Unexpected {
            "failed"
        } else {
            "errored"
        }
    }

    #[inline]
    fn err_level(&self, err: &Error) -> Option<Level> {
        if err.kind() == ErrorKind::Unexpected {
            self.failure_level
        } else {
            self.error_level
        }
    }
}

#[async_trait]
impl ObjectPage for LoggingPager {
    async fn next_page(&mut self) -> Result<Option<Vec<ObjectEntry>>> {
        let res = self.inner.next_page().await;

        match &res {
            Ok(Some(des)) => {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> listed {} entries",
                    self.scheme,
                    Operation::List,
                    self.path,
                    des.len(),
                );
            }
            Ok(None) => {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> finished",
                    self.scheme,
                    Operation::List,
                    self.path
                );
                self.finished = true;
            }
            Err(err) => {
                if let Some(lvl) = self.err_level(err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} -> {}: {err:?}",
                        self.scheme,
                        Operation::List,
                        self.path,
                        self.err_status(err)
                    )
                }
            }
        };

        res
    }
}

struct BlockingLoggingPager {
    scheme: Scheme,
    path: String,
    finished: bool,
    inner: BlockingObjectPager,
    error_level: Option<Level>,
    failure_level: Option<Level>,
}

impl BlockingLoggingPager {
    fn new(
        scheme: Scheme,
        path: &str,
        inner: BlockingObjectPager,
        error_level: Option<Level>,
        failure_level: Option<Level>,
    ) -> Self {
        Self {
            scheme,
            path: path.to_string(),
            finished: false,
            inner,
            error_level,
            failure_level,
        }
    }
}

impl Drop for BlockingLoggingPager {
    fn drop(&mut self) {
        if self.finished {
            debug!(
                target: LOGGING_TARGET,
                "service={} operation={} path={} -> consumed dir fully",
                self.scheme,
                Operation::BlockingList,
                self.path
            );
        } else {
            debug!(
                target: LOGGING_TARGET,
                "service={} operation={} path={} -> dropped dir",
                self.scheme,
                Operation::BlockingList,
                self.path
            );
        }
    }
}

impl BlockingLoggingPager {
    #[inline]
    fn err_status(&self, err: &Error) -> &'static str {
        if err.kind() == ErrorKind::Unexpected {
            "failed"
        } else {
            "errored"
        }
    }

    #[inline]
    fn err_level(&self, err: &Error) -> Option<Level> {
        if err.kind() == ErrorKind::Unexpected {
            self.failure_level
        } else {
            self.error_level
        }
    }
}

impl BlockingObjectPage for BlockingLoggingPager {
    fn next_page(&mut self) -> Result<Option<Vec<ObjectEntry>>> {
        let res = self.inner.next_page();

        match &res {
            Ok(Some(des)) => {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> got {} entries",
                    self.scheme,
                    Operation::BlockingList,
                    self.path,
                    des.len(),
                );
            }
            Ok(None) => {
                debug!(
                    target: LOGGING_TARGET,
                    "service={} operation={} path={} -> finished",
                    self.scheme,
                    Operation::BlockingList,
                    self.path
                );
                self.finished = true;
            }
            Err(err) => {
                if let Some(lvl) = self.err_level(err) {
                    log!(
                        target: LOGGING_TARGET,
                        lvl,
                        "service={} operation={} path={} -> {}: {err:?}",
                        self.scheme,
                        Operation::BlockingList,
                        self.path,
                        self.err_status(err)
                    )
                }
            }
        };

        res
    }
}
