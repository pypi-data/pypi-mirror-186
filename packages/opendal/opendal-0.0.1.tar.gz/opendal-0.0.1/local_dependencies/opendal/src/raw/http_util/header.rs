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

use http::header::HeaderName;
use http::header::CONTENT_LENGTH;
use http::header::CONTENT_RANGE;
use http::header::CONTENT_TYPE;
use http::header::ETAG;
use http::header::LAST_MODIFIED;
use http::HeaderMap;
use time::format_description::well_known::Rfc2822;
use time::OffsetDateTime;

use crate::raw::*;
use crate::Error;
use crate::ErrorKind;
use crate::ObjectMetadata;
use crate::ObjectMode;
use crate::Result;

/// Parse content length from header map.
pub fn parse_content_length(headers: &HeaderMap) -> Result<Option<u64>> {
    match headers.get(CONTENT_LENGTH) {
        None => Ok(None),
        Some(v) => Ok(Some(
            v.to_str()
                .map_err(|e| {
                    Error::new(
                        ErrorKind::Unexpected,
                        "header value is not valid utf-8 string",
                    )
                    .with_operation("http_util::parse_content_length")
                    .set_source(e)
                })?
                .parse::<u64>()
                .map_err(|e| {
                    Error::new(ErrorKind::Unexpected, "header value is not valid integer")
                        .with_operation("http_util::parse_content_length")
                        .set_source(e)
                })?,
        )),
    }
}

/// Parse content md5 from header map.
pub fn parse_content_md5(headers: &HeaderMap) -> Result<Option<&str>> {
    match headers.get(HeaderName::from_static("content-md5")) {
        None => Ok(None),
        Some(v) => Ok(Some(v.to_str().map_err(|e| {
            Error::new(
                ErrorKind::Unexpected,
                "header value is not valid utf-8 string",
            )
            .with_operation("http_util::parse_content_md5")
            .set_source(e)
        })?)),
    }
}

/// Parse content type from header map.
pub fn parse_content_type(headers: &HeaderMap) -> Result<Option<&str>> {
    match headers.get(CONTENT_TYPE) {
        None => Ok(None),
        Some(v) => Ok(Some(v.to_str().map_err(|e| {
            Error::new(
                ErrorKind::Unexpected,
                "header value is not valid utf-8 string",
            )
            .with_operation("http_util::parse_content_type")
            .set_source(e)
        })?)),
    }
}

/// Parse content range from header map.
pub fn parse_content_range(headers: &HeaderMap) -> Result<Option<BytesContentRange>> {
    match headers.get(CONTENT_RANGE) {
        None => Ok(None),
        Some(v) => Ok(Some(
            v.to_str()
                .map_err(|e| {
                    Error::new(
                        ErrorKind::Unexpected,
                        "header value is not valid utf-8 string",
                    )
                    .with_operation("http_util::parse_content_range")
                    .set_source(e)
                })?
                .parse()?,
        )),
    }
}

/// Parse last modified from header map.
pub fn parse_last_modified(headers: &HeaderMap) -> Result<Option<OffsetDateTime>> {
    match headers.get(LAST_MODIFIED) {
        None => Ok(None),
        Some(v) => {
            let v = v.to_str().map_err(|e| {
                Error::new(
                    ErrorKind::Unexpected,
                    "header value is not valid utf-8 string",
                )
                .with_operation("http_util::parse_last_modified")
                .set_source(e)
            })?;
            let t = OffsetDateTime::parse(v, &Rfc2822).map_err(|e| {
                Error::new(
                    ErrorKind::Unexpected,
                    "header value is not valid rfc2822 time",
                )
                .with_operation("http_util::parse_last_modified")
                .set_source(e)
            })?;

            Ok(Some(t))
        }
    }
}

/// Parse etag from header map.
pub fn parse_etag(headers: &HeaderMap) -> Result<Option<&str>> {
    match headers.get(ETAG) {
        None => Ok(None),
        Some(v) => Ok(Some(v.to_str().map_err(|e| {
            Error::new(
                ErrorKind::Unexpected,
                "header value is not valid utf-8 string",
            )
            .with_operation("http_util::parse_etag")
            .set_source(e)
        })?)),
    }
}

/// parse_into_object_metadata will parse standards http headers into ObjectMetadata.
///
/// # Notes
///
/// parse_into_object_metadata only handles the standard behavior of http
/// headers. If services have their own logic, they should update the parsed
/// metadata on demand.
pub fn parse_into_object_metadata(path: &str, headers: &HeaderMap) -> Result<ObjectMetadata> {
    let mode = if path.ends_with('/') {
        ObjectMode::DIR
    } else {
        ObjectMode::FILE
    };
    let mut m = ObjectMetadata::new(mode);

    if let Some(v) = parse_content_length(headers)? {
        m.set_content_length(v);
    }

    if let Some(v) = parse_content_type(headers)? {
        m.set_content_type(v);
    }

    if let Some(v) = parse_content_range(headers)? {
        m.set_content_range(v);
    }

    if let Some(v) = parse_etag(headers)? {
        m.set_etag(v);
    }

    if let Some(v) = parse_content_md5(headers)? {
        m.set_content_md5(v);
    }

    if let Some(v) = parse_last_modified(headers)? {
        m.set_last_modified(v);
    }

    Ok(m)
}
