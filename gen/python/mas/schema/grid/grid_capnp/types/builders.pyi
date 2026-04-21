"""Builder helper types for `grid.capnp`."""

from typing import Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.grid.grid_capnp.types import lists as lists
from mas.schema.grid.grid_capnp.types import readers as readers

class ValueBuilder(_DynamicStructBuilder):
    @property
    def f(self) -> float: ...
    @f.setter
    def f(self, value: float) -> None: ...
    @property
    def i(self) -> int: ...
    @i.setter
    def i(self, value: int) -> None: ...
    @property
    def ui(self) -> int: ...
    @ui.setter
    def ui(self, value: int) -> None: ...
    @property
    def no(self) -> bool: ...
    @no.setter
    def no(self, value: bool) -> None: ...
    @override
    def which(self) -> Literal["f", "i", "ui", "no"]: ...
    @override
    def as_reader(self) -> readers.ValueReader: ...

class ResolutionBuilder(_DynamicStructBuilder):
    @property
    def meter(self) -> int: ...
    @meter.setter
    def meter(self, value: int) -> None: ...
    @property
    def degree(self) -> float: ...
    @degree.setter
    def degree(self, value: float) -> None: ...
    @override
    def which(self) -> Literal["meter", "degree"]: ...
    @override
    def as_reader(self) -> readers.ResolutionReader: ...

class RowColBuilder(_DynamicStructBuilder):
    @property
    def row(self) -> int: ...
    @row.setter
    def row(self, value: int) -> None: ...
    @property
    def col(self) -> int: ...
    @col.setter
    def col(self, value: int) -> None: ...
    @override
    def as_reader(self) -> readers.RowColReader: ...

class AggregationPartBuilder(_DynamicStructBuilder):
    @property
    def value(self) -> ValueBuilder: ...
    @value.setter
    def value(
        self,
        value: ValueBuilder | readers.ValueReader | dict[str, Any],
    ) -> None: ...
    @property
    def rowCol(self) -> RowColBuilder: ...
    @rowCol.setter
    def rowCol(
        self,
        value: RowColBuilder | readers.RowColReader | dict[str, Any],
    ) -> None: ...
    @property
    def areaFrac(self) -> float: ...
    @areaFrac.setter
    def areaFrac(self, value: float) -> None: ...
    @property
    def iValue(self) -> float: ...
    @iValue.setter
    def iValue(self, value: float) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["value"],
        size: int | None = None,
    ) -> ValueBuilder: ...
    @overload
    def init(
        self,
        field: Literal["rowCol"],
        size: int | None = None,
    ) -> RowColBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.AggregationPartReader: ...

class LocationBuilder(_DynamicStructBuilder):
    @property
    def latLonCoord(self) -> LatLonCoordBuilder: ...
    @latLonCoord.setter
    def latLonCoord(
        self,
        value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any],
    ) -> None: ...
    @property
    def rowCol(self) -> RowColBuilder: ...
    @rowCol.setter
    def rowCol(
        self,
        value: RowColBuilder | readers.RowColReader | dict[str, Any],
    ) -> None: ...
    @property
    def value(self) -> ValueBuilder: ...
    @value.setter
    def value(
        self,
        value: ValueBuilder | readers.ValueReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["latLonCoord"],
        size: int | None = None,
    ) -> LatLonCoordBuilder: ...
    @overload
    def init(
        self,
        field: Literal["rowCol"],
        size: int | None = None,
    ) -> RowColBuilder: ...
    @overload
    def init(
        self,
        field: Literal["value"],
        size: int | None = None,
    ) -> ValueBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.LocationReader: ...

type AggregationPartListBuilder = lists._AggregationPartList.Builder

type LocationListBuilder = lists._LocationList.Builder
