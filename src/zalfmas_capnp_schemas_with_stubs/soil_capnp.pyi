"""This is an automatically generated stub for `soil.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
from contextlib import contextmanager
from enum import Enum
from io import BufferedWriter
from typing import Any, BinaryIO, Literal, Protocol, overload

from capnp import _DynamicListBuilder

from .common_capnp import Identifiable
from .geo_capnp import LatLonCoord, LatLonCoordBuilder, LatLonCoordReader
from .persistence_capnp import Persistent

class SType(Enum):
    unknown = "unknown"
    ka5 = "ka5"

class PropertyName(Enum):
    soilType = "soilType"
    sand = "sand"
    clay = "clay"
    silt = "silt"
    pH = "pH"
    sceleton = "sceleton"
    organicCarbon = "organicCarbon"
    organicMatter = "organicMatter"
    bulkDensity = "bulkDensity"
    rawDensity = "rawDensity"
    fieldCapacity = "fieldCapacity"
    permanentWiltingPoint = "permanentWiltingPoint"
    saturation = "saturation"
    soilMoisture = "soilMoisture"
    soilWaterConductivityCoefficient = "soilWaterConductivityCoefficient"
    ammonium = "ammonium"
    nitrate = "nitrate"
    cnRatio = "cnRatio"
    inGroundwater = "inGroundwater"
    impenetrable = "impenetrable"

class Layer:
    class Property:
        @property
        def name(self) -> PropertyName: ...
        @property
        def f32Value(self) -> float: ...
        @property
        def bValue(self) -> bool: ...
        @property
        def type(self) -> str: ...
        @property
        def unset(self) -> None: ...
        def which(self) -> Literal["f32Value", "bValue", "type", "unset"]: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Layer.PropertyReader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Layer.PropertyReader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            name: PropertyName
            | Literal[
                "soilType",
                "sand",
                "clay",
                "silt",
                "pH",
                "sceleton",
                "organicCarbon",
                "organicMatter",
                "bulkDensity",
                "rawDensity",
                "fieldCapacity",
                "permanentWiltingPoint",
                "saturation",
                "soilMoisture",
                "soilWaterConductivityCoefficient",
                "ammonium",
                "nitrate",
                "cnRatio",
                "inGroundwater",
                "impenetrable",
            ]
            | None = None,
            f32Value: float | None = None,
            bValue: bool | None = None,
            type: str | None = None,
            unset: None | None = None,
        ) -> Layer.PropertyBuilder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Layer.PropertyReader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Layer.PropertyReader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class PropertyReader(Layer.Property):
        def as_builder(self) -> Layer.PropertyBuilder: ...

    class PropertyBuilder(Layer.Property):
        @property
        def name(self) -> PropertyName: ...
        @name.setter
        def name(
            self,
            value: PropertyName
            | Literal[
                "soilType",
                "sand",
                "clay",
                "silt",
                "pH",
                "sceleton",
                "organicCarbon",
                "organicMatter",
                "bulkDensity",
                "rawDensity",
                "fieldCapacity",
                "permanentWiltingPoint",
                "saturation",
                "soilMoisture",
                "soilWaterConductivityCoefficient",
                "ammonium",
                "nitrate",
                "cnRatio",
                "inGroundwater",
                "impenetrable",
            ],
        ) -> None: ...
        @property
        def f32Value(self) -> float: ...
        @f32Value.setter
        def f32Value(self, value: float) -> None: ...
        @property
        def bValue(self) -> bool: ...
        @bValue.setter
        def bValue(self, value: bool) -> None: ...
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str) -> None: ...
        @property
        def unset(self) -> None: ...
        @unset.setter
        def unset(self, value: None) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Layer.PropertyBuilder: ...
        def copy(self) -> Layer.PropertyBuilder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Layer.PropertyReader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @property
    def properties(self) -> Sequence[Layer.Property]: ...
    @property
    def size(self) -> float: ...
    @property
    def description(self) -> str: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[LayerReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> LayerReader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        properties: Sequence[Layer.PropertyBuilder]
        | Sequence[dict[str, Any]]
        | None = None,
        size: float | None = None,
        description: str | None = None,
    ) -> LayerBuilder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> LayerReader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> LayerReader: ...
    def to_dict(self) -> dict[str, Any]: ...

class LayerReader(Layer):
    @property
    def properties(self) -> Sequence[Layer.PropertyReader]: ...
    def as_builder(self) -> LayerBuilder: ...

class LayerBuilder(Layer):
    @property
    def properties(self) -> _DynamicListBuilder[Layer.PropertyBuilder]: ...
    @properties.setter
    def properties(
        self,
        value: Sequence[Layer.Property | Layer.PropertyBuilder | Layer.PropertyReader]
        | Sequence[dict[str, Any]],
    ) -> None: ...
    @property
    def size(self) -> float: ...
    @size.setter
    def size(self, value: float) -> None: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str) -> None: ...
    @staticmethod
    def from_dict(dictionary: dict[str, Any]) -> LayerBuilder: ...
    def init(
        self: Any, name: Literal["properties"], size: int = ...
    ) -> _DynamicListBuilder[Layer.PropertyBuilder]: ...
    def copy(self) -> LayerBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> LayerReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class Query:
    class Result:
        @property
        def failed(self) -> bool: ...
        @property
        def mandatory(self) -> Sequence[PropertyName]: ...
        @property
        def optional(self) -> Sequence[PropertyName]: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Query.ResultReader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Query.ResultReader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            failed: bool | None = None,
            mandatory: Sequence[PropertyName] | None = None,
            optional: Sequence[PropertyName] | None = None,
        ) -> Query.ResultBuilder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Query.ResultReader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Query.ResultReader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class ResultReader(Query.Result):
        def as_builder(self) -> Query.ResultBuilder: ...

    class ResultBuilder(Query.Result):
        @property
        def failed(self) -> bool: ...
        @failed.setter
        def failed(self, value: bool) -> None: ...
        @property
        def mandatory(self) -> Sequence[PropertyName]: ...
        @mandatory.setter
        def mandatory(self, value: Sequence[PropertyName]) -> None: ...
        @property
        def optional(self) -> Sequence[PropertyName]: ...
        @optional.setter
        def optional(self, value: Sequence[PropertyName]) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Query.ResultBuilder: ...
        @overload
        def init(
            self: Any, name: Literal["mandatory"], size: int = ...
        ) -> _DynamicListBuilder[PropertyName]: ...
        @overload
        def init(
            self: Any, name: Literal["optional"], size: int = ...
        ) -> _DynamicListBuilder[PropertyName]: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        def copy(self) -> Query.ResultBuilder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Query.ResultReader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @property
    def mandatory(self) -> Sequence[PropertyName]: ...
    @property
    def optional(self) -> Sequence[PropertyName]: ...
    @property
    def onlyRawData(self) -> bool: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[QueryReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> QueryReader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        mandatory: Sequence[PropertyName] | None = None,
        optional: Sequence[PropertyName] | None = None,
        onlyRawData: bool | None = None,
    ) -> QueryBuilder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> QueryReader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> QueryReader: ...
    def to_dict(self) -> dict[str, Any]: ...

class QueryReader(Query):
    def as_builder(self) -> QueryBuilder: ...

class QueryBuilder(Query):
    @property
    def mandatory(self) -> Sequence[PropertyName]: ...
    @mandatory.setter
    def mandatory(self, value: Sequence[PropertyName]) -> None: ...
    @property
    def optional(self) -> Sequence[PropertyName]: ...
    @optional.setter
    def optional(self, value: Sequence[PropertyName]) -> None: ...
    @property
    def onlyRawData(self) -> bool: ...
    @onlyRawData.setter
    def onlyRawData(self, value: bool) -> None: ...
    @staticmethod
    def from_dict(dictionary: dict[str, Any]) -> QueryBuilder: ...
    @overload
    def init(
        self: Any, name: Literal["mandatory"], size: int = ...
    ) -> _DynamicListBuilder[PropertyName]: ...
    @overload
    def init(
        self: Any, name: Literal["optional"], size: int = ...
    ) -> _DynamicListBuilder[PropertyName]: ...
    def init(self: Any, name: str, size: int = ...) -> Any: ...
    def copy(self) -> QueryBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> QueryReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class ProfileData:
    @property
    def layers(self) -> Sequence[Layer]: ...
    @property
    def percentageOfArea(self) -> float: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[ProfileDataReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ProfileDataReader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        layers: Sequence[LayerBuilder] | Sequence[dict[str, Any]] | None = None,
        percentageOfArea: float | None = None,
    ) -> ProfileDataBuilder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ProfileDataReader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ProfileDataReader: ...
    def to_dict(self) -> dict[str, Any]: ...

class ProfileDataReader(ProfileData):
    @property
    def layers(self) -> Sequence[LayerReader]: ...
    def as_builder(self) -> ProfileDataBuilder: ...

class ProfileDataBuilder(ProfileData):
    @property
    def layers(self) -> _DynamicListBuilder[LayerBuilder]: ...
    @layers.setter
    def layers(
        self,
        value: Sequence[Layer | LayerBuilder | LayerReader] | Sequence[dict[str, Any]],
    ) -> None: ...
    @property
    def percentageOfArea(self) -> float: ...
    @percentageOfArea.setter
    def percentageOfArea(self, value: float) -> None: ...
    @staticmethod
    def from_dict(dictionary: dict[str, Any]) -> ProfileDataBuilder: ...
    def init(
        self: Any, name: Literal["layers"], size: int = ...
    ) -> _DynamicListBuilder[LayerBuilder]: ...
    def copy(self) -> ProfileDataBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> ProfileDataReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class Profile(Identifiable, Persistent, Protocol):
    def data(self) -> Awaitable[ProfileDataReader]: ...
    class DataRequest(Protocol):
        def send(self) -> Awaitable[ProfileDataReader]: ...

    def data_request(self) -> DataRequest: ...
    def geoLocation(self) -> Awaitable[LatLonCoordReader]: ...
    class GeolocationRequest(Protocol):
        def send(self) -> Awaitable[LatLonCoordReader]: ...

    def geoLocation_request(self) -> GeolocationRequest: ...
    class Server(Identifiable.Server, Persistent.Server):
        def data(self, **kwargs) -> Awaitable[ProfileData]: ...
        def geoLocation(self, **kwargs) -> Awaitable[LatLonCoord]: ...

class Service(Identifiable, Persistent, Protocol):
    class Stream(Protocol):
        class NextprofilesResult(Awaitable[NextprofilesResult], Protocol):
            profiles: Sequence[Profile]

        def nextProfiles(self, maxCount: int) -> NextprofilesResult: ...
        class NextprofilesRequest(Protocol):
            maxCount: int
            def send(self) -> Service.Stream.NextprofilesResult: ...

        def nextProfiles_request(self) -> NextprofilesRequest: ...
        class Server:
            def nextProfiles(
                self, maxCount: int, **kwargs
            ) -> Awaitable[Sequence[Profile]]: ...

    def checkAvailableParameters(
        self,
        mandatory: Sequence[PropertyName],
        optional: Sequence[PropertyName],
        onlyRawData: bool,
    ) -> Awaitable[Query.ResultReader]: ...
    class CheckavailableparametersRequest(Protocol):
        mandatory: Sequence[PropertyName]
        optional: Sequence[PropertyName]
        onlyRawData: bool
        def send(self) -> Awaitable[Query.ResultReader]: ...

    def checkAvailableParameters_request(self) -> CheckavailableparametersRequest: ...
    class GetallavailableparametersResult(
        Awaitable[GetallavailableparametersResult], Protocol
    ):
        mandatory: Sequence[PropertyName]
        optional: Sequence[PropertyName]

    def getAllAvailableParameters(
        self, onlyRawData: bool
    ) -> GetallavailableparametersResult: ...
    class GetallavailableparametersRequest(Protocol):
        onlyRawData: bool
        def send(self) -> Service.GetallavailableparametersResult: ...

    def getAllAvailableParameters_request(self) -> GetallavailableparametersRequest: ...
    class ClosestprofilesatResult(Awaitable[ClosestprofilesatResult], Protocol):
        profiles: Sequence[Profile]

    def closestProfilesAt(
        self, coord: LatLonCoord | dict[str, Any], query: Query | dict[str, Any]
    ) -> ClosestprofilesatResult: ...
    class ClosestprofilesatRequest(Protocol):
        coord: LatLonCoordBuilder
        query: QueryBuilder
        def send(self) -> Service.ClosestprofilesatResult: ...

    def closestProfilesAt_request(self) -> ClosestprofilesatRequest: ...
    class StreamallprofilesResult(Awaitable[StreamallprofilesResult], Protocol):
        allProfiles: Service.Stream

    def streamAllProfiles(
        self,
        mandatory: Sequence[PropertyName],
        optional: Sequence[PropertyName],
        onlyRawData: bool,
    ) -> StreamallprofilesResult: ...
    class StreamallprofilesRequest(Protocol):
        mandatory: Sequence[PropertyName]
        optional: Sequence[PropertyName]
        onlyRawData: bool
        def send(self) -> Service.StreamallprofilesResult: ...

    def streamAllProfiles_request(self) -> StreamallprofilesRequest: ...
    class Server(Identifiable.Server, Persistent.Server):
        def checkAvailableParameters(
            self,
            mandatory: Sequence[PropertyName],
            optional: Sequence[PropertyName],
            onlyRawData: bool,
            **kwargs,
        ) -> Awaitable[Query.Result]: ...
        def getAllAvailableParameters(
            self, onlyRawData: bool, **kwargs
        ) -> Awaitable[Service.GetallavailableparametersResult]: ...
        def closestProfilesAt(
            self, coord: LatLonCoordReader, query: QueryReader, **kwargs
        ) -> Awaitable[Sequence[Profile]]: ...
        def streamAllProfiles(
            self,
            mandatory: Sequence[PropertyName],
            optional: Sequence[PropertyName],
            onlyRawData: bool,
            **kwargs,
        ) -> Awaitable[Service.Stream | Service.Stream.Server]: ...
