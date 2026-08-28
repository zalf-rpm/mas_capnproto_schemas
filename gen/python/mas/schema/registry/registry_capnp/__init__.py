# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `registry.capnp`."""

from __future__ import annotations

# Load schemas and build module structure
from importlib import import_module
from typing import cast

from capnp.lib.capnp import SchemaLoader, _InterfaceModule, _StructModule


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
