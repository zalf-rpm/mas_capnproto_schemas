# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `grid.capnp`."""

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
