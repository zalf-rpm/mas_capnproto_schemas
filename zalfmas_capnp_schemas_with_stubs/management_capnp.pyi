"""This is an automatically generated stub for `management.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, MutableSequence, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

from .common_capnp import (
    _IdentifiableModule,
    _IdInformationModule,
)
from .crop_capnp import _CropModule
from .date_capnp import _DateModule
from .persistence_capnp import _PersistentModule
from .registry_capnp import _RegistryModule

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = (
    str
    | bytes
    | _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicCapabilityClient
    | _DynamicCapabilityServer
)

class _EventTypeModule:
    sowing: int
    automaticSowing: int
    harvest: int
    automaticHarvest: int
    irrigation: int
    tillage: int
    organicFertilization: int
    mineralFertilization: int
    nDemandFertilization: int
    cutting: int
    setValue: int
    saveState: int

class _PlantOrganModule:
    root: int
    leaf: int
    shoot: int
    fruit: int
    strukt: int
    sugar: int

class _EventModule(_StructModule):
    class _ExternalTypeModule:
        sowing: int
        automaticSowing: int
        harvest: int
        automaticHarvest: int
        irrigation: int
        tillage: int
        organicFertilization: int
        mineralFertilization: int
        nDemandFertilization: int
        cutting: int

    ExternalType: _ExternalTypeModule
    class _PhenoStageModule:
        emergence: int
        flowering: int
        anthesis: int
        maturity: int

    PhenoStage: _PhenoStageModule
    class _TypeModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def external(self) -> EventExternalTypeEnum: ...
            @property
            def internal(self) -> EventPhenoStageEnum: ...
            @override
            def which(self) -> Literal["external", "internal"]: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> TypeBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def external(self) -> EventExternalTypeEnum: ...
            @external.setter
            def external(self, value: EventExternalTypeEnum) -> None: ...
            @property
            def internal(self) -> EventPhenoStageEnum: ...
            @internal.setter
            def internal(self, value: EventPhenoStageEnum) -> None: ...
            @override
            def which(self) -> Literal["external", "internal"]: ...
            @override
            def as_reader(self) -> TypeReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            external: EventExternalTypeEnum | None = None,
            internal: EventPhenoStageEnum | None = None,
            **kwargs: Any,
        ) -> TypeBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[TypeReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[TypeReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[TypeBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> TypeReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> TypeReader: ...

    type TypeReader = _TypeModule.Reader
    type TypeBuilder = _TypeModule.Builder
    Type: _TypeModule
    class _AtModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def date(self) -> _DateModule.Reader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> AtBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def date(self) -> _DateModule.Builder: ...
            @date.setter
            def date(
                self, value: _DateModule.Builder | _DateModule.Reader | dict[str, Any]
            ) -> None: ...
            def init(
                self, field: Literal["date"], size: int | None = None
            ) -> _DateModule.Builder: ...
            @override
            def as_reader(self) -> AtReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            date: _DateModule.Builder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> AtBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[AtReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[AtReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[AtBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AtReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AtReader: ...

    type AtReader = _AtModule.Reader
    type AtBuilder = _AtModule.Builder
    At: _AtModule
    class _BetweenModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def earliest(self) -> _DateModule.Reader: ...
            @property
            def latest(self) -> _DateModule.Reader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> BetweenBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def earliest(self) -> _DateModule.Builder: ...
            @earliest.setter
            def earliest(
                self, value: _DateModule.Builder | _DateModule.Reader | dict[str, Any]
            ) -> None: ...
            @property
            def latest(self) -> _DateModule.Builder: ...
            @latest.setter
            def latest(
                self, value: _DateModule.Builder | _DateModule.Reader | dict[str, Any]
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["earliest"], size: int | None = None
            ) -> _DateModule.Builder: ...
            @overload
            def init(
                self, field: Literal["latest"], size: int | None = None
            ) -> _DateModule.Builder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> BetweenReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            earliest: _DateModule.Builder | dict[str, Any] | None = None,
            latest: _DateModule.Builder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> BetweenBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[BetweenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[BetweenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[BetweenBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> BetweenReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> BetweenReader: ...

    type BetweenReader = _BetweenModule.Reader
    type BetweenBuilder = _BetweenModule.Builder
    Between: _BetweenModule
    class _AfterModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def event(self) -> TypeReader: ...
            @property
            def days(self) -> int: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> AfterBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def event(self) -> TypeBuilder: ...
            @event.setter
            def event(
                self, value: TypeBuilder | TypeReader | dict[str, Any]
            ) -> None: ...
            @property
            def days(self) -> int: ...
            @days.setter
            def days(self, value: int) -> None: ...
            def init(
                self, field: Literal["event"], size: int | None = None
            ) -> TypeBuilder: ...
            @override
            def as_reader(self) -> AfterReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            event: TypeBuilder | dict[str, Any] | None = None,
            days: int | None = None,
            **kwargs: Any,
        ) -> AfterBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[AfterReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[AfterReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[AfterBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AfterReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AfterReader: ...

    type AfterReader = _AfterModule.Reader
    type AfterBuilder = _AfterModule.Builder
    After: _AfterModule
    class Reader(_DynamicStructReader):
        @property
        def type(self) -> EventExternalTypeEnum: ...
        @property
        def info(self) -> _IdInformationModule.Reader: ...
        @property
        def at(self) -> AtReader: ...
        @property
        def between(self) -> BetweenReader: ...
        @property
        def after(self) -> AfterReader: ...
        @property
        def params(self) -> Any: ...
        @property
        def runAtStartOfDay(self) -> bool: ...
        @override
        def which(self) -> Literal["at", "between", "after"]: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> EventBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def type(self) -> EventExternalTypeEnum: ...
        @type.setter
        def type(self, value: EventExternalTypeEnum) -> None: ...
        @property
        def info(self) -> _IdInformationModule.Builder: ...
        @info.setter
        def info(
            self,
            value: _IdInformationModule.Builder
            | _IdInformationModule.Reader
            | dict[str, Any],
        ) -> None: ...
        @property
        def at(self) -> AtBuilder: ...
        @at.setter
        def at(self, value: AtBuilder | AtReader | dict[str, Any]) -> None: ...
        @property
        def between(self) -> BetweenBuilder: ...
        @between.setter
        def between(
            self, value: BetweenBuilder | BetweenReader | dict[str, Any]
        ) -> None: ...
        @property
        def after(self) -> AfterBuilder: ...
        @after.setter
        def after(self, value: AfterBuilder | AfterReader | dict[str, Any]) -> None: ...
        @property
        def params(self) -> Any: ...
        @params.setter
        def params(self, value: Any) -> None: ...
        @property
        def runAtStartOfDay(self) -> bool: ...
        @runAtStartOfDay.setter
        def runAtStartOfDay(self, value: bool) -> None: ...
        @override
        def which(self) -> Literal["at", "between", "after"]: ...
        @overload
        def init(
            self, field: Literal["info"], size: int | None = None
        ) -> _IdInformationModule.Builder: ...
        @overload
        def init(self, field: Literal["at"], size: int | None = None) -> AtBuilder: ...
        @overload
        def init(
            self, field: Literal["between"], size: int | None = None
        ) -> BetweenBuilder: ...
        @overload
        def init(
            self, field: Literal["after"], size: int | None = None
        ) -> AfterBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> EventReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        type: EventExternalTypeEnum | None = None,
        info: _IdInformationModule.Builder | dict[str, Any] | None = None,
        at: AtBuilder | dict[str, Any] | None = None,
        between: BetweenBuilder | dict[str, Any] | None = None,
        after: AfterBuilder | dict[str, Any] | None = None,
        params: Any | None = None,
        runAtStartOfDay: bool | None = None,
        **kwargs: Any,
    ) -> EventBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[EventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[EventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[EventBuilder]: ...
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> EventReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> EventReader: ...

Event: _EventModule

class _FertilizerModule(_IdentifiableModule, _PersistentModule):
    class NutrientsRequest(Protocol):
        def send(self) -> _FertilizerModule.FertilizerClient.NutrientsResult: ...

    class ParametersRequest(Protocol):
        def send(self) -> _FertilizerModule.FertilizerClient.ParametersResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _FertilizerModule.FertilizerClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class NutrientsResult(Awaitable[NutrientsResult], Protocol):
            nutrients: Sequence[_NutrientModule.Builder | _NutrientModule.Reader]

        class ParametersResult(Awaitable[ParametersResult], Protocol):
            params: AnyPointer

        class NutrientsResultTuple(NamedTuple):
            nutrients: Sequence[_NutrientModule]

        class ParametersResultTuple(NamedTuple):
            params: AnyPointer

        class NutrientsParams(Protocol): ...

        class NutrientsCallContext(Protocol):
            params: _FertilizerModule.Server.NutrientsParams
            results: _FertilizerModule.Server.NutrientsResult

        class ParametersParams(Protocol): ...

        class ParametersCallContext(Protocol):
            params: _FertilizerModule.Server.ParametersParams
            results: _FertilizerModule.Server.ParametersResult

        def nutrients(
            self,
            _context: _FertilizerModule.Server.NutrientsCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_FertilizerModule.Server.NutrientsResultTuple | None]: ...
        def nutrients_context(
            self, context: _FertilizerModule.Server.NutrientsCallContext
        ) -> Awaitable[None]: ...
        def parameters(
            self,
            _context: _FertilizerModule.Server.ParametersCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_FertilizerModule.Server.ParametersResultTuple | None]: ...
        def parameters_context(
            self, context: _FertilizerModule.Server.ParametersCallContext
        ) -> Awaitable[None]: ...

    class FertilizerClient(
        _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
    ):
        class NutrientsResult(Awaitable[NutrientsResult], Protocol):
            nutrients: Sequence[_NutrientModule.Builder | _NutrientModule.Reader]

        class ParametersResult(Awaitable[ParametersResult], Protocol):
            params: _DynamicObjectReader

        def nutrients(self) -> _FertilizerModule.FertilizerClient.NutrientsResult: ...
        def parameters(self) -> _FertilizerModule.FertilizerClient.ParametersResult: ...
        def nutrients_request(self) -> _FertilizerModule.NutrientsRequest: ...
        def parameters_request(self) -> _FertilizerModule.ParametersRequest: ...

class _NutrientModule(_StructModule):
    class _NameModule:
        urea: int
        ammonia: int
        nitrate: int
        phosphorus: int
        potassium: int
        sulfate: int
        organicC: int
        organicN: int
        organicP: int
        organicNFast: int
        organicNSlow: int

    Name: _NameModule
    class _UnitModule:
        none: int
        fraction: int
        percent: int

    Unit: _UnitModule
    class Reader(_DynamicStructReader):
        @property
        def nutrient(self) -> NutrientNameEnum: ...
        @property
        def value(self) -> float: ...
        @property
        def unit(self) -> NutrientUnitEnum: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> NutrientBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def nutrient(self) -> NutrientNameEnum: ...
        @nutrient.setter
        def nutrient(self, value: NutrientNameEnum) -> None: ...
        @property
        def value(self) -> float: ...
        @value.setter
        def value(self, value: float) -> None: ...
        @property
        def unit(self) -> NutrientUnitEnum: ...
        @unit.setter
        def unit(self, value: NutrientUnitEnum) -> None: ...
        @override
        def as_reader(self) -> NutrientReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        nutrient: NutrientNameEnum | None = None,
        value: float | None = None,
        unit: NutrientUnitEnum | None = None,
        **kwargs: Any,
    ) -> NutrientBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[NutrientReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[NutrientReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[NutrientBuilder]: ...
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> NutrientReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> NutrientReader: ...

Nutrient: _NutrientModule
Fertilizer: _FertilizerModule

class _ParamsModule(_StructModule):
    class _SowingModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def cultivar(self) -> str: ...
            @property
            def plantDensity(self) -> int: ...
            @property
            def crop(self) -> _CropModule.CropClient: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> SowingBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def cultivar(self) -> str: ...
            @cultivar.setter
            def cultivar(self, value: str) -> None: ...
            @property
            def plantDensity(self) -> int: ...
            @plantDensity.setter
            def plantDensity(self, value: int) -> None: ...
            @property
            def crop(self) -> _CropModule.CropClient: ...
            @crop.setter
            def crop(
                self, value: _CropModule.CropClient | _CropModule.Server
            ) -> None: ...
            @override
            def as_reader(self) -> SowingReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            cultivar: str | None = None,
            plantDensity: int | None = None,
            crop: _CropModule.CropClient | _CropModule.Server | None = None,
            **kwargs: Any,
        ) -> SowingBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[SowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[SowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[SowingBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> SowingReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> SowingReader: ...

    type SowingReader = _SowingModule.Reader
    type SowingBuilder = _SowingModule.Builder
    Sowing: _SowingModule
    class _AutomaticSowingModule(_StructModule):
        class _AvgSoilTempModule(_StructModule):
            class Reader(_DynamicStructReader):
                @property
                def soilDepthForAveraging(self) -> float: ...
                @property
                def daysInSoilTempWindow(self) -> int: ...
                @property
                def sowingIfAboveAvgSoilTemp(self) -> float: ...
                @override
                def as_builder(
                    self,
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Any = None,
                ) -> AvgSoilTempBuilder: ...

            class Builder(_DynamicStructBuilder):
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
                @override
                def as_reader(self) -> AvgSoilTempReader: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                soilDepthForAveraging: float | None = None,
                daysInSoilTempWindow: int | None = None,
                sowingIfAboveAvgSoilTemp: float | None = None,
                **kwargs: Any,
            ) -> AvgSoilTempBuilder: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> AbstractContextManager[AvgSoilTempReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[AvgSoilTempReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[AvgSoilTempBuilder]: ...
            def from_bytes_packed(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> _DynamicStructReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> AvgSoilTempReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> AvgSoilTempReader: ...

        type AvgSoilTempReader = _AvgSoilTempModule.Reader
        type AvgSoilTempBuilder = _AvgSoilTempModule.Builder
        AvgSoilTemp: _AvgSoilTempModule
        class Reader(_DynamicStructReader):
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
            def avgSoilTemp(self) -> AvgSoilTempReader: ...
            @property
            def sowing(self) -> SowingReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> AutomaticSowingBuilder: ...

        class Builder(_DynamicStructBuilder):
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
            def avgSoilTemp(self) -> AvgSoilTempBuilder: ...
            @avgSoilTemp.setter
            def avgSoilTemp(
                self, value: AvgSoilTempBuilder | AvgSoilTempReader | dict[str, Any]
            ) -> None: ...
            @property
            def sowing(self) -> SowingBuilder: ...
            @sowing.setter
            def sowing(
                self, value: SowingBuilder | SowingReader | dict[str, Any]
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["avgSoilTemp"], size: int | None = None
            ) -> AvgSoilTempBuilder: ...
            @overload
            def init(
                self, field: Literal["sowing"], size: int | None = None
            ) -> SowingBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> AutomaticSowingReader: ...

        @override
        def new_message(
            self,
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
            avgSoilTemp: AvgSoilTempBuilder | dict[str, Any] | None = None,
            sowing: SowingBuilder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> AutomaticSowingBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[AutomaticSowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[AutomaticSowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[AutomaticSowingBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AutomaticSowingReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AutomaticSowingReader: ...

    type AutomaticSowingReader = _AutomaticSowingModule.Reader
    type AutomaticSowingBuilder = _AutomaticSowingModule.Builder
    AutomaticSowing: _AutomaticSowingModule
    class _HarvestModule(_StructModule):
        class _CropUsageModule:
            greenManure: int
            biomassProduction: int

        CropUsage: _CropUsageModule
        class _OptCarbonMgmtDataModule(_StructModule):
            class Reader(_DynamicStructReader):
                @property
                def optCarbonConservation(self) -> bool: ...
                @property
                def cropImpactOnHumusBalance(self) -> float: ...
                @property
                def cropUsage(self) -> ParamsHarvestCropUsageEnum: ...
                @property
                def residueHeq(self) -> float: ...
                @property
                def organicFertilizerHeq(self) -> float: ...
                @property
                def maxResidueRecoverFraction(self) -> float: ...
                @override
                def as_builder(
                    self,
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Any = None,
                ) -> OptCarbonMgmtDataBuilder: ...

            class Builder(_DynamicStructBuilder):
                @property
                def optCarbonConservation(self) -> bool: ...
                @optCarbonConservation.setter
                def optCarbonConservation(self, value: bool) -> None: ...
                @property
                def cropImpactOnHumusBalance(self) -> float: ...
                @cropImpactOnHumusBalance.setter
                def cropImpactOnHumusBalance(self, value: float) -> None: ...
                @property
                def cropUsage(self) -> ParamsHarvestCropUsageEnum: ...
                @cropUsage.setter
                def cropUsage(self, value: ParamsHarvestCropUsageEnum) -> None: ...
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
                @override
                def as_reader(self) -> OptCarbonMgmtDataReader: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                optCarbonConservation: bool | None = None,
                cropImpactOnHumusBalance: float | None = None,
                cropUsage: ParamsHarvestCropUsageEnum | None = None,
                residueHeq: float | None = None,
                organicFertilizerHeq: float | None = None,
                maxResidueRecoverFraction: float | None = None,
                **kwargs: Any,
            ) -> OptCarbonMgmtDataBuilder: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> AbstractContextManager[OptCarbonMgmtDataReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[OptCarbonMgmtDataReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[OptCarbonMgmtDataBuilder]: ...
            def from_bytes_packed(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> _DynamicStructReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> OptCarbonMgmtDataReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> OptCarbonMgmtDataReader: ...

        type OptCarbonMgmtDataReader = _OptCarbonMgmtDataModule.Reader
        type OptCarbonMgmtDataBuilder = _OptCarbonMgmtDataModule.Builder
        OptCarbonMgmtData: _OptCarbonMgmtDataModule
        class Reader(_DynamicStructReader):
            @property
            def exported(self) -> bool: ...
            @property
            def optCarbMgmtData(self) -> OptCarbonMgmtDataReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> HarvestBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def exported(self) -> bool: ...
            @exported.setter
            def exported(self, value: bool) -> None: ...
            @property
            def optCarbMgmtData(self) -> OptCarbonMgmtDataBuilder: ...
            @optCarbMgmtData.setter
            def optCarbMgmtData(
                self,
                value: OptCarbonMgmtDataBuilder
                | OptCarbonMgmtDataReader
                | dict[str, Any],
            ) -> None: ...
            def init(
                self, field: Literal["optCarbMgmtData"], size: int | None = None
            ) -> OptCarbonMgmtDataBuilder: ...
            @override
            def as_reader(self) -> HarvestReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            exported: bool | None = None,
            optCarbMgmtData: OptCarbonMgmtDataBuilder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> HarvestBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[HarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[HarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[HarvestBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> HarvestReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> HarvestReader: ...

    type HarvestReader = _HarvestModule.Reader
    type HarvestBuilder = _HarvestModule.Builder
    Harvest: _HarvestModule
    class _AutomaticHarvestModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def minPercentASW(self) -> float: ...
            @property
            def maxPercentASW(self) -> float: ...
            @property
            def max3dayPrecipSum(self) -> float: ...
            @property
            def maxCurrentDayPrecipSum(self) -> float: ...
            @property
            def harvestTime(self) -> EventPhenoStageEnum: ...
            @property
            def harvest(self) -> HarvestReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> AutomaticHarvestBuilder: ...

        class Builder(_DynamicStructBuilder):
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
            def harvestTime(self) -> EventPhenoStageEnum: ...
            @harvestTime.setter
            def harvestTime(self, value: EventPhenoStageEnum) -> None: ...
            @property
            def harvest(self) -> HarvestBuilder: ...
            @harvest.setter
            def harvest(
                self, value: HarvestBuilder | HarvestReader | dict[str, Any]
            ) -> None: ...
            def init(
                self, field: Literal["harvest"], size: int | None = None
            ) -> HarvestBuilder: ...
            @override
            def as_reader(self) -> AutomaticHarvestReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            minPercentASW: float | None = None,
            maxPercentASW: float | None = None,
            max3dayPrecipSum: float | None = None,
            maxCurrentDayPrecipSum: float | None = None,
            harvestTime: EventPhenoStageEnum | None = None,
            harvest: HarvestBuilder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> AutomaticHarvestBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[AutomaticHarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[AutomaticHarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[AutomaticHarvestBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AutomaticHarvestReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AutomaticHarvestReader: ...

    type AutomaticHarvestReader = _AutomaticHarvestModule.Reader
    type AutomaticHarvestBuilder = _AutomaticHarvestModule.Builder
    AutomaticHarvest: _AutomaticHarvestModule
    class _CuttingModule(_StructModule):
        class _CLModule:
            cut: int
            left: int

        CL: _CLModule
        class _UnitModule:
            percentage: int
            biomass: int
            lai: int

        Unit: _UnitModule
        class _SpecModule(_StructModule):
            class Reader(_DynamicStructReader):
                @property
                def organ(self) -> PlantOrganEnum: ...
                @property
                def value(self) -> float: ...
                @property
                def unit(self) -> ParamsCuttingUnitEnum: ...
                @property
                def cutOrLeft(self) -> ParamsCuttingCLEnum: ...
                @property
                def exportPercentage(self) -> float: ...
                @override
                def as_builder(
                    self,
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Any = None,
                ) -> SpecBuilder: ...

            class Builder(_DynamicStructBuilder):
                @property
                def organ(self) -> PlantOrganEnum: ...
                @organ.setter
                def organ(self, value: PlantOrganEnum) -> None: ...
                @property
                def value(self) -> float: ...
                @value.setter
                def value(self, value: float) -> None: ...
                @property
                def unit(self) -> ParamsCuttingUnitEnum: ...
                @unit.setter
                def unit(self, value: ParamsCuttingUnitEnum) -> None: ...
                @property
                def cutOrLeft(self) -> ParamsCuttingCLEnum: ...
                @cutOrLeft.setter
                def cutOrLeft(self, value: ParamsCuttingCLEnum) -> None: ...
                @property
                def exportPercentage(self) -> float: ...
                @exportPercentage.setter
                def exportPercentage(self, value: float) -> None: ...
                @override
                def as_reader(self) -> SpecReader: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                organ: PlantOrganEnum | None = None,
                value: float | None = None,
                unit: ParamsCuttingUnitEnum | None = None,
                cutOrLeft: ParamsCuttingCLEnum | None = None,
                exportPercentage: float | None = None,
                **kwargs: Any,
            ) -> SpecBuilder: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> AbstractContextManager[SpecReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[SpecReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[SpecBuilder]: ...
            def from_bytes_packed(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> _DynamicStructReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> SpecReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> SpecReader: ...

        type SpecReader = _SpecModule.Reader
        type SpecBuilder = _SpecModule.Builder
        Spec: _SpecModule
        class Reader(_DynamicStructReader):
            @property
            def cuttingSpec(self) -> Sequence[SpecReader]: ...
            @property
            def cutMaxAssimilationRatePercentage(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> CuttingBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def cuttingSpec(self) -> MutableSequence[SpecBuilder]: ...
            @cuttingSpec.setter
            def cuttingSpec(
                self,
                value: Sequence[SpecBuilder | SpecReader] | Sequence[dict[str, Any]],
            ) -> None: ...
            @property
            def cutMaxAssimilationRatePercentage(self) -> float: ...
            @cutMaxAssimilationRatePercentage.setter
            def cutMaxAssimilationRatePercentage(self, value: float) -> None: ...
            def init(
                self, field: Literal["cuttingSpec"], size: int | None = None
            ) -> MutableSequence[SpecBuilder]: ...
            @override
            def as_reader(self) -> CuttingReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            cuttingSpec: Sequence[SpecBuilder] | Sequence[dict[str, Any]] | None = None,
            cutMaxAssimilationRatePercentage: float | None = None,
            **kwargs: Any,
        ) -> CuttingBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[CuttingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[CuttingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[CuttingBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> CuttingReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> CuttingReader: ...

    type CuttingReader = _CuttingModule.Reader
    type CuttingBuilder = _CuttingModule.Builder
    Cutting: _CuttingModule
    class _MineralFertilizationModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def fertilizer(self) -> _FertilizerModule.FertilizerClient: ...
            @property
            def amount(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> MineralFertilizationBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def fertilizer(self) -> _FertilizerModule.FertilizerClient: ...
            @fertilizer.setter
            def fertilizer(
                self,
                value: _FertilizerModule.FertilizerClient | _FertilizerModule.Server,
            ) -> None: ...
            @property
            def amount(self) -> float: ...
            @amount.setter
            def amount(self, value: float) -> None: ...
            @override
            def as_reader(self) -> MineralFertilizationReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            fertilizer: _FertilizerModule.FertilizerClient
            | _FertilizerModule.Server
            | None = None,
            amount: float | None = None,
            **kwargs: Any,
        ) -> MineralFertilizationBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[MineralFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[MineralFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[MineralFertilizationBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> MineralFertilizationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> MineralFertilizationReader: ...

    type MineralFertilizationReader = _MineralFertilizationModule.Reader
    type MineralFertilizationBuilder = _MineralFertilizationModule.Builder
    MineralFertilization: _MineralFertilizationModule
    class _NDemandFertilizationModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def nDemand(self) -> float: ...
            @property
            def fertilizer(self) -> _FertilizerModule.FertilizerClient: ...
            @property
            def depth(self) -> float: ...
            @property
            def stage(self) -> int: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> NDemandFertilizationBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def nDemand(self) -> float: ...
            @nDemand.setter
            def nDemand(self, value: float) -> None: ...
            @property
            def fertilizer(self) -> _FertilizerModule.FertilizerClient: ...
            @fertilizer.setter
            def fertilizer(
                self,
                value: _FertilizerModule.FertilizerClient | _FertilizerModule.Server,
            ) -> None: ...
            @property
            def depth(self) -> float: ...
            @depth.setter
            def depth(self, value: float) -> None: ...
            @property
            def stage(self) -> int: ...
            @stage.setter
            def stage(self, value: int) -> None: ...
            @override
            def as_reader(self) -> NDemandFertilizationReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            nDemand: float | None = None,
            fertilizer: _FertilizerModule.FertilizerClient
            | _FertilizerModule.Server
            | None = None,
            depth: float | None = None,
            stage: int | None = None,
            **kwargs: Any,
        ) -> NDemandFertilizationBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[NDemandFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[NDemandFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[NDemandFertilizationBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> NDemandFertilizationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> NDemandFertilizationReader: ...

    type NDemandFertilizationReader = _NDemandFertilizationModule.Reader
    type NDemandFertilizationBuilder = _NDemandFertilizationModule.Builder
    NDemandFertilization: _NDemandFertilizationModule
    class _OrganicFertilizationModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def fertilizer(self) -> _FertilizerModule.FertilizerClient: ...
            @property
            def amount(self) -> float: ...
            @property
            def incorporation(self) -> bool: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> OrganicFertilizationBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def fertilizer(self) -> _FertilizerModule.FertilizerClient: ...
            @fertilizer.setter
            def fertilizer(
                self,
                value: _FertilizerModule.FertilizerClient | _FertilizerModule.Server,
            ) -> None: ...
            @property
            def amount(self) -> float: ...
            @amount.setter
            def amount(self, value: float) -> None: ...
            @property
            def incorporation(self) -> bool: ...
            @incorporation.setter
            def incorporation(self, value: bool) -> None: ...
            @override
            def as_reader(self) -> OrganicFertilizationReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            fertilizer: _FertilizerModule.FertilizerClient
            | _FertilizerModule.Server
            | None = None,
            amount: float | None = None,
            incorporation: bool | None = None,
            **kwargs: Any,
        ) -> OrganicFertilizationBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[OrganicFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[OrganicFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[OrganicFertilizationBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> OrganicFertilizationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> OrganicFertilizationReader: ...

    type OrganicFertilizationReader = _OrganicFertilizationModule.Reader
    type OrganicFertilizationBuilder = _OrganicFertilizationModule.Builder
    OrganicFertilization: _OrganicFertilizationModule
    class _TillageModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def depth(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> TillageBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def depth(self) -> float: ...
            @depth.setter
            def depth(self, value: float) -> None: ...
            @override
            def as_reader(self) -> TillageReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            depth: float | None = None,
            **kwargs: Any,
        ) -> TillageBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[TillageReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[TillageReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[TillageBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> TillageReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> TillageReader: ...

    type TillageReader = _TillageModule.Reader
    type TillageBuilder = _TillageModule.Builder
    Tillage: _TillageModule
    class _IrrigationModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def amount(self) -> float: ...
            @property
            def nutrientConcentrations(self) -> Sequence[NutrientReader]: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> IrrigationBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def amount(self) -> float: ...
            @amount.setter
            def amount(self, value: float) -> None: ...
            @property
            def nutrientConcentrations(self) -> MutableSequence[NutrientBuilder]: ...
            @nutrientConcentrations.setter
            def nutrientConcentrations(
                self,
                value: Sequence[NutrientBuilder | NutrientReader]
                | Sequence[dict[str, Any]],
            ) -> None: ...
            def init(
                self, field: Literal["nutrientConcentrations"], size: int | None = None
            ) -> MutableSequence[NutrientBuilder]: ...
            @override
            def as_reader(self) -> IrrigationReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            amount: float | None = None,
            nutrientConcentrations: Sequence[NutrientBuilder]
            | Sequence[dict[str, Any]]
            | None = None,
            **kwargs: Any,
        ) -> IrrigationBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[IrrigationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[IrrigationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[IrrigationBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> IrrigationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> IrrigationReader: ...

    type IrrigationReader = _IrrigationModule.Reader
    type IrrigationBuilder = _IrrigationModule.Builder
    Irrigation: _IrrigationModule
    class Reader(_DynamicStructReader):
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> ParamsBuilder: ...

    class Builder(_DynamicStructBuilder):
        @override
        def as_reader(self) -> ParamsReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        **kwargs: Any,
    ) -> ParamsBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[ParamsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[ParamsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[ParamsBuilder]: ...
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ParamsReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ParamsReader: ...

Params: _ParamsModule

class _FertilizerServiceModule(_RegistryModule):
    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _FertilizerServiceModule.FertilizerServiceClient: ...
    class Server(_RegistryModule.Server): ...
    class FertilizerServiceClient(_RegistryModule.RegistryClient): ...

FertilizerService: _FertilizerServiceModule

class _ServiceModule(_IdentifiableModule):
    class ManagementatRequest(Protocol):
        lat: float
        lon: float
        def send(self) -> _ServiceModule.ServiceClient.ManagementatResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _ServiceModule.ServiceClient: ...
    class Server(_IdentifiableModule.Server):
        class ManagementatResult(Awaitable[ManagementatResult], Protocol):
            mgmt: Sequence[_EventModule.Builder | _EventModule.Reader]

        class ManagementatResultTuple(NamedTuple):
            mgmt: Sequence[_EventModule]

        class ManagementatParams(Protocol):
            lat: float
            lon: float

        class ManagementatCallContext(Protocol):
            params: _ServiceModule.Server.ManagementatParams
            results: _ServiceModule.Server.ManagementatResult

        def managementAt(
            self,
            lat: float,
            lon: float,
            _context: _ServiceModule.Server.ManagementatCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_ServiceModule.Server.ManagementatResultTuple | None]: ...
        def managementAt_context(
            self, context: _ServiceModule.Server.ManagementatCallContext
        ) -> Awaitable[None]: ...

    class ServiceClient(_IdentifiableModule.IdentifiableClient):
        class ManagementatResult(Awaitable[ManagementatResult], Protocol):
            mgmt: Sequence[_EventModule.Builder | _EventModule.Reader]

        def managementAt(
            self, lat: float | None = None, lon: float | None = None
        ) -> _ServiceModule.ServiceClient.ManagementatResult: ...
        def managementAt_request(
            self, lat: float | None = None, lon: float | None = None
        ) -> _ServiceModule.ManagementatRequest: ...

Service: _ServiceModule

# Top-level type aliases for use in type annotations
type AfterBuilder = _EventModule._AfterModule.Builder
type AfterReader = _EventModule._AfterModule.Reader
type AtBuilder = _EventModule._AtModule.Builder
type AtReader = _EventModule._AtModule.Reader
type AutomaticHarvestBuilder = _ParamsModule._AutomaticHarvestModule.Builder
type AutomaticHarvestReader = _ParamsModule._AutomaticHarvestModule.Reader
type AutomaticSowingBuilder = _ParamsModule._AutomaticSowingModule.Builder
type AutomaticSowingReader = _ParamsModule._AutomaticSowingModule.Reader
type AvgSoilTempBuilder = (
    _ParamsModule._AutomaticSowingModule._AvgSoilTempModule.Builder
)
type AvgSoilTempReader = _ParamsModule._AutomaticSowingModule._AvgSoilTempModule.Reader
type BetweenBuilder = _EventModule._BetweenModule.Builder
type BetweenReader = _EventModule._BetweenModule.Reader
type CuttingBuilder = _ParamsModule._CuttingModule.Builder
type CuttingReader = _ParamsModule._CuttingModule.Reader
type EventBuilder = _EventModule.Builder
type EventExternalTypeEnum = (
    int
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
)
type EventPhenoStageEnum = (
    int | Literal["emergence", "flowering", "anthesis", "maturity"]
)
type EventReader = _EventModule.Reader
type EventTypeEnum = (
    int
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
        "setValue",
        "saveState",
    ]
)
type FertilizerClient = _FertilizerModule.FertilizerClient
type FertilizerServiceClient = _FertilizerServiceModule.FertilizerServiceClient
type HarvestBuilder = _ParamsModule._HarvestModule.Builder
type HarvestReader = _ParamsModule._HarvestModule.Reader
type IrrigationBuilder = _ParamsModule._IrrigationModule.Builder
type IrrigationReader = _ParamsModule._IrrigationModule.Reader
type ManagementatResult = _ServiceModule.ServiceClient.ManagementatResult
type MineralFertilizationBuilder = _ParamsModule._MineralFertilizationModule.Builder
type MineralFertilizationReader = _ParamsModule._MineralFertilizationModule.Reader
type NDemandFertilizationBuilder = _ParamsModule._NDemandFertilizationModule.Builder
type NDemandFertilizationReader = _ParamsModule._NDemandFertilizationModule.Reader
type NutrientBuilder = _NutrientModule.Builder
type NutrientNameEnum = (
    int
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
)
type NutrientReader = _NutrientModule.Reader
type NutrientUnitEnum = int | Literal["none", "fraction", "percent"]
type NutrientsResult = _FertilizerModule.FertilizerClient.NutrientsResult
type OptCarbonMgmtDataBuilder = (
    _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Builder
)
type OptCarbonMgmtDataReader = (
    _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Reader
)
type OrganicFertilizationBuilder = _ParamsModule._OrganicFertilizationModule.Builder
type OrganicFertilizationReader = _ParamsModule._OrganicFertilizationModule.Reader
type ParametersResult = _FertilizerModule.FertilizerClient.ParametersResult
type ParamsBuilder = _ParamsModule.Builder
type ParamsCuttingCLEnum = int | Literal["cut", "left"]
type ParamsCuttingUnitEnum = int | Literal["percentage", "biomass", "lai"]
type ParamsHarvestCropUsageEnum = int | Literal["greenManure", "biomassProduction"]
type ParamsReader = _ParamsModule.Reader
type PlantOrganEnum = int | Literal["root", "leaf", "shoot", "fruit", "strukt", "sugar"]
type ServiceClient = _ServiceModule.ServiceClient
type SowingBuilder = _ParamsModule._SowingModule.Builder
type SowingReader = _ParamsModule._SowingModule.Reader
type SpecBuilder = _ParamsModule._CuttingModule._SpecModule.Builder
type SpecReader = _ParamsModule._CuttingModule._SpecModule.Reader
type TillageBuilder = _ParamsModule._TillageModule.Builder
type TillageReader = _ParamsModule._TillageModule.Reader
type TypeBuilder = _EventModule._TypeModule.Builder
type TypeReader = _EventModule._TypeModule.Reader
