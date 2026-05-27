# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `common.capnp`."""

from __future__ import annotations

# Load schemas and build module structure
from importlib import import_module
from typing import cast

from capnp.lib.capnp import SchemaLoader, _EnumModule, _InterfaceModule, _StructModule


def _import_schema_bundle() -> object:
    bundle_module_name = "_capnp_schema_bundle_65374570872b"
    try:
        return import_module(bundle_module_name)
    except ModuleNotFoundError as error:
        original_error = error
        package_name = __package__

    while package_name:
        try:
            return import_module(f"{package_name}.{bundle_module_name}")
        except ModuleNotFoundError:
            package_name = package_name.rpartition(".")[0]

    raise original_error


_schema_bundle = _import_schema_bundle()


def get_schema_by_id(schema_id: int) -> object:
    return cast("object", _schema_bundle.get_schema_by_id(schema_id))


def load_capnp_file(path: str, imports: list[str] | tuple[str, ...] = ()) -> object:
    return cast("object", _schema_bundle.load_capnp_file(path, imports))


_loader: SchemaLoader = cast("SchemaLoader", _schema_bundle.get_schema_loader())

# Build module structure inline

IdInformation = _StructModule(
    _loader.get(0xD4CB7ECBFE03DAD3).as_struct(),
    "IdInformation",
)
Identifiable = _InterfaceModule(
    _loader.get(0xB2AFD1CB599C48D5).as_interface(),
    "Identifiable",
)
StructuredText = _StructModule(
    _loader.get(0xED6C098B67CAD454).as_struct(),
    "StructuredText",
)
StructuredText.Type = _EnumModule(
    StructuredText.schema.fields["type"].schema,
    "Type",
)
MimeTypes = _StructModule(
    _loader.get(0xA2B2BEC826CD860B).as_struct(),
    "MimeTypes",
)
MimeTypes.textPlain = _loader.get(0xA1FB63F567498202).as_const_value()
MimeTypes.textHtml = _loader.get(0xEABEA137FFA10C15).as_const_value()
MimeTypes.textCss = _loader.get(0xC35C5DFA12865F7C).as_const_value()
MimeTypes.textCsv = _loader.get(0xDB3C835EEAAFC524).as_const_value()
MimeTypes.textJavascript = _loader.get(0xB770F661310FFD5D).as_const_value()
MimeTypes.textMarkdown = _loader.get(0xF58D4413623395B8).as_const_value()
MimeTypes.textXml = _loader.get(0x9B0F84052EDBC30A).as_const_value()
MimeTypes.applicationJson = _loader.get(0xA727E0D037E26C2D).as_const_value()
MimeTypes.applicationXml = _loader.get(0x89904B7AF536F230).as_const_value()
MimeTypes.applicationPdf = _loader.get(0xE2067BB8749F32F8).as_const_value()
MimeTypes.applicationZip = _loader.get(0xBDA515C77765B8C7).as_const_value()
MimeTypes.applicationGzip = _loader.get(0xFBECBA511EB4D275).as_const_value()
MimeTypes.applicationOctetStream = _loader.get(0xB6356D9A0671045D).as_const_value()
MimeTypes.applicationJavascript = _loader.get(0xA4FFF2B2C27EB1AA).as_const_value()
MimeTypes.applicationWwwFormUrlencoded = _loader.get(
    0xF995D3AB16E271EE,
).as_const_value()
MimeTypes.multipartFormData = _loader.get(0xE67422806E9EECB5).as_const_value()
MimeTypes.applicationVndApacheParquet = _loader.get(0x95CCA6EB99E82455).as_const_value()
MimeTypes.imagePng = _loader.get(0x954D7D5F7E52AEE7).as_const_value()
MimeTypes.imageJpeg = _loader.get(0xA3BB3AB5CA7F522A).as_const_value()
MimeTypes.imageGif = _loader.get(0xE437EA6ED9AB4E31).as_const_value()
MimeTypes.imageWebp = _loader.get(0x9446D647F76DB683).as_const_value()
MimeTypes.imageSvgXml = _loader.get(0xFD19F3577D92B2E4).as_const_value()
MimeTypes.imageBmp = _loader.get(0x878346A0CD2D946B).as_const_value()
MimeTypes.imageTiff = _loader.get(0xAA69086CB639C01E).as_const_value()
MimeTypes.imageXIcon = _loader.get(0x8115DF9F9EF5C669).as_const_value()
MimeTypes.imageTiffApplicationGeotiff = _loader.get(0xB56CA4F1A1CE62FC).as_const_value()
MimeTypes.imageTiffApplicationGeotiffCloudOptimized = _loader.get(
    0x856FD18C6D9660FD,
).as_const_value()
MimeTypes.audioMpeg = _loader.get(0xB9582BAE43A84AE4).as_const_value()
MimeTypes.audioMp4 = _loader.get(0xA3268F2A2ADEBFA1).as_const_value()
MimeTypes.audioOgg = _loader.get(0xDFF6EA723D278FD9).as_const_value()
MimeTypes.audioWav = _loader.get(0x83F67481E7528A12).as_const_value()
MimeTypes.audioWebm = _loader.get(0xFFB7DB5D8B8260C5).as_const_value()
MimeTypes.audioAac = _loader.get(0x93D7BDA9C4270D55).as_const_value()
MimeTypes.videoMp4 = _loader.get(0x89128773FCFDFA42).as_const_value()
MimeTypes.videoMpeg = _loader.get(0xD45602E908076A86).as_const_value()
MimeTypes.videoOgg = _loader.get(0xC5D6BDE191C852D8).as_const_value()
MimeTypes.videoWebm = _loader.get(0xE9034D1B15D7AAA9).as_const_value()
MimeTypes.videoQuicktime = _loader.get(0xCE2BA2AB46A85910).as_const_value()
MimeTypes.videoXMsVideo = _loader.get(0xD43A69DA0D30EE9D).as_const_value()
MimeTypes.fontTtf = _loader.get(0xCA9F97FD5C5B0A1C).as_const_value()
MimeTypes.fontOtf = _loader.get(0xFD19908E527BEBE9).as_const_value()
MimeTypes.fontWoff = _loader.get(0xA40FB95ABDEF8710).as_const_value()
MimeTypes.fontWoff2 = _loader.get(0xF69A9B0BB16714DE).as_const_value()
Blob = _StructModule(
    _loader.get(0xC7180E2EF517A317).as_struct(),
    "Blob",
)
Value = _StructModule(
    _loader.get(0xE17592335373B246).as_struct(),
    "Value",
)
Factory = _InterfaceModule(
    _loader.get(0xA869F50B8C586ED9).as_interface(),
    "Factory",
)
IOFactory = _InterfaceModule(
    _loader.get(0x9771E5B5C6A27B68).as_interface(),
    "IOFactory",
)
Pair = _StructModule(
    _loader.get(0xB9D4864725174733).as_struct(),
    "Pair",
)
Holder = _InterfaceModule(
    _loader.get(0xC83045CCBB0B6AC5).as_interface(),
    "Holder",
)
IdentifiableHolder = _InterfaceModule(
    _loader.get(0xEE543D7C305D56F6).as_interface(),
    "IdentifiableHolder",
)
