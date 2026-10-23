# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `grid.capnp`."""

# Load schemas and build module structure
from importlib import import_module as _import_module
from typing import cast as _cast

from capnp.lib.capnp import (
    SchemaLoader as _SchemaLoader,
)
from capnp.lib.capnp import (
    _EnumModule,
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

Aggregation = _EnumModule(
    _loader.get(0xA5ECDC7767A6B301).as_enum(),
    "Aggregation",
)
Grid = _InterfaceModule(
    _loader.get(0xE42973B29661E3C6).as_interface(),
    "Grid",
)
Grid.Value = _StructModule(
    Grid.schema.methods["closestValueAt"].result_type.fields["val"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "Value",
)
Grid.Resolution = _StructModule(
    Grid.schema.methods["closestValueAt"].param_type.fields["resolution"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "Resolution",
)
Grid.RowCol = _StructModule(
    Grid.schema.methods["closestValueAt"].result_type.fields["tl"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "RowCol",
)
Grid.AggregationPart = _StructModule(
    Grid.schema.methods["closestValueAt"]
    .result_type.fields["aggParts"]
    .schema.elementType,  # pyright: ignore[reportUnknownArgumentType]
    "AggregationPart",
)
Grid.Location = _StructModule(
    Grid.schema.methods["streamCells"]
    .result_type.fields["callback"]
    .schema.methods["sendCells"]
    .result_type.fields["locations"]
    .schema.elementType,  # pyright: ignore[reportUnknownArgumentType]
    "Location",
)
Grid.Callback = _InterfaceModule(
    Grid.schema.methods["streamCells"].result_type.fields["callback"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "Callback",
)

__all__ = ["Aggregation", "Grid", "get_schema_by_id", "load_capnp_file", "types"]
