"""Reader helper types for `geo.capnp`."""

from collections.abc import Callable
from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicObjectReader,
    _DynamicStructReader,
)

from mas.schema.geo.geo_capnp.types import builders as builders

class EPSGReader(_DynamicStructReader):
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.EPSGBuilder: ...

class UTMCoordReader(_DynamicStructReader):
    @property
    def zone(self) -> int: ...
    @property
    def latitudeBand(self) -> str: ...
    @property
    def r(self) -> float: ...
    @property
    def h(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.UTMCoordBuilder: ...

class LatLonCoordReader(_DynamicStructReader):
    @property
    def lat(self) -> float: ...
    @property
    def lon(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.LatLonCoordBuilder: ...

class GKCoordReader(_DynamicStructReader):
    @property
    def meridianNo(self) -> int: ...
    @property
    def r(self) -> float: ...
    @property
    def h(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.GKCoordBuilder: ...

class Point2DReader(_DynamicStructReader):
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.Point2DBuilder: ...

class RowColReader(_DynamicStructReader):
    @property
    def row(self) -> int: ...
    @property
    def col(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.RowColBuilder: ...

class CoordReader(_DynamicStructReader):
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
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.CoordBuilder: ...

class RectBoundsReader(_DynamicStructReader):
    @property
    def tl(self) -> _DynamicObjectReader: ...
    @property
    def br(self) -> _DynamicObjectReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.RectBoundsBuilder: ...
