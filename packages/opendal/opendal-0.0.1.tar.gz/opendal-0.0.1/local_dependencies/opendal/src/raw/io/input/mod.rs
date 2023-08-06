// Copyright 2023 Datafuse Labs.
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

//! `input` provides traits and types that opendal accepts as input.
//!
//! Most of them are just alias to `futures::AsyncRead` or `std::io::Read`.
//! They are provided for convenient and will not have actual logic.

mod read;
pub use read::Read;
pub use read::Reader;

mod blocking_read;
pub use blocking_read::BlockingRead;
pub use blocking_read::BlockingReader;

mod write;
pub use write::Write;
pub use write::Writer;

mod stream;
pub use stream::Stream;
pub use stream::Streamer;

mod sink;
pub use sink::Sink;

pub mod into_reader;

mod into_writer;
pub use into_writer::into_writer;

mod into_sink;
pub use into_sink::into_sink;

mod into_stream;
pub use into_stream::into_stream;
