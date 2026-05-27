# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `storage.capnp`."""

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

Store = _InterfaceModule(
    _loader.get(0xE69F958AA2386F06).as_interface(),
    "Store",
)
Store.Container = _InterfaceModule(
    Store.schema.methods["newContainer"].result_type.fields["container"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "Container",
)
Store.Container.Entry = _InterfaceModule(
    Store.Container.schema.methods["listEntries"]
    .result_type.fields["entries"]
    .schema.elementType.fields["entry"]
    .schema,  # pyright: ignore[reportUnknownArgumentType]
    "Entry",
)
Store.Container.Entry.Value = _StructModule(
    Store.Container.Entry.schema.methods["getValue"].result_type.fields["value"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "Value",
)
Store.Container.KeyAndEntry = _StructModule(
    Store.Container.schema.methods["listEntries"]
    .result_type.fields["entries"]
    .schema.elementType,  # pyright: ignore[reportUnknownArgumentType]
    "KeyAndEntry",
)
Store.InfoAndContainer = _StructModule(
    Store.schema.methods["listContainers"]
    .result_type.fields["containers"]
    .schema.elementType,  # pyright: ignore[reportUnknownArgumentType]
    "InfoAndContainer",
)
Store.ImportExportData = _StructModule(
    _loader.get(0x847D262CEFD2F142).as_struct(),
    "ImportExportData",
)
