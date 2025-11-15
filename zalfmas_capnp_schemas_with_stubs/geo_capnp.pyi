"""This is an automatically generated stub for `geo.capnp`."""

from __future__ import annotations

from enum import Enum
from typing import Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _Request,
    _StructModule,
)

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

class _CoordTypeModule(Enum):
    gk = 0
    utm = 1
    latlon = 2

class _EPSGModule(_StructModule):
    wgs84: int
    utm21S: int
    utm32N: int
    gk5: int
    gk4: int
    gk3: int
    class Reader(_DynamicStructReader):
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> EPSGBuilder: ...

    class Builder(_DynamicStructBuilder):
        @override
        def as_reader(self) -> EPSGReader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> EPSGBuilder: ...

EPSG: _EPSGModule

class _UTMCoordModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def zone(self) -> int: ...
        @property
        def latitudeBand(self) -> str: ...
        @property
        def r(self) -> float: ...
        @property
        def h(self) -> float: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> UTMCoordBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def zone(self) -> int: ...
        @zone.setter
        def zone(self, value: int) -> None: ...
        @property
        def latitudeBand(self) -> str: ...
        @latitudeBand.setter
        def latitudeBand(self, value: str) -> None: ...
        @property
        def r(self) -> float: ...
        @r.setter
        def r(self, value: float) -> None: ...
        @property
        def h(self) -> float: ...
        @h.setter
        def h(self, value: float) -> None: ...
        @override
        def as_reader(self) -> UTMCoordReader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, zone: int | None = None, latitudeBand: str | None = None, r: float | None = None, h: float | None = None) -> UTMCoordBuilder: ...

UTMCoord: _UTMCoordModule

class _LatLonCoordModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def lat(self) -> float: ...
        @property
        def lon(self) -> float: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> LatLonCoordBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def lat(self) -> float: ...
        @lat.setter
        def lat(self, value: float) -> None: ...
        @property
        def lon(self) -> float: ...
        @lon.setter
        def lon(self, value: float) -> None: ...
        @override
        def as_reader(self) -> LatLonCoordReader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, lat: float | None = None, lon: float | None = None) -> LatLonCoordBuilder: ...

LatLonCoord: _LatLonCoordModule

class _GKCoordModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def meridianNo(self) -> int: ...
        @property
        def r(self) -> float: ...
        @property
        def h(self) -> float: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> GKCoordBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def meridianNo(self) -> int: ...
        @meridianNo.setter
        def meridianNo(self, value: int) -> None: ...
        @property
        def r(self) -> float: ...
        @r.setter
        def r(self, value: float) -> None: ...
        @property
        def h(self) -> float: ...
        @h.setter
        def h(self, value: float) -> None: ...
        @override
        def as_reader(self) -> GKCoordReader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, meridianNo: int | None = None, r: float | None = None, h: float | None = None) -> GKCoordBuilder: ...

GKCoord: _GKCoordModule

class _Point2DModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def x(self) -> float: ...
        @property
        def y(self) -> float: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> Point2DBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def x(self) -> float: ...
        @x.setter
        def x(self, value: float) -> None: ...
        @property
        def y(self) -> float: ...
        @y.setter
        def y(self, value: float) -> None: ...
        @override
        def as_reader(self) -> Point2DReader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, x: float | None = None, y: float | None = None) -> Point2DBuilder: ...

Point2D: _Point2DModule

class _RowColModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def row(self) -> int: ...
        @property
        def col(self) -> int: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> RowColBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def row(self) -> int: ...
        @row.setter
        def row(self, value: int) -> None: ...
        @property
        def col(self) -> int: ...
        @col.setter
        def col(self, value: int) -> None: ...
        @override
        def as_reader(self) -> RowColReader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, row: int | None = None, col: int | None = None) -> RowColBuilder: ...

RowCol: _RowColModule

class _CoordModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def gk(self) -> GKCoordReader: ...
        @property
        def latlon(self) -> LatLonCoordReader: ...
        @property
        def utm(self) -> UTMCoordReader: ...
        @property
        def p2D(self) -> Point2DReader: ...
        @property
        def rowcol(self) -> RowColReader: ...
        @override
        def which(self) -> Literal["gk", "latlon", "utm", "p2D", "rowcol"]: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> CoordBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def gk(self) -> GKCoordBuilder: ...
        @gk.setter
        def gk(self, value: GKCoordBuilder | GKCoordReader | dict[str, Any]) -> None: ...
        @property
        def latlon(self) -> LatLonCoordBuilder: ...
        @latlon.setter
        def latlon(self, value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]) -> None: ...
        @property
        def utm(self) -> UTMCoordBuilder: ...
        @utm.setter
        def utm(self, value: UTMCoordBuilder | UTMCoordReader | dict[str, Any]) -> None: ...
        @property
        def p2D(self) -> Point2DBuilder: ...
        @p2D.setter
        def p2D(self, value: Point2DBuilder | Point2DReader | dict[str, Any]) -> None: ...
        @property
        def rowcol(self) -> RowColBuilder: ...
        @rowcol.setter
        def rowcol(self, value: RowColBuilder | RowColReader | dict[str, Any]) -> None: ...
        @override
        def which(self) -> Literal["gk", "latlon", "utm", "p2D", "rowcol"]: ...
        @overload
        def init(self, field: Literal["gk"], size: int | None = None) -> _GKCoordModule.Builder: ...
        @overload
        def init(self, field: Literal["latlon"], size: int | None = None) -> _LatLonCoordModule.Builder: ...
        @overload
        def init(self, field: Literal["utm"], size: int | None = None) -> _UTMCoordModule.Builder: ...
        @overload
        def init(self, field: Literal["p2D"], size: int | None = None) -> _Point2DModule.Builder: ...
        @overload
        def init(self, field: Literal["rowcol"], size: int | None = None) -> _RowColModule.Builder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> CoordReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        gk: GKCoordBuilder | dict[str, Any] | None = None,
        latlon: LatLonCoordBuilder | dict[str, Any] | None = None,
        utm: UTMCoordBuilder | dict[str, Any] | None = None,
        p2D: Point2DBuilder | dict[str, Any] | None = None,
        rowcol: RowColBuilder | dict[str, Any] | None = None,
    ) -> CoordBuilder: ...

Coord: _CoordModule

class _RectBoundsModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def tl(self) -> _DynamicObjectReader: ...
        @property
        def br(self) -> _DynamicObjectReader: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> RectBoundsBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def tl(self) -> _DynamicObjectReader: ...
        @tl.setter
        def tl(self, value: AnyPointer) -> None: ...
        @property
        def br(self) -> _DynamicObjectReader: ...
        @br.setter
        def br(self, value: AnyPointer) -> None: ...
        @override
        def as_reader(self) -> RectBoundsReader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, tl: AnyPointer | None = None, br: AnyPointer | None = None) -> RectBoundsBuilder: ...

RectBounds: _RectBoundsModule

# Top-level type aliases for use in type annotations
type CoordBuilder = _CoordModule.Builder
type CoordReader = _CoordModule.Reader
type CoordType = _CoordTypeModule
type EPSGBuilder = _EPSGModule.Builder
type EPSGReader = _EPSGModule.Reader
type GKCoordBuilder = _GKCoordModule.Builder
type GKCoordReader = _GKCoordModule.Reader
type LatLonCoordBuilder = _LatLonCoordModule.Builder
type LatLonCoordReader = _LatLonCoordModule.Reader
type Point2DBuilder = _Point2DModule.Builder
type Point2DReader = _Point2DModule.Reader
type RectBoundsBuilder = _RectBoundsModule.Builder
type RectBoundsReader = _RectBoundsModule.Reader
type RowColBuilder = _RowColModule.Builder
type RowColReader = _RowColModule.Reader
type UTMCoordBuilder = _UTMCoordModule.Builder
type UTMCoordReader = _UTMCoordModule.Reader
