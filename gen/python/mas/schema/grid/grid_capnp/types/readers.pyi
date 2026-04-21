"""Reader helper types for `grid.capnp`."""

from collections.abc import Callable
from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicStructReader,
)

from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.grid.grid_capnp.types import builders as builders
from mas.schema.grid.grid_capnp.types import lists as lists

class ValueReader(_DynamicStructReader):
    @property
    def f(self) -> float: ...
    @property
    def i(self) -> int: ...
    @property
    def ui(self) -> int: ...
    @property
    def no(self) -> bool: ...
    @override
    def which(self) -> Literal["f", "i", "ui", "no"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ValueBuilder: ...

class ResolutionReader(_DynamicStructReader):
    @property
    def meter(self) -> int: ...
    @property
    def degree(self) -> float: ...
    @override
    def which(self) -> Literal["meter", "degree"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ResolutionBuilder: ...

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

class AggregationPartReader(_DynamicStructReader):
    @property
    def value(self) -> ValueReader: ...
    @property
    def rowCol(self) -> RowColReader: ...
    @property
    def areaFrac(self) -> float: ...
    @property
    def iValue(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.AggregationPartBuilder: ...

class LocationReader(_DynamicStructReader):
    @property
    def latLonCoord(self) -> LatLonCoordReader: ...
    @property
    def rowCol(self) -> RowColReader: ...
    @property
    def value(self) -> ValueReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.LocationBuilder: ...

type AggregationPartListReader = lists._AggregationPartList.Reader

type LocationListReader = lists._LocationList.Reader
