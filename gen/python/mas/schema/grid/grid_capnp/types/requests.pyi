"""Request helper types for `grid.capnp`."""

from typing import Any, Literal, Protocol, overload

from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.grid.grid_capnp.types import builders as builders
from mas.schema.grid.grid_capnp.types import enums as enums
from mas.schema.grid.grid_capnp.types.results import client as results_client

class SendcellsRequest(Protocol):
    maxCount: int
    def send(self) -> results_client.SendcellsResult: ...

class ClosestvalueatRequest(Protocol):
    latlonCoord: LatLonCoordBuilder
    ignoreNoData: bool
    resolution: builders.ResolutionBuilder
    agg: enums.AggregationEnum
    returnRowCols: bool
    includeAggParts: bool
    @overload
    def init(self, name: Literal["latlonCoord"]) -> LatLonCoordBuilder: ...
    @overload
    def init(self, name: Literal["resolution"]) -> builders.ResolutionBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.ClosestvalueatResult: ...

class ResolutionRequest(Protocol):
    def send(self) -> results_client.ResolutionResult: ...

class DimensionRequest(Protocol):
    def send(self) -> results_client.DimensionResult: ...

class NodatavalueRequest(Protocol):
    def send(self) -> results_client.NodatavalueResult: ...

class ValueatRequest(Protocol):
    row: int
    col: int
    resolution: builders.ResolutionBuilder
    agg: enums.AggregationEnum
    includeAggParts: bool
    @overload
    def init(self, name: Literal["resolution"]) -> builders.ResolutionBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.ValueatResult: ...

class LatlonboundsRequest(Protocol):
    useCellCenter: bool
    def send(self) -> results_client.LatlonboundsResult: ...

class StreamcellsRequest(Protocol):
    topLeft: builders.RowColBuilder
    bottomRight: builders.RowColBuilder
    @overload
    def init(self, name: Literal["topLeft"]) -> builders.RowColBuilder: ...
    @overload
    def init(self, name: Literal["bottomRight"]) -> builders.RowColBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.StreamcellsResult: ...

class UnitRequest(Protocol):
    def send(self) -> results_client.UnitResult: ...
