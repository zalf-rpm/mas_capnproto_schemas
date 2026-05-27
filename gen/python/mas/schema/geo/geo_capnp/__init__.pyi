"""This is an automatically generated stub for `geo.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.geo.geo_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

CoordType: types.modules._CoordTypeEnumModule
EPSG: types.modules._EPSGStructModule
UTMCoord: types.modules._UTMCoordStructModule
LatLonCoord: types.modules._LatLonCoordStructModule
GKCoord: types.modules._GKCoordStructModule
Point2D: types.modules._Point2DStructModule
RowCol: types.modules._RowColStructModule
Coord: types.modules._CoordStructModule
RectBounds: types.modules._RectBoundsStructModule

__all__ = [
    "EPSG",
    "Coord",
    "CoordType",
    "GKCoord",
    "LatLonCoord",
    "Point2D",
    "RectBounds",
    "RowCol",
    "UTMCoord",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
