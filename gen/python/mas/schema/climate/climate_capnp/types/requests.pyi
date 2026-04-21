"""Request helper types for `climate.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, Protocol, overload

from mas.schema.climate.climate_capnp.types import builders as builders
from mas.schema.climate.climate_capnp.types import clients as clients
from mas.schema.climate.climate_capnp.types import enums as enums
from mas.schema.climate.climate_capnp.types import modules as modules
from mas.schema.climate.climate_capnp.types import readers as readers
from mas.schema.climate.climate_capnp.types.results import client as results_client
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder

class CategoriesRequest(Protocol):
    def send(self) -> results_client.CategoriesResult: ...

class SupportedvaluesRequest(Protocol):
    typeId: str
    def send(self) -> results_client.SupportedvaluesResult: ...

class ForoneRequest(Protocol):
    entry: builders.EntryBuilder
    @overload
    def init(self, name: Literal["entry"]) -> builders.EntryBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.ForoneResult: ...

class ForallRequest(Protocol):
    def send(self) -> results_client.ForallResult: ...

class ResolutionRequest(Protocol):
    def send(self) -> results_client.ResolutionResult: ...

class RangeRequest(Protocol):
    def send(self) -> results_client.RangeResult: ...

class HeaderRequest(Protocol):
    def send(self) -> results_client.HeaderResult: ...

class DataRequest(Protocol):
    def send(self) -> results_client.DataResult: ...

class DatatRequest(Protocol):
    def send(self) -> results_client.DatatResult: ...

class SubrangeRequest(Protocol):
    start: DateBuilder
    end: DateBuilder
    @overload
    def init(self, name: Literal["start"]) -> DateBuilder: ...
    @overload
    def init(self, name: Literal["end"]) -> DateBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.SubrangeResult: ...

class SubheaderRequest(Protocol):
    elements: (
        builders.ElementEnumListBuilder | readers.ElementEnumListReader | Sequence[Any]
    )
    @overload
    def init(
        self,
        name: Literal["elements"],
        size: int = ...,
    ) -> builders.ElementEnumListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.SubheaderResult: ...

class TimeSeriesMetadataRequest(Protocol):
    def send(self) -> results_client.TimeSeriesMetadataResult: ...

class LocationRequest(Protocol):
    def send(self) -> results_client.LocationResult: ...

class NextlocationsRequest(Protocol):
    maxCount: int
    def send(self) -> results_client.NextlocationsResult: ...

class DatasetMetadataRequest(Protocol):
    def send(self) -> results_client.DatasetMetadataResult: ...

class ClosesttimeseriesatRequest(Protocol):
    latlon: LatLonCoordBuilder
    @overload
    def init(self, name: Literal["latlon"]) -> LatLonCoordBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.ClosesttimeseriesatResult: ...

class TimeseriesatRequest(Protocol):
    locationId: str
    def send(self) -> results_client.TimeseriesatResult: ...

class LocationsRequest(Protocol):
    def send(self) -> results_client.LocationsResult: ...

class StreamlocationsRequest(Protocol):
    startAfterLocationId: str
    def send(self) -> results_client.StreamlocationsResult: ...

class GetavailabledatasetsRequest(Protocol):
    def send(self) -> results_client.GetavailabledatasetsResult: ...

class GetdatasetsforRequest(Protocol):
    template: builders.MetadataBuilder
    @overload
    def init(self, name: Literal["template"]) -> builders.MetadataBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.GetdatasetsforResult: ...

class CreateRequest(Protocol):
    csvData: str
    config: builders.CSVConfigBuilder
    @overload
    def init(self, name: Literal["config"]) -> builders.CSVConfigBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.CreateResult: ...

class WrappedtimeseriesRequest(Protocol):
    def send(self) -> results_client.WrappedtimeseriesResult: ...

class AlteredelementsRequest(Protocol):
    def send(self) -> results_client.AlteredelementsResult: ...

class AlterRequest(Protocol):
    desc: builders.AlteredBuilder
    asNewTimeSeries: bool
    @overload
    def init(self, name: Literal["desc"]) -> builders.AlteredBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.AlterResult: ...

class RemoveRequest(Protocol):
    alteredElement: enums.ElementEnum
    def send(self) -> results_client.RemoveResult: ...

class ReplacewrappedtimeseriesRequest(Protocol):
    timeSeries: clients.TimeSeriesClient | modules._TimeSeriesInterfaceModule.Server
    def send(self) -> results_client.ReplacewrappedtimeseriesResult: ...

class WrapRequest(Protocol):
    timeSeries: clients.TimeSeriesClient | modules._TimeSeriesInterfaceModule.Server
    def send(self) -> results_client.WrapResult: ...
