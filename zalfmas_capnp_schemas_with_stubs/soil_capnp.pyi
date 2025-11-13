"""This is an automatically generated stub for `soil.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
from contextlib import contextmanager
from enum import Enum
from io import BufferedWriter
from typing import Any, BinaryIO, Literal, NamedTuple, Protocol, TypeAlias, overload

from .common_capnp import Identifiable, IdentifiableClient
from .persistence_capnp import Persistent, PersistentClient

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

LayerBuilder: TypeAlias = Layer.Builder
LayerReader: TypeAlias = Layer.Reader

class Layer:
    PropertyBuilder: TypeAlias = Property.Builder
    PropertyReader: TypeAlias = Property.Reader
    class Property:
        class Reader:
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
            def as_builder(self) -> Layer.Property.Builder: ...

        class Builder:
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
            def which(self) -> Literal["f32Value", "bValue", "type", "unset"]: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Layer.Property.Builder: ...
            def copy(self) -> Layer.Property.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Layer.Property.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def which(self) -> Literal["f32Value", "bValue", "type", "unset"]: ...
        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Layer.Property.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Layer.Property.Reader: ...
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
        ) -> Layer.Property.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Layer.Property.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Layer.Property.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Reader:
        @property
        def properties(self) -> Sequence[Layer.Property.Reader]: ...
        @property
        def size(self) -> float: ...
        @property
        def description(self) -> str: ...
        def as_builder(self) -> Layer.Builder: ...

    class Builder:
        @property
        def properties(self) -> Sequence[Layer.Property.Builder]: ...
        @properties.setter
        def properties(
            self,
            value: Sequence[Layer.Property.Builder | Layer.Property.Reader]
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
        def from_dict(dictionary: dict[str, Any]) -> Layer.Builder: ...
        def init(
            self, name: Literal["properties"], size: int = ...
        ) -> Sequence[Layer.Property.Builder]: ...
        def copy(self) -> Layer.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Layer.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @contextmanager
    @staticmethod
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[Layer.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Layer.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        properties: Sequence[Layer.Property.Builder]
        | Sequence[dict[str, Any]]
        | None = None,
        size: float | None = None,
        description: str | None = None,
    ) -> Layer.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Layer.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Layer.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

QueryBuilder: TypeAlias = Query.Builder
QueryReader: TypeAlias = Query.Reader

class Query:
    ResultBuilder: TypeAlias = Result.Builder
    ResultReader: TypeAlias = Result.Reader
    class Result:
        class Reader:
            @property
            def failed(self) -> bool: ...
            @property
            def mandatory(self) -> Sequence[PropertyName]: ...
            @property
            def optional(self) -> Sequence[PropertyName]: ...
            def as_builder(self) -> Query.Result.Builder: ...

        class Builder:
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
            def from_dict(dictionary: dict[str, Any]) -> Query.Result.Builder: ...
            @overload
            def init(
                self: Any, name: Literal["mandatory"], size: int = ...
            ) -> Sequence[PropertyName]: ...
            @overload
            def init(
                self: Any, name: Literal["optional"], size: int = ...
            ) -> Sequence[PropertyName]: ...
            def init(self: Any, name: str, size: int = ...) -> Any: ...
            def copy(self) -> Query.Result.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Query.Result.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Query.Result.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Query.Result.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            failed: bool | None = None,
            mandatory: Sequence[PropertyName] | None = None,
            optional: Sequence[PropertyName] | None = None,
        ) -> Query.Result.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Query.Result.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Query.Result.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Reader:
        @property
        def mandatory(self) -> Sequence[PropertyName]: ...
        @property
        def optional(self) -> Sequence[PropertyName]: ...
        @property
        def onlyRawData(self) -> bool: ...
        def as_builder(self) -> Query.Builder: ...

    class Builder:
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
        def from_dict(dictionary: dict[str, Any]) -> Query.Builder: ...
        @overload
        def init(
            self: Any, name: Literal["mandatory"], size: int = ...
        ) -> Sequence[PropertyName]: ...
        @overload
        def init(
            self: Any, name: Literal["optional"], size: int = ...
        ) -> Sequence[PropertyName]: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        def copy(self) -> Query.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Query.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @contextmanager
    @staticmethod
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[Query.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Query.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        mandatory: Sequence[PropertyName] | None = None,
        optional: Sequence[PropertyName] | None = None,
        onlyRawData: bool | None = None,
    ) -> Query.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Query.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Query.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

ProfileDataBuilder: TypeAlias = ProfileData.Builder
ProfileDataReader: TypeAlias = ProfileData.Reader

class ProfileData:
    class Reader:
        @property
        def layers(self) -> Sequence[Layer.Reader]: ...
        @property
        def percentageOfArea(self) -> float: ...
        def as_builder(self) -> ProfileData.Builder: ...

    class Builder:
        @property
        def layers(self) -> Sequence[Layer.Builder]: ...
        @layers.setter
        def layers(
            self,
            value: Sequence[Layer.Builder | Layer.Reader] | Sequence[dict[str, Any]],
        ) -> None: ...
        @property
        def percentageOfArea(self) -> float: ...
        @percentageOfArea.setter
        def percentageOfArea(self, value: float) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> ProfileData.Builder: ...
        def init(
            self, name: Literal["layers"], size: int = ...
        ) -> Sequence[Layer.Builder]: ...
        def copy(self) -> ProfileData.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> ProfileData.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @contextmanager
    @staticmethod
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[ProfileData.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ProfileData.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        layers: Sequence[Layer.Builder] | Sequence[dict[str, Any]] | None = None,
        percentageOfArea: float | None = None,
    ) -> ProfileData.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ProfileData.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ProfileData.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

class Profile:
    class DataRequest(Protocol):
        def send(self) -> Profile.DataResult: ...

    class DataResult(Awaitable[DataResult], Protocol):
        layers: Sequence[Layer.Builder | Layer.Reader]
        percentageOfArea: float

    class GeolocationRequest(Protocol):
        def send(self) -> Profile.GeolocationResult: ...

    class GeolocationResult(Awaitable[GeolocationResult], Protocol):
        lat: float
        lon: float

    @classmethod
    def _new_client(
        cls, server: Profile.Server | Identifiable.Server | Persistent.Server
    ) -> ProfileClient: ...
    class Server(Identifiable.Server, Persistent.Server):
        class DataResultTuple(NamedTuple):
            layers: Sequence[Layer]
            percentageOfArea: float

        class GeolocationResultTuple(NamedTuple):
            lat: float
            lon: float

        class DataCallContext(Protocol):
            params: Profile.DataRequest
            results: Profile.DataResult

        class GeolocationCallContext(Protocol):
            params: Profile.GeolocationRequest
            results: Profile.GeolocationResult

        def data(
            self, _context: Profile.Server.DataCallContext, **kwargs: Any
        ) -> Awaitable[Profile.Server.DataResultTuple | None]: ...
        def data_context(
            self, context: Profile.Server.DataCallContext
        ) -> Awaitable[None]: ...
        def geoLocation(
            self, _context: Profile.Server.GeolocationCallContext, **kwargs: Any
        ) -> Awaitable[Profile.Server.GeolocationResultTuple | None]: ...
        def geoLocation_context(
            self, context: Profile.Server.GeolocationCallContext
        ) -> Awaitable[None]: ...

class ProfileClient(IdentifiableClient, PersistentClient):
    def data(self) -> Profile.DataResult: ...
    def geoLocation(self) -> Profile.GeolocationResult: ...
    def data_request(self) -> Profile.DataRequest: ...
    def geoLocation_request(self) -> Profile.GeolocationRequest: ...

class Service:
    class Stream:
        class NextprofilesRequest(Protocol):
            maxCount: int
            def send(self) -> Service.Stream.NextprofilesResult: ...

        class NextprofilesResult(Awaitable[NextprofilesResult], Protocol):
            profiles: Sequence[Profile]

        @classmethod
        def _new_client(cls, server: Service.Stream.Server) -> Service.StreamClient: ...
        class Server(Protocol):
            class NextprofilesResultTuple(NamedTuple):
                profiles: Sequence[Profile]

            class NextprofilesCallContext(Protocol):
                params: Service.Stream.NextprofilesRequest
                results: Service.Stream.NextprofilesResult

            def nextProfiles(
                self,
                maxCount: int,
                _context: Service.Stream.Server.NextprofilesCallContext,
                **kwargs: Any,
            ) -> Awaitable[Service.Stream.Server.NextprofilesResultTuple | None]: ...
            def nextProfiles_context(
                self, context: Service.Stream.Server.NextprofilesCallContext
            ) -> Awaitable[None]: ...

    class StreamClient(Protocol):
        def nextProfiles(
            self, maxCount: int | None = None
        ) -> Service.Stream.NextprofilesResult: ...
        def nextProfiles_request(
            self, maxCount: int | None = None
        ) -> Service.Stream.NextprofilesRequest: ...

    class CheckavailableparametersRequest(Protocol):
        mandatory: Sequence[PropertyName]
        optional: Sequence[PropertyName]
        onlyRawData: bool
        @overload
        def init(
            self, name: Literal["mandatory"], size: int = ...
        ) -> Sequence[PropertyName]: ...
        @overload
        def init(
            self, name: Literal["optional"], size: int = ...
        ) -> Sequence[PropertyName]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Service.CheckavailableparametersResult: ...

    class CheckavailableparametersResult(
        Awaitable[CheckavailableparametersResult], Protocol
    ):
        failed: bool
        mandatory: Sequence[PropertyName]
        optional: Sequence[PropertyName]

    class GetallavailableparametersRequest(Protocol):
        onlyRawData: bool
        def send(self) -> Service.GetallavailableparametersResult: ...

    class GetallavailableparametersResult(
        Awaitable[GetallavailableparametersResult], Protocol
    ):
        mandatory: Sequence[PropertyName]
        optional: Sequence[PropertyName]

    class ClosestprofilesatRequest(Protocol):
        query: Query.Builder
        @overload
        def init(self, name: Literal["query"]) -> Query.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Service.ClosestprofilesatResult: ...

    class ClosestprofilesatResult(Awaitable[ClosestprofilesatResult], Protocol):
        profiles: Sequence[Profile]

    class StreamallprofilesRequest(Protocol):
        mandatory: Sequence[PropertyName]
        optional: Sequence[PropertyName]
        onlyRawData: bool
        @overload
        def init(
            self, name: Literal["mandatory"], size: int = ...
        ) -> Sequence[PropertyName]: ...
        @overload
        def init(
            self, name: Literal["optional"], size: int = ...
        ) -> Sequence[PropertyName]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Service.StreamallprofilesResult: ...

    class StreamallprofilesResult(Awaitable[StreamallprofilesResult], Protocol):
        allProfiles: Service.StreamClient

    @classmethod
    def _new_client(
        cls, server: Service.Server | Identifiable.Server | Persistent.Server
    ) -> ServiceClient: ...
    class Server(Identifiable.Server, Persistent.Server):
        class CheckavailableparametersResultTuple(NamedTuple):
            failed: bool
            mandatory: Sequence[PropertyName]
            optional: Sequence[PropertyName]

        class GetallavailableparametersResultTuple(NamedTuple):
            mandatory: Sequence[PropertyName]
            optional: Sequence[PropertyName]

        class ClosestprofilesatResultTuple(NamedTuple):
            profiles: Sequence[Profile]

        class StreamallprofilesResultTuple(NamedTuple):
            allProfiles: Service.Stream.Server

        class CheckavailableparametersCallContext(Protocol):
            params: Service.CheckavailableparametersRequest
            results: Service.CheckavailableparametersResult

        class GetallavailableparametersCallContext(Protocol):
            params: Service.GetallavailableparametersRequest
            results: Service.GetallavailableparametersResult

        class ClosestprofilesatCallContext(Protocol):
            params: Service.ClosestprofilesatRequest
            results: Service.ClosestprofilesatResult

        class StreamallprofilesCallContext(Protocol):
            params: Service.StreamallprofilesRequest
            results: Service.StreamallprofilesResult

        def checkAvailableParameters(
            self,
            mandatory: Sequence[PropertyName],
            optional: Sequence[PropertyName],
            onlyRawData: bool,
            _context: Service.Server.CheckavailableparametersCallContext,
            **kwargs: Any,
        ) -> Awaitable[Service.Server.CheckavailableparametersResultTuple | None]: ...
        def checkAvailableParameters_context(
            self, context: Service.Server.CheckavailableparametersCallContext
        ) -> Awaitable[None]: ...
        def getAllAvailableParameters(
            self,
            onlyRawData: bool,
            _context: Service.Server.GetallavailableparametersCallContext,
            **kwargs: Any,
        ) -> Awaitable[Service.Server.GetallavailableparametersResultTuple | None]: ...
        def getAllAvailableParameters_context(
            self, context: Service.Server.GetallavailableparametersCallContext
        ) -> Awaitable[None]: ...
        def closestProfilesAt(
            self,
            query: Query.Reader,
            _context: Service.Server.ClosestprofilesatCallContext,
            **kwargs: Any,
        ) -> Awaitable[Service.Server.ClosestprofilesatResultTuple | None]: ...
        def closestProfilesAt_context(
            self, context: Service.Server.ClosestprofilesatCallContext
        ) -> Awaitable[None]: ...
        def streamAllProfiles(
            self,
            mandatory: Sequence[PropertyName],
            optional: Sequence[PropertyName],
            onlyRawData: bool,
            _context: Service.Server.StreamallprofilesCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            Service.Stream.Server | Service.Server.StreamallprofilesResultTuple | None
        ]: ...
        def streamAllProfiles_context(
            self, context: Service.Server.StreamallprofilesCallContext
        ) -> Awaitable[None]: ...

class ServiceClient(IdentifiableClient, PersistentClient):
    def checkAvailableParameters(
        self,
        mandatory: Sequence[PropertyName] | None = None,
        optional: Sequence[PropertyName] | None = None,
        onlyRawData: bool | None = None,
    ) -> Service.CheckavailableparametersResult: ...
    def getAllAvailableParameters(
        self, onlyRawData: bool | None = None
    ) -> Service.GetallavailableparametersResult: ...
    def closestProfilesAt(
        self, query: Query | dict[str, Any] | None = None
    ) -> Service.ClosestprofilesatResult: ...
    def streamAllProfiles(
        self,
        mandatory: Sequence[PropertyName] | None = None,
        optional: Sequence[PropertyName] | None = None,
        onlyRawData: bool | None = None,
    ) -> Service.StreamallprofilesResult: ...
    def checkAvailableParameters_request(
        self,
        mandatory: Sequence[PropertyName] | None = None,
        optional: Sequence[PropertyName] | None = None,
        onlyRawData: bool | None = None,
    ) -> Service.CheckavailableparametersRequest: ...
    def getAllAvailableParameters_request(
        self, onlyRawData: bool | None = None
    ) -> Service.GetallavailableparametersRequest: ...
    def closestProfilesAt_request(
        self, query: Query.Builder | None = None
    ) -> Service.ClosestprofilesatRequest: ...
    def streamAllProfiles_request(
        self,
        mandatory: Sequence[PropertyName] | None = None,
        optional: Sequence[PropertyName] | None = None,
        onlyRawData: bool | None = None,
    ) -> Service.StreamallprofilesRequest: ...
