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

//! io Providing IO related functions like `into_sink`, `into_stream`.
//!
//! # NOTE
//!
//! This mod is not a part of OpenDAL's public API. We expose them out to make
//! it easier to develop services and layers outside opendal.

pub mod input;
pub mod output;

#[cfg(feature = "compress")]
mod compress;
#[cfg(feature = "compress")]
pub use compress::CompressAlgorithm;
#[cfg(feature = "compress")]
pub use compress::DecompressCodec;
#[cfg(feature = "compress")]
pub use compress::DecompressDecoder;
#[cfg(feature = "compress")]
pub use compress::DecompressReader;
#[cfg(feature = "compress")]
pub use compress::DecompressState;

mod walk;
pub use walk::BottomUpWalker;
pub use walk::TopDownWalker;
