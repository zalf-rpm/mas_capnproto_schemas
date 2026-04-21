"""Result tuple helper types for `grid.capnp`."""

from collections.abc import Sequence
from typing import Any, NamedTuple

from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.grid.grid_capnp.types import builders as builders
from mas.schema.grid.grid_capnp.types import clients as clients
from mas.schema.grid.grid_capnp.types import modules as modules
from mas.schema.grid.grid_capnp.types import readers as readers

class SendcellsResultTuple(NamedTuple):
    locations: builders.LocationListBuilder | readers.LocationListReader | Sequence[Any]

class ClosestvalueatResultTuple(NamedTuple):
    val: builders.ValueBuilder | readers.ValueReader | dict[str, Any]
    tl: builders.RowColBuilder | readers.RowColReader | dict[str, Any]
    br: builders.RowColBuilder | readers.RowColReader | dict[str, Any]
    aggParts: (
        builders.AggregationPartListBuilder
        | readers.AggregationPartListReader
        | Sequence[Any]
    )

class ResolutionResultTuple(NamedTuple):
    res: builders.ResolutionBuilder | readers.ResolutionReader | dict[str, Any]

class DimensionResultTuple(NamedTuple):
    rows: int
    cols: int

class NodatavalueResultTuple(NamedTuple):
    nodata: builders.ValueBuilder | readers.ValueReader | dict[str, Any]

class ValueatResultTuple(NamedTuple):
    val: builders.ValueBuilder | readers.ValueReader | dict[str, Any]
    aggParts: (
        builders.AggregationPartListBuilder
        | readers.AggregationPartListReader
        | Sequence[Any]
    )

class LatlonboundsResultTuple(NamedTuple):
    tl: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]
    tr: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]
    br: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]
    bl: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]

class StreamcellsResultTuple(NamedTuple):
    callback: (
        modules._GridInterfaceModule._CallbackInterfaceModule.Server
        | clients.CallbackClient
    )

class UnitResultTuple(NamedTuple):
    unit: str
