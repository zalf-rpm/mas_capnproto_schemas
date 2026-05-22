@0x99f1c9a775a88ac9;

using Cxx = import "/capnp/c++.capnp";
$Cxx.namespace("mas::schema::common");

using Python = import "/capnp/python.capnp";
$Python.module("mas.schema.common");

using Go = import "/capnp/go.capnp";
$Go.package("common");
$Go.import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/common");

struct IdInformation {
  id @0 :Text; # could be a UUID4
  name @1 :Text;
  description @2 :Text;
}

interface Identifiable {
  # interface to retrieve id information from an object
  info @0 () -> IdInformation;
}

struct StructuredText {
  # some structured text, always encoded in UTF-8

  value @0 :Text;
  # text stream

  enum Type {
    unstructured    @0;
    json            @1;
    xml             @2;
    toml            @3;
    sturdyRef       @4;
    csv             @5;
  }
  type @1 :Type = unstructured;
}

struct MimeTypes {
  const textPlain :Text = "text/plain";
  const textHtml :Text = "text/html";
  const textCss :Text = "text/css";
  const textCsv :Text = "text/csv";
  const textJavascript :Text = "text/javascript";
  const textMarkdown :Text = "text/markdown";
  const textXml :Text = "text/xml";

  const applicationJson :Text = "application/json";
  const applicationXml :Text = "application/xml";
  const applicationPdf :Text = "application/pdf";
  const applicationZip :Text = "application/zip";
  const applicationGzip :Text = "application/gzip";
  const applicationOctetStream :Text = "application/octet-stream";
  const applicationJavascript :Text = "application/javascript";
  const applicationWwwFormUrlencoded :Text = "application/x-www-form-urlencoded";
  const multipartFormData :Text = "multipart/form-data";

  const applicationVndApacheParquet :Text = "application/vnd.apache.parquet";

  const imagePng :Text = "image/png";
  const imageJpeg :Text = "image/jpeg";
  const imageGif :Text = "image/gif";
  const imageWebp :Text = "image/webp";
  const imageSvgXml :Text = "image/svg+xml";
  const imageBmp :Text = "image/bmp";
  const imageTiff :Text = "image/tiff";
  const imageXIcon :Text = "image/x-icon";

  # Full content types with parameters:
  const imageTiffApplicationGeotiff :Text =
      "image/tiff; application=geotiff";

  const imageTiffApplicationGeotiffCloudOptimized :Text =
      "image/tiff; application=geotiff; profile=cloud-optimized";

  const audioMpeg :Text = "audio/mpeg";
  const audioMp4 :Text = "audio/mp4";
  const audioOgg :Text = "audio/ogg";
  const audioWav :Text = "audio/wav";
  const audioWebm :Text = "audio/webm";
  const audioAac :Text = "audio/aac";

  const videoMp4 :Text = "video/mp4";
  const videoMpeg :Text = "video/mpeg";
  const videoOgg :Text = "video/ogg";
  const videoWebm :Text = "video/webm";
  const videoQuicktime :Text = "video/quicktime";
  const videoXMsVideo :Text = "video/x-msvideo";

  const fontTtf :Text = "font/ttf";
  const fontOtf :Text = "font/otf";
  const fontWoff :Text = "font/woff";
  const fontWoff2 :Text = "font/woff2";
}

struct Blob{
  contentType @0 :Text;
  data @1:Data;
}

struct Value {
  union {
    f64   @0    :Float64;
    f32   @1    :Float32;
    i64   @2    :Int64;
    i32   @3    :Int32;
    i16   @4    :Int16;
    i8    @5    :Int8;
    ui64  @6    :UInt64;
    ui32  @7    :UInt32;
    ui16  @8    :UInt16;
    ui8   @9    :UInt8;
    b     @10   :Bool;
    t     @11   :Text;
    d     @12   :Data;
    p     @13   :AnyPointer;
    cap   @14   :Capability;
    lf64  @15   :List(Float64);
    lf32  @16   :List(Float32);
    li64  @17   :List(Int64);
    li32  @18   :List(Int32);
    li16  @19   :List(Int16);
    li8   @20   :List(Int8);
    lui64 @21   :List(UInt64);
    lui32 @22   :List(UInt32);
    lui16 @23   :List(UInt16);
    lui8  @24   :List(UInt8);
    lb    @25   :List(Bool);
    lt    @26   :List(Text);
    ld    @27   :List(Data);
    lcap  @28   :List(Capability);
    lpair @29   :List(Pair);
    lv    @30   :List(Value);
  }
}

interface Factory(Output) extends(Identifiable) {
  # minimal interface to produce some output

  create @0 () -> (out :Output);
}

interface IOFactory(Input, Output) extends(Identifiable) {
  # minimal interface to produce some output from input

  produce @0 (in :Input) -> (out :Output);
}

struct Pair(F, S) {
  fst @0 :F;
  snd @1 :S;
}

#struct LL(H, T) {
#  head @0 :H;
#  tail @1 :T;
#}

#interface Clock(T) {
  # represents a syncronizing clock

#  tick @0 (time :T);
  # forward clock one step to time T (which could also be just a Common.Date)
#}

interface Holder(T) {
    # hold a value of type T

    value @0 () -> (value :T);
    # get the value being hold
}

interface IdentifiableHolder(T) extends(Identifiable, Holder(T)) {}
