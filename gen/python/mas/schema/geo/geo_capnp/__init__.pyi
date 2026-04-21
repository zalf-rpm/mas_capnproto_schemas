"""This is an automatically generated stub for `geo.capnp`."""

from mas.schema.geo.geo_capnp import types as types

class _CoordTypeEnumModule:
    gk: int
    utm: int
    latlon: int

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
    "GKCoord",
    "LatLonCoord",
    "Point2D",
    "RectBounds",
    "RowCol",
    "UTMCoord",
    "types",
]
