# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `x.capnp`."""

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

S = _StructModule(
    _loader.get(0xD227EF68DE0BC647).as_struct(),
    "S",
)
X = _InterfaceModule(
    _loader.get(0xDCF28E81FA4DE615).as_interface(),
    "X",
)
Y = _InterfaceModule(
    _loader.get(0xAC121E5AA82CA6BD).as_interface(),
    "Y",
)
Z = _InterfaceModule(
    _loader.get(0xC64526206425C2AB).as_interface(),
    "Z",
)
