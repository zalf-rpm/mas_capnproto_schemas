# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `registry.capnp`."""

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
    _loader.get(0xF503F3237666574E).as_interface(),
    "Admin",
)
Registry = _InterfaceModule(
    _loader.get(0xCA7B4BD1600633B8).as_interface(),
    "Registry",
)
Registry.Entry = _StructModule(
    _loader.get(0xC17987510CF7AC13).as_struct(),
    "Entry",
)
Registrar = _InterfaceModule(
    _loader.get(0xABAEF93C36F2D1EA).as_interface(),
    "Registrar",
)
Registrar.CrossDomainRestore = _StructModule(
    Registrar.schema.methods["register"].param_type.fields["xDomain"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "CrossDomainRestore",
)
Registrar.RegParams = _StructModule(
    Registrar.schema.methods["register"].param_type,  # pyright: ignore[reportUnknownArgumentType]
    "RegParams",
)
Registrar.Unregister = _InterfaceModule(
    Registrar.schema.methods["register"].result_type.fields["unreg"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "Unregister",
)

__all__ = [
    "Admin",
    "Registrar",
    "Registry",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
