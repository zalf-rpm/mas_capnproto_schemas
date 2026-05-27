# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `yieldstat.capnp`."""

from __future__ import annotations

# Load schemas and build module structure
from importlib import import_module
from typing import cast

from capnp.lib.capnp import SchemaLoader, _EnumModule, _StructModule


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

ResultId = _EnumModule(
    _loader.get(0xCFE218C48D227E0D).as_enum(),
    "ResultId",
)
RestInput = _StructModule(
    _loader.get(0xA47F8D65869200AF).as_struct(),
    "RestInput",
)
Result = _StructModule(
    _loader.get(0x8DB55634A0E7D054).as_struct(),
    "Result",
)
Result.ResultToValue = _StructModule(
    Result.schema.fields["values"].schema.elementType,
    "ResultToValue",
)
Output = _StructModule(
    _loader.get(0x932A681F81B4BE19).as_struct(),
    "Output",
)
Output.YearToResult = _StructModule(
    Output.schema.fields["results"].schema.elementType,
    "YearToResult",
)
