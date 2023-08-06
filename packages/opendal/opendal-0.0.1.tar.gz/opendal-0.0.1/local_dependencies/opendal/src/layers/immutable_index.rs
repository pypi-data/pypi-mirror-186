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

use std::collections::BTreeSet;
use std::collections::HashSet;
use std::fmt::Debug;
use std::mem;
use std::sync::Arc;

use async_trait::async_trait;

use crate::object::*;
use crate::raw::*;
use crate::*;

/// ImmutableIndexLayer is used to add an immutable in-memory index for
/// underlying storage services.
///
/// Especially useful for services without list capability like HTTP.
///
/// # Examples
///
/// ```rust, no_run
/// use opendal::layers::ImmutableIndexLayer;
/// use opendal::Operator;
/// use opendal::Scheme;
///
/// let mut iil = ImmutableIndexLayer::default();
///
/// for i in ["file", "dir/", "dir/file", "dir_without_prefix/file"] {
///     iil.insert(i.to_string())
/// }
///
/// let op = Operator::from_env(Scheme::Http).unwrap().layer(iil);
/// ```
#[derive(Default, Debug, Clone)]
pub struct ImmutableIndexLayer {
    set: BTreeSet<String>,
}

impl ImmutableIndexLayer {
    /// Insert a key into index.
    pub fn insert(&mut self, key: String) {
        self.set.insert(key);
    }

    /// Insert keys from iter.
    pub fn extend_iter<I>(&mut self, iter: I)
    where
        I: IntoIterator<Item = String>,
    {
        self.set.extend(iter);
    }
}

impl Layer for ImmutableIndexLayer {
    fn layer(&self, inner: Arc<dyn Accessor>) -> Arc<dyn Accessor> {
        Arc::new(ImmutableIndexAccessor {
            set: self.set.clone(),
            inner,
        })
    }
}

#[derive(Debug, Clone)]
struct ImmutableIndexAccessor {
    inner: Arc<dyn Accessor>,
    /// TODO: we can introduce trie here to lower the memory footprint.
    set: BTreeSet<String>,
}

impl ImmutableIndexAccessor {
    fn children(&self, path: &str) -> Vec<String> {
        let mut res = HashSet::new();

        for i in self.set.iter() {
            // `/xyz` should not belong to `/abc`
            if !i.starts_with(path) {
                continue;
            }

            // remove `/abc` if self
            if i == path {
                continue;
            }

            match i[path.len()..].find('/') {
                // File `/abc/def.csv` must belong to `/abc`
                None => {
                    res.insert(i.to_string());
                }
                Some(idx) => {
                    // The index of first `/` after `/abc`.
                    let dir_idx = idx + 1 + path.len();

                    if dir_idx == i.len() {
                        // Dir `/abc/def/` belongs to `/abc/`
                        res.insert(i.to_string());
                    } else {
                        // File/Dir `/abc/def/xyz` doesn't belong to `/abc`.
                        // But we need to list `/abc/def` out so that we can walk down.
                        res.insert(i[..dir_idx].to_string());
                    }
                }
            }
        }

        res.into_iter().collect()
    }
}

#[async_trait]
impl Accessor for ImmutableIndexAccessor {
    fn inner(&self) -> Option<Arc<dyn Accessor>> {
        Some(self.inner.clone())
    }

    /// Add list capabilities for underlying storage services.
    fn metadata(&self) -> AccessorMetadata {
        let mut meta = self.inner.metadata();
        meta.set_capabilities(meta.capabilities() | AccessorCapability::List);

        meta
    }

    async fn list(&self, path: &str, _: OpList) -> Result<(RpList, ObjectPager)> {
        let mut path = path;
        if path == "/" {
            path = ""
        }

        Ok((
            RpList::default(),
            Box::new(ImmutableDir::new(self.children(path))),
        ))
    }

    fn blocking_list(&self, path: &str, _: OpList) -> Result<(RpList, BlockingObjectPager)> {
        let mut path = path;
        if path == "/" {
            path = ""
        }

        Ok((
            RpList::default(),
            Box::new(ImmutableDir::new(self.children(path))) as BlockingObjectPager,
        ))
    }
}

struct ImmutableDir {
    idx: Vec<String>,
}

impl ImmutableDir {
    fn new(idx: Vec<String>) -> Self {
        Self { idx }
    }

    fn inner_next_page(&mut self) -> Option<Vec<ObjectEntry>> {
        if self.idx.is_empty() {
            return None;
        }

        let vs = mem::take(&mut self.idx);

        Some(
            vs.into_iter()
                .map(|v| {
                    let mode = if v.ends_with('/') {
                        ObjectMode::DIR
                    } else {
                        ObjectMode::FILE
                    };
                    let meta = ObjectMetadata::new(mode);
                    ObjectEntry::with(v, meta)
                })
                .collect(),
        )
    }
}

#[async_trait]
impl ObjectPage for ImmutableDir {
    async fn next_page(&mut self) -> Result<Option<Vec<ObjectEntry>>> {
        Ok(self.inner_next_page())
    }
}

impl BlockingObjectPage for ImmutableDir {
    fn next_page(&mut self) -> Result<Option<Vec<ObjectEntry>>> {
        Ok(self.inner_next_page())
    }
}

#[cfg(test)]
mod tests {
    use std::collections::HashMap;
    use std::collections::HashSet;

    use anyhow::Result;
    use futures::TryStreamExt;
    use log::debug;

    use super::*;
    use crate::layers::LoggingLayer;
    use crate::ObjectMode;
    use crate::Operator;
    use crate::Scheme;

    #[tokio::test]
    async fn test_list() -> Result<()> {
        let _ = env_logger::try_init();

        let mut iil = ImmutableIndexLayer::default();
        for i in ["file", "dir/", "dir/file", "dir_without_prefix/file"] {
            iil.insert(i.to_string())
        }

        let op = Operator::from_iter(
            Scheme::Http,
            vec![("endpoint".to_string(), "https://xuanwo.io".to_string())].into_iter(),
        )?
        .layer(LoggingLayer::default())
        .layer(iil);

        let mut map = HashMap::new();
        let mut set = HashSet::new();
        let mut ds = op.object("").list().await?;
        while let Some(entry) = ds.try_next().await? {
            assert!(
                set.insert(entry.path().to_string()),
                "duplicated value: {}",
                entry.path()
            );
            map.insert(entry.path().to_string(), entry.mode().await?);
        }

        assert_eq!(map["file"], ObjectMode::FILE);
        assert_eq!(map["dir/"], ObjectMode::DIR);
        assert_eq!(map["dir_without_prefix/"], ObjectMode::DIR);
        Ok(())
    }

    #[tokio::test]
    async fn test_walk_top_down() -> Result<()> {
        let _ = env_logger::try_init();

        let mut iil = ImmutableIndexLayer::default();
        for i in ["file", "dir/", "dir/file", "dir_without_prefix/file"] {
            iil.insert(i.to_string())
        }

        let op = Operator::from_iter(
            Scheme::Http,
            vec![("endpoint".to_string(), "https://xuanwo.io".to_string())].into_iter(),
        )?
        .layer(LoggingLayer::default())
        .layer(iil);

        let mut ds = op.batch().walk_top_down("/")?;
        let mut set = HashSet::new();
        let mut map = HashMap::new();
        while let Some(entry) = ds.try_next().await? {
            assert!(
                set.insert(entry.path().to_string()),
                "duplicated value: {}",
                entry.path()
            );
            map.insert(entry.path().to_string(), entry.mode().await?);
        }

        debug!("current files: {:?}", map);

        assert_eq!(map.len(), 6);
        assert_eq!(map["file"], ObjectMode::FILE);
        assert_eq!(map["dir/"], ObjectMode::DIR);
        assert_eq!(map["dir_without_prefix/"], ObjectMode::DIR);
        Ok(())
    }

    #[tokio::test]
    async fn test_list_dir() -> Result<()> {
        let _ = env_logger::try_init();

        let mut iil = ImmutableIndexLayer::default();
        for i in [
            "dataset/stateful/ontime_2007_200.csv",
            "dataset/stateful/ontime_2008_200.csv",
            "dataset/stateful/ontime_2009_200.csv",
        ] {
            iil.insert(i.to_string())
        }

        let op = Operator::from_iter(
            Scheme::Http,
            vec![("endpoint".to_string(), "https://xuanwo.io".to_string())].into_iter(),
        )?
        .layer(LoggingLayer::default())
        .layer(iil);

        //  List /
        let mut map = HashMap::new();
        let mut set = HashSet::new();
        let mut ds = op.object("/").list().await?;
        while let Some(entry) = ds.try_next().await? {
            assert!(
                set.insert(entry.path().to_string()),
                "duplicated value: {}",
                entry.path()
            );
            map.insert(entry.path().to_string(), entry.mode().await?);
        }

        assert_eq!(map.len(), 1);
        assert_eq!(map["dataset/"], ObjectMode::DIR);

        //  List dataset/stateful/
        let mut map = HashMap::new();
        let mut set = HashSet::new();
        let mut ds = op.object("dataset/stateful/").list().await?;
        while let Some(entry) = ds.try_next().await? {
            assert!(
                set.insert(entry.path().to_string()),
                "duplicated value: {}",
                entry.path()
            );
            map.insert(entry.path().to_string(), entry.mode().await?);
        }

        assert_eq!(map.len(), 3);
        assert_eq!(
            map["dataset/stateful/ontime_2007_200.csv"],
            ObjectMode::FILE
        );
        assert_eq!(
            map["dataset/stateful/ontime_2008_200.csv"],
            ObjectMode::FILE
        );
        assert_eq!(
            map["dataset/stateful/ontime_2009_200.csv"],
            ObjectMode::FILE
        );
        Ok(())
    }

    #[tokio::test]
    async fn test_walk_top_down_dir() -> Result<()> {
        let _ = env_logger::try_init();

        let mut iil = ImmutableIndexLayer::default();
        for i in [
            "dataset/stateful/ontime_2007_200.csv",
            "dataset/stateful/ontime_2008_200.csv",
            "dataset/stateful/ontime_2009_200.csv",
        ] {
            iil.insert(i.to_string())
        }

        let op = Operator::from_iter(
            Scheme::Http,
            vec![("endpoint".to_string(), "https://xuanwo.io".to_string())].into_iter(),
        )?
        .layer(LoggingLayer::default())
        .layer(iil);

        let mut ds = op.batch().walk_top_down("/")?;

        let mut map = HashMap::new();
        let mut set = HashSet::new();
        while let Some(entry) = ds.try_next().await? {
            assert!(
                set.insert(entry.path().to_string()),
                "duplicated value: {}",
                entry.path()
            );
            map.insert(entry.path().to_string(), entry.mode().await?);
        }

        debug!("current files: {:?}", map);

        assert_eq!(map.len(), 6);
        assert_eq!(
            map["dataset/stateful/ontime_2007_200.csv"],
            ObjectMode::FILE
        );
        assert_eq!(
            map["dataset/stateful/ontime_2008_200.csv"],
            ObjectMode::FILE
        );
        assert_eq!(
            map["dataset/stateful/ontime_2009_200.csv"],
            ObjectMode::FILE
        );
        Ok(())
    }
}
