"""Client helper types for `climate.capnp`."""

from collections.abc import Sequence
from typing import Any

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.climate.climate_capnp.types import builders as builders
from mas.schema.climate.climate_capnp.types import enums as enums
from mas.schema.climate.climate_capnp.types import modules as modules
from mas.schema.climate.climate_capnp.types import readers as readers
from mas.schema.climate.climate_capnp.types import requests as requests
from mas.schema.climate.climate_capnp.types.results import client as results_client
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient

class SupportedClient(_DynamicCapabilityClient):
    def categories(self) -> results_client.CategoriesResult: ...
    def supportedValues(
        self,
        typeId: str | None = None,
    ) -> results_client.SupportedvaluesResult: ...
    def categories_request(self) -> requests.CategoriesRequest: ...
    def supportedValues_request(
        self,
        typeId: str | None = None,
    ) -> requests.SupportedvaluesRequest: ...

class InformationClient(_DynamicCapabilityClient):
    def forOne(
        self,
        entry: builders.EntryBuilder
        | readers.EntryReader
        | dict[str, Any]
        | None = None,
    ) -> results_client.ForoneResult: ...
    def forAll(self) -> results_client.ForallResult: ...
    def forOne_request(
        self,
        entry: builders.EntryBuilder | None = None,
    ) -> requests.ForoneRequest: ...
    def forAll_request(self) -> requests.ForallRequest: ...

class TimeSeriesClient(IdentifiableClient, PersistentClient):
    def resolution(self) -> results_client.ResolutionResult: ...
    def range(self) -> results_client.RangeResult: ...
    def header(self) -> results_client.HeaderResult: ...
    def data(self) -> results_client.DataResult: ...
    def dataT(self) -> results_client.DatatResult: ...
    def subrange(
        self,
        start: DateBuilder | DateReader | dict[str, Any] | None = None,
        end: DateBuilder | DateReader | dict[str, Any] | None = None,
    ) -> results_client.SubrangeResult: ...
    def subheader(
        self,
        elements: builders.ElementEnumListBuilder
        | readers.ElementEnumListReader
        | Sequence[Any]
        | None = None,
    ) -> results_client.SubheaderResult: ...
    def metadata(self) -> results_client.TimeSeriesMetadataResult: ...
    def location(self) -> results_client.LocationResult: ...
    def resolution_request(self) -> requests.ResolutionRequest: ...
    def range_request(self) -> requests.RangeRequest: ...
    def header_request(self) -> requests.HeaderRequest: ...
    def data_request(self) -> requests.DataRequest: ...
    def dataT_request(self) -> requests.DatatRequest: ...
    def subrange_request(
        self,
        start: DateBuilder | None = None,
        end: DateBuilder | None = None,
    ) -> requests.SubrangeRequest: ...
    def subheader_request(
        self,
        elements: builders.ElementEnumListBuilder
        | readers.ElementEnumListReader
        | Sequence[Any]
        | None = None,
    ) -> requests.SubheaderRequest: ...
    def metadata_request(self) -> requests.TimeSeriesMetadataRequest: ...
    def location_request(self) -> requests.LocationRequest: ...

class GetLocationsCallbackClient(_DynamicCapabilityClient):
    def nextLocations(
        self,
        maxCount: int | None = None,
    ) -> results_client.NextlocationsResult: ...
    def nextLocations_request(
        self,
        maxCount: int | None = None,
    ) -> requests.NextlocationsRequest: ...

class DatasetClient(IdentifiableClient, PersistentClient):
    def metadata(self) -> results_client.DatasetMetadataResult: ...
    def closestTimeSeriesAt(
        self,
        latlon: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any] | None = None,
    ) -> results_client.ClosesttimeseriesatResult: ...
    def timeSeriesAt(
        self,
        locationId: str | None = None,
    ) -> results_client.TimeseriesatResult: ...
    def locations(self) -> results_client.LocationsResult: ...
    def streamLocations(
        self,
        startAfterLocationId: str | None = None,
    ) -> results_client.StreamlocationsResult: ...
    def metadata_request(self) -> requests.DatasetMetadataRequest: ...
    def closestTimeSeriesAt_request(
        self,
        latlon: LatLonCoordBuilder | None = None,
    ) -> requests.ClosesttimeseriesatRequest: ...
    def timeSeriesAt_request(
        self,
        locationId: str | None = None,
    ) -> requests.TimeseriesatRequest: ...
    def locations_request(self) -> requests.LocationsRequest: ...
    def streamLocations_request(
        self,
        startAfterLocationId: str | None = None,
    ) -> requests.StreamlocationsRequest: ...

class ServiceClient(IdentifiableClient, PersistentClient):
    def getAvailableDatasets(self) -> results_client.GetavailabledatasetsResult: ...
    def getDatasetsFor(
        self,
        template: builders.MetadataBuilder
        | readers.MetadataReader
        | dict[str, Any]
        | None = None,
    ) -> results_client.GetdatasetsforResult: ...
    def getAvailableDatasets_request(self) -> requests.GetavailabledatasetsRequest: ...
    def getDatasetsFor_request(
        self,
        template: builders.MetadataBuilder | None = None,
    ) -> requests.GetdatasetsforRequest: ...

class CSVTimeSeriesFactoryClient(IdentifiableClient):
    def create(
        self,
        csvData: str | None = None,
        config: builders.CSVConfigBuilder
        | readers.CSVConfigReader
        | dict[str, Any]
        | None = None,
    ) -> results_client.CreateResult: ...
    def create_request(
        self,
        csvData: str | None = None,
        config: builders.CSVConfigBuilder | None = None,
    ) -> requests.CreateRequest: ...

class AlterTimeSeriesWrapperClient(TimeSeriesClient):
    def wrappedTimeSeries(self) -> results_client.WrappedtimeseriesResult: ...
    def alteredElements(self) -> results_client.AlteredelementsResult: ...
    def alter(
        self,
        desc: builders.AlteredBuilder
        | readers.AlteredReader
        | dict[str, Any]
        | None = None,
        asNewTimeSeries: bool | None = None,
    ) -> results_client.AlterResult: ...
    def remove(
        self,
        alteredElement: enums.ElementEnum | None = None,
    ) -> results_client.RemoveResult: ...
    def replaceWrappedTimeSeries(
        self,
        timeSeries: TimeSeriesClient
        | modules._TimeSeriesInterfaceModule.Server
        | None = None,
    ) -> results_client.ReplacewrappedtimeseriesResult: ...
    def wrappedTimeSeries_request(self) -> requests.WrappedtimeseriesRequest: ...
    def alteredElements_request(self) -> requests.AlteredelementsRequest: ...
    def alter_request(
        self,
        desc: builders.AlteredBuilder | None = None,
        asNewTimeSeries: bool | None = None,
    ) -> requests.AlterRequest: ...
    def remove_request(
        self,
        alteredElement: enums.ElementEnum | None = None,
    ) -> requests.RemoveRequest: ...
    def replaceWrappedTimeSeries_request(
        self,
        timeSeries: TimeSeriesClient
        | modules._TimeSeriesInterfaceModule.Server
        | None = None,
    ) -> requests.ReplacewrappedtimeseriesRequest: ...

class AlterTimeSeriesWrapperFactoryClient(IdentifiableClient):
    def wrap(
        self,
        timeSeries: TimeSeriesClient
        | modules._TimeSeriesInterfaceModule.Server
        | None = None,
    ) -> results_client.WrapResult: ...
    def wrap_request(
        self,
        timeSeries: TimeSeriesClient
        | modules._TimeSeriesInterfaceModule.Server
        | None = None,
    ) -> requests.WrapRequest: ...
