"""Runtime placeholder module for result tuple helpers of `climate.capnp`."""

from typing import NamedTuple


class WrapResultTuple(NamedTuple):
    wrapper: object


class AlterResultTuple(NamedTuple):
    timeSeries: object


class AlteredelementsResultTuple(NamedTuple):
    list: object


class WrappedtimeseriesResultTuple(NamedTuple):
    timeSeries: object


class CreateResultTuple(NamedTuple):
    timeseries: object
    error: object


class ClosesttimeseriesatResultTuple(NamedTuple):
    timeSeries: object


class DatasetMetadataResultTuple(NamedTuple):
    entries: object
    info: object


class LocationsResultTuple(NamedTuple):
    locations: object


class StreamlocationsResultTuple(NamedTuple):
    locationsCallback: object


class TimeseriesatResultTuple(NamedTuple):
    timeSeries: object


class NextlocationsResultTuple(NamedTuple):
    locations: object


class ForallResultTuple(NamedTuple):
    all: object


class ForoneResultTuple(NamedTuple):
    id: object
    name: object
    description: object


class CategoriesResultTuple(NamedTuple):
    types: object


class SupportedvaluesResultTuple(NamedTuple):
    values: object


class GetavailabledatasetsResultTuple(NamedTuple):
    datasets: object


class GetdatasetsforResultTuple(NamedTuple):
    datasets: object


class DataResultTuple(NamedTuple):
    data: object


class DatatResultTuple(NamedTuple):
    data: object


class HeaderResultTuple(NamedTuple):
    header: object


class LocationResultTuple(NamedTuple):
    id: object
    heightNN: object
    latlon: object
    timeSeries: object
    customData: object


class RangeResultTuple(NamedTuple):
    startDate: object
    endDate: object


class ResolutionResultTuple(NamedTuple):
    resolution: object


class SubheaderResultTuple(NamedTuple):
    timeSeries: object


class SubrangeResultTuple(NamedTuple):
    timeSeries: object


class TimeSeriesMetadataResultTuple(NamedTuple):
    entries: object
    info: object


__all__ = [
    "AlterResultTuple",
    "AlteredelementsResultTuple",
    "CategoriesResultTuple",
    "ClosesttimeseriesatResultTuple",
    "CreateResultTuple",
    "DataResultTuple",
    "DatasetMetadataResultTuple",
    "DatatResultTuple",
    "ForallResultTuple",
    "ForoneResultTuple",
    "GetavailabledatasetsResultTuple",
    "GetdatasetsforResultTuple",
    "HeaderResultTuple",
    "LocationResultTuple",
    "LocationsResultTuple",
    "NextlocationsResultTuple",
    "RangeResultTuple",
    "ResolutionResultTuple",
    "StreamlocationsResultTuple",
    "SubheaderResultTuple",
    "SubrangeResultTuple",
    "SupportedvaluesResultTuple",
    "TimeSeriesMetadataResultTuple",
    "TimeseriesatResultTuple",
    "WrapResultTuple",
    "WrappedtimeseriesResultTuple",
]
