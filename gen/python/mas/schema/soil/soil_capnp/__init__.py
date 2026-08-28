# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `soil.capnp`."""

from __future__ import annotations

# Load schemas and build module structure
from importlib import import_module
from typing import cast

from capnp.lib.capnp import SchemaLoader, _EnumModule, _InterfaceModule, _StructModule


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

SType = _EnumModule(
    _loader.get(0xC2E4A3C8FF61B40A).as_enum(),
    "SType",
)
PropertyName = _EnumModule(
    _loader.get(0x9E391AE1C6CD2567).as_enum(),
    "PropertyName",
)
Layer = _StructModule(
    _loader.get(0x984640F05B3ADA4F).as_struct(),
    "Layer",
)
Layer.Property = _StructModule(
    Layer.schema.fields["properties"].schema.elementType,
    "Property",
)
Query = _StructModule(
    _loader.get(0xBD4065087E22CA0D).as_struct(),
    "Query",
)
Query.Result = _StructModule(
    _loader.get(0xBF4E1B07AD88943F).as_struct(),
    "Result",
)
ProfileData = _StructModule(
    _loader.get(0xDF4BBF1C883A8790).as_struct(),
    "ProfileData",
)
Profile = _InterfaceModule(
    _loader.get(0xFF67C2A593419C29).as_interface(),
    "Profile",
)
Service = _InterfaceModule(
    _loader.get(0xA09AA71427DC64E1).as_interface(),
    "Service",
)
Service.Stream = _InterfaceModule(
    Service.schema.methods["streamAllProfiles"]
    .result_type.fields["allProfiles"]
    .schema,  # pyright: ignore[reportUnknownArgumentType]
    "Stream",
)
