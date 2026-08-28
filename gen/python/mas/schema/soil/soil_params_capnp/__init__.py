# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `soil_params.capnp`."""

from __future__ import annotations

# Load schemas and build module structure
from importlib import import_module
from typing import cast

from capnp.lib.capnp import SchemaLoader, _StructModule


def _import_schema_bundle() -> object:
    bundle_module_name = "_capnp_schema_bundle_b45e9cb539b9"
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

SoilCharacteristicData = _StructModule(
    _loader.get(0xFC682227304E2281).as_struct(),
    "SoilCharacteristicData",
)
SoilCharacteristicData.Data = _StructModule(
    SoilCharacteristicData.schema.fields["list"].schema.elementType,
    "Data",
)
SoilCharacteristicModifier = _StructModule(
    _loader.get(0xE4EB0A9BB0E5BB53).as_struct(),
    "SoilCharacteristicModifier",
)
SoilCharacteristicModifier.Data = _StructModule(
    SoilCharacteristicModifier.schema.fields["list"].schema.elementType,
    "Data",
)
CapillaryRiseRate = _StructModule(
    _loader.get(0x9B169BC96BB3D24B).as_struct(),
    "CapillaryRiseRate",
)
CapillaryRiseRate.Data = _StructModule(
    CapillaryRiseRate.schema.fields["list"].schema.elementType,
    "Data",
)
