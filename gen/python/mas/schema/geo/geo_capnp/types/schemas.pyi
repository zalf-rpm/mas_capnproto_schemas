"""Schema helper types for `geo.capnp`."""

from mas.schema.geo.geo_capnp.types import modules as modules

type _CoordSchema = modules._CoordStructModule._CoordSchema

type _CoordTypeEnumSchema = modules._CoordTypeEnumModule._CoordTypeSchema

type _EPSGSchema = modules._EPSGStructModule._EPSGSchema

type _GKCoordSchema = modules._GKCoordStructModule._GKCoordSchema

type _LatLonCoordSchema = modules._LatLonCoordStructModule._LatLonCoordSchema

type _Point2DSchema = modules._Point2DStructModule._Point2DSchema

type _RectBoundsSchema = modules._RectBoundsStructModule._RectBoundsSchema

type _RowColSchema = modules._RowColStructModule._RowColSchema

type _UTMCoordSchema = modules._UTMCoordStructModule._UTMCoordSchema
