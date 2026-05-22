# common/common.capnp
@0x99f1c9a775a88ac9;
$import "/capnp/c++.capnp".namespace("mas::schema::common");
$import "/capnp/python.capnp".module("mas.schema.common");
$import "/capnp/go.capnp".package("common");
$import "/capnp/go.capnp".import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/common");
struct IdInformation @0xd4cb7ecbfe03dad3 {  # 0 bytes, 3 ptrs
  id @0 :Text;  # ptr[0]
  name @1 :Text;  # ptr[1]
  description @2 :Text;  # ptr[2]
}
interface Identifiable @0xb2afd1cb599c48d5 {
  info @0 () -> IdInformation;
}
struct StructuredText @0xed6c098b67cad454 {  # 8 bytes, 1 ptrs
  value @0 :Text;  # ptr[0]
  type @1 :Type;  # bits[0, 16)
  enum Type @0x9eebc43e17b5974f {
    unstructured @0;
    json @1;
    xml @2;
    toml @3;
    sturdyRef @4;
    csv @5;
  }
}
struct MimeTypes @0xa2b2bec826cd860b {  # 0 bytes, 0 ptrs
  const textPlain @0xa1fb63f567498202 :Text = "text/plain";
  const textHtml @0xeabea137ffa10c15 :Text = "text/html";
  const textCss @0xc35c5dfa12865f7c :Text = "text/css";
  const textCsv @0xdb3c835eeaafc524 :Text = "text/csv";
  const textJavascript @0xb770f661310ffd5d :Text = "text/javascript";
  const textMarkdown @0xf58d4413623395b8 :Text = "text/markdown";
  const textXml @0x9b0f84052edbc30a :Text = "text/xml";
  const applicationJson @0xa727e0d037e26c2d :Text = "application/json";
  const applicationXml @0x89904b7af536f230 :Text = "application/xml";
  const applicationPdf @0xe2067bb8749f32f8 :Text = "application/pdf";
  const applicationZip @0xbda515c77765b8c7 :Text = "application/zip";
  const applicationGzip @0xfbecba511eb4d275 :Text = "application/gzip";
  const applicationOctetStream @0xb6356d9a0671045d :Text = "application/octet-stream";
  const applicationJavascript @0xa4fff2b2c27eb1aa :Text = "application/javascript";
  const applicationWwwFormUrlencoded @0xf995d3ab16e271ee :Text = "application/x-www-form-urlencoded";
  const multipartFormData @0xe67422806e9eecb5 :Text = "multipart/form-data";
  const applicationVndApacheParquet @0x95cca6eb99e82455 :Text = "application/vnd.apache.parquet";
  const imagePng @0x954d7d5f7e52aee7 :Text = "image/png";
  const imageJpeg @0xa3bb3ab5ca7f522a :Text = "image/jpeg";
  const imageGif @0xe437ea6ed9ab4e31 :Text = "image/gif";
  const imageWebp @0x9446d647f76db683 :Text = "image/webp";
  const imageSvgXml @0xfd19f3577d92b2e4 :Text = "image/svg+xml";
  const imageBmp @0x878346a0cd2d946b :Text = "image/bmp";
  const imageTiff @0xaa69086cb639c01e :Text = "image/tiff";
  const imageXIcon @0x8115df9f9ef5c669 :Text = "image/x-icon";
  const imageTiffApplicationGeotiff @0xb56ca4f1a1ce62fc :Text = "image/tiff; application=geotiff";
  const imageTiffApplicationGeotiffCloudOptimized @0x856fd18c6d9660fd :Text = "image/tiff; application=geotiff; profile=cloud-optimized";
  const audioMpeg @0xb9582bae43a84ae4 :Text = "audio/mpeg";
  const audioMp4 @0xa3268f2a2adebfa1 :Text = "audio/mp4";
  const audioOgg @0xdff6ea723d278fd9 :Text = "audio/ogg";
  const audioWav @0x83f67481e7528a12 :Text = "audio/wav";
  const audioWebm @0xffb7db5d8b8260c5 :Text = "audio/webm";
  const audioAac @0x93d7bda9c4270d55 :Text = "audio/aac";
  const videoMp4 @0x89128773fcfdfa42 :Text = "video/mp4";
  const videoMpeg @0xd45602e908076a86 :Text = "video/mpeg";
  const videoOgg @0xc5d6bde191c852d8 :Text = "video/ogg";
  const videoWebm @0xe9034d1b15d7aaa9 :Text = "video/webm";
  const videoQuicktime @0xce2ba2ab46a85910 :Text = "video/quicktime";
  const videoXMsVideo @0xd43a69da0d30ee9d :Text = "video/x-msvideo";
  const fontTtf @0xca9f97fd5c5b0a1c :Text = "font/ttf";
  const fontOtf @0xfd19908e527bebe9 :Text = "font/otf";
  const fontWoff @0xa40fb95abdef8710 :Text = "font/woff";
  const fontWoff2 @0xf69a9b0bb16714de :Text = "font/woff2";
}
struct Blob @0xc7180e2ef517a317 {  # 0 bytes, 2 ptrs
  contentType @0 :Text;  # ptr[0]
  data @1 :Data;  # ptr[1]
}
struct Value @0xe17592335373b246 {  # 16 bytes, 1 ptrs
  union {  # tag bits [64, 80)
    f64 @0 :Float64;  # bits[0, 64), union tag = 0
    f32 @1 :Float32;  # bits[0, 32), union tag = 1
    i64 @2 :Int64;  # bits[0, 64), union tag = 2
    i32 @3 :Int32;  # bits[0, 32), union tag = 3
    i16 @4 :Int16;  # bits[0, 16), union tag = 4
    i8 @5 :Int8;  # bits[0, 8), union tag = 5
    ui64 @6 :UInt64;  # bits[0, 64), union tag = 6
    ui32 @7 :UInt32;  # bits[0, 32), union tag = 7
    ui16 @8 :UInt16;  # bits[0, 16), union tag = 8
    ui8 @9 :UInt8;  # bits[0, 8), union tag = 9
    b @10 :Bool;  # bits[0, 1), union tag = 10
    t @11 :Text;  # ptr[0], union tag = 11
    d @12 :Data;  # ptr[0], union tag = 12
    p @13 :AnyPointer;  # ptr[0], union tag = 13
    cap @14 :Capability;  # ptr[0], union tag = 14
    lf64 @15 :List(Float64);  # ptr[0], union tag = 15
    lf32 @16 :List(Float32);  # ptr[0], union tag = 16
    li64 @17 :List(Int64);  # ptr[0], union tag = 17
    li32 @18 :List(Int32);  # ptr[0], union tag = 18
    li16 @19 :List(Int16);  # ptr[0], union tag = 19
    li8 @20 :List(Int8);  # ptr[0], union tag = 20
    lui64 @21 :List(UInt64);  # ptr[0], union tag = 21
    lui32 @22 :List(UInt32);  # ptr[0], union tag = 22
    lui16 @23 :List(UInt16);  # ptr[0], union tag = 23
    lui8 @24 :List(UInt8);  # ptr[0], union tag = 24
    lb @25 :List(Bool);  # ptr[0], union tag = 25
    lt @26 :List(Text);  # ptr[0], union tag = 26
    ld @27 :List(Data);  # ptr[0], union tag = 27
    lcap @28 :List(Capability);  # ptr[0], union tag = 28
    lpair @29 :List(Pair);  # ptr[0], union tag = 29
    lv @30 :List(Value);  # ptr[0], union tag = 30
  }
}
interface Factory @0xa869f50b8c586ed9 (Output) superclasses(Identifiable) {
  create @0 () -> (out :Output);
}
interface IOFactory @0x9771e5b5c6a27b68 (Input, Output) superclasses(Identifiable) {
  produce @0 (in :Input) -> (out :Output);
}
struct Pair @0xb9d4864725174733 (F, S) {  # 0 bytes, 2 ptrs
  fst @0 :F;  # ptr[0]
  snd @1 :S;  # ptr[1]
}
interface Holder @0xc83045ccbb0b6ac5 (T) {
  value @0 () -> (value :T);
}
interface IdentifiableHolder @0xee543d7c305d56f6 (T) superclasses(Identifiable, Holder(T)) {
}
