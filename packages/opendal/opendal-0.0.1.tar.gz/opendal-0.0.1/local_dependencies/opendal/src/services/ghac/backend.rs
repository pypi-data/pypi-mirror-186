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

use std::env;

use async_trait::async_trait;
use bytes::Bytes;
use http::header::ACCEPT;
use http::header::AUTHORIZATION;
use http::header::CONTENT_LENGTH;
use http::header::CONTENT_RANGE;
use http::header::CONTENT_TYPE;
use http::header::USER_AGENT;
use http::Request;
use http::Response;
use http::StatusCode;
use log::debug;
use serde::Deserialize;
use serde::Serialize;

use super::error::parse_error;
use crate::raw::*;
use crate::*;

/// The base url for cache url.
const CACHE_URL_BASE: &str = "_apis/artifactcache";
/// Cache API requires to provide an accept header.
const CACHE_HEADER_ACCEPT: &str = "application/json;api-version=6.0-preview.1";
/// The cache url env for ghac.
///
/// The url will be like `https://artifactcache.actions.githubusercontent.com/<id>/`
const ACTIONS_CACHE_URL: &str = "ACTIONS_CACHE_URL";
/// The runtime token env for ghac.
///
/// This token will be valid for 6h and github action will running for 6
/// hours at most. So we don't need to refetch it again.
const ACTIONS_RUNTIME_TOKEN: &str = "ACTIONS_RUNTIME_TOKEN";
/// The token provided by workflow;
const GITHUB_TOKEN: &str = "GITHUB_TOKEN";
/// The github api url for ghac.
const GITHUB_API_URL: &str = "GITHUB_API_URL";
/// The repository that runs this action.
const GITHUB_REPOSITORY: &str = "GITHUB_REPOSITORY";
/// The github API version that used by OpenDAL.
const GITHUB_API_VERSION: &str = "2022-11-28";

/// Builder for github action cache services.
#[derive(Debug, Default)]
pub struct Builder {
    root: Option<String>,
    version: Option<String>,
    enable_create_simulation: bool,

    http_client: Option<HttpClient>,
}

impl Builder {
    pub(crate) fn from_iter(it: impl Iterator<Item = (String, String)>) -> Self {
        let mut builder = Builder::default();
        for (k, v) in it {
            let v = v.as_str();
            match k.as_ref() {
                "root" => builder.root(v),
                "version" => builder.version(v),
                "enable_create_simulation" if !v.is_empty() => builder.enable_create_simulation(),
                _ => continue,
            };
        }
        builder
    }

    /// set the working directory root of backend
    pub fn root(&mut self, root: &str) -> &mut Self {
        if !root.is_empty() {
            self.root = Some(root.to_string())
        }

        self
    }

    /// set the version that used by cache.
    ///
    /// The version is the unique value that provides namespacing.
    /// It's better to make sure this value is only used by this backend.
    ///
    /// If not set, we will use `opendal` as default.
    pub fn version(&mut self, version: &str) -> &mut Self {
        if !version.is_empty() {
            self.version = Some(version.to_string())
        }

        self
    }

    /// Enable create simulation for ghac service.
    ///
    /// ghac service doesn't support create empty files. By enabling
    /// create simulation, we will create a 1 byte file to represent
    /// empty file.
    ///
    /// As a side effect, we can't create file with only 1 byte anymore.
    pub fn enable_create_simulation(&mut self) -> &mut Self {
        self.enable_create_simulation = true;
        self
    }

    /// Specify the http client that used by this service.
    ///
    /// # Notes
    ///
    /// This API is part of OpenDAL's Raw API. `HttpClient` could be changed
    /// during minor updates.
    pub fn http_client(&mut self, client: HttpClient) -> &mut Self {
        self.http_client = Some(client);
        self
    }

    /// Build a github action cache runner.
    pub fn build(&mut self) -> Result<impl Accessor> {
        debug!("backend build started: {:?}", self);

        let root = normalize_root(&self.root.take().unwrap_or_default());
        debug!("backend use root {}", root);

        let client = if let Some(client) = self.http_client.take() {
            client
        } else {
            HttpClient::new().map_err(|err| {
                err.with_operation("Builder::build")
                    .with_context("service", Scheme::Ghac)
            })?
        };

        let backend = Backend {
            root,
            enable_create_simulation: self.enable_create_simulation,

            cache_url: env::var(ACTIONS_CACHE_URL).map_err(|err| {
                Error::new(
                    ErrorKind::BackendConfigInvalid,
                    "ACTIONS_CACHE_URL not found, maybe not in github action environment?",
                )
                .with_operation("Builder::build")
                .set_source(err)
            })?,
            catch_token: env::var(ACTIONS_RUNTIME_TOKEN).map_err(|err| {
                Error::new(
                    ErrorKind::BackendConfigInvalid,
                    "ACTIONS_RUNTIME_TOKEN not found, maybe not in github action environment?",
                )
                .with_operation("Builder::build")
                .set_source(err)
            })?,
            version: self
                .version
                .clone()
                .unwrap_or_else(|| "opendal".to_string()),

            api_url: env::var(GITHUB_API_URL)
                .unwrap_or_else(|_| "https://api.github.com".to_string()),
            api_token: env::var(GITHUB_TOKEN).unwrap_or_default(),
            repo: env::var(GITHUB_REPOSITORY).unwrap_or_default(),

            client,
        };

        Ok(apply_wrapper(backend))
    }
}

/// Backend for github action cache services.
#[derive(Debug)]
pub struct Backend {
    // root should end with "/"
    root: String,
    enable_create_simulation: bool,

    cache_url: String,
    catch_token: String,
    version: String,

    api_url: String,
    api_token: String,
    repo: String,

    client: HttpClient,
}

#[async_trait]
impl Accessor for Backend {
    fn metadata(&self) -> AccessorMetadata {
        let mut am = AccessorMetadata::default();
        am.set_scheme(Scheme::Ghac)
            .set_root(&self.root)
            .set_name(&self.version)
            .set_capabilities(AccessorCapability::Read | AccessorCapability::Write)
            .set_hints(AccessorHint::ReadIsStreamable);
        am
    }

    async fn create(&self, path: &str, _: OpCreate) -> Result<RpCreate> {
        // ignore creation of dir.
        if path.ends_with('/') {
            return Ok(RpCreate::default());
        }
        if !self.enable_create_simulation {
            return Err(Error::new(
                ErrorKind::Unsupported,
                "ghac service doesn't support create empty file",
            ));
        }

        let req = self.ghac_reserve(path, 1).await?;

        let resp = self.client.send_async(req).await?;

        let cache_id = if resp.status().is_success() {
            let slc = resp.into_body().bytes().await?;
            let reserve_resp: GhacReserveResponse =
                serde_json::from_slice(&slc).map_err(parse_json_deserialize_error)?;
            reserve_resp.cache_id
        } else if resp.status().as_u16() == StatusCode::CONFLICT {
            // If the file is already exist, just return Ok.
            return Ok(RpCreate::default());
        } else {
            return Err(parse_error(resp)
                .await
                .map(|err| err.with_operation("Backend::ghac_reserve"))?);
        };

        // Write only 1 byte to allow create.
        let req = self
            .ghac_upload(cache_id, 1, AsyncBody::Bytes(Bytes::from_static(&[0])))
            .await?;

        let resp = self.client.send_async(req).await?;

        if resp.status().is_success() {
            resp.into_body().consume().await?;
        } else {
            return Err(parse_error(resp)
                .await
                .map(|err| err.with_operation("Backend::ghac_upload"))?);
        }

        let req = self.ghac_commmit(cache_id, 1).await?;
        let resp = self.client.send_async(req).await?;

        if resp.status().is_success() {
            resp.into_body().consume().await?;
            Ok(RpCreate::default())
        } else {
            Err(parse_error(resp)
                .await
                .map(|err| err.with_operation("Backend::ghac_commmit"))?)
        }
    }

    async fn read(&self, path: &str, args: OpRead) -> Result<(RpRead, output::Reader)> {
        let req = self.ghac_query(path).await?;

        let resp = self.client.send_async(req).await?;

        let location = if resp.status() == StatusCode::OK {
            let slc = resp.into_body().bytes().await?;
            let query_resp: GhacQueryResponse =
                serde_json::from_slice(&slc).map_err(parse_json_deserialize_error)?;
            query_resp.archive_location
        } else {
            return Err(parse_error(resp).await?);
        };

        let req = self.ghac_get_location(&location, args.range()).await?;
        let resp = self.client.send_async(req).await?;

        let status = resp.status();
        match status {
            StatusCode::OK | StatusCode::PARTIAL_CONTENT => {
                let meta = parse_into_object_metadata(path, resp.headers())?;
                Ok((RpRead::with_metadata(meta), resp.into_body().reader()))
            }
            _ => Err(parse_error(resp).await?),
        }
    }

    async fn write(&self, path: &str, args: OpWrite, r: input::Reader) -> Result<RpWrite> {
        let req = self.ghac_reserve(path, args.size()).await?;

        let resp = self.client.send_async(req).await?;

        let cache_id = if resp.status().is_success() {
            let slc = resp.into_body().bytes().await?;
            let reserve_resp: GhacReserveResponse =
                serde_json::from_slice(&slc).map_err(parse_json_deserialize_error)?;
            reserve_resp.cache_id
        } else {
            return Err(parse_error(resp)
                .await
                .map(|err| err.with_operation("Backend::ghac_reserve"))?);
        };

        let req = self
            .ghac_upload(cache_id, args.size(), AsyncBody::Reader(r))
            .await?;

        let resp = self.client.send_async(req).await?;

        if resp.status().is_success() {
            resp.into_body().consume().await?;
        } else {
            return Err(parse_error(resp)
                .await
                .map(|err| err.with_operation("Backend::ghac_commmit"))?);
        }

        let req = self.ghac_commmit(cache_id, args.size()).await?;
        let resp = self.client.send_async(req).await?;

        if resp.status().is_success() {
            resp.into_body().consume().await?;
            Ok(RpWrite::new(args.size()))
        } else {
            Err(parse_error(resp)
                .await
                .map(|err| err.with_operation("Backend::ghac_commmit"))?)
        }
    }

    async fn stat(&self, path: &str, _: OpStat) -> Result<RpStat> {
        // Stat root always returns a DIR.
        if path == "/" {
            return Ok(RpStat::new(ObjectMetadata::new(ObjectMode::DIR)));
        }

        let req = self.ghac_query(path).await?;

        let resp = self.client.send_async(req).await?;

        let location = if resp.status() == StatusCode::OK {
            let slc = resp.into_body().bytes().await?;
            let query_resp: GhacQueryResponse =
                serde_json::from_slice(&slc).map_err(parse_json_deserialize_error)?;
            query_resp.archive_location
        } else if resp.status() == StatusCode::NO_CONTENT && path.ends_with('/') {
            return Ok(RpStat::new(ObjectMetadata::new(ObjectMode::DIR)));
        } else {
            return Err(parse_error(resp).await?);
        };

        let req = self.ghac_head_location(&location).await?;
        let resp = self.client.send_async(req).await?;

        let status = resp.status();
        match status {
            StatusCode::OK => {
                let mut meta = parse_into_object_metadata(path, resp.headers())?;

                // Hack for enable_create_simulation.
                if self.enable_create_simulation && meta.content_length_raw() == Some(1) {
                    meta.set_content_length(0);
                }

                Ok(RpStat::new(meta))
            }
            _ => Err(parse_error(resp).await?),
        }
    }

    async fn delete(&self, path: &str, _: OpDelete) -> Result<RpDelete> {
        if self.api_token.is_empty() {
            return Err(Error::new(
                ErrorKind::ObjectPermissionDenied,
                "github token is not configued, delete is permission denied",
            ));
        }

        let resp = self.ghac_delete(path).await?;

        // deleting not existing objects is ok
        if resp.status().is_success() || resp.status() == StatusCode::NOT_FOUND {
            Ok(RpDelete::default())
        } else {
            Err(parse_error(resp).await?)
        }
    }
}

impl Backend {
    async fn ghac_query(&self, path: &str) -> Result<Request<AsyncBody>> {
        let p = build_abs_path(&self.root, path);

        let url = format!(
            "{}{CACHE_URL_BASE}/cache?keys={}&version={}",
            self.cache_url,
            percent_encode_path(&p),
            self.version
        );

        let mut req = Request::get(&url);
        req = req.header(AUTHORIZATION, format!("Bearer {}", self.catch_token));
        req = req.header(ACCEPT, CACHE_HEADER_ACCEPT);

        let req = req
            .body(AsyncBody::Empty)
            .map_err(new_request_build_error)?;

        Ok(req)
    }

    async fn ghac_get_location(
        &self,
        location: &str,
        range: BytesRange,
    ) -> Result<Request<AsyncBody>> {
        let mut req = Request::get(location);

        if !range.is_full() {
            // ghac is backed by azblob, and azblob doesn't support
            // read with suffix range
            //
            // ref: https://learn.microsoft.com/en-us/rest/api/storageservices/specifying-the-range-header-for-blob-service-operations
            if range.offset().is_none() && range.size().is_some() {
                return Err(Error::new(
                    ErrorKind::Unsupported,
                    "ghac doesn't support read with suffix range",
                ));
            }

            req = req.header(http::header::RANGE, range.to_header());
        }

        req.body(AsyncBody::Empty).map_err(new_request_build_error)
    }

    async fn ghac_head_location(&self, location: &str) -> Result<Request<AsyncBody>> {
        Request::head(location)
            .body(AsyncBody::Empty)
            .map_err(new_request_build_error)
    }

    async fn ghac_reserve(&self, path: &str, size: u64) -> Result<Request<AsyncBody>> {
        let p = build_abs_path(&self.root, path);

        let url = format!("{}{CACHE_URL_BASE}/caches", self.cache_url);

        let bs = serde_json::to_vec(&GhacReserveRequest {
            key: p,
            version: self.version.to_string(),
            cache_size: size,
        })
        .map_err(parse_json_serialize_error)?;

        let mut req = Request::post(&url);
        req = req.header(AUTHORIZATION, format!("Bearer {}", self.catch_token));
        req = req.header(ACCEPT, CACHE_HEADER_ACCEPT);
        req = req.header(CONTENT_LENGTH, bs.len());
        req = req.header(CONTENT_TYPE, "application/json");

        let req = req
            .body(AsyncBody::Bytes(Bytes::from(bs)))
            .map_err(new_request_build_error)?;

        Ok(req)
    }

    async fn ghac_upload(
        &self,
        cache_id: i64,
        size: u64,
        body: AsyncBody,
    ) -> Result<Request<AsyncBody>> {
        let url = format!("{}{CACHE_URL_BASE}/caches/{cache_id}", self.cache_url);

        let mut req = Request::patch(&url);
        req = req.header(AUTHORIZATION, format!("Bearer {}", self.catch_token));
        req = req.header(ACCEPT, CACHE_HEADER_ACCEPT);
        req = req.header(CONTENT_LENGTH, size);
        req = req.header(CONTENT_TYPE, "application/octet-stream");
        req = req.header(
            CONTENT_RANGE,
            BytesContentRange::default()
                .with_range(0, size - 1)
                .to_header(),
        );

        let req = req.body(body).map_err(new_request_build_error)?;

        Ok(req)
    }

    async fn ghac_commmit(&self, cache_id: i64, size: u64) -> Result<Request<AsyncBody>> {
        let url = format!("{}{CACHE_URL_BASE}/caches/{cache_id}", self.cache_url);

        let bs =
            serde_json::to_vec(&GhacCommitRequest { size }).map_err(parse_json_serialize_error)?;

        let mut req = Request::post(&url);
        req = req.header(AUTHORIZATION, format!("Bearer {}", self.catch_token));
        req = req.header(ACCEPT, CACHE_HEADER_ACCEPT);
        req = req.header(CONTENT_TYPE, "application/json");
        req = req.header(CONTENT_LENGTH, bs.len());

        let req = req
            .body(AsyncBody::Bytes(Bytes::from(bs)))
            .map_err(new_request_build_error)?;

        Ok(req)
    }

    async fn ghac_delete(&self, path: &str) -> Result<Response<IncomingAsyncBody>> {
        let p = build_abs_path(&self.root, path);

        let url = format!(
            "{}/repos/{}/actions/caches?key={}",
            self.api_url,
            self.repo,
            percent_encode_path(&p)
        );

        let mut req = Request::delete(&url);
        req = req.header(AUTHORIZATION, format!("Bearer {}", self.api_token));
        req = req.header(USER_AGENT, format!("opendal/{VERSION} (service ghac)"));
        req = req.header("X-GitHub-Api-Version", GITHUB_API_VERSION);

        let req = req
            .body(AsyncBody::Empty)
            .map_err(new_request_build_error)?;

        self.client.send_async(req).await
    }
}

#[derive(Deserialize)]
#[serde(rename_all = "camelCase")]
struct GhacQueryResponse {
    // Not used fields.
    // cache_key: String,
    // scope: String,
    archive_location: String,
}

#[derive(Serialize)]
struct GhacReserveRequest {
    key: String,
    version: String,
    cache_size: u64,
}

#[derive(Deserialize)]
#[serde(rename_all = "camelCase")]
struct GhacReserveResponse {
    cache_id: i64,
}

#[derive(Serialize)]
struct GhacCommitRequest {
    size: u64,
}

pub fn parse_json_serialize_error(e: serde_json::Error) -> Error {
    Error::new(ErrorKind::Unexpected, "serialize json").set_source(e)
}

pub fn parse_json_deserialize_error(e: serde_json::Error) -> Error {
    Error::new(ErrorKind::Unexpected, "deserialize json").set_source(e)
}
