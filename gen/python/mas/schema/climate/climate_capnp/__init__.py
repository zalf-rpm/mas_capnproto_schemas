# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `climate.capnp`."""

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

GCM = _EnumModule(
    _loader.get(0xCE396869EEDE9F10).as_enum(),
    "GCM",
)
RCM = _EnumModule(
    _loader.get(0x8671DEC53083E351).as_enum(),
    "RCM",
)
SSP = _EnumModule(
    _loader.get(0xD3780AE416347AEE).as_enum(),
    "SSP",
)
RCP = _EnumModule(
    _loader.get(0x8EF30778310C94CC).as_enum(),
    "RCP",
)
EnsembleMember = _StructModule(
    _loader.get(0xC8CAACD1CD5DA434).as_struct(),
    "EnsembleMember",
)
Metadata = _StructModule(
    _loader.get(0xFB36D2E966556DB0).as_struct(),
    "Metadata",
)
Metadata.Supported = _InterfaceModule(
    _loader.get(0xAB06444B30722E01).as_interface(),
    "Supported",
)
Metadata.Value = _StructModule(
    _loader.get(0xC48E24C968A234DB).as_struct(),
    "Value",
)
Metadata.Entry = _StructModule(
    Metadata.schema.fields["entries"].schema.elementType,
    "Entry",
)
Metadata.Information = _InterfaceModule(
    Metadata.schema.fields["info"].schema,
    "Information",
)
Dataset = _InterfaceModule(
    _loader.get(0xF635FDD1F05960F0).as_interface(),
    "Dataset",
)
Dataset.GetLocationsCallback = _InterfaceModule(
    Dataset.schema.methods["streamLocations"]
    .result_type.fields["locationsCallback"]
    .schema,  # pyright: ignore[reportUnknownArgumentType]
    "GetLocationsCallback",
)
MetaPlusData = _StructModule(
    _loader.get(0xD7A67FEC5F22E5A0).as_struct(),
    "MetaPlusData",
)
Element = _EnumModule(
    _loader.get(0xE35760B4DB5AB564).as_enum(),
    "Element",
)
Location = _StructModule(
    _loader.get(0x85BA7385F313FE19).as_struct(),
    "Location",
)
Location.KV = _StructModule(
    Location.schema.fields["customData"].schema.elementType,
    "KV",
)
TimeSeries = _InterfaceModule(
    _loader.get(0xA7769F40FE6E6DE8).as_interface(),
    "TimeSeries",
)
TimeSeries.Resolution = _EnumModule(
    _loader.get(0xB466CACF63EC03C2).as_enum(),
    "Resolution",
)
TimeSeriesData = _StructModule(
    _loader.get(0xF1C1CCF59BC6964F).as_struct(),
    "TimeSeriesData",
)
Service = _InterfaceModule(
    _loader.get(0xFE7D08D4352B0C5F).as_interface(),
    "Service",
)
CSVTimeSeriesFactory = _InterfaceModule(
    _loader.get(0xA418C26CC59929D9).as_interface(),
    "CSVTimeSeriesFactory",
)
CSVTimeSeriesFactory.CSVConfig = _StructModule(
    CSVTimeSeriesFactory.schema.methods["create"].param_type.fields["config"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "CSVConfig",
)
AlterTimeSeriesWrapper = _InterfaceModule(
    _loader.get(0xE1F480EF979784B2).as_interface(),
    "AlterTimeSeriesWrapper",
)
AlterTimeSeriesWrapper.Altered = _StructModule(
    AlterTimeSeriesWrapper.schema.methods["alteredElements"]
    .result_type.fields["list"]
    .schema.elementType,  # pyright: ignore[reportUnknownArgumentType]
    "Altered",
)
AlterTimeSeriesWrapper.AlterType = _EnumModule(
    AlterTimeSeriesWrapper.schema.methods["alteredElements"]
    .result_type.fields["list"]
    .schema.elementType.fields["type"]
    .schema,  # pyright: ignore[reportUnknownArgumentType]
    "AlterType",
)
AlterTimeSeriesWrapperFactory = _InterfaceModule(
    _loader.get(0xC5F12DF0A2A52744).as_interface(),
    "AlterTimeSeriesWrapperFactory",
)
