"""Client result helper types for `grid.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.grid.grid_capnp.types import clients as clients
from mas.schema.grid.grid_capnp.types import readers as readers

class SendcellsResult(Awaitable[SendcellsResult], Protocol):
    locations: readers.LocationListReader

class ClosestvalueatResult(Awaitable[ClosestvalueatResult], Protocol):
    val: readers.ValueReader
    tl: readers.RowColReader
    br: readers.RowColReader
    aggParts: readers.AggregationPartListReader

class ResolutionResult(Awaitable[ResolutionResult], Protocol):
    res: readers.ResolutionReader

class DimensionResult(Awaitable[DimensionResult], Protocol):
    rows: int
    cols: int

class NodatavalueResult(Awaitable[NodatavalueResult], Protocol):
    nodata: readers.ValueReader

class ValueatResult(Awaitable[ValueatResult], Protocol):
    val: readers.ValueReader
    aggParts: readers.AggregationPartListReader

class LatlonboundsResult(Awaitable[LatlonboundsResult], Protocol):
    tl: LatLonCoordReader
    tr: LatLonCoordReader
    br: LatLonCoordReader
    bl: LatLonCoordReader

class StreamcellsResult(Awaitable[StreamcellsResult], Protocol):
    callback: clients.CallbackClient

class UnitResult(Awaitable[UnitResult], Protocol):
    unit: str
