"""This is an automatically generated stub for `management.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
from contextlib import contextmanager
from enum import Enum
from io import BufferedWriter
from typing import Any, BinaryIO, Literal, NamedTuple, Protocol, TypeAlias, overload

from .common_capnp import Identifiable, IdentifiableClient, IdInformation
from .crop_capnp import Crop, CropClient
from .date_capnp import Date
from .persistence_capnp import Persistent, PersistentClient
from .registry_capnp import Registry, RegistryClient

class EventType(Enum):
    sowing = "sowing"
    automaticSowing = "automaticSowing"
    harvest = "harvest"
    automaticHarvest = "automaticHarvest"
    irrigation = "irrigation"
    tillage = "tillage"
    organicFertilization = "organicFertilization"
    mineralFertilization = "mineralFertilization"
    nDemandFertilization = "nDemandFertilization"
    cutting = "cutting"
    setValue = "setValue"
    saveState = "saveState"

class PlantOrgan(Enum):
    root = "root"
    leaf = "leaf"
    shoot = "shoot"
    fruit = "fruit"
    strukt = "strukt"
    sugar = "sugar"

EventBuilder: TypeAlias = Event.Builder
EventReader: TypeAlias = Event.Reader

class Event:
    class ExternalType(Enum):
        sowing = "sowing"
        automaticSowing = "automaticSowing"
        harvest = "harvest"
        automaticHarvest = "automaticHarvest"
        irrigation = "irrigation"
        tillage = "tillage"
        organicFertilization = "organicFertilization"
        mineralFertilization = "mineralFertilization"
        nDemandFertilization = "nDemandFertilization"
        cutting = "cutting"

    class PhenoStage(Enum):
        emergence = "emergence"
        flowering = "flowering"
        anthesis = "anthesis"
        maturity = "maturity"

    TypeBuilder: TypeAlias = Type.Builder
    TypeReader: TypeAlias = Type.Reader
    class Type:
        class Reader:
            @property
            def external(self) -> Event.ExternalType: ...
            @property
            def internal(self) -> Event.PhenoStage: ...
            def which(self) -> Literal["external", "internal"]: ...
            def as_builder(self) -> Event.Type.Builder: ...

        class Builder:
            @property
            def external(self) -> Event.ExternalType: ...
            @external.setter
            def external(
                self,
                value: Event.ExternalType
                | Literal[
                    "sowing",
                    "automaticSowing",
                    "harvest",
                    "automaticHarvest",
                    "irrigation",
                    "tillage",
                    "organicFertilization",
                    "mineralFertilization",
                    "nDemandFertilization",
                    "cutting",
                ],
            ) -> None: ...
            @property
            def internal(self) -> Event.PhenoStage: ...
            @internal.setter
            def internal(
                self,
                value: Event.PhenoStage
                | Literal["emergence", "flowering", "anthesis", "maturity"],
            ) -> None: ...
            def which(self) -> Literal["external", "internal"]: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Event.Type.Builder: ...
            def copy(self) -> Event.Type.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Event.Type.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def which(self) -> Literal["external", "internal"]: ...
        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Event.Type.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Event.Type.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            external: Event.ExternalType
            | Literal[
                "sowing",
                "automaticSowing",
                "harvest",
                "automaticHarvest",
                "irrigation",
                "tillage",
                "organicFertilization",
                "mineralFertilization",
                "nDemandFertilization",
                "cutting",
            ]
            | None = None,
            internal: Event.PhenoStage
            | Literal["emergence", "flowering", "anthesis", "maturity"]
            | None = None,
        ) -> Event.Type.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Event.Type.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Event.Type.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    AtBuilder: TypeAlias = At.Builder
    AtReader: TypeAlias = At.Reader
    class At:
        class Reader:
            @property
            def date(self) -> Date.Reader: ...
            def as_builder(self) -> Event.At.Builder: ...

        class Builder:
            @property
            def date(self) -> Date.Builder: ...
            @date.setter
            def date(
                self, value: Date.Builder | Date.Reader | dict[str, Any]
            ) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Event.At.Builder: ...
            def init(self, name: Literal["date"]) -> Date.Builder: ...
            def copy(self) -> Event.At.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Event.At.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def init(self, name: Literal["date"]) -> Date: ...
        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Event.At.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Event.At.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            date: Date.Builder | dict[str, Any] | None = None,
        ) -> Event.At.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Event.At.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Event.At.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    BetweenBuilder: TypeAlias = Between.Builder
    BetweenReader: TypeAlias = Between.Reader
    class Between:
        class Reader:
            @property
            def earliest(self) -> Date.Reader: ...
            @property
            def latest(self) -> Date.Reader: ...
            def as_builder(self) -> Event.Between.Builder: ...

        class Builder:
            @property
            def earliest(self) -> Date.Builder: ...
            @earliest.setter
            def earliest(
                self, value: Date.Builder | Date.Reader | dict[str, Any]
            ) -> None: ...
            @property
            def latest(self) -> Date.Builder: ...
            @latest.setter
            def latest(
                self, value: Date.Builder | Date.Reader | dict[str, Any]
            ) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Event.Between.Builder: ...
            @overload
            def init(self: Any, name: Literal["earliest"]) -> Date.Builder: ...
            @overload
            def init(self: Any, name: Literal["latest"]) -> Date.Builder: ...
            def init(self: Any, name: str, size: int = ...) -> Any: ...
            def copy(self) -> Event.Between.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Event.Between.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @overload
        def init(self, name: Literal["earliest"]) -> Date: ...
        @overload
        def init(self, name: Literal["latest"]) -> Date: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Event.Between.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Event.Between.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            earliest: Date.Builder | dict[str, Any] | None = None,
            latest: Date.Builder | dict[str, Any] | None = None,
        ) -> Event.Between.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Event.Between.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Event.Between.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    AfterBuilder: TypeAlias = After.Builder
    AfterReader: TypeAlias = After.Reader
    class After:
        class Reader:
            @property
            def event(self) -> Event.Type.Reader: ...
            @property
            def days(self) -> int: ...
            def as_builder(self) -> Event.After.Builder: ...

        class Builder:
            @property
            def event(self) -> Event.Type.Builder: ...
            @event.setter
            def event(
                self, value: Event.Type.Builder | Event.Type.Reader | dict[str, Any]
            ) -> None: ...
            @property
            def days(self) -> int: ...
            @days.setter
            def days(self, value: int) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Event.After.Builder: ...
            def init(self, name: Literal["event"]) -> Event.Type.Builder: ...
            def copy(self) -> Event.After.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Event.After.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def init(self, name: Literal["event"]) -> Event.Type: ...
        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Event.After.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Event.After.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            event: Event.Type.Builder | dict[str, Any] | None = None,
            days: int | None = None,
        ) -> Event.After.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Event.After.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Event.After.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Reader:
        @property
        def type(self) -> Event.ExternalType: ...
        @property
        def info(self) -> IdInformation.Reader: ...
        @property
        def at(self) -> Event.At.Reader: ...
        @property
        def between(self) -> Event.Between.Reader: ...
        @property
        def after(self) -> Event.After.Reader: ...
        @property
        def params(self) -> Any: ...
        @property
        def runAtStartOfDay(self) -> bool: ...
        def which(self) -> Literal["at", "between", "after"]: ...
        def as_builder(self) -> Event.Builder: ...

    class Builder:
        @property
        def type(self) -> Event.ExternalType: ...
        @type.setter
        def type(
            self,
            value: Event.ExternalType
            | Literal[
                "sowing",
                "automaticSowing",
                "harvest",
                "automaticHarvest",
                "irrigation",
                "tillage",
                "organicFertilization",
                "mineralFertilization",
                "nDemandFertilization",
                "cutting",
            ],
        ) -> None: ...
        @property
        def info(self) -> IdInformation.Builder: ...
        @info.setter
        def info(
            self, value: IdInformation.Builder | IdInformation.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def at(self) -> Event.At.Builder: ...
        @at.setter
        def at(
            self, value: Event.At.Builder | Event.At.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def between(self) -> Event.Between.Builder: ...
        @between.setter
        def between(
            self, value: Event.Between.Builder | Event.Between.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def after(self) -> Event.After.Builder: ...
        @after.setter
        def after(
            self, value: Event.After.Builder | Event.After.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def params(self) -> Any: ...
        @params.setter
        def params(self, value: Any) -> None: ...
        @property
        def runAtStartOfDay(self) -> bool: ...
        @runAtStartOfDay.setter
        def runAtStartOfDay(self, value: bool) -> None: ...
        def which(self) -> Literal["at", "between", "after"]: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Event.Builder: ...
        @overload
        def init(self: Any, name: Literal["info"]) -> IdInformation.Builder: ...
        @overload
        def init(self: Any, name: Literal["at"]) -> Event.At.Builder: ...
        @overload
        def init(self: Any, name: Literal["between"]) -> Event.Between.Builder: ...
        @overload
        def init(self: Any, name: Literal["after"]) -> Event.After.Builder: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        def copy(self) -> Event.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Event.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    def which(self) -> Literal["at", "between", "after"]: ...
    @overload
    def init(self, name: Literal["info"]) -> IdInformation: ...
    @overload
    def init(self, name: Literal["at"]) -> Event.At: ...
    @overload
    def init(self, name: Literal["between"]) -> Event.Between: ...
    @overload
    def init(self, name: Literal["after"]) -> Event.After: ...
    def init(self: Any, name: str, size: int = ...) -> Any: ...
    @contextmanager
    @staticmethod
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[Event.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Event.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        type: Event.ExternalType
        | Literal[
            "sowing",
            "automaticSowing",
            "harvest",
            "automaticHarvest",
            "irrigation",
            "tillage",
            "organicFertilization",
            "mineralFertilization",
            "nDemandFertilization",
            "cutting",
        ]
        | None = None,
        info: IdInformation.Builder | dict[str, Any] | None = None,
        at: Event.At.Builder | dict[str, Any] | None = None,
        between: Event.Between.Builder | dict[str, Any] | None = None,
        after: Event.After.Builder | dict[str, Any] | None = None,
        params: Any | None = None,
        runAtStartOfDay: bool | None = None,
    ) -> Event.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Event.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Event.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

class Fertilizer:
    class NutrientsRequest(Protocol):
        def send(self) -> Fertilizer.NutrientsResult: ...

    class NutrientsResult(Awaitable[NutrientsResult], Protocol):
        nutrients: Sequence[Nutrient.Builder | Nutrient.Reader]

    class ParametersRequest(Protocol):
        def send(self) -> Fertilizer.ParametersResult: ...

    class ParametersResult(Awaitable[ParametersResult], Protocol):
        params: Any

    @classmethod
    def _new_client(
        cls, server: Fertilizer.Server | Identifiable.Server | Persistent.Server
    ) -> FertilizerClient: ...
    class Server(Identifiable.Server, Persistent.Server):
        class NutrientsResultTuple(NamedTuple):
            nutrients: Sequence[Nutrient]

        class ParametersResultTuple(NamedTuple):
            params: Any

        class NutrientsCallContext(Protocol):
            params: Fertilizer.NutrientsRequest
            results: Fertilizer.NutrientsResult

        class ParametersCallContext(Protocol):
            params: Fertilizer.ParametersRequest
            results: Fertilizer.ParametersResult

        def nutrients(
            self, _context: Fertilizer.Server.NutrientsCallContext, **kwargs: Any
        ) -> Awaitable[Fertilizer.Server.NutrientsResultTuple | None]: ...
        def nutrients_context(
            self, context: Fertilizer.Server.NutrientsCallContext
        ) -> Awaitable[None]: ...
        def parameters(
            self, _context: Fertilizer.Server.ParametersCallContext, **kwargs: Any
        ) -> Awaitable[Fertilizer.Server.ParametersResultTuple | None]: ...
        def parameters_context(
            self, context: Fertilizer.Server.ParametersCallContext
        ) -> Awaitable[None]: ...

NutrientBuilder: TypeAlias = Nutrient.Builder
NutrientReader: TypeAlias = Nutrient.Reader

class Nutrient:
    class Name(Enum):
        urea = "urea"
        ammonia = "ammonia"
        nitrate = "nitrate"
        phosphorus = "phosphorus"
        potassium = "potassium"
        sulfate = "sulfate"
        organicC = "organicC"
        organicN = "organicN"
        organicP = "organicP"
        organicNFast = "organicNFast"
        organicNSlow = "organicNSlow"

    class Unit(Enum):
        none = "none"
        fraction = "fraction"
        percent = "percent"

    class Reader:
        @property
        def nutrient(self) -> Nutrient.Name: ...
        @property
        def value(self) -> float: ...
        @property
        def unit(self) -> Nutrient.Unit: ...
        def as_builder(self) -> Nutrient.Builder: ...

    class Builder:
        @property
        def nutrient(self) -> Nutrient.Name: ...
        @nutrient.setter
        def nutrient(
            self,
            value: Nutrient.Name
            | Literal[
                "urea",
                "ammonia",
                "nitrate",
                "phosphorus",
                "potassium",
                "sulfate",
                "organicC",
                "organicN",
                "organicP",
                "organicNFast",
                "organicNSlow",
            ],
        ) -> None: ...
        @property
        def value(self) -> float: ...
        @value.setter
        def value(self, value: float) -> None: ...
        @property
        def unit(self) -> Nutrient.Unit: ...
        @unit.setter
        def unit(
            self, value: Nutrient.Unit | Literal["none", "fraction", "percent"]
        ) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Nutrient.Builder: ...
        def copy(self) -> Nutrient.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Nutrient.Reader: ...
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
    ) -> Iterator[Nutrient.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Nutrient.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        nutrient: Nutrient.Name
        | Literal[
            "urea",
            "ammonia",
            "nitrate",
            "phosphorus",
            "potassium",
            "sulfate",
            "organicC",
            "organicN",
            "organicP",
            "organicNFast",
            "organicNSlow",
        ]
        | None = None,
        value: float | None = None,
        unit: Nutrient.Unit | Literal["none", "fraction", "percent"] | None = None,
    ) -> Nutrient.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Nutrient.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Nutrient.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

class FertilizerClient(IdentifiableClient, PersistentClient):
    def nutrients(self) -> Fertilizer.NutrientsResult: ...
    def parameters(self) -> Fertilizer.ParametersResult: ...
    def nutrients_request(self) -> Fertilizer.NutrientsRequest: ...
    def parameters_request(self) -> Fertilizer.ParametersRequest: ...

ParamsBuilder: TypeAlias = Params.Builder
ParamsReader: TypeAlias = Params.Reader

class Params:
    SowingBuilder: TypeAlias = Sowing.Builder
    SowingReader: TypeAlias = Sowing.Reader
    class Sowing:
        class Reader:
            @property
            def cultivar(self) -> str: ...
            @property
            def plantDensity(self) -> int: ...
            @property
            def crop(self) -> CropClient: ...
            def as_builder(self) -> Params.Sowing.Builder: ...

        class Builder:
            @property
            def cultivar(self) -> str: ...
            @cultivar.setter
            def cultivar(self, value: str) -> None: ...
            @property
            def plantDensity(self) -> int: ...
            @plantDensity.setter
            def plantDensity(self, value: int) -> None: ...
            @property
            def crop(self) -> CropClient: ...
            @crop.setter
            def crop(self, value: CropClient | Crop.Server) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Params.Sowing.Builder: ...
            def copy(self) -> Params.Sowing.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Params.Sowing.Reader: ...
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
        ) -> Iterator[Params.Sowing.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Sowing.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            cultivar: str | None = None,
            plantDensity: int | None = None,
            crop: CropClient | Crop.Server | None = None,
        ) -> Params.Sowing.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Sowing.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Sowing.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    AutomaticSowingBuilder: TypeAlias = AutomaticSowing.Builder
    AutomaticSowingReader: TypeAlias = AutomaticSowing.Reader
    class AutomaticSowing:
        AvgSoilTempBuilder: TypeAlias = AvgSoilTemp.Builder
        AvgSoilTempReader: TypeAlias = AvgSoilTemp.Reader
        class AvgSoilTemp:
            class Reader:
                @property
                def soilDepthForAveraging(self) -> float: ...
                @property
                def daysInSoilTempWindow(self) -> int: ...
                @property
                def sowingIfAboveAvgSoilTemp(self) -> float: ...
                def as_builder(self) -> Params.AutomaticSowing.AvgSoilTemp.Builder: ...

            class Builder:
                @property
                def soilDepthForAveraging(self) -> float: ...
                @soilDepthForAveraging.setter
                def soilDepthForAveraging(self, value: float) -> None: ...
                @property
                def daysInSoilTempWindow(self) -> int: ...
                @daysInSoilTempWindow.setter
                def daysInSoilTempWindow(self, value: int) -> None: ...
                @property
                def sowingIfAboveAvgSoilTemp(self) -> float: ...
                @sowingIfAboveAvgSoilTemp.setter
                def sowingIfAboveAvgSoilTemp(self, value: float) -> None: ...
                @staticmethod
                def from_dict(
                    dictionary: dict[str, Any],
                ) -> Params.AutomaticSowing.AvgSoilTemp.Builder: ...
                def copy(self) -> Params.AutomaticSowing.AvgSoilTemp.Builder: ...
                def to_bytes(self) -> bytes: ...
                def to_bytes_packed(self) -> bytes: ...
                def to_segments(self) -> list[bytes]: ...
                def as_reader(self) -> Params.AutomaticSowing.AvgSoilTemp.Reader: ...
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
            ) -> Iterator[Params.AutomaticSowing.AvgSoilTemp.Reader]: ...
            @staticmethod
            def from_bytes_packed(
                data: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> Params.AutomaticSowing.AvgSoilTemp.Reader: ...
            @staticmethod
            def new_message(
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                soilDepthForAveraging: float | None = None,
                daysInSoilTempWindow: int | None = None,
                sowingIfAboveAvgSoilTemp: float | None = None,
            ) -> Params.AutomaticSowing.AvgSoilTemp.Builder: ...
            @staticmethod
            def read(
                file: BinaryIO,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> Params.AutomaticSowing.AvgSoilTemp.Reader: ...
            @staticmethod
            def read_packed(
                file: BinaryIO,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> Params.AutomaticSowing.AvgSoilTemp.Reader: ...
            def to_dict(self) -> dict[str, Any]: ...

        class Reader:
            @property
            def minTempThreshold(self) -> float: ...
            @property
            def daysInTempWindow(self) -> int: ...
            @property
            def minPercentASW(self) -> float: ...
            @property
            def maxPercentASW(self) -> float: ...
            @property
            def max3dayPrecipSum(self) -> float: ...
            @property
            def maxCurrentDayPrecipSum(self) -> float: ...
            @property
            def tempSumAboveBaseTemp(self) -> float: ...
            @property
            def baseTemp(self) -> float: ...
            @property
            def avgSoilTemp(self) -> Params.AutomaticSowing.AvgSoilTemp.Reader: ...
            @property
            def sowing(self) -> Params.Sowing.Reader: ...
            def as_builder(self) -> Params.AutomaticSowing.Builder: ...

        class Builder:
            @property
            def minTempThreshold(self) -> float: ...
            @minTempThreshold.setter
            def minTempThreshold(self, value: float) -> None: ...
            @property
            def daysInTempWindow(self) -> int: ...
            @daysInTempWindow.setter
            def daysInTempWindow(self, value: int) -> None: ...
            @property
            def minPercentASW(self) -> float: ...
            @minPercentASW.setter
            def minPercentASW(self, value: float) -> None: ...
            @property
            def maxPercentASW(self) -> float: ...
            @maxPercentASW.setter
            def maxPercentASW(self, value: float) -> None: ...
            @property
            def max3dayPrecipSum(self) -> float: ...
            @max3dayPrecipSum.setter
            def max3dayPrecipSum(self, value: float) -> None: ...
            @property
            def maxCurrentDayPrecipSum(self) -> float: ...
            @maxCurrentDayPrecipSum.setter
            def maxCurrentDayPrecipSum(self, value: float) -> None: ...
            @property
            def tempSumAboveBaseTemp(self) -> float: ...
            @tempSumAboveBaseTemp.setter
            def tempSumAboveBaseTemp(self, value: float) -> None: ...
            @property
            def baseTemp(self) -> float: ...
            @baseTemp.setter
            def baseTemp(self, value: float) -> None: ...
            @property
            def avgSoilTemp(self) -> Params.AutomaticSowing.AvgSoilTemp.Builder: ...
            @avgSoilTemp.setter
            def avgSoilTemp(
                self,
                value: Params.AutomaticSowing.AvgSoilTemp.Builder
                | Params.AutomaticSowing.AvgSoilTemp.Reader
                | dict[str, Any],
            ) -> None: ...
            @property
            def sowing(self) -> Params.Sowing.Builder: ...
            @sowing.setter
            def sowing(
                self,
                value: Params.Sowing.Builder | Params.Sowing.Reader | dict[str, Any],
            ) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Params.AutomaticSowing.Builder: ...
            @overload
            def init(
                self: Any, name: Literal["avgSoilTemp"]
            ) -> Params.AutomaticSowing.AvgSoilTemp.Builder: ...
            @overload
            def init(self: Any, name: Literal["sowing"]) -> Params.Sowing.Builder: ...
            def init(self: Any, name: str, size: int = ...) -> Any: ...
            def copy(self) -> Params.AutomaticSowing.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Params.AutomaticSowing.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @overload
        def init(
            self, name: Literal["avgSoilTemp"]
        ) -> Params.AutomaticSowing.AvgSoilTemp: ...
        @overload
        def init(self, name: Literal["sowing"]) -> Params.Sowing: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Params.AutomaticSowing.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.AutomaticSowing.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            minTempThreshold: float | None = None,
            daysInTempWindow: int | None = None,
            minPercentASW: float | None = None,
            maxPercentASW: float | None = None,
            max3dayPrecipSum: float | None = None,
            maxCurrentDayPrecipSum: float | None = None,
            tempSumAboveBaseTemp: float | None = None,
            baseTemp: float | None = None,
            avgSoilTemp: Params.AutomaticSowing.AvgSoilTemp.Builder
            | dict[str, Any]
            | None = None,
            sowing: Params.Sowing.Builder | dict[str, Any] | None = None,
        ) -> Params.AutomaticSowing.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.AutomaticSowing.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.AutomaticSowing.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    HarvestBuilder: TypeAlias = Harvest.Builder
    HarvestReader: TypeAlias = Harvest.Reader
    class Harvest:
        class CropUsage(Enum):
            greenManure = "greenManure"
            biomassProduction = "biomassProduction"

        OptCarbonMgmtDataBuilder: TypeAlias = OptCarbonMgmtData.Builder
        OptCarbonMgmtDataReader: TypeAlias = OptCarbonMgmtData.Reader
        class OptCarbonMgmtData:
            class Reader:
                @property
                def optCarbonConservation(self) -> bool: ...
                @property
                def cropImpactOnHumusBalance(self) -> float: ...
                @property
                def cropUsage(self) -> Params.Harvest.CropUsage: ...
                @property
                def residueHeq(self) -> float: ...
                @property
                def organicFertilizerHeq(self) -> float: ...
                @property
                def maxResidueRecoverFraction(self) -> float: ...
                def as_builder(self) -> Params.Harvest.OptCarbonMgmtData.Builder: ...

            class Builder:
                @property
                def optCarbonConservation(self) -> bool: ...
                @optCarbonConservation.setter
                def optCarbonConservation(self, value: bool) -> None: ...
                @property
                def cropImpactOnHumusBalance(self) -> float: ...
                @cropImpactOnHumusBalance.setter
                def cropImpactOnHumusBalance(self, value: float) -> None: ...
                @property
                def cropUsage(self) -> Params.Harvest.CropUsage: ...
                @cropUsage.setter
                def cropUsage(
                    self,
                    value: Params.Harvest.CropUsage
                    | Literal["greenManure", "biomassProduction"],
                ) -> None: ...
                @property
                def residueHeq(self) -> float: ...
                @residueHeq.setter
                def residueHeq(self, value: float) -> None: ...
                @property
                def organicFertilizerHeq(self) -> float: ...
                @organicFertilizerHeq.setter
                def organicFertilizerHeq(self, value: float) -> None: ...
                @property
                def maxResidueRecoverFraction(self) -> float: ...
                @maxResidueRecoverFraction.setter
                def maxResidueRecoverFraction(self, value: float) -> None: ...
                @staticmethod
                def from_dict(
                    dictionary: dict[str, Any],
                ) -> Params.Harvest.OptCarbonMgmtData.Builder: ...
                def copy(self) -> Params.Harvest.OptCarbonMgmtData.Builder: ...
                def to_bytes(self) -> bytes: ...
                def to_bytes_packed(self) -> bytes: ...
                def to_segments(self) -> list[bytes]: ...
                def as_reader(self) -> Params.Harvest.OptCarbonMgmtData.Reader: ...
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
            ) -> Iterator[Params.Harvest.OptCarbonMgmtData.Reader]: ...
            @staticmethod
            def from_bytes_packed(
                data: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> Params.Harvest.OptCarbonMgmtData.Reader: ...
            @staticmethod
            def new_message(
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                optCarbonConservation: bool | None = None,
                cropImpactOnHumusBalance: float | None = None,
                cropUsage: Params.Harvest.CropUsage
                | Literal["greenManure", "biomassProduction"]
                | None = None,
                residueHeq: float | None = None,
                organicFertilizerHeq: float | None = None,
                maxResidueRecoverFraction: float | None = None,
            ) -> Params.Harvest.OptCarbonMgmtData.Builder: ...
            @staticmethod
            def read(
                file: BinaryIO,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> Params.Harvest.OptCarbonMgmtData.Reader: ...
            @staticmethod
            def read_packed(
                file: BinaryIO,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> Params.Harvest.OptCarbonMgmtData.Reader: ...
            def to_dict(self) -> dict[str, Any]: ...

        class Reader:
            @property
            def exported(self) -> bool: ...
            @property
            def optCarbMgmtData(self) -> Params.Harvest.OptCarbonMgmtData.Reader: ...
            def as_builder(self) -> Params.Harvest.Builder: ...

        class Builder:
            @property
            def exported(self) -> bool: ...
            @exported.setter
            def exported(self, value: bool) -> None: ...
            @property
            def optCarbMgmtData(self) -> Params.Harvest.OptCarbonMgmtData.Builder: ...
            @optCarbMgmtData.setter
            def optCarbMgmtData(
                self,
                value: Params.Harvest.OptCarbonMgmtData.Builder
                | Params.Harvest.OptCarbonMgmtData.Reader
                | dict[str, Any],
            ) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Params.Harvest.Builder: ...
            def init(
                self, name: Literal["optCarbMgmtData"]
            ) -> Params.Harvest.OptCarbonMgmtData.Builder: ...
            def copy(self) -> Params.Harvest.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Params.Harvest.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def init(
            self, name: Literal["optCarbMgmtData"]
        ) -> Params.Harvest.OptCarbonMgmtData: ...
        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Params.Harvest.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Harvest.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            exported: bool | None = None,
            optCarbMgmtData: Params.Harvest.OptCarbonMgmtData.Builder
            | dict[str, Any]
            | None = None,
        ) -> Params.Harvest.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Harvest.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Harvest.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    AutomaticHarvestBuilder: TypeAlias = AutomaticHarvest.Builder
    AutomaticHarvestReader: TypeAlias = AutomaticHarvest.Reader
    class AutomaticHarvest:
        class Reader:
            @property
            def minPercentASW(self) -> float: ...
            @property
            def maxPercentASW(self) -> float: ...
            @property
            def max3dayPrecipSum(self) -> float: ...
            @property
            def maxCurrentDayPrecipSum(self) -> float: ...
            @property
            def harvestTime(self) -> Event.PhenoStage: ...
            @property
            def harvest(self) -> Params.Harvest.Reader: ...
            def as_builder(self) -> Params.AutomaticHarvest.Builder: ...

        class Builder:
            @property
            def minPercentASW(self) -> float: ...
            @minPercentASW.setter
            def minPercentASW(self, value: float) -> None: ...
            @property
            def maxPercentASW(self) -> float: ...
            @maxPercentASW.setter
            def maxPercentASW(self, value: float) -> None: ...
            @property
            def max3dayPrecipSum(self) -> float: ...
            @max3dayPrecipSum.setter
            def max3dayPrecipSum(self, value: float) -> None: ...
            @property
            def maxCurrentDayPrecipSum(self) -> float: ...
            @maxCurrentDayPrecipSum.setter
            def maxCurrentDayPrecipSum(self, value: float) -> None: ...
            @property
            def harvestTime(self) -> Event.PhenoStage: ...
            @harvestTime.setter
            def harvestTime(
                self,
                value: Event.PhenoStage
                | Literal["emergence", "flowering", "anthesis", "maturity"],
            ) -> None: ...
            @property
            def harvest(self) -> Params.Harvest.Builder: ...
            @harvest.setter
            def harvest(
                self,
                value: Params.Harvest.Builder | Params.Harvest.Reader | dict[str, Any],
            ) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Params.AutomaticHarvest.Builder: ...
            def init(self, name: Literal["harvest"]) -> Params.Harvest.Builder: ...
            def copy(self) -> Params.AutomaticHarvest.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Params.AutomaticHarvest.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def init(self, name: Literal["harvest"]) -> Params.Harvest: ...
        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Params.AutomaticHarvest.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.AutomaticHarvest.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            minPercentASW: float | None = None,
            maxPercentASW: float | None = None,
            max3dayPrecipSum: float | None = None,
            maxCurrentDayPrecipSum: float | None = None,
            harvestTime: Event.PhenoStage
            | Literal["emergence", "flowering", "anthesis", "maturity"]
            | None = None,
            harvest: Params.Harvest.Builder | dict[str, Any] | None = None,
        ) -> Params.AutomaticHarvest.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.AutomaticHarvest.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.AutomaticHarvest.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    CuttingBuilder: TypeAlias = Cutting.Builder
    CuttingReader: TypeAlias = Cutting.Reader
    class Cutting:
        class CL(Enum):
            cut = "cut"
            left = "left"

        class Unit(Enum):
            percentage = "percentage"
            biomass = "biomass"
            lai = "lai"

        SpecBuilder: TypeAlias = Spec.Builder
        SpecReader: TypeAlias = Spec.Reader
        class Spec:
            class Reader:
                @property
                def organ(self) -> PlantOrgan: ...
                @property
                def value(self) -> float: ...
                @property
                def unit(self) -> Params.Cutting.Unit: ...
                @property
                def cutOrLeft(self) -> Params.Cutting.CL: ...
                @property
                def exportPercentage(self) -> float: ...
                def as_builder(self) -> Params.Cutting.Spec.Builder: ...

            class Builder:
                @property
                def organ(self) -> PlantOrgan: ...
                @organ.setter
                def organ(
                    self,
                    value: PlantOrgan
                    | Literal["root", "leaf", "shoot", "fruit", "strukt", "sugar"],
                ) -> None: ...
                @property
                def value(self) -> float: ...
                @value.setter
                def value(self, value: float) -> None: ...
                @property
                def unit(self) -> Params.Cutting.Unit: ...
                @unit.setter
                def unit(
                    self,
                    value: Params.Cutting.Unit
                    | Literal["percentage", "biomass", "lai"],
                ) -> None: ...
                @property
                def cutOrLeft(self) -> Params.Cutting.CL: ...
                @cutOrLeft.setter
                def cutOrLeft(
                    self, value: Params.Cutting.CL | Literal["cut", "left"]
                ) -> None: ...
                @property
                def exportPercentage(self) -> float: ...
                @exportPercentage.setter
                def exportPercentage(self, value: float) -> None: ...
                @staticmethod
                def from_dict(
                    dictionary: dict[str, Any],
                ) -> Params.Cutting.Spec.Builder: ...
                def copy(self) -> Params.Cutting.Spec.Builder: ...
                def to_bytes(self) -> bytes: ...
                def to_bytes_packed(self) -> bytes: ...
                def to_segments(self) -> list[bytes]: ...
                def as_reader(self) -> Params.Cutting.Spec.Reader: ...
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
            ) -> Iterator[Params.Cutting.Spec.Reader]: ...
            @staticmethod
            def from_bytes_packed(
                data: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> Params.Cutting.Spec.Reader: ...
            @staticmethod
            def new_message(
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                organ: PlantOrgan
                | Literal["root", "leaf", "shoot", "fruit", "strukt", "sugar"]
                | None = None,
                value: float | None = None,
                unit: Params.Cutting.Unit
                | Literal["percentage", "biomass", "lai"]
                | None = None,
                cutOrLeft: Params.Cutting.CL | Literal["cut", "left"] | None = None,
                exportPercentage: float | None = None,
            ) -> Params.Cutting.Spec.Builder: ...
            @staticmethod
            def read(
                file: BinaryIO,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> Params.Cutting.Spec.Reader: ...
            @staticmethod
            def read_packed(
                file: BinaryIO,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> Params.Cutting.Spec.Reader: ...
            def to_dict(self) -> dict[str, Any]: ...

        class Reader:
            @property
            def cuttingSpec(self) -> Sequence[Params.Cutting.Spec.Reader]: ...
            @property
            def cutMaxAssimilationRatePercentage(self) -> float: ...
            def as_builder(self) -> Params.Cutting.Builder: ...

        class Builder:
            @property
            def cuttingSpec(self) -> Sequence[Params.Cutting.Spec.Builder]: ...
            @cuttingSpec.setter
            def cuttingSpec(
                self,
                value: Sequence[
                    Params.Cutting.Spec.Builder | Params.Cutting.Spec.Reader
                ]
                | Sequence[dict[str, Any]],
            ) -> None: ...
            @property
            def cutMaxAssimilationRatePercentage(self) -> float: ...
            @cutMaxAssimilationRatePercentage.setter
            def cutMaxAssimilationRatePercentage(self, value: float) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Params.Cutting.Builder: ...
            def init(
                self, name: Literal["cuttingSpec"], size: int = ...
            ) -> Sequence[Params.Cutting.Spec.Builder]: ...
            def copy(self) -> Params.Cutting.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Params.Cutting.Reader: ...
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
        ) -> Iterator[Params.Cutting.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Cutting.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            cuttingSpec: Sequence[Params.Cutting.Spec.Builder]
            | Sequence[dict[str, Any]]
            | None = None,
            cutMaxAssimilationRatePercentage: float | None = None,
        ) -> Params.Cutting.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Cutting.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Cutting.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    MineralFertilizationBuilder: TypeAlias = MineralFertilization.Builder
    MineralFertilizationReader: TypeAlias = MineralFertilization.Reader
    class MineralFertilization:
        class Reader:
            @property
            def fertilizer(self) -> FertilizerClient: ...
            @property
            def amount(self) -> float: ...
            def as_builder(self) -> Params.MineralFertilization.Builder: ...

        class Builder:
            @property
            def fertilizer(self) -> FertilizerClient: ...
            @fertilizer.setter
            def fertilizer(
                self, value: FertilizerClient | Fertilizer.Server
            ) -> None: ...
            @property
            def amount(self) -> float: ...
            @amount.setter
            def amount(self, value: float) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Params.MineralFertilization.Builder: ...
            def copy(self) -> Params.MineralFertilization.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Params.MineralFertilization.Reader: ...
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
        ) -> Iterator[Params.MineralFertilization.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.MineralFertilization.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            fertilizer: FertilizerClient | Fertilizer.Server | None = None,
            amount: float | None = None,
        ) -> Params.MineralFertilization.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.MineralFertilization.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.MineralFertilization.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    NDemandFertilizationBuilder: TypeAlias = NDemandFertilization.Builder
    NDemandFertilizationReader: TypeAlias = NDemandFertilization.Reader
    class NDemandFertilization:
        class Reader:
            @property
            def nDemand(self) -> float: ...
            @property
            def fertilizer(self) -> FertilizerClient: ...
            @property
            def depth(self) -> float: ...
            @property
            def stage(self) -> int: ...
            def as_builder(self) -> Params.NDemandFertilization.Builder: ...

        class Builder:
            @property
            def nDemand(self) -> float: ...
            @nDemand.setter
            def nDemand(self, value: float) -> None: ...
            @property
            def fertilizer(self) -> FertilizerClient: ...
            @fertilizer.setter
            def fertilizer(
                self, value: FertilizerClient | Fertilizer.Server
            ) -> None: ...
            @property
            def depth(self) -> float: ...
            @depth.setter
            def depth(self, value: float) -> None: ...
            @property
            def stage(self) -> int: ...
            @stage.setter
            def stage(self, value: int) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Params.NDemandFertilization.Builder: ...
            def copy(self) -> Params.NDemandFertilization.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Params.NDemandFertilization.Reader: ...
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
        ) -> Iterator[Params.NDemandFertilization.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.NDemandFertilization.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            nDemand: float | None = None,
            fertilizer: FertilizerClient | Fertilizer.Server | None = None,
            depth: float | None = None,
            stage: int | None = None,
        ) -> Params.NDemandFertilization.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.NDemandFertilization.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.NDemandFertilization.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    OrganicFertilizationBuilder: TypeAlias = OrganicFertilization.Builder
    OrganicFertilizationReader: TypeAlias = OrganicFertilization.Reader
    class OrganicFertilization:
        class Reader:
            @property
            def fertilizer(self) -> FertilizerClient: ...
            @property
            def amount(self) -> float: ...
            @property
            def incorporation(self) -> bool: ...
            def as_builder(self) -> Params.OrganicFertilization.Builder: ...

        class Builder:
            @property
            def fertilizer(self) -> FertilizerClient: ...
            @fertilizer.setter
            def fertilizer(
                self, value: FertilizerClient | Fertilizer.Server
            ) -> None: ...
            @property
            def amount(self) -> float: ...
            @amount.setter
            def amount(self, value: float) -> None: ...
            @property
            def incorporation(self) -> bool: ...
            @incorporation.setter
            def incorporation(self, value: bool) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Params.OrganicFertilization.Builder: ...
            def copy(self) -> Params.OrganicFertilization.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Params.OrganicFertilization.Reader: ...
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
        ) -> Iterator[Params.OrganicFertilization.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.OrganicFertilization.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            fertilizer: FertilizerClient | Fertilizer.Server | None = None,
            amount: float | None = None,
            incorporation: bool | None = None,
        ) -> Params.OrganicFertilization.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.OrganicFertilization.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.OrganicFertilization.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    TillageBuilder: TypeAlias = Tillage.Builder
    TillageReader: TypeAlias = Tillage.Reader
    class Tillage:
        class Reader:
            @property
            def depth(self) -> float: ...
            def as_builder(self) -> Params.Tillage.Builder: ...

        class Builder:
            @property
            def depth(self) -> float: ...
            @depth.setter
            def depth(self, value: float) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Params.Tillage.Builder: ...
            def copy(self) -> Params.Tillage.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Params.Tillage.Reader: ...
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
        ) -> Iterator[Params.Tillage.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Tillage.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            depth: float | None = None,
        ) -> Params.Tillage.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Tillage.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Tillage.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    IrrigationBuilder: TypeAlias = Irrigation.Builder
    IrrigationReader: TypeAlias = Irrigation.Reader
    class Irrigation:
        class Reader:
            @property
            def amount(self) -> float: ...
            @property
            def nutrientConcentrations(self) -> Sequence[Nutrient.Reader]: ...
            def as_builder(self) -> Params.Irrigation.Builder: ...

        class Builder:
            @property
            def amount(self) -> float: ...
            @amount.setter
            def amount(self, value: float) -> None: ...
            @property
            def nutrientConcentrations(self) -> Sequence[Nutrient.Builder]: ...
            @nutrientConcentrations.setter
            def nutrientConcentrations(
                self,
                value: Sequence[Nutrient.Builder | Nutrient.Reader]
                | Sequence[dict[str, Any]],
            ) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Params.Irrigation.Builder: ...
            def init(
                self, name: Literal["nutrientConcentrations"], size: int = ...
            ) -> Sequence[Nutrient.Builder]: ...
            def copy(self) -> Params.Irrigation.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Params.Irrigation.Reader: ...
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
        ) -> Iterator[Params.Irrigation.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Irrigation.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            amount: float | None = None,
            nutrientConcentrations: Sequence[Nutrient.Builder]
            | Sequence[dict[str, Any]]
            | None = None,
        ) -> Params.Irrigation.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Irrigation.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Params.Irrigation.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Reader:
        def as_builder(self) -> Params.Builder: ...

    class Builder:
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Params.Builder: ...
        def copy(self) -> Params.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Params.Reader: ...
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
    ) -> Iterator[Params.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Params.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None, allocate_seg_callable: Any = None
    ) -> Params.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Params.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Params.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

class FertilizerService:
    @classmethod
    def _new_client(
        cls, server: FertilizerService.Server | Identifiable.Server | Registry.Server
    ) -> FertilizerServiceClient: ...
    class Server(Registry.Server): ...

class FertilizerServiceClient(RegistryClient): ...

class Service:
    class ManagementatRequest(Protocol):
        lat: float
        lon: float
        def send(self) -> Service.ManagementatResult: ...

    class ManagementatResult(Awaitable[ManagementatResult], Protocol):
        mgmt: Sequence[Event.Builder | Event.Reader]

    @classmethod
    def _new_client(
        cls, server: Service.Server | Identifiable.Server
    ) -> ServiceClient: ...
    class Server(Identifiable.Server):
        class ManagementatResultTuple(NamedTuple):
            mgmt: Sequence[Event]

        class ManagementatCallContext(Protocol):
            params: Service.ManagementatRequest
            results: Service.ManagementatResult

        def managementAt(
            self,
            lat: float,
            lon: float,
            _context: Service.Server.ManagementatCallContext,
            **kwargs: Any,
        ) -> Awaitable[Service.Server.ManagementatResultTuple | None]: ...
        def managementAt_context(
            self, context: Service.Server.ManagementatCallContext
        ) -> Awaitable[None]: ...

class ServiceClient(IdentifiableClient):
    def managementAt(
        self, lat: float | None = None, lon: float | None = None
    ) -> Service.ManagementatResult: ...
    def managementAt_request(
        self, lat: float | None = None, lon: float | None = None
    ) -> Service.ManagementatRequest: ...
