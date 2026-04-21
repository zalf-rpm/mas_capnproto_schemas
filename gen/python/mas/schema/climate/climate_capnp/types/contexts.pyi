"""Context helper types for `climate.capnp`."""

from typing import Protocol

from mas.schema.climate.climate_capnp.types import builders as builders
from mas.schema.climate.climate_capnp.types import clients as clients
from mas.schema.climate.climate_capnp.types import enums as enums
from mas.schema.climate.climate_capnp.types import readers as readers
from mas.schema.climate.climate_capnp.types.results import server as results_server
from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader

class CategoriesParams(Protocol): ...

class CategoriesCallContext(Protocol):
    params: CategoriesParams
    @property
    def results(self) -> results_server.CategoriesServerResult: ...

class SupportedvaluesParams(Protocol):
    typeId: str

class SupportedvaluesCallContext(Protocol):
    params: SupportedvaluesParams
    @property
    def results(self) -> results_server.SupportedvaluesServerResult: ...

class ForoneParams(Protocol):
    entry: readers.EntryReader

class ForoneCallContext(Protocol):
    params: ForoneParams
    @property
    def results(self) -> IdInformationBuilder: ...

class ForallParams(Protocol): ...

class ForallCallContext(Protocol):
    params: ForallParams
    @property
    def results(self) -> results_server.ForallServerResult: ...

class ResolutionParams(Protocol): ...

class ResolutionCallContext(Protocol):
    params: ResolutionParams
    @property
    def results(self) -> results_server.ResolutionServerResult: ...

class RangeParams(Protocol): ...

class RangeCallContext(Protocol):
    params: RangeParams
    @property
    def results(self) -> results_server.RangeServerResult: ...

class HeaderParams(Protocol): ...

class HeaderCallContext(Protocol):
    params: HeaderParams
    @property
    def results(self) -> results_server.HeaderServerResult: ...

class DataParams(Protocol): ...

class DataCallContext(Protocol):
    params: DataParams
    @property
    def results(self) -> results_server.DataServerResult: ...

class DatatParams(Protocol): ...

class DatatCallContext(Protocol):
    params: DatatParams
    @property
    def results(self) -> results_server.DatatServerResult: ...

class SubrangeParams(Protocol):
    start: DateReader
    end: DateReader

class SubrangeCallContext(Protocol):
    params: SubrangeParams
    @property
    def results(self) -> results_server.SubrangeServerResult: ...

class SubheaderParams(Protocol):
    elements: readers.ElementEnumListReader

class SubheaderCallContext(Protocol):
    params: SubheaderParams
    @property
    def results(self) -> results_server.SubheaderServerResult: ...

class TimeSeriesMetadataParams(Protocol): ...

class TimeSeriesMetadataCallContext(Protocol):
    params: TimeSeriesMetadataParams
    @property
    def results(self) -> builders.MetadataBuilder: ...

class LocationParams(Protocol): ...

class LocationCallContext(Protocol):
    params: LocationParams
    @property
    def results(self) -> builders.LocationBuilder: ...

class NextlocationsParams(Protocol):
    maxCount: int

class NextlocationsCallContext(Protocol):
    params: NextlocationsParams
    @property
    def results(self) -> results_server.NextlocationsServerResult: ...

class DatasetMetadataParams(Protocol): ...

class DatasetMetadataCallContext(Protocol):
    params: DatasetMetadataParams
    @property
    def results(self) -> builders.MetadataBuilder: ...

class ClosesttimeseriesatParams(Protocol):
    latlon: LatLonCoordReader

class ClosesttimeseriesatCallContext(Protocol):
    params: ClosesttimeseriesatParams
    @property
    def results(self) -> results_server.ClosesttimeseriesatServerResult: ...

class TimeseriesatParams(Protocol):
    locationId: str

class TimeseriesatCallContext(Protocol):
    params: TimeseriesatParams
    @property
    def results(self) -> results_server.TimeseriesatServerResult: ...

class LocationsParams(Protocol): ...

class LocationsCallContext(Protocol):
    params: LocationsParams
    @property
    def results(self) -> results_server.LocationsServerResult: ...

class StreamlocationsParams(Protocol):
    startAfterLocationId: str

class StreamlocationsCallContext(Protocol):
    params: StreamlocationsParams
    @property
    def results(self) -> results_server.StreamlocationsServerResult: ...

class GetavailabledatasetsParams(Protocol): ...

class GetavailabledatasetsCallContext(Protocol):
    params: GetavailabledatasetsParams
    @property
    def results(self) -> results_server.GetavailabledatasetsServerResult: ...

class GetdatasetsforParams(Protocol):
    template: readers.MetadataReader

class GetdatasetsforCallContext(Protocol):
    params: GetdatasetsforParams
    @property
    def results(self) -> results_server.GetdatasetsforServerResult: ...

class CreateParams(Protocol):
    csvData: str
    config: readers.CSVConfigReader

class CreateCallContext(Protocol):
    params: CreateParams
    @property
    def results(self) -> results_server.CreateServerResult: ...

class WrappedtimeseriesParams(Protocol): ...

class WrappedtimeseriesCallContext(Protocol):
    params: WrappedtimeseriesParams
    @property
    def results(self) -> results_server.WrappedtimeseriesServerResult: ...

class AlteredelementsParams(Protocol): ...

class AlteredelementsCallContext(Protocol):
    params: AlteredelementsParams
    @property
    def results(self) -> results_server.AlteredelementsServerResult: ...

class AlterParams(Protocol):
    desc: readers.AlteredReader
    asNewTimeSeries: bool

class AlterCallContext(Protocol):
    params: AlterParams
    @property
    def results(self) -> results_server.AlterServerResult: ...

class RemoveParams(Protocol):
    alteredElement: enums.ElementEnum

class RemoveCallContext(Protocol):
    params: RemoveParams

class ReplacewrappedtimeseriesParams(Protocol):
    timeSeries: clients.TimeSeriesClient

class ReplacewrappedtimeseriesCallContext(Protocol):
    params: ReplacewrappedtimeseriesParams

class WrapParams(Protocol):
    timeSeries: clients.TimeSeriesClient

class WrapCallContext(Protocol):
    params: WrapParams
    @property
    def results(self) -> results_server.WrapServerResult: ...
