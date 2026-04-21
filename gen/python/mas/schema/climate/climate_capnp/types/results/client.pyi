"""Client result helper types for `climate.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from mas.schema.climate.climate_capnp.types import clients as clients
from mas.schema.climate.climate_capnp.types import enums as enums
from mas.schema.climate.climate_capnp.types import readers as readers
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader

class CategoriesResult(Awaitable[CategoriesResult], Protocol):
    types: readers.IdInformationListReader

class SupportedvaluesResult(Awaitable[SupportedvaluesResult], Protocol):
    values: readers.IdInformationListReader

class ForoneResult(Awaitable[ForoneResult], Protocol):
    id: str
    name: str
    description: str

class ForallResult(Awaitable[ForallResult], Protocol):
    all: readers.PairListReader

class ResolutionResult(Awaitable[ResolutionResult], Protocol):
    resolution: enums.TimeSeriesResolutionEnum

class RangeResult(Awaitable[RangeResult], Protocol):
    startDate: DateReader
    endDate: DateReader

class HeaderResult(Awaitable[HeaderResult], Protocol):
    header: readers.ElementEnumListReader

class DataResult(Awaitable[DataResult], Protocol):
    data: readers.Float32ListListReader

class DatatResult(Awaitable[DatatResult], Protocol):
    data: readers.Float32ListListReader

class SubrangeResult(Awaitable[SubrangeResult], Protocol):
    timeSeries: clients.TimeSeriesClient

class SubheaderResult(Awaitable[SubheaderResult], Protocol):
    timeSeries: clients.TimeSeriesClient

class TimeSeriesMetadataResult(Awaitable[TimeSeriesMetadataResult], Protocol):
    entries: readers.EntryListReader
    info: clients.InformationClient

class LocationResult(Awaitable[LocationResult], Protocol):
    id: IdInformationReader
    heightNN: float
    latlon: LatLonCoordReader
    timeSeries: clients.TimeSeriesClient
    customData: readers.KVListReader

class NextlocationsResult(Awaitable[NextlocationsResult], Protocol):
    locations: readers.LocationListReader

class DatasetMetadataResult(Awaitable[DatasetMetadataResult], Protocol):
    entries: readers.EntryListReader
    info: clients.InformationClient

class ClosesttimeseriesatResult(Awaitable[ClosesttimeseriesatResult], Protocol):
    timeSeries: clients.TimeSeriesClient

class TimeseriesatResult(Awaitable[TimeseriesatResult], Protocol):
    timeSeries: clients.TimeSeriesClient

class LocationsResult(Awaitable[LocationsResult], Protocol):
    locations: readers.LocationListReader

class StreamlocationsResult(Awaitable[StreamlocationsResult], Protocol):
    locationsCallback: clients.GetLocationsCallbackClient

class GetavailabledatasetsResult(Awaitable[GetavailabledatasetsResult], Protocol):
    datasets: readers.MetaPlusDataListReader

class GetdatasetsforResult(Awaitable[GetdatasetsforResult], Protocol):
    datasets: readers.DatasetClientListReader

class CreateResult(Awaitable[CreateResult], Protocol):
    timeseries: clients.TimeSeriesClient
    error: str

class WrappedtimeseriesResult(Awaitable[WrappedtimeseriesResult], Protocol):
    timeSeries: clients.TimeSeriesClient

class AlteredelementsResult(Awaitable[AlteredelementsResult], Protocol):
    list: readers.AlteredListReader

class AlterResult(Awaitable[AlterResult], Protocol):
    timeSeries: clients.TimeSeriesClient

class RemoveResult(Awaitable[None], Protocol): ...
class ReplacewrappedtimeseriesResult(Awaitable[None], Protocol): ...

class WrapResult(Awaitable[WrapResult], Protocol):
    wrapper: clients.AlterTimeSeriesWrapperClient
