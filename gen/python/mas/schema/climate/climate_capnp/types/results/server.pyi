"""Server result helper types for `climate.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.climate.climate_capnp.types import builders as builders
from mas.schema.climate.climate_capnp.types import clients as clients
from mas.schema.climate.climate_capnp.types import enums as enums
from mas.schema.climate.climate_capnp.types import modules as modules
from mas.schema.climate.climate_capnp.types import readers as readers
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.common.date_capnp.types.readers import DateReader

class CategoriesServerResult(_DynamicStructBuilder):
    @property
    def types(self) -> builders.IdInformationListBuilder: ...
    @types.setter
    def types(
        self,
        value: builders.IdInformationListBuilder
        | readers.IdInformationListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["types"],
        size: int | None = None,
    ) -> builders.IdInformationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class SupportedvaluesServerResult(_DynamicStructBuilder):
    @property
    def values(self) -> builders.IdInformationListBuilder: ...
    @values.setter
    def values(
        self,
        value: builders.IdInformationListBuilder
        | readers.IdInformationListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["values"],
        size: int | None = None,
    ) -> builders.IdInformationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ForallServerResult(_DynamicStructBuilder):
    @property
    def all(self) -> builders.PairListBuilder: ...
    @all.setter
    def all(
        self,
        value: builders.PairListBuilder | readers.PairListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["all"],
        size: int | None = None,
    ) -> builders.PairListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ResolutionServerResult(_DynamicStructBuilder):
    @property
    def resolution(self) -> enums.TimeSeriesResolutionEnum: ...
    @resolution.setter
    def resolution(self, value: enums.TimeSeriesResolutionEnum) -> None: ...

class RangeServerResult(_DynamicStructBuilder):
    @property
    def startDate(self) -> DateBuilder: ...
    @startDate.setter
    def startDate(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
    @property
    def endDate(self) -> DateBuilder: ...
    @endDate.setter
    def endDate(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
    @overload
    def init(
        self,
        field: Literal["startDate"],
        size: int | None = None,
    ) -> DateBuilder: ...
    @overload
    def init(
        self,
        field: Literal["endDate"],
        size: int | None = None,
    ) -> DateBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class HeaderServerResult(_DynamicStructBuilder):
    @property
    def header(self) -> builders.ElementEnumListBuilder: ...
    @header.setter
    def header(
        self,
        value: builders.ElementEnumListBuilder
        | readers.ElementEnumListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["header"],
        size: int | None = None,
    ) -> builders.ElementEnumListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class DataServerResult(_DynamicStructBuilder):
    @property
    def data(self) -> builders.Float32ListListBuilder: ...
    @data.setter
    def data(
        self,
        value: builders.Float32ListListBuilder
        | readers.Float32ListListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["data"],
        size: int | None = None,
    ) -> builders.Float32ListListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class DatatServerResult(_DynamicStructBuilder):
    @property
    def data(self) -> builders.Float32ListListBuilder: ...
    @data.setter
    def data(
        self,
        value: builders.Float32ListListBuilder
        | readers.Float32ListListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["data"],
        size: int | None = None,
    ) -> builders.Float32ListListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class SubrangeServerResult(_DynamicStructBuilder):
    @property
    def timeSeries(
        self,
    ) -> modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient,
    ) -> None: ...

class SubheaderServerResult(_DynamicStructBuilder):
    @property
    def timeSeries(
        self,
    ) -> modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient,
    ) -> None: ...

class NextlocationsServerResult(_DynamicStructBuilder):
    @property
    def locations(self) -> builders.LocationListBuilder: ...
    @locations.setter
    def locations(
        self,
        value: builders.LocationListBuilder
        | readers.LocationListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["locations"],
        size: int | None = None,
    ) -> builders.LocationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ClosesttimeseriesatServerResult(_DynamicStructBuilder):
    @property
    def timeSeries(
        self,
    ) -> modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient,
    ) -> None: ...

class TimeseriesatServerResult(_DynamicStructBuilder):
    @property
    def timeSeries(
        self,
    ) -> modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient,
    ) -> None: ...

class LocationsServerResult(_DynamicStructBuilder):
    @property
    def locations(self) -> builders.LocationListBuilder: ...
    @locations.setter
    def locations(
        self,
        value: builders.LocationListBuilder
        | readers.LocationListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["locations"],
        size: int | None = None,
    ) -> builders.LocationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class StreamlocationsServerResult(_DynamicStructBuilder):
    @property
    def locationsCallback(
        self,
    ) -> (
        modules._DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
        | clients.GetLocationsCallbackClient
    ): ...
    @locationsCallback.setter
    def locationsCallback(
        self,
        value: modules._DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
        | clients.GetLocationsCallbackClient,
    ) -> None: ...

class GetavailabledatasetsServerResult(_DynamicStructBuilder):
    @property
    def datasets(self) -> builders.MetaPlusDataListBuilder: ...
    @datasets.setter
    def datasets(
        self,
        value: builders.MetaPlusDataListBuilder
        | readers.MetaPlusDataListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["datasets"],
        size: int | None = None,
    ) -> builders.MetaPlusDataListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class GetdatasetsforServerResult(_DynamicStructBuilder):
    @property
    def datasets(self) -> builders.DatasetClientListBuilder: ...
    @datasets.setter
    def datasets(
        self,
        value: builders.DatasetClientListBuilder
        | readers.DatasetClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["datasets"],
        size: int | None = None,
    ) -> builders.DatasetClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class CreateServerResult(_DynamicStructBuilder):
    @property
    def timeseries(
        self,
    ) -> modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient: ...
    @timeseries.setter
    def timeseries(
        self,
        value: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient,
    ) -> None: ...
    @property
    def error(self) -> str: ...
    @error.setter
    def error(self, value: str) -> None: ...

class WrappedtimeseriesServerResult(_DynamicStructBuilder):
    @property
    def timeSeries(
        self,
    ) -> modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient,
    ) -> None: ...

class AlteredelementsServerResult(_DynamicStructBuilder):
    @property
    def list(self) -> builders.AlteredListBuilder: ...
    @list.setter
    def list(
        self,
        value: builders.AlteredListBuilder | readers.AlteredListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["list"],
        size: int | None = None,
    ) -> builders.AlteredListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class AlterServerResult(_DynamicStructBuilder):
    @property
    def timeSeries(
        self,
    ) -> modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: modules._TimeSeriesInterfaceModule.Server | clients.TimeSeriesClient,
    ) -> None: ...

class WrapServerResult(_DynamicStructBuilder):
    @property
    def wrapper(
        self,
    ) -> (
        modules._AlterTimeSeriesWrapperInterfaceModule.Server
        | clients.AlterTimeSeriesWrapperClient
    ): ...
    @wrapper.setter
    def wrapper(
        self,
        value: modules._AlterTimeSeriesWrapperInterfaceModule.Server
        | clients.AlterTimeSeriesWrapperClient,
    ) -> None: ...
