# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `service.capnp`."""

from __future__ import annotations

# Load schemas and build module structure
from importlib import import_module
from typing import cast

from capnp.lib.capnp import SchemaLoader, _InterfaceModule, _StructModule


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
