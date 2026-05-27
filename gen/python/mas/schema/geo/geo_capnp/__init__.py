# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `geo.capnp`."""

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

CoordType = _EnumModule(
    _loader.get(0xE529B4DEB322ECE8).as_enum(),
    "CoordType",
)
EPSG = _StructModule(
    _loader.get(0xB79427A74EB97FC0).as_struct(),
    "EPSG",
)
EPSG.wgs84 = _loader.get(0xCDAF64C4789F2B7D).as_const_value()
EPSG.utm21S = _loader.get(0xC8FB53981E470885).as_const_value()
EPSG.utm32N = _loader.get(0xCC67DEE69497E2F3).as_const_value()
EPSG.gk5 = _loader.get(0x958C02356C8797E1).as_const_value()
EPSG.gk4 = _loader.get(0xE4AFDDDDDEC2511D).as_const_value()
EPSG.gk3 = _loader.get(0xF5B9E8307038AD86).as_const_value()
UTMCoord = _StructModule(
    _loader.get(0xEB1ACD255E40F049).as_struct(),
    "UTMCoord",
)
LatLonCoord = _StructModule(
    _loader.get(0xECF1FC3039CC8FFB).as_struct(),
    "LatLonCoord",
)
GKCoord = _StructModule(
    _loader.get(0x97FF7D61786091AE).as_struct(),
    "GKCoord",
)
Point2D = _StructModule(
    _loader.get(0xC88FB91C1E6986E2).as_struct(),
    "Point2D",
)
RowCol = _StructModule(
    _loader.get(0xB0C6993E13E314AD).as_struct(),
    "RowCol",
)
Coord = _StructModule(
    _loader.get(0xB8F6A6192A7359F8).as_struct(),
    "Coord",
)
RectBounds = _StructModule(
    _loader.get(0xB952DBE83866DA4A).as_struct(),
    "RectBounds",
)
