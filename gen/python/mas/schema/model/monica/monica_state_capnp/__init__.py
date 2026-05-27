# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `monica_state.capnp`."""

from __future__ import annotations

# Load schemas and build module structure
from importlib import import_module
from typing import cast

from capnp.lib.capnp import SchemaLoader, _StructModule


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

MaybeBool = _StructModule(
    _loader.get(0xD8AF9210839BC071).as_struct(),
    "MaybeBool",
)
RuntimeState = _StructModule(
    _loader.get(0xD599D06DC405571A).as_struct(),
    "RuntimeState",
)
CropState = _StructModule(
    _loader.get(0x8B008567C93F7C7D).as_struct(),
    "CropState",
)
AOMProperties = _StructModule(
    _loader.get(0xE3512E62DF901C18).as_struct(),
    "AOMProperties",
)
SoilColumnState = _StructModule(
    _loader.get(0xEF3E4198D3E35596).as_struct(),
    "SoilColumnState",
)
SoilColumnState.DelayedNMinApplicationParams = _StructModule(
    SoilColumnState.schema.fields["delayedNMinApplications"].schema.elementType,
    "DelayedNMinApplicationParams",
)
SoilLayerState = _StructModule(
    _loader.get(0xDD1E0C7C94DC4211).as_struct(),
    "SoilLayerState",
)
MonicaModelState = _StructModule(
    _loader.get(0xAB56969492D293B3).as_struct(),
    "MonicaModelState",
)
MonicaModelState.ACDToValue = _StructModule(
    MonicaModelState.schema.fields["climateData"].schema.elementType.elementType,
    "ACDToValue",
)
CropModuleState = _StructModule(
    _loader.get(0x811D54AC7DEBC21E).as_struct(),
    "CropModuleState",
)
SnowModuleState = _StructModule(
    _loader.get(0xA4DA01D10B3B6ACD).as_struct(),
    "SnowModuleState",
)
FrostModuleState = _StructModule(
    _loader.get(0xB4F16EA3144D85A6).as_struct(),
    "FrostModuleState",
)
SoilMoistureModuleState = _StructModule(
    _loader.get(0xCD05962719BF7EC8).as_struct(),
    "SoilMoistureModuleState",
)
SoilOrganicModuleState = _StructModule(
    _loader.get(0xD594E64F6B5F461D).as_struct(),
    "SoilOrganicModuleState",
)
SoilTemperatureModuleState = _StructModule(
    _loader.get(0xBD3E199EB9B03758).as_struct(),
    "SoilTemperatureModuleState",
)
SoilTransportModuleState = _StructModule(
    _loader.get(0xB1760F65E652E737).as_struct(),
    "SoilTransportModuleState",
)
ICData = _StructModule(
    _loader.get(0xF03D8FD1BBE75519).as_struct(),
    "ICData",
)
