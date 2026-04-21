"""Client helper types for `grid.capnp`."""

from typing import Any

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.grid.grid_capnp.types import builders as builders
from mas.schema.grid.grid_capnp.types import enums as enums
from mas.schema.grid.grid_capnp.types import readers as readers
from mas.schema.grid.grid_capnp.types import requests as requests
from mas.schema.grid.grid_capnp.types.results import client as results_client
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient

class CallbackClient(_DynamicCapabilityClient):
    def sendCells(
        self,
        maxCount: int | None = None,
    ) -> results_client.SendcellsResult: ...
    def sendCells_request(
        self,
        maxCount: int | None = None,
    ) -> requests.SendcellsRequest: ...

class GridClient(IdentifiableClient, PersistentClient):
    def closestValueAt(
        self,
        latlonCoord: LatLonCoordBuilder
        | LatLonCoordReader
        | dict[str, Any]
        | None = None,
        ignoreNoData: bool | None = None,
        resolution: builders.ResolutionBuilder
        | readers.ResolutionReader
        | dict[str, Any]
        | None = None,
        agg: enums.AggregationEnum | None = None,
        returnRowCols: bool | None = None,
        includeAggParts: bool | None = None,
    ) -> results_client.ClosestvalueatResult: ...
    def resolution(self) -> results_client.ResolutionResult: ...
    def dimension(self) -> results_client.DimensionResult: ...
    def noDataValue(self) -> results_client.NodatavalueResult: ...
    def valueAt(
        self,
        row: int | None = None,
        col: int | None = None,
        resolution: builders.ResolutionBuilder
        | readers.ResolutionReader
        | dict[str, Any]
        | None = None,
        agg: enums.AggregationEnum | None = None,
        includeAggParts: bool | None = None,
    ) -> results_client.ValueatResult: ...
    def latLonBounds(
        self,
        useCellCenter: bool | None = None,
    ) -> results_client.LatlonboundsResult: ...
    def streamCells(
        self,
        topLeft: builders.RowColBuilder
        | readers.RowColReader
        | dict[str, Any]
        | None = None,
        bottomRight: builders.RowColBuilder
        | readers.RowColReader
        | dict[str, Any]
        | None = None,
    ) -> results_client.StreamcellsResult: ...
    def unit(self) -> results_client.UnitResult: ...
    def closestValueAt_request(
        self,
        latlonCoord: LatLonCoordBuilder | None = None,
        ignoreNoData: bool | None = None,
        resolution: builders.ResolutionBuilder | None = None,
        agg: enums.AggregationEnum | None = None,
        returnRowCols: bool | None = None,
        includeAggParts: bool | None = None,
    ) -> requests.ClosestvalueatRequest: ...
    def resolution_request(self) -> requests.ResolutionRequest: ...
    def dimension_request(self) -> requests.DimensionRequest: ...
    def noDataValue_request(self) -> requests.NodatavalueRequest: ...
    def valueAt_request(
        self,
        row: int | None = None,
        col: int | None = None,
        resolution: builders.ResolutionBuilder | None = None,
        agg: enums.AggregationEnum | None = None,
        includeAggParts: bool | None = None,
    ) -> requests.ValueatRequest: ...
    def latLonBounds_request(
        self,
        useCellCenter: bool | None = None,
    ) -> requests.LatlonboundsRequest: ...
    def streamCells_request(
        self,
        topLeft: builders.RowColBuilder | None = None,
        bottomRight: builders.RowColBuilder | None = None,
    ) -> requests.StreamcellsRequest: ...
    def unit_request(self) -> requests.UnitRequest: ...
