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
use std::fmt::Formatter;

use async_trait::async_trait;
use http::Request;
use http::Response;
use http::StatusCode;
use log::debug;

use super::error::parse_error;
use crate::raw::*;
use crate::*;

/// Builder for http backend.
#[derive(Default)]
pub struct Builder {
    endpoint: Option<String>,
    root: Option<String>,
    http_client: Option<HttpClient>,
}

impl Debug for Builder {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        let mut de = f.debug_struct("Builder");
        de.field("endpoint", &self.endpoint);
        de.field("root", &self.root);

        de.finish()
    }
}

impl Builder {
    pub(crate) fn from_iter(it: impl Iterator<Item = (String, String)>) -> Self {
        let mut builder = Builder::default();

        for (k, v) in it {
            let v = v.as_str();
            match k.as_ref() {
                "root" => builder.root(v),
                "endpoint" => builder.endpoint(v),
                _ => continue,
            };
        }

        builder
    }

    /// Set endpoint for http backend.
    ///
    /// For example: `https://example.com`
    pub fn endpoint(&mut self, endpoint: &str) -> &mut Self {
        self.endpoint = if endpoint.is_empty() {
            None
        } else {
            Some(endpoint.to_string())
        };

        self
    }

    /// Set root path of http backend.
    pub fn root(&mut self, root: &str) -> &mut Self {
        self.root = if root.is_empty() {
            None
        } else {
            Some(root.to_string())
        };

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

    /// Build a HTTP backend.
    pub fn build(&mut self) -> Result<impl Accessor> {
        debug!("backend build started: {:?}", &self);

        let endpoint = match &self.endpoint {
            Some(v) => v,
            None => {
                return Err(
                    Error::new(ErrorKind::BackendConfigInvalid, "endpoint is empty")
                        .with_context("service", Scheme::Http),
                )
            }
        };

        let root = normalize_root(&self.root.take().unwrap_or_default());
        debug!("backend use root {}", root);

        let client = if let Some(client) = self.http_client.take() {
            client
        } else {
            HttpClient::new().map_err(|err| {
                err.with_operation("Builder::build")
                    .with_context("service", Scheme::Http)
            })?
        };

        debug!("backend build finished: {:?}", &self);
        Ok(apply_wrapper(Backend {
            endpoint: endpoint.to_string(),
            root,
            client,
        }))
    }
}

/// Backend is used to serve `Accessor` support for http.
#[derive(Clone)]
pub struct Backend {
    endpoint: String,
    root: String,
    client: HttpClient,
}

impl Debug for Backend {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("Backend")
            .field("endpoint", &self.endpoint)
            .field("root", &self.root)
            .field("client", &self.client)
            .finish()
    }
}

#[async_trait]
impl Accessor for Backend {
    fn metadata(&self) -> AccessorMetadata {
        let mut ma = AccessorMetadata::default();
        ma.set_scheme(Scheme::Http)
            .set_root(&self.root)
            .set_capabilities(AccessorCapability::Read)
            .set_hints(AccessorHint::ReadIsStreamable);

        ma
    }

    async fn read(&self, path: &str, args: OpRead) -> Result<(RpRead, output::Reader)> {
        let resp = self.http_get(path, args.range()).await?;

        let status = resp.status();

        match status {
            StatusCode::OK | StatusCode::PARTIAL_CONTENT => {
                let meta = parse_into_object_metadata(path, resp.headers())?;
                Ok((RpRead::with_metadata(meta), resp.into_body().reader()))
            }
            _ => Err(parse_error(resp).await?),
        }
    }

    async fn stat(&self, path: &str, _: OpStat) -> Result<RpStat> {
        // Stat root always returns a DIR.
        if path == "/" {
            return Ok(RpStat::new(ObjectMetadata::new(ObjectMode::DIR)));
        }

        let resp = self.http_head(path).await?;

        let status = resp.status();

        match status {
            StatusCode::OK => parse_into_object_metadata(path, resp.headers()).map(RpStat::new),
            // HTTP Server like nginx could return FORBIDDEN if auto-index
            // is not enabled, we should ignore them.
            StatusCode::NOT_FOUND | StatusCode::FORBIDDEN if path.ends_with('/') => {
                Ok(RpStat::new(ObjectMetadata::new(ObjectMode::DIR)))
            }
            _ => Err(parse_error(resp).await?),
        }
    }
}

impl Backend {
    async fn http_get(&self, path: &str, range: BytesRange) -> Result<Response<IncomingAsyncBody>> {
        let p = build_rooted_abs_path(&self.root, path);

        let url = format!("{}{}", self.endpoint, percent_encode_path(&p));

        let mut req = Request::get(&url);

        if !range.is_full() {
            req = req.header(http::header::RANGE, range.to_header());
        }

        let req = req
            .body(AsyncBody::Empty)
            .map_err(new_request_build_error)?;

        self.client.send_async(req).await
    }

    async fn http_head(&self, path: &str) -> Result<Response<IncomingAsyncBody>> {
        let p = build_rooted_abs_path(&self.root, path);

        let url = format!("{}{}", self.endpoint, percent_encode_path(&p));

        let req = Request::head(&url);

        let req = req
            .body(AsyncBody::Empty)
            .map_err(new_request_build_error)?;

        self.client.send_async(req).await
    }
}

#[cfg(test)]
mod tests {
    use anyhow::Result;
    use wiremock::matchers::method;
    use wiremock::matchers::path;
    use wiremock::Mock;
    use wiremock::MockServer;
    use wiremock::ResponseTemplate;

    use super::*;
    use crate::Operator;

    #[tokio::test]
    async fn test_read() -> Result<()> {
        let _ = env_logger::builder().is_test(true).try_init();

        let mock_server = MockServer::start().await;
        Mock::given(method("GET"))
            .and(path("/hello"))
            .respond_with(ResponseTemplate::new(200).set_body_string("Hello, World!"))
            .mount(&mock_server)
            .await;

        let mut builder = Builder::default();
        builder.endpoint(&mock_server.uri());
        builder.root("/");
        let op = Operator::new(builder.build()?);

        let bs = op.object("hello").read().await?;

        assert_eq!(bs, b"Hello, World!");
        Ok(())
    }

    #[tokio::test]
    async fn test_stat() -> Result<()> {
        let _ = env_logger::builder().is_test(true).try_init();

        let mock_server = MockServer::start().await;
        Mock::given(method("HEAD"))
            .and(path("/hello"))
            .respond_with(ResponseTemplate::new(200).insert_header("content-length", "128"))
            .mount(&mock_server)
            .await;

        let mut builder = Builder::default();
        builder.endpoint(&mock_server.uri());
        builder.root("/");
        let op = Operator::new(builder.build()?);

        let bs = op.object("hello").metadata().await?;

        assert_eq!(bs.mode(), ObjectMode::FILE);
        assert_eq!(bs.content_length(), 128);
        Ok(())
    }
}
