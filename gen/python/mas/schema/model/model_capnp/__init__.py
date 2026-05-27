# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `model.capnp`."""

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

XYResult = _StructModule(
    _loader.get(0x851D47C6CCDECF08).as_struct(),
    "XYResult",
)
Stat = _StructModule(
    _loader.get(0xA6BE2E805EA10A68).as_struct(),
    "Stat",
)
Stat.Type = _EnumModule(
    Stat.schema.fields["type"].schema,
    "Type",
)
XYPlusResult = _StructModule(
    _loader.get(0x8F86B66260D02D1D).as_struct(),
    "XYPlusResult",
)
ClimateInstance = _InterfaceModule(
    _loader.get(0xDFCFEB783C4948FC).as_interface(),
    "ClimateInstance",
)
Env = _StructModule(
    _loader.get(0xB7FC866EF1127F7C).as_struct(),
    "Env",
)
EnvInstance = _InterfaceModule(
    _loader.get(0xA5FEEDAFA5EC5C4A).as_interface(),
    "EnvInstance",
)
EnvInstanceProxy = _InterfaceModule(
    _loader.get(0x87CBEBFC1164A24A).as_interface(),
    "EnvInstanceProxy",
)
EnvInstanceProxy.Unregister = _InterfaceModule(
    EnvInstanceProxy.schema.methods["registerEnvInstance"]
    .result_type.fields["unregister"]
    .schema,  # pyright: ignore[reportUnknownArgumentType]
    "Unregister",
)
InstanceFactory = _InterfaceModule(
    _loader.get(0xCE552EEF738A45EA).as_interface(),
    "InstanceFactory",
)
