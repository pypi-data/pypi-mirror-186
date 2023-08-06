# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/)
and this project adheres to [Semantic Versioning](https://semver.org/).

## [v0.25.0] - 2023-01-18

### Added

- feat: Add dns cache for std dns resolver (#1191)
- feat: Allow setting http client that built from external (#1192)
- feat: Implement BlockingObjectReader (#1194)

### Changed

- chore(deps): replace dotenv with dotenvy (#1187)
- refactor: Avoid calling detect region if we know the region (#1188)
- chore: ensure minimal version buildable (#1193)

## [v0.24.6] - 2023-01-12

### Added

- feat: implement tokio::io::{AsyncRead, AsyncSeek} for ObjectReader (#1175)
- feat(services/hdfs): Evaluating the new async implementation (#1176)
- feat(services/ghac): Handling too many requests error (#1181)

### Fixed

- doc: fix name change in README (#1179)


## [v0.24.5] - 2023-01-09

### Fixed

- fix(services/memcached): TcpStream should only accept host:port (#1170)

## [v0.24.4] - 2023-01-09

### Added

- feat: Add presign endpoint option for OSS (#1135)
- feat: Reset state while returning error so that we can retry IO (#1166)

### Changed

- chore(deps): update base64 requirement from 0.20 to 0.21 (#1164)

### Fixed

- fix: Memcached can't work on windows (#1165)

## [v0.24.3] - 2023-01-09

### Added

- feat: Implement memcached service support (#1161)

## [v0.24.2] - 2023-01-08

### Changed

- refactor: Use dep: to make our features more clean (#1153)

### Fixed

- fix: ghac shall return ObjectAlreadyExists for writing the same path (#1156)
- fix: futures read_to_end will lead to performance regression (#1158)

## [v0.24.1] - 2023-01-08

### Fixed

- fix: Allow range_read to be retired (#1149)

## [v0.24.0] - 2023-01-07

### Added

- Add support for SAS tokens in Azure blob storage (#1124)
- feat: Add github action cache service support (#1111)
- docs: Add docs for ghac service (#1126)
- feat: Implement offset seekable reader for zero cost read (#1133)
- feat: Implement fuzz test on ObjectReader (#1140)

### Changed

- chore(deps): update quick-xml requirement from 0.26 to 0.27 (#1101)
- ci: Enable rust cache for CI (#1107)
- deps(oay,oli): Update dependences of oay and oli (#1122)
- refactor: Only add content length hint if we already know length (#1123)
- refactor: Redesign outpu bytes reader trait (#1127)
- refactor: Remove open related APIs (#1129)
- refactor: Merge and cleanup io & io_util modules (#1136)

### Fixed

- ci: Fix build for oay and oli (#1097)
- fix: Fix rustls support for suppaftp (#1102)
- fix(services/ghac): Fix pkg version not used correctly (#1125)

## [v0.23.0] - 2022-12-22

### Added

- feat: Implement object handler so that we can do seek on file (#1091)
- feat: Implement blocking for hdfs (#1092)
- feat(services/hdfs): Implement open and blocking open (#1093)
- docs: Add mozilla/sccache into projects (#1094)

## [v0.22.6] - 2022-12-20

### Added

- feat(io): make BlockingBytesRead Send + Sync (#1083)
- feat(fs): skip seek if offset is 0 (#1082)
- RFC-1085: Object Handler (#1085)
- feat(services/s3,gcs): Allow accepting signer directly (#1087)

## [v0.22.5] - 2022-12-13

### Added

- feat: Add service account support for gcs (#1076)

## [v0.22.4] - 2022-12-13

### Added

- improve blocking read use read_to_end (#1072)
- feat(services/gcs): Fully implement default credential support (#1073)

### Fixed

- fix: read a large range without error and add test (#1068)
- fix(services/oss): Enable standard behavior for oss range (#1070)

## [v0.22.3] - 2022-12-11

### Added

- feat(layers/metrics): Merge error and failure counters together (#1058)
- feat: Set MSRV to 1.60 (#1060)
- feat: Add unwind safe flag for operator (#1061)
- feat(azblob): Add build from connection string support (#1064)

### Fixed

- fix(services/moka): Don't print all content in cache (#1057)

## [v0.22.2] - 2022-12-07

### Added

- feat(presign): support presign head method for s3 and oss (#1049)

## [v0.22.1] - 2022-12-05

### Fixed

- fix(services/s3): Allow disable loading from imds_v2 and assume_role (#1044)

## [v0.22.0] - 2022-12-05

### Added

- feat: improve temp file organization when enable atomic write in fs (#1017)
- feat: Allow configure LoggingLayer's level (#1021)
- feat: Enable users to specify the cache policy (#1024)
- feat: Implement presign for oss (#1035)

### Changed

- refactor: Polish error handling of different services (#1018)
- refactor: Merge metadata and content cache together (#1020)
- refactor(layer/cache): Allow users implement cache by themselves (#1040)

### Fixed

- fix(services/fs): Make sure writing file is truncated (#1036)

## [v0.21.2] - 2022-11-27

### Added

- feat: Add azdfs support (#1009)
- feat: Set MSRV of opendal to 1.60 (#1012)

### Docs

- docs: Fix docs for azdfs service (#1010)

## [v0.21.1] - 2022-11-26

### Added

- feat: Export ObjectLister as public type (#1006)

### Changed

- deps: Remove not used thiserror and num-trait (#1005)

## [v0.21.0] - 2022-11-25

### Added

- docs: Add greptimedb and mars into projects (#975)
- RFC-0977: Refactor Error (#977)
- feat: impl atomic write for fs service (#991)
- feat: Add OperatorMetadata to avoid expose AccessorMetadata (#997)
- feat: Improve display for error (#1002)

### Changed

- refactor: Use seperate Error instead of std::io::Error to avoid confusing (#976)
- refactor: Return ReplyCreate for create operation (#981)
- refactor: Add ReplyRead for read operation (#982)
- refactor: Add RpWrite for write operation (#983)
- refactor: Add RpStat for stat operation (#984)
- refactor: Add RpDelete for delete operations (#985)
- refactor: Add RpPresign for presign operation (#986)
- refactor: Add reply for all multipart operations (#988)
- refactor: Add Reply for all blocking operations (#989)
- refactor: Avoid accessor in object entry (#992)
- refactor: Move accessor into raw apis (#994)
- refactor: Move io to raw (#996)
- refactor: Move {path,wrapper,http_util,io_util} into raw modules (#998)
- refactor: Move ObjectEntry and ObjectPage into raw (#999)
- refactor: Accept Operator intead of `Arc<dyn Accessor>` (#1001)

### Fixed

- fix: RetryAccessor is too verbose (#980)

## [v0.20.1] - 2022-11-18

### Added

- feat: Implement blocking operations for cache services (#970)

### Fixed

- fix: Use std Duration as args instead (#966)
- build: Make opendal buildable on 1.60 (#968)
- fix: Avoid cache missing after write (#971)

## [v0.20.0] - 2022-11-17

### Added

- RFC-0926: Object Reader (#926)
- feat: Implement Object Reader (#928)
- feat(services/s3): Return Object Meta for Read operation (#932)
- feat: Implement Bytes Content Range (#933)
- feat: Add Content Range support in ObjectMetadata (#935)
- feat(layers/content_cache): Implement WholeCacheReader (#936)
- feat: CompressAlgorithm derive serde. (#939)
- feat: Allow using opendal without tls support (#945)
- refactor: Refactor OpRead with BytesRange (#946)
- feat: Allow using opendal with native tls support (#949)
- docs: add docs for tls dependencies features (#951)
- feat: Make ObjectReader content_length returned for all services (#954)
- feat(layers): Implement fixed content cache (#953)
- feat: Enable default_ttl support for redis (#960)

### Changed

- refactor: Return ObjectReader in Accessor::read (#929)
- refactor(oay,oli): drop unnecessary patch.crates-io from `Cargo.toml`
- refactor: Polish bytes range (#950)
- refactor: Use simplifed kv adapter instead (#959)

### Fixed

- fix(ops): Fix suffix range behavior of bytes range (#942)
- fix: Fix cache path not used correctly (#958)

## [v0.19.8] - 2022-11-13

### Added

- feat(services/moka): Use entry's bytes as capacity weigher (#914)
- feat: Implement rocksdb service (#913)

### Changed

- refactor: Reduce backend builder log level to debug (#907)
- refactor: Remove deprecated features (#920)
- refactor: use moka::sync::SegmentedCache (#921)

### Fixed

- fix(http): Check already read size before returning (#919)

## [v0.19.7] - 2022-10-31

### Added

- feat: Implement content type support for stat (#891)

### Changed

- refactor(layers/metrics): Holding all metrics handlers to avoid lock (#894)
- refactor(layers/metrics): Only update metrics while dropping readers (#896)

## [v0.19.6] - 2022-10-25

### Fixed

- fix: Metrics blocking reader doesn't handle operation correctly (#887)

## [v0.19.5] - 2022-10-24

### Added

- feat: add a feature named trust-dns (#879)
- feat: implement write_with (#880)
- feat: `content-type` configuration (#878)

### Fixed

- fix: Allow forward layers' acesser operations to inner (#884)

## [v0.19.4] - 2022-10-15

### Added

- feat: Improve into_stream by reduce zero byte fill (#864)
- debug: Add log for sync http client (#865)
- feat: Add debug log for finishing read (#867)
- feat: Try to use trust-dns-resolver (#869)
- feat: Add log for dropping reader and streamer (#870)

### Changed

- refactor: replace md5 with md-5 (#862)
- refactor: replace the hard code to X_AMZ_BUCKET_REGION constant (#866)

## [v0.19.3] - 2022-10-13

### Fixed

- fix: Retry for write is not implemented correctly (#860)

## [v0.19.2] - 2022-10-13

### Added

- feat(experiment): Allow user to config http connection pool (#843)
- feat: Add concurrent limit layer (#848)
- feat: Allow kv services implemented without list support (#850)
- feat: Implement service for moka (#852)
- docs: Add docs for moka service and concurrent limit layer (#857)

## [v0.19.1] - 2022-10-11

### Added

- feat: Allow retry read and write (#826)
- feat: Convert interrupted error to permanent after retry (#827)
- feat(services/ftp): Add connection pool for FTP (#832)
- feat: Implement retry for write operation (#831)
- feat: Bump reqsign to latest version (#837)
- feat(services/s3): Add role_arn and external_id for assume_role (#838)

### Changed

- test: accelerate behaviour test `test_list_rich_dir` (#828)

### Fixed

- fix: ObjectEntry returned in batch operator doesn't have corrent accessor (#839)
- fix: Accessor in layers not set correctly (#840)

## [v0.19.0] - 2022-10-08

### Added

- feat: Implement object page stream for services like s3 (#787)
- RFC-0793: Generic KV Services (#793)
- feat(services/kv): Implement Scoped Key (#796)
- feat: Add scan in KeyValueAccessor (#797)
- feat: Implement basic kv services support (#799)
- feat: Introduce kv adapter for opendal (#802)
- feat: Add integration test for redis (#804)
- feat: Add OSS Service Support (#801)
- feat: Add integration tests for OSS (#814)

### Changed

- refactor: Move object to mod (#786)
- refactor: Implement azblob dir stream based on ObjectPageStream (#790)
- refactor: Implement memory services by generic kv (#800)
- refactor: Don't expose backend to users (#816)
- tests: allow running tests when env is `true` (#818)
- refactor: Remove deprecated type aliases (#819)
- test: list rich dir (#820)

### Fixed

- fix(services/redis): MATCH can't handle correctly (#803)
- fix: Disable ipfs redirection (#809)
- fix(services/ipfs): Use ipfs files API to copy data (#811)
- fix(services/hdfs): Allow retrying would block (#815)

## [v0.18.2] - 2022-10-01

### Added

- feat: Enable retry layer by default (#781)

### Changed

- ci: Enable IPFS NoFecth to avoid networking timeout (#780)
- ci: Build all feature in release to prevent build failure under release profile (#783)

### Fixed

- fix: Fix build error under release profile (#782)

## [v0.18.1] - 2022-10-01

### Fixed

- fix(services/s3): Content MD5 not set during list (#775)
- test: Add a test for ObjectEntry metadata cache (#776)

## [v0.18.0] - 2022-10-01

### Added

- feat: Add Metadata Cache Layer (#739)
- feat: Bump reqsign version to 0.5 (#741)
- feat: Derive Hash, Eq, PartialEq for Operation (#749)
- feat: Make AccessorMetadata public so outer users can use (#750)
- feat: Expose AccessorCapability to users (#751)
- feat: Expose opendal's http util to users (#753)
- feat: Implement convert from PresignedRequest (#756)
- feat: Make ObjectMetadata setter public (#758)
- feat: Implement cached metadata for ObjectEntry (#761)
- feat: Assign unique name for memory backend (#769)

### Changed

- refactor: replace error::other with new_other_object_error (#738)
- chore(compress): log with trace level instead of debug. (#752)
- refactor: Rename DirXxxx to ObjectXxxx instead (#759)

### Fixed

- fix(http_util): Disable auto compress and enable http proxy (#731)
- deps: Fix build after bump deps of oli and oay (#766)

## [v0.17.4] - 2022-09-27

### Fixed

- fix(http_util): Allow retry more errors (#724)
- fix(services/ftp): Suffix endpoints with default port (#726)

## [v0.17.3] - 2022-09-26

### Added

- feat: Add SubdirLayer to allowing switch directory (#718)
- feat(layers/retry): Add warning log while retry happened (#721)

### Fixed

- fix: update metrics on result (#716)
- fix: SubdirLayer should handle dir correctly (#720)

## [v0.17.2] - 2022-09-26

### Add

- feat: implement basic cp command (#688)
- chore: also parse 'FTPS' to Scheme::Ftp (#704)

### Changed

- refactor: remove `enable_secure` in FTP service (#709)
- oli: refactor copy implementation (#710)

### Fixed

- fix: Handle slash normalized false positives properly (#702)
- fix: Tracing is too verbose (#707)
- chore: fix error message in ftp service (#705)

## [v0.17.1] - 2022-09-19

### Added

- feat: redis service implement (#679)
- feat: Implement AsyncBufRead for IntoReader (#690)
- feat: expose security token of s3 (#693)

### Changed

- refactor: avoid unnecessary parent creating in Redis service (#692)
- refactor: Refactor HTTP Client to split sending and incoming logic (#695)

### Fixed

- fix: Handle write data in async way for IPMFS (#694)

## [v0.17.0] - 2022-09-15

### Added

- RFC: Path In Accessor (#661)
- feat: Implement RFC-0661: Path In Accessor (#664)
- feat: Hide http client internal details from users (#672)
- feat: make rustls the default tls implementation (#674)
- feat: Implement benches for layers (#681)

### Docs

- docs: Add how to implement service docs (#665)
- refactor: update redis support rfc (#676)
- docs: update metrics documentation (#684)

### Fixed

- fix: Immutable Index Layer could return duplicated pathes (#671)
- fix: Remove not needed type parameter for immutable_layer (#677)
- fix: Don't trace buf field in poll_read (#682)
- fix: List non-exist dir should return empty (#683)
- fix: Add path validation for fs backend (#685)

## [v0.16.0] - 2022-09-12

### Added

- feat: Implement tests for read-only services (#634)
- feat(services/ftp): Implemented multi connection (#637)
- feat: Finalize FTP read operation (#644)
- feat: Implement service for IPFS HTTP Gateway (#645)
- feat: Add ImmutableIndexLayer (#651)
- feat: derive Hash for Scheme (#653)
- feat(services/ftp): Setup integration tests (#648)

### Changed

- refactor: Migrate all behavior tests to capability based (#635)
- refactor: Remove list support from http service (#639)
- refactor: Replace isahc with reqwest and ureq (#642)

## Deps

- deps: Bump reqsign to v0.4 (#643)
- deps: Remove not used features (#658)
- chore(deps): Update criterion requirement from 0.3 to 0.4 (#656)
- chore(deps): Update quick-xml requirement from 0.24 to 0.25 (#657)

### Docs

- docs: Add docs for ipfs (#649)
- docs: Fix typo (#650)
- docs: Add docs for ftp services (#655)

## RFCs

- RFC-0623: Redis Service (#623)

## [v0.15.0] - 2022-09-05

### Added

- RFC-0599: Blocking API (#599)
- feat: Add blocking API in Accessor (#604)
- feat: Implement blocking API for fs (#606)
- feat: improve observability of `BytesReader` and `DirStreamer` (#603)
- feat: Add behavior tests for blocking operations (#607)
- feat: Add integration tests for ipfs (#610)
- feat: implemented ftp backend (#581)
- RFC-0627: Split Capabilities (#627)

### Changed

- refactor: Extrace normalize_root functions (#619)
- refactor: Extrace build_abs_path and build_rooted_abs_path (#620)
- refactor: Extract build_rel_path (#621)
- feat: Rename ipfs to ipmfs to better reflect its naming (#629)

## [v0.14.1] - 2022-08-30

### Added

- feat: Add IPFS backend (#481)
- refactor: IPFS service cleanup (#590)

### Docs

- docs: Add obs in OpenDAL lib docs (#585)

### Fixed

- fix(services/s3): If input range is `0..`, don't insert range header (#592)

## [v0.14.0] - 2022-08-28

### Added

- RFC-0554: Write Refactor (#554)
- feat: Implement huaweicloud obs service other op support (#557)
- feat: Add new operations in Accessor (#564)
- feat: Implement obs create and write (#565)
- feat(services/s3): Implement Multipart support (#571)
- feat: Implement MultipartObject public API (#574)
- feat: Implement integration tests for multipart (#575)
- feat: Implement presign for write multipart (#576)
- test: Add assert of public struct size (#578)
- feat: List metadata reuse (#577)
- feat: Implement integration test for obs (#572)

### Changed

- refactor(ops): Promote ops as a parent mod (#553)
- refactor: Implement RFC-0554 Write Refactor (#556)
- refactor: Remove all unused qualifications (#560)
- refactor: Fix typo in azblob backend (#569)
- refactor: change ObjectError's op from &'static str to Operation (#580)

### Deleted

- refactor: Remove deprecated APIs (#582)

### Docs

- docs: Add docs for obs service (#579)

## [v0.13.1] - 2022-08-22

### Added

- feat: Add walk for BatchOperator (#543)
- feat: Mark Scheme non_exhaustive and extendable (#544)
- feat: Try to limit the max_connections for http client (#545)
- feat: Implement huaweicloud obs service read support (#540)

### Docs

- docs: Fix gcs is missing from index (#546)

## [v0.13.0] - 2022-08-17

### Added

- feat: Refactor metrics and hide under feature layers-metrics (#521)
- feat(layer): Add TracingLayer support (#523)
- feature: Google Cloud Storage support skeleton (#513)
- feat: Add LoggingLayer to replace service internal logs (#526)
- feat: Implement integration tests for gcs (#532)
- docs: Add docs for new layers (#534)
- docs: Add docs for gcs backend (#535)

### Changed

- refactor: Rewrite retry layer support (#522)

### Fixed

- fix: Make ProtocolViolation a retryable error (#528)

## [v0.12.0] - 2022-08-12

### Added

- RFC-0501: New Builder (#501)
- feat: Implement RFC-0501 New Builder (#510)

### Changed

- feat: Use isahc to replace hyper (#471)
- refactor: make parse http error code public (#511)
- refactor: Extrace new http error APIs (#515)
- refactor: Simplify the error response parse logic (#516)

### Removed

- refactor: Remove deprecated struct Metadata (#503)

## [v0.11.4] - 2022-08-02

### Added

- feat: Support using rustls for TLS (#491)

### Changed

- feat: try to support epoll (#478)
- deps: Lower the requirement of deps (#495)
- Revert "feat: try to support epoll" (#496)

### Fixed

- fix: Uri encode continuation-token before signing (#494)

### Docs

- docs: Add downloads in README (#485)
- docs: Update slogan for OpenDAL (#486)

## [v0.11.3] - 2022-07-26

### Changed

- build: Remove not used features (#472)

### Fixed

- fix: Disable connection pool as workaround for async runtime hang (#474)

### Dependencies

- chore(deps): Bump clap from 3.2.12 to 3.2.15 in /oay (#461)
- chore(deps): Bump clap from 3.2.12 to 3.2.15 in /oli (#460)
- chore(deps): Update metrics requirement from 0.19.0 to 0.20.0 (#462)
- chore(deps): Bump tokio from 1.20.0 to 1.20.1 in /oay (#468)

## [v0.11.2] - 2022-07-19

### Fixed

- fix: Service HTTP deosn't handle dir correctly (#455)
- fix: Service HTTP inserted with wrong key (#457)

## [v0.11.1] - 2022-07-19

### Added

- RFC-0438: Multipart (#438)
- RFC-0443: Gateway (#443)
- feat: Add basic oay support for http (#445)
- feat: BytesRange supports parsing from range and content-range (#449)
- feat(oay): Implement range support (#450)
- feat(services-http): Implement write and delete for testing (#451)

## [v0.11.0] - 2022-07-11

### Added

- feat: derive Deserialize/Serialize for ObjectMetaData (#420)
- RFC-0423: Command Line Interface (#423)
- feat: optimize range read (#425)
- feat(oli): Add basic layout for oli (#426)
- RFC-0429: Init From Iter (#429)
- feat: Implement RFC-0429 Init From Iter (#432)
- feat(oli): Add cp command layout (#428)

### Docs

- docs: Update description of OpenDAL (#434)

## [v0.10.0] - 2022-07-04

### Added

- RFC-0409: Accessor Capabilities (#409)
- feat: Implement RFC-0409 Accessor Capabilities (#411)
- RFC-0413: Presign (#413)
- feat: Implement presign support for s3 (#414)

### Docs

- docs: Add new RFCs in list (#415)

### Dependencies

- chore(deps): Update reqsign requirement from 0.1.1 to 0.2.0 (#412)

## [v0.9.1] - 2022-06-27

### Added

- feat(object): Add ETag support (#381)
- feat: Convert retryable hyper errors into Interrupted (#396)

### Changed

- build: Exclude docs from publish (#383)
- ci: Don't run CI on not needed push (#395)
- refactor: Use list for check instead of stat (#399)

### Dependencies

- chore(deps): Update size requirement from 0.1.2 to 0.2.0 (#385)
- Upgrade dev-dependency `size` to 0.4 (#392)

### Fixed

- fix: Special chars not handled correctly (#398)

## [v0.9.0] - 2022-06-14

### Added

- feat: Implement http service support (#368)
- feat: Add http_header to handle HTTP header parse (#369)
- feat(services/s3): Add virtual host API style support (#374)

### Changed

- refactor: Use the same http client across project (#364)
- refactor(services/{s3,azblob}): Make sure error response parsed correctly and safely (#375)

### Docs

- docs: Add concepts for Accessor, Operator and Object (#354)
- docs: Aad docs for batch operations (#363)

## [v0.8.0] - 2022-06-09

### Added

- RFC-0337: Dir Entry (#337)
- feat: Implement RFC-0337: Dir Entry (#342)
- feat: Add batch operation support (#346)

### Changed

- refactor: Rename Metadata to ObjectMetadata for clearify (#339)

### Others

- chore(deps): Bump actions/setup-python from 3 to 4 (#343)
- chore(deps): Bump amondnet/vercel-action from 20 to 25 (#344)

## [v0.7.3] - 2022-06-03

### Fixed

- fix(services/s3,hdfs): List empty dir should not return itself (#327)
- fix(services/hdfs): Root path not cleaned correctly (#330)

## [v0.7.2] - 2022-06-01

### Added

- feat(io_util): Improve debug logging for compress (#310)
- feat(services/s3): Add disable_credential_loader support (#317)
- feat: Allow check user input (#318)
- docs: Add services and features docs (#319)
- feat: Add name to object metadata (#304)
- fix(io_util/compress): Fix decoder's buf not all consumed (#323)

### Changed

- chore(deps): Update metrics requirement from 0.18.1 to 0.19.0 (#314)
- docs: Update README to reflect current status (#321)
- refactor(object): Make Metadata::name() return &str (#322)

### Fixed

- docs: Fix typo in examples (#320)
- fix(services): Don't throw error message for stat operation (#324)

## [v0.7.1] - 2022-05-29

### Fixed

- publish: Fix git version not allowed (#306)
- fix(io_util/compress): Decompress read exit too early (#308)

## [v0.7.0] - 2022-05-29

### Added

- feat: Add support for blocking decompress_read (#289)
- feat: Add check for operator (#290)
- docs: Use mdbook to generate documentation (#291)
- proposal: Object ID (#293)
- feat: Implement operator metadata support (#296)
- feat: Implement RFC-0293 Object ID (#298)

### Changed

- chore(deps): Update quick-xml requirement from 0.22.0 to 0.23.0 (#286)
- feat(io_util): Refactor decompress decoder (#302)
- ci: Adopt amondnet/vercel-action (#303)

### Fixed

- fix(services/aws): Increase retry times for AWS STS (#299)

## [v0.6.3] - 2022-05-25

### Added

- ci: Add all issues into databend-storage project (#277)
- feat(services/s3): Add retry in load_credential (#281)
- feat(services): Allow endpoint has trailing slash (#282)
- feat(services): Attach more context in error messages (#283)

## [v0.6.2] - 2022-05-12

### Fixed

- fix(azblob): Request URL not construct correctly (#270)

## [v0.6.1] - 2022-05-09

### Added

- feat: Add hdfs scheme (#266)

## [v0.6.0] - 2022-05-07

### Added

- docs: Improve docs to 100% coverage (#246)
- RFC-0247: Retryable Error (#247)
- feat: Implement retry layers (#249)
- feat: Implement retryable errors for azblob and s3 (#254)
- feat: Implement hdfs service support (#255)
- docs: Add docs for hdfs services (#262)

### Changed

- docs: Make sure code examples are formatted (#251)
- chore(deps): Update uuid requirement from 0.8.2 to 1.0.0 (#252)
- refactor: Remove deprecated modules (#259)

### Fixed

- ci: Fix docs build (#260)
- fix: HDFS jar not load (#261)

## [v0.5.2] - 2022-04-08

### Changed

- chore: Build all features for docs.rs (#238)
- ci: Enable auto dependence upgrade (#239)
- chore(deps): Bump actions/checkout from 2 to 3 (#240)
- docs: Refactor examples (#241)

### Fixed

- fix(services/s3): Endpoint without scheme should also supported (#242)

## [v0.5.1] - 2022-04-08

### Added

- docs: Add behavior docs for create operation (#235)

### Fixed

- fix(services/fs): Create on existing dir should succeed (#234)

## [v0.5.0] - 2022-04-07

### Added

- feat: Improve error message (#220)
- RFC-0221: Create Dir (#221)
- feat: Simplify create API (#225)
- feat: Implement decompress read support (#227)
- ci: Enable behavior test for azblob (#229)
- docs: Add docs for azblob's public structs (#230)

### Changed

- refactor: Move op.objects() to o.list() (#224)
- refactor: Improve behavior_tests so that cargo test works without --all-features (#231)

### Fixed

- fix: Azblob should pass all behavior tests now (#228)

## [v0.4.2] - 2022-04-03

### Added

- feat: Add seekable_reader on Object (#215)

### Fixed

- fix: Object last_modified should carry timezone (#217)

## [v0.4.1] - 2022-04-02

### Added

- feat: Export SeekableReader (#212)

## [v0.4.0] - 2022-04-02

**Refer to [Upgrade](./docs/upgrade.md) `From v0.3 to v0.4` section for more upgrade details.**

### Added

- feat(services/azblob): Implement list support (#193)
- feat: Implement io_util like into_sink and into_stream (#197)
- docs: Add docs for all newly added public functions (#199)
- feat(io_util): Implement observer for sink and stream (#198)
- docs: Add docs for public types (#206)

### Changed

- refactor: Make read return BytesStream instead (#192)
- RFC-0191: Async Streaming IO (#191)
- refactor: New public API design (#201)
- refactor: Adopt io::Result instead (#204)
- refactor: Rollback changes around async streaming io (#205)
- refactor: Refactor behavior tests with macro_rules (#207)

### Fixed

- deps: Bump to reqsign to fix s3 url encode issue (#202)

### Removed

- RFC-0203: Remove Credential (#203)

## [v0.3.0] - 2022-03-25

### Added

- feat: Add azure blob support (#165)
- feat: Add tracing support via minitrace (#175)
- feat(service/s3): Implement server side encryption support (#182)

### Changed

- chore: Level down some log entry to debug (#181)

### Fixed

- fix(service/s3): Endpoint template should be applied if region exists (#180)

## [v0.2.5] - 2022-03-22

### Added

- feat: Adopt quick_xml to parse xml (#164)
- test: Add behavior test for not exist object (#166)
- feat: Allow user input region (#168)

## Changed

- feat: Improve error handle for s3 service (#169)
- feat: Read error response for better debugging (#170)
- examples: Improve examples for s3 (#171)

## [v0.2.4] - 2022-03-18

### Added

- feat: Add content_md5 and last_modified in metadata (#158)

### Changed

- refactor: Say goodbye to aws-s3-sdk (#152)

## [v0.2.3] - 2022-03-14

### Added

- feat: Export BoxedObjectStream so that users can implement Layer (#147)

## [v0.2.2] - 2022-03-14

### Fixed

- services/fs: Refactor via tokio::fs (#142)
- fix: Stat root should return a dir object (#143)

## [v0.2.1] - 2022-03-10

### Added

- \*: Implement logging support (#122)
- feat(service): Add service memory read support (#121)
- services: Add basic metrics (#127)
- services: Add full memory support (#134)

### Changed

- benches: Refactor to support more read pattern (#126)
- services: Refactor into directories (#131)

### Docs

- docs: Cover all public types and functions (#128)
- docs: Update README (#129)
- ci: Generate main docs to <opendal.databend.rs> (#132)
- docs: Enrich README (#133)
- Add examples for object (#135)

## [v0.2.0] - 2022-03-08

### Added

- RFC-112: Path Normalization (#112)
- examples: Add more examples for services and operations (#113)

### Changed

- benches: Refactor to make code more readable (#104)
- object: Refactor ObjectMode into enum (#114)

## [v0.1.4] - 2022-03-04

### Added

- services/s3: Implement anonymous read support (#97)
- bench: Add parallel_read bench (#100)
- services/s3: Add test for anonymous support (#99)

## [v0.1.3] - 2022-03-02

### Added

- RFC and implementations for limited reader (#90)
- readers: Implement observe reader support (#92)

### Changed

- deps: Bump s3 sdk to 0.8 (#87)
- bench: Improve logic (#89)

### New RFCs

- [limited_reader](https://github.com/datafuselabs/opendal/blob/main/docs/rfcs/0090-limited-reader.md)

## [v0.1.2] - 2022-03-01

### Changed

- object: Polish API for Metadata (#80)

## [v0.1.1] - 2022-03-01

### Added

- RFC and implementation of feature Object Stream (#69)
- services/s3: Implement List support (#76)
- credential: Add Plain variant to allow more input (#78)

### Changed

- backend/s3: Change from lazy_static to once_cell (#62)
- backend/s3: Enable test on AWS S3 (#64)

## [v0.1.0] - 2022-02-24

### Added

- docs: Add README for behavior test and ops benchmarks (#53)
- RFC-0057: Auto Region (#57)
- backend/s3: Implement RFC-57 Auto Region (#59)

### Changed

- io: Rename BoxedAsyncRead to BoxedAsyncReader (#55)
- \*: Refactor tests (#60)

## [v0.0.5] - 2022-02-23

### Fixed

- io: Remove not used debug print (#48)

## [v0.0.4] - 2022-02-23

### Added

- readers: Allow config prefetch size (#31)
- RFC-0041: Object Native API (#41)
- \*: Implement RFC-0041 Object Native API (#35)
- RFC-0044: Error Handle (#44)
- error: Implement RFC-0044 Error Handle (#43)

### Changed

- services/fs: Use separate dedicated thread pool instead (#42)

## [v0.0.3] - 2022-02-16

### Added

- benches: Implement benches for ops (#26)

### Changed

- services/s3: Don't load_from_env if users already inputs (#23)
- readers: Improve seekable performance (#25)

## [v0.0.2] - 2022-02-15

### Added

- tests: Implement behavior tests (#13)
- services/s3: Add support for endpoints without scheme (#15)
- tests: Implement integration tests for s3 (#18)

### Fixed

- services/s3: Allow set endpoint and region while input value is valid (#17)

## v0.0.1 - 2022-02-14

### Added

Hello, OpenDAL!

[v0.25.0]: https://github.com/datafuselabs/opendal/compare/v0.24.6...v0.25.0
[v0.24.6]: https://github.com/datafuselabs/opendal/compare/v0.24.5...v0.24.6
[v0.24.5]: https://github.com/datafuselabs/opendal/compare/v0.24.4...v0.24.5
[v0.24.4]: https://github.com/datafuselabs/opendal/compare/v0.24.3...v0.24.4
[v0.24.3]: https://github.com/datafuselabs/opendal/compare/v0.24.2...v0.24.3
[v0.24.2]: https://github.com/datafuselabs/opendal/compare/v0.24.1...v0.24.2
[v0.24.1]: https://github.com/datafuselabs/opendal/compare/v0.24.0...v0.24.1
[v0.24.0]: https://github.com/datafuselabs/opendal/compare/v0.23.0...v0.24.0
[v0.23.0]: https://github.com/datafuselabs/opendal/compare/v0.22.6...v0.23.0
[v0.22.6]: https://github.com/datafuselabs/opendal/compare/v0.22.5...v0.22.6
[v0.22.5]: https://github.com/datafuselabs/opendal/compare/v0.22.4...v0.22.5
[v0.22.4]: https://github.com/datafuselabs/opendal/compare/v0.22.3...v0.22.4
[v0.22.3]: https://github.com/datafuselabs/opendal/compare/v0.22.2...v0.22.3
[v0.22.2]: https://github.com/datafuselabs/opendal/compare/v0.22.1...v0.22.2
[v0.22.1]: https://github.com/datafuselabs/opendal/compare/v0.22.0...v0.22.1
[v0.22.0]: https://github.com/datafuselabs/opendal/compare/v0.21.2...v0.22.0
[v0.21.2]: https://github.com/datafuselabs/opendal/compare/v0.21.1...v0.21.2
[v0.21.1]: https://github.com/datafuselabs/opendal/compare/v0.21.0...v0.21.1
[v0.21.0]: https://github.com/datafuselabs/opendal/compare/v0.20.1...v0.21.0
[v0.20.1]: https://github.com/datafuselabs/opendal/compare/v0.20.0...v0.20.1
[v0.20.0]: https://github.com/datafuselabs/opendal/compare/v0.19.8...v0.20.0
[v0.19.8]: https://github.com/datafuselabs/opendal/compare/v0.19.7...v0.19.8
[v0.19.7]: https://github.com/datafuselabs/opendal/compare/v0.19.6...v0.19.7
[v0.19.6]: https://github.com/datafuselabs/opendal/compare/v0.19.5...v0.19.6
[v0.19.5]: https://github.com/datafuselabs/opendal/compare/v0.19.4...v0.19.5
[v0.19.4]: https://github.com/datafuselabs/opendal/compare/v0.19.3...v0.19.4
[v0.19.3]: https://github.com/datafuselabs/opendal/compare/v0.19.2...v0.19.3
[v0.19.2]: https://github.com/datafuselabs/opendal/compare/v0.19.1...v0.19.2
[v0.19.1]: https://github.com/datafuselabs/opendal/compare/v0.19.0...v0.19.1
[v0.19.0]: https://github.com/datafuselabs/opendal/compare/v0.18.2...v0.19.0
[v0.18.2]: https://github.com/datafuselabs/opendal/compare/v0.18.1...v0.18.2
[v0.18.1]: https://github.com/datafuselabs/opendal/compare/v0.18.0...v0.18.1
[v0.18.0]: https://github.com/datafuselabs/opendal/compare/v0.17.4...v0.18.0
[v0.17.4]: https://github.com/datafuselabs/opendal/compare/v0.17.3...v0.17.4
[v0.17.3]: https://github.com/datafuselabs/opendal/compare/v0.17.2...v0.17.3
[v0.17.2]: https://github.com/datafuselabs/opendal/compare/v0.17.1...v0.17.2
[v0.17.1]: https://github.com/datafuselabs/opendal/compare/v0.17.0...v0.17.1
[v0.17.0]: https://github.com/datafuselabs/opendal/compare/v0.16.0...v0.17.0
[v0.16.0]: https://github.com/datafuselabs/opendal/compare/v0.15.0...v0.16.0
[v0.15.0]: https://github.com/datafuselabs/opendal/compare/v0.14.1...v0.15.0
[v0.14.1]: https://github.com/datafuselabs/opendal/compare/v0.14.0...v0.14.1
[v0.14.0]: https://github.com/datafuselabs/opendal/compare/v0.13.1...v0.14.0
[v0.13.1]: https://github.com/datafuselabs/opendal/compare/v0.13.0...v0.13.1
[v0.13.0]: https://github.com/datafuselabs/opendal/compare/v0.12.0...v0.13.0
[v0.12.0]: https://github.com/datafuselabs/opendal/compare/v0.11.4...v0.12.0
[v0.11.4]: https://github.com/datafuselabs/opendal/compare/v0.11.3...v0.11.4
[v0.11.3]: https://github.com/datafuselabs/opendal/compare/v0.11.2...v0.11.3
[v0.11.2]: https://github.com/datafuselabs/opendal/compare/v0.11.1...v0.11.2
[v0.11.1]: https://github.com/datafuselabs/opendal/compare/v0.11.0...v0.11.1
[v0.11.0]: https://github.com/datafuselabs/opendal/compare/v0.10.0...v0.11.0
[v0.10.0]: https://github.com/datafuselabs/opendal/compare/v0.9.1...v0.10.0
[v0.9.1]: https://github.com/datafuselabs/opendal/compare/v0.9.0...v0.9.1
[v0.9.0]: https://github.com/datafuselabs/opendal/compare/v0.8.0...v0.9.0
[v0.8.0]: https://github.com/datafuselabs/opendal/compare/v0.7.3...v0.8.0
[v0.7.3]: https://github.com/datafuselabs/opendal/compare/v0.7.2...v0.7.3
[v0.7.2]: https://github.com/datafuselabs/opendal/compare/v0.7.1...v0.7.2
[v0.7.1]: https://github.com/datafuselabs/opendal/compare/v0.7.0...v0.7.1
[v0.7.0]: https://github.com/datafuselabs/opendal/compare/v0.6.3...v0.7.0
[v0.6.3]: https://github.com/datafuselabs/opendal/compare/v0.6.2...v0.6.3
[v0.6.2]: https://github.com/datafuselabs/opendal/compare/v0.6.1...v0.6.2
[v0.6.1]: https://github.com/datafuselabs/opendal/compare/v0.6.0...v0.6.1
[v0.6.0]: https://github.com/datafuselabs/opendal/compare/v0.5.2...v0.6.0
[v0.5.2]: https://github.com/datafuselabs/opendal/compare/v0.5.1...v0.5.2
[v0.5.1]: https://github.com/datafuselabs/opendal/compare/v0.5.0...v0.5.1
[v0.5.0]: https://github.com/datafuselabs/opendal/compare/v0.4.2...v0.5.0
[v0.4.2]: https://github.com/datafuselabs/opendal/compare/v0.4.1...v0.4.2
[v0.4.1]: https://github.com/datafuselabs/opendal/compare/v0.4.0...v0.4.1
[v0.4.0]: https://github.com/datafuselabs/opendal/compare/v0.3.0...v0.4.0
[v0.3.0]: https://github.com/datafuselabs/opendal/compare/v0.2.5...v0.3.0
[v0.2.5]: https://github.com/datafuselabs/opendal/compare/v0.2.4...v0.2.5
[v0.2.4]: https://github.com/datafuselabs/opendal/compare/v0.2.3...v0.2.4
[v0.2.3]: https://github.com/datafuselabs/opendal/compare/v0.2.2...v0.2.3
[v0.2.2]: https://github.com/datafuselabs/opendal/compare/v0.2.1...v0.2.2
[v0.2.1]: https://github.com/datafuselabs/opendal/compare/v0.2.0...v0.2.1
[v0.2.0]: https://github.com/datafuselabs/opendal/compare/v0.1.4...v0.2.0
[v0.1.4]: https://github.com/datafuselabs/opendal/compare/v0.1.3...v0.1.4
[v0.1.3]: https://github.com/datafuselabs/opendal/compare/v0.1.2...v0.1.3
[v0.1.2]: https://github.com/datafuselabs/opendal/compare/v0.1.1...v0.1.2
[v0.1.1]: https://github.com/datafuselabs/opendal/compare/v0.1.0...v0.1.1
[v0.1.0]: https://github.com/datafuselabs/opendal/compare/v0.0.5...v0.1.0
[v0.0.5]: https://github.com/datafuselabs/opendal/compare/v0.0.4...v0.0.5
[v0.0.4]: https://github.com/datafuselabs/opendal/compare/v0.0.3...v0.0.4
[v0.0.3]: https://github.com/datafuselabs/opendal/compare/v0.0.2...v0.0.3
[v0.0.2]: https://github.com/datafuselabs/opendal/compare/v0.0.1...v0.0.2
