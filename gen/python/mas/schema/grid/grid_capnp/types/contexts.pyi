"""Context helper types for `grid.capnp`."""

from typing import Protocol

from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.grid.grid_capnp.types import enums as enums
from mas.schema.grid.grid_capnp.types import readers as readers
from mas.schema.grid.grid_capnp.types.results import server as results_server

class SendcellsParams(Protocol):
    maxCount: int

class SendcellsCallContext(Protocol):
    params: SendcellsParams
    @property
    def results(self) -> results_server.SendcellsServerResult: ...

class ClosestvalueatParams(Protocol):
    latlonCoord: LatLonCoordReader
    ignoreNoData: bool
    resolution: readers.ResolutionReader
    agg: enums.AggregationEnum
    returnRowCols: bool
    includeAggParts: bool

class ClosestvalueatCallContext(Protocol):
    params: ClosestvalueatParams
    @property
    def results(self) -> results_server.ClosestvalueatServerResult: ...

class ResolutionParams(Protocol): ...

class ResolutionCallContext(Protocol):
    params: ResolutionParams
    @property
    def results(self) -> results_server.ResolutionServerResult: ...

class DimensionParams(Protocol): ...

class DimensionCallContext(Protocol):
    params: DimensionParams
    @property
    def results(self) -> results_server.DimensionServerResult: ...

class NodatavalueParams(Protocol): ...

class NodatavalueCallContext(Protocol):
    params: NodatavalueParams
    @property
    def results(self) -> results_server.NodatavalueServerResult: ...

class ValueatParams(Protocol):
    row: int
    col: int
    resolution: readers.ResolutionReader
    agg: enums.AggregationEnum
    includeAggParts: bool

class ValueatCallContext(Protocol):
    params: ValueatParams
    @property
    def results(self) -> results_server.ValueatServerResult: ...

class LatlonboundsParams(Protocol):
    useCellCenter: bool

class LatlonboundsCallContext(Protocol):
    params: LatlonboundsParams
    @property
    def results(self) -> results_server.LatlonboundsServerResult: ...

class StreamcellsParams(Protocol):
    topLeft: readers.RowColReader
    bottomRight: readers.RowColReader

class StreamcellsCallContext(Protocol):
    params: StreamcellsParams
    @property
    def results(self) -> results_server.StreamcellsServerResult: ...

class UnitParams(Protocol): ...

class UnitCallContext(Protocol):
    params: UnitParams
    @property
    def results(self) -> results_server.UnitServerResult: ...
