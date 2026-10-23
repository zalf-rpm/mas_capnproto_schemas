# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `service.capnp`."""

# Load schemas and build module structure
from importlib import import_module as _import_module
from typing import cast as _cast

from capnp.lib.capnp import (
    SchemaLoader as _SchemaLoader,
)
from capnp.lib.capnp import (
    _InterfaceModule,
    _StructModule,
)

from . import types as types


def _import_schema_bundle() -> object:
    bundle_module_name = "_capnp_schema_bundle_594b8b9e7273"
    try:
        return _import_module(bundle_module_name)
    except ModuleNotFoundError as error:
        original_error = error
        package_name = __package__

    while package_name:
        try:
            return _import_module(f"{package_name}.{bundle_module_name}")
        except ModuleNotFoundError:
            package_name = package_name.rpartition(".")[0]

    raise original_error


_schema_bundle = _import_schema_bundle()


def get_schema_by_id(schema_id: int) -> object:
    return _cast("object", _schema_bundle.get_schema_by_id(schema_id))


def load_capnp_file(path: str, imports: list[str] | tuple[str, ...] = ()) -> object:
    return _cast("object", _schema_bundle.load_capnp_file(path, imports))


_loader: _SchemaLoader = _cast("_SchemaLoader", _schema_bundle.get_schema_loader())

# Build module structure inline

Admin = _InterfaceModule(
    _loader.get(0xFEC1F88B198DF649).as_interface(),
    "Admin",
)
SimpleFactory = _InterfaceModule(
    _loader.get(0xABA5829222C213CB).as_interface(),
    "SimpleFactory",
)
Factory = _InterfaceModule(
    _loader.get(0x8AB0ECB99C269C7F).as_interface(),
    "Factory",
)
Factory.CreateParams = _StructModule(
    Factory.schema.methods["create"].param_type,  # pyright: ignore[reportUnknownArgumentType]
    "CreateParams",
)
Factory.AccessInfo = _StructModule(
    Factory.schema.methods["create"].result_type,  # pyright: ignore[reportUnknownArgumentType]
    "AccessInfo",
)
Stoppable = _InterfaceModule(
    _loader.get(0xCD5F6458232E9276).as_interface(),
    "Stoppable",
)

__all__ = [
    "Admin",
    "Factory",
    "SimpleFactory",
    "Stoppable",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
