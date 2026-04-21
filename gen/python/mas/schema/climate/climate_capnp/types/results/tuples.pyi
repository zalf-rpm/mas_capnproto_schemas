"""Result tuple helper types for `climate.capnp`."""

from collections.abc import Sequence
from typing import Any, NamedTuple

from mas.schema.climate.climate_capnp.types import builders as builders
from mas.schema.climate.climate_capnp.types import clients as clients
from mas.schema.climate.climate_capnp.types import enums as enums
from mas.schema.climate.climate_capnp.types import modules as modules
from mas.schema.climate.climate_capnp.types import readers as readers
from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader

class CategoriesResultTuple(NamedTuple):
    types: (
        builders.IdInformationListBuilder
        | readers.IdInformationListReader
        | Sequence[Any]
    )

class SupportedvaluesResultTuple(NamedTuple):
    values: (
        builders.IdInformationListBuilder
        | readers.IdInformationListReader
        | Sequence[Any]
    )

class ForoneResultTuple(NamedTuple):
    id: str
    name: str
    description: str

class ForallResultTuple(NamedTuple):
    all: builders.PairListBuilder | readers.PairListReader | Sequence[Any]

class ResolutionResultTuple(NamedTuple):
    resolution: enums.TimeSeriesResolutionEnum

class RangeResultTuple(NamedTuple):
    startDate: DateBuilder | DateReader | dict[str, Any]
    endDate: DateBuilder | DateReader | dict[str, Any]

class HeaderResultTuple(NamedTuple):
    header: (
        builders.ElementEnumListBuilder | readers.ElementEnumListReader | Sequence[Any]
    )

class DataResultTuple(NamedTuple):
    data: (
        builders.Float32ListListBuilder | readers.Float32ListListReader | Sequence[Any]
    )

class DatatResultTuple(NamedTuple):
    data: (
        builders.Float32ListListBuilder | readers.Float32ListListReader | Sequence[Any]
    )

class SubrangeResultTuple(NamedTuple):
    timeSeries: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient

class SubheaderResultTuple(NamedTuple):
    timeSeries: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient

class TimeSeriesMetadataResultTuple(NamedTuple):
    entries: builders.EntryListBuilder | readers.EntryListReader | Sequence[Any]
    info: (
        modules._MetadataStructModule._InformationInterfaceModule.Server
        | clients.InformationClient
    )

class LocationResultTuple(NamedTuple):
    id: IdInformationBuilder | IdInformationReader | dict[str, Any]
    heightNN: float
    latlon: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]
    timeSeries: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient
    customData: builders.KVListBuilder | readers.KVListReader | Sequence[Any]

class NextlocationsResultTuple(NamedTuple):
    locations: builders.LocationListBuilder | readers.LocationListReader | Sequence[Any]

class DatasetMetadataResultTuple(NamedTuple):
    entries: builders.EntryListBuilder | readers.EntryListReader | Sequence[Any]
    info: (
        modules._MetadataStructModule._InformationInterfaceModule.Server
        | clients.InformationClient
    )

class ClosesttimeseriesatResultTuple(NamedTuple):
    timeSeries: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient

class TimeseriesatResultTuple(NamedTuple):
    timeSeries: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient

class LocationsResultTuple(NamedTuple):
    locations: builders.LocationListBuilder | readers.LocationListReader | Sequence[Any]

class StreamlocationsResultTuple(NamedTuple):
    locationsCallback: (
        modules._DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
        | clients.GetLocationsCallbackClient
    )

class GetavailabledatasetsResultTuple(NamedTuple):
    datasets: (
        builders.MetaPlusDataListBuilder
        | readers.MetaPlusDataListReader
        | Sequence[Any]
    )

class GetdatasetsforResultTuple(NamedTuple):
    datasets: (
        builders.DatasetClientListBuilder
        | readers.DatasetClientListReader
        | Sequence[Any]
    )

class CreateResultTuple(NamedTuple):
    timeseries: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient
    error: str

class WrappedtimeseriesResultTuple(NamedTuple):
    timeSeries: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient

class AlteredelementsResultTuple(NamedTuple):
    list: builders.AlteredListBuilder | readers.AlteredListReader | Sequence[Any]

class AlterResultTuple(NamedTuple):
    timeSeries: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient

class WrapResultTuple(NamedTuple):
    wrapper: (
        modules._AlterTimeSeriesWrapperInterfaceModule.Server
        | clients.AlterTimeSeriesWrapperClient
    )
