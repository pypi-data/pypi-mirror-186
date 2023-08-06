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

//! Example for initiating a s3 backend with SSE-KMS and customer managed key.
use anyhow::Result;
use log::info;
use opendal::services::s3;
use opendal::services::s3::Builder;
use opendal::Operator;

#[tokio::main]
async fn main() -> Result<()> {
    let mut builder: Builder = s3::Builder::default();

    // Setup builders

    // Enable SSE-KMS with customer managed kms key
    builder.server_side_encryption_with_customer_managed_kms_key("aws_kms_key_id");

    let op = Operator::new(builder.build()?);
    info!("operator: {:?}", op);

    // Writing your testing code here.

    Ok(())
}
