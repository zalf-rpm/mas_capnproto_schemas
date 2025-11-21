"""This is an automatically generated stub for `monica_management.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, MutableSequence, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

from ...climate_capnp import ElementEnum
from ...common_capnp import (
    IdInformationBuilder,
    IdInformationReader,
    _IdentifiableModule,
)
from ...crop_capnp import _CropModule
from ...date_capnp import DateBuilder, DateReader

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = (
    str
    | bytes
    | _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicListBuilder
    | _DynamicListReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class _ILRDatesModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def sowing(self) -> DateReader: ...
        @property
        def earliestSowing(self) -> DateReader: ...
        @property
        def latestSowing(self) -> DateReader: ...
        @property
        def harvest(self) -> DateReader: ...
        @property
        def latestHarvest(self) -> DateReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> ILRDatesBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def sowing(self) -> DateBuilder: ...
        @sowing.setter
        def sowing(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
        @property
        def earliestSowing(self) -> DateBuilder: ...
        @earliestSowing.setter
        def earliestSowing(
            self, value: DateBuilder | DateReader | dict[str, Any]
        ) -> None: ...
        @property
        def latestSowing(self) -> DateBuilder: ...
        @latestSowing.setter
        def latestSowing(
            self, value: DateBuilder | DateReader | dict[str, Any]
        ) -> None: ...
        @property
        def harvest(self) -> DateBuilder: ...
        @harvest.setter
        def harvest(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
        @property
        def latestHarvest(self) -> DateBuilder: ...
        @latestHarvest.setter
        def latestHarvest(
            self, value: DateBuilder | DateReader | dict[str, Any]
        ) -> None: ...
        @overload
        def init(
            self, field: Literal["sowing"], size: int | None = None
        ) -> DateBuilder: ...
        @overload
        def init(
            self, field: Literal["earliestSowing"], size: int | None = None
        ) -> DateBuilder: ...
        @overload
        def init(
            self, field: Literal["latestSowing"], size: int | None = None
        ) -> DateBuilder: ...
        @overload
        def init(
            self, field: Literal["harvest"], size: int | None = None
        ) -> DateBuilder: ...
        @overload
        def init(
            self, field: Literal["latestHarvest"], size: int | None = None
        ) -> DateBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> ILRDatesReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        sowing: DateBuilder | dict[str, Any] | None = None,
        earliestSowing: DateBuilder | dict[str, Any] | None = None,
        latestSowing: DateBuilder | dict[str, Any] | None = None,
        harvest: DateBuilder | dict[str, Any] | None = None,
        latestHarvest: DateBuilder | dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> ILRDatesBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[ILRDatesReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[ILRDatesReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[ILRDatesBuilder]: ...
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
    ) -> ILRDatesReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ILRDatesReader: ...

ILRDates: _ILRDatesModule

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
        setValue: int
        saveState: int
        weather: int

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
            def date(self) -> DateReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> AtBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def date(self) -> DateBuilder: ...
            @date.setter
            def date(
                self, value: DateBuilder | DateReader | dict[str, Any]
            ) -> None: ...
            def init(
                self, field: Literal["date"], size: int | None = None
            ) -> DateBuilder: ...
            @override
            def as_reader(self) -> AtReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            date: DateBuilder | dict[str, Any] | None = None,
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
            def earliest(self) -> DateReader: ...
            @property
            def latest(self) -> DateReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> BetweenBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def earliest(self) -> DateBuilder: ...
            @earliest.setter
            def earliest(
                self, value: DateBuilder | DateReader | dict[str, Any]
            ) -> None: ...
            @property
            def latest(self) -> DateBuilder: ...
            @latest.setter
            def latest(
                self, value: DateBuilder | DateReader | dict[str, Any]
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["earliest"], size: int | None = None
            ) -> DateBuilder: ...
            @overload
            def init(
                self, field: Literal["latest"], size: int | None = None
            ) -> DateBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> BetweenReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            earliest: DateBuilder | dict[str, Any] | None = None,
            latest: DateBuilder | dict[str, Any] | None = None,
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
        def info(self) -> IdInformationReader: ...
        @property
        def at(self) -> AtReader: ...
        @property
        def between(self) -> BetweenReader: ...
        @property
        def after(self) -> AfterReader: ...
        @property
        def params(self) -> _DynamicObjectReader: ...
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
        def info(self) -> IdInformationBuilder: ...
        @info.setter
        def info(
            self, value: IdInformationBuilder | IdInformationReader | dict[str, Any]
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
        def params(self) -> _DynamicObjectBuilder: ...
        @params.setter
        def params(self, value: AnyPointer) -> None: ...
        @property
        def runAtStartOfDay(self) -> bool: ...
        @runAtStartOfDay.setter
        def runAtStartOfDay(self, value: bool) -> None: ...
        @override
        def which(self) -> Literal["at", "between", "after"]: ...
        @overload
        def init(
            self, field: Literal["info"], size: int | None = None
        ) -> IdInformationBuilder: ...
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
        info: IdInformationBuilder | dict[str, Any] | None = None,
        at: AtBuilder | dict[str, Any] | None = None,
        between: BetweenBuilder | dict[str, Any] | None = None,
        after: AfterBuilder | dict[str, Any] | None = None,
        params: AnyPointer | None = None,
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

class _ParamsModule(_StructModule):
    class _DailyWeatherModule(_StructModule):
        class _KVModule(_StructModule):
            class Reader(_DynamicStructReader):
                @property
                def key(self) -> ElementEnum: ...
                @property
                def value(self) -> float: ...
                @override
                def as_builder(
                    self,
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Any = None,
                ) -> KVBuilder: ...

            class Builder(_DynamicStructBuilder):
                @property
                def key(self) -> ElementEnum: ...
                @key.setter
                def key(self, value: ElementEnum) -> None: ...
                @property
                def value(self) -> float: ...
                @value.setter
                def value(self, value: float) -> None: ...
                @override
                def as_reader(self) -> KVReader: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                key: ElementEnum | None = None,
                value: float | None = None,
                **kwargs: Any,
            ) -> KVBuilder: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> AbstractContextManager[KVReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[KVReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[KVBuilder]: ...
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
            ) -> KVReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> KVReader: ...

        type KVReader = _KVModule.Reader
        type KVBuilder = _KVModule.Builder
        KV: _KVModule
        class Reader(_DynamicStructReader):
            @property
            def data(self) -> Sequence[KVReader]: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> DailyWeatherBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def data(self) -> MutableSequence[KVBuilder]: ...
            @data.setter
            def data(
                self, value: Sequence[KVBuilder | KVReader] | Sequence[dict[str, Any]]
            ) -> None: ...
            def init(
                self, field: Literal["data"], size: int | None = None
            ) -> MutableSequence[KVBuilder]: ...
            @override
            def as_reader(self) -> DailyWeatherReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            data: Sequence[KVBuilder] | Sequence[dict[str, Any]] | None = None,
            **kwargs: Any,
        ) -> DailyWeatherBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[DailyWeatherReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[DailyWeatherReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[DailyWeatherBuilder]: ...
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
        ) -> DailyWeatherReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> DailyWeatherReader: ...

    type DailyWeatherReader = _DailyWeatherModule.Reader
    type DailyWeatherBuilder = _DailyWeatherModule.Builder
    DailyWeather: _DailyWeatherModule
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
        class _ParametersModule(_StructModule):
            class Reader(_DynamicStructReader):
                @property
                def id(self) -> str: ...
                @property
                def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
                @property
                def carbamid(self) -> float: ...
                @property
                def nh4(self) -> float: ...
                @property
                def no3(self) -> float: ...
                @override
                def as_builder(
                    self,
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Any = None,
                ) -> ParametersBuilder: ...

            class Builder(_DynamicStructBuilder):
                @property
                def id(self) -> str: ...
                @id.setter
                def id(self, value: str) -> None: ...
                @property
                def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
                @name.setter
                def name(self, value: str) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
                @property
                def carbamid(self) -> float: ...
                @carbamid.setter
                def carbamid(self, value: float) -> None: ...
                @property
                def nh4(self) -> float: ...
                @nh4.setter
                def nh4(self, value: float) -> None: ...
                @property
                def no3(self) -> float: ...
                @no3.setter
                def no3(self, value: float) -> None: ...
                @override
                def as_reader(self) -> ParametersReader: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                id: str | None = None,
                name: str | None = None,
                carbamid: float | None = None,
                nh4: float | None = None,
                no3: float | None = None,
                **kwargs: Any,
            ) -> ParametersBuilder: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> AbstractContextManager[ParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[ParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[ParametersBuilder]: ...
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
            ) -> ParametersReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> ParametersReader: ...

        type ParametersReader = _ParametersModule.Reader
        type ParametersBuilder = _ParametersModule.Builder
        Parameters: _ParametersModule
        class Reader(_DynamicStructReader):
            @property
            def partition(self) -> ParametersReader: ...
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
            def partition(self) -> ParametersBuilder: ...
            @partition.setter
            def partition(
                self, value: ParametersBuilder | ParametersReader | dict[str, Any]
            ) -> None: ...
            @property
            def amount(self) -> float: ...
            @amount.setter
            def amount(self, value: float) -> None: ...
            def init(
                self, field: Literal["partition"], size: int | None = None
            ) -> ParametersBuilder: ...
            @override
            def as_reader(self) -> MineralFertilizationReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            partition: ParametersBuilder | dict[str, Any] | None = None,
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
            def partition(self) -> ParametersReader: ...
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
            def partition(self) -> ParametersBuilder: ...
            @partition.setter
            def partition(
                self, value: ParametersBuilder | ParametersReader | dict[str, Any]
            ) -> None: ...
            @property
            def depth(self) -> float: ...
            @depth.setter
            def depth(self, value: float) -> None: ...
            @property
            def stage(self) -> int: ...
            @stage.setter
            def stage(self, value: int) -> None: ...
            def init(
                self, field: Literal["partition"], size: int | None = None
            ) -> ParametersBuilder: ...
            @override
            def as_reader(self) -> NDemandFertilizationReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            nDemand: float | None = None,
            partition: ParametersBuilder | dict[str, Any] | None = None,
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
        class _OrganicMatterParametersModule(_StructModule):
            class Reader(_DynamicStructReader):
                @property
                def aomDryMatterContent(self) -> float: ...
                @property
                def aomNH4Content(self) -> float: ...
                @property
                def aomNO3Content(self) -> float: ...
                @property
                def aomCarbamidContent(self) -> float: ...
                @property
                def aomSlowDecCoeffStandard(self) -> float: ...
                @property
                def aomFastDecCoeffStandard(self) -> float: ...
                @property
                def partAOMToAOMSlow(self) -> float: ...
                @property
                def partAOMToAOMFast(self) -> float: ...
                @property
                def cnRatioAOMSlow(self) -> float: ...
                @property
                def cnRatioAOMFast(self) -> float: ...
                @property
                def partAOMSlowToSMBSlow(self) -> float: ...
                @property
                def partAOMSlowToSMBFast(self) -> float: ...
                @property
                def nConcentration(self) -> float: ...
                @override
                def as_builder(
                    self,
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Any = None,
                ) -> OrganicMatterParametersBuilder: ...

            class Builder(_DynamicStructBuilder):
                @property
                def aomDryMatterContent(self) -> float: ...
                @aomDryMatterContent.setter
                def aomDryMatterContent(self, value: float) -> None: ...
                @property
                def aomNH4Content(self) -> float: ...
                @aomNH4Content.setter
                def aomNH4Content(self, value: float) -> None: ...
                @property
                def aomNO3Content(self) -> float: ...
                @aomNO3Content.setter
                def aomNO3Content(self, value: float) -> None: ...
                @property
                def aomCarbamidContent(self) -> float: ...
                @aomCarbamidContent.setter
                def aomCarbamidContent(self, value: float) -> None: ...
                @property
                def aomSlowDecCoeffStandard(self) -> float: ...
                @aomSlowDecCoeffStandard.setter
                def aomSlowDecCoeffStandard(self, value: float) -> None: ...
                @property
                def aomFastDecCoeffStandard(self) -> float: ...
                @aomFastDecCoeffStandard.setter
                def aomFastDecCoeffStandard(self, value: float) -> None: ...
                @property
                def partAOMToAOMSlow(self) -> float: ...
                @partAOMToAOMSlow.setter
                def partAOMToAOMSlow(self, value: float) -> None: ...
                @property
                def partAOMToAOMFast(self) -> float: ...
                @partAOMToAOMFast.setter
                def partAOMToAOMFast(self, value: float) -> None: ...
                @property
                def cnRatioAOMSlow(self) -> float: ...
                @cnRatioAOMSlow.setter
                def cnRatioAOMSlow(self, value: float) -> None: ...
                @property
                def cnRatioAOMFast(self) -> float: ...
                @cnRatioAOMFast.setter
                def cnRatioAOMFast(self, value: float) -> None: ...
                @property
                def partAOMSlowToSMBSlow(self) -> float: ...
                @partAOMSlowToSMBSlow.setter
                def partAOMSlowToSMBSlow(self, value: float) -> None: ...
                @property
                def partAOMSlowToSMBFast(self) -> float: ...
                @partAOMSlowToSMBFast.setter
                def partAOMSlowToSMBFast(self, value: float) -> None: ...
                @property
                def nConcentration(self) -> float: ...
                @nConcentration.setter
                def nConcentration(self, value: float) -> None: ...
                @override
                def as_reader(self) -> OrganicMatterParametersReader: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                aomDryMatterContent: float | None = None,
                aomNH4Content: float | None = None,
                aomNO3Content: float | None = None,
                aomCarbamidContent: float | None = None,
                aomSlowDecCoeffStandard: float | None = None,
                aomFastDecCoeffStandard: float | None = None,
                partAOMToAOMSlow: float | None = None,
                partAOMToAOMFast: float | None = None,
                cnRatioAOMSlow: float | None = None,
                cnRatioAOMFast: float | None = None,
                partAOMSlowToSMBSlow: float | None = None,
                partAOMSlowToSMBFast: float | None = None,
                nConcentration: float | None = None,
                **kwargs: Any,
            ) -> OrganicMatterParametersBuilder: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> AbstractContextManager[OrganicMatterParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[OrganicMatterParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[OrganicMatterParametersBuilder]: ...
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
            ) -> OrganicMatterParametersReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> OrganicMatterParametersReader: ...

        type OrganicMatterParametersReader = _OrganicMatterParametersModule.Reader
        type OrganicMatterParametersBuilder = _OrganicMatterParametersModule.Builder
        OrganicMatterParameters: _OrganicMatterParametersModule
        class _ParametersModule(_StructModule):
            class Reader(_DynamicStructReader):
                @property
                def params(self) -> OrganicMatterParametersReader: ...
                @property
                def id(self) -> str: ...
                @property
                def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
                @override
                def as_builder(
                    self,
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Any = None,
                ) -> ParametersBuilder: ...

            class Builder(_DynamicStructBuilder):
                @property
                def params(self) -> OrganicMatterParametersBuilder: ...
                @params.setter
                def params(
                    self,
                    value: OrganicMatterParametersBuilder
                    | OrganicMatterParametersReader
                    | dict[str, Any],
                ) -> None: ...
                @property
                def id(self) -> str: ...
                @id.setter
                def id(self, value: str) -> None: ...
                @property
                def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
                @name.setter
                def name(self, value: str) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
                def init(
                    self, field: Literal["params"], size: int | None = None
                ) -> OrganicMatterParametersBuilder: ...
                @override
                def as_reader(self) -> ParametersReader: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                params: OrganicMatterParametersBuilder | dict[str, Any] | None = None,
                id: str | None = None,
                name: str | None = None,
                **kwargs: Any,
            ) -> ParametersBuilder: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> AbstractContextManager[ParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[ParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[ParametersBuilder]: ...
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
            ) -> ParametersReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> ParametersReader: ...

        type ParametersReader = _ParametersModule.Reader
        type ParametersBuilder = _ParametersModule.Builder
        Parameters: _ParametersModule
        class Reader(_DynamicStructReader):
            @property
            def params(self) -> ParametersReader: ...
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
            def params(self) -> ParametersBuilder: ...
            @params.setter
            def params(
                self, value: ParametersBuilder | ParametersReader | dict[str, Any]
            ) -> None: ...
            @property
            def amount(self) -> float: ...
            @amount.setter
            def amount(self, value: float) -> None: ...
            @property
            def incorporation(self) -> bool: ...
            @incorporation.setter
            def incorporation(self, value: bool) -> None: ...
            def init(
                self, field: Literal["params"], size: int | None = None
            ) -> ParametersBuilder: ...
            @override
            def as_reader(self) -> OrganicFertilizationReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            params: ParametersBuilder | dict[str, Any] | None = None,
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
        class _ParametersModule(_StructModule):
            class Reader(_DynamicStructReader):
                @property
                def nitrateConcentration(self) -> float: ...
                @property
                def sulfateConcentration(self) -> float: ...
                @override
                def as_builder(
                    self,
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Any = None,
                ) -> ParametersBuilder: ...

            class Builder(_DynamicStructBuilder):
                @property
                def nitrateConcentration(self) -> float: ...
                @nitrateConcentration.setter
                def nitrateConcentration(self, value: float) -> None: ...
                @property
                def sulfateConcentration(self) -> float: ...
                @sulfateConcentration.setter
                def sulfateConcentration(self, value: float) -> None: ...
                @override
                def as_reader(self) -> ParametersReader: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                nitrateConcentration: float | None = None,
                sulfateConcentration: float | None = None,
                **kwargs: Any,
            ) -> ParametersBuilder: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> AbstractContextManager[ParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[ParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[ParametersBuilder]: ...
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
            ) -> ParametersReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> ParametersReader: ...

        type ParametersReader = _ParametersModule.Reader
        type ParametersBuilder = _ParametersModule.Builder
        Parameters: _ParametersModule
        class Reader(_DynamicStructReader):
            @property
            def amount(self) -> float: ...
            @property
            def params(self) -> ParametersReader: ...
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
            def params(self) -> ParametersBuilder: ...
            @params.setter
            def params(
                self, value: ParametersBuilder | ParametersReader | dict[str, Any]
            ) -> None: ...
            def init(
                self, field: Literal["params"], size: int | None = None
            ) -> ParametersBuilder: ...
            @override
            def as_reader(self) -> IrrigationReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            amount: float | None = None,
            params: ParametersBuilder | dict[str, Any] | None = None,
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
    class _SaveStateModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def noOfPreviousDaysSerializedClimateData(self) -> int: ...
            @property
            def asJson(self) -> bool: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> SaveStateBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def noOfPreviousDaysSerializedClimateData(self) -> int: ...
            @noOfPreviousDaysSerializedClimateData.setter
            def noOfPreviousDaysSerializedClimateData(self, value: int) -> None: ...
            @property
            def asJson(self) -> bool: ...
            @asJson.setter
            def asJson(self, value: bool) -> None: ...
            @override
            def as_reader(self) -> SaveStateReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            noOfPreviousDaysSerializedClimateData: int | None = None,
            asJson: bool | None = None,
            **kwargs: Any,
        ) -> SaveStateBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[SaveStateReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[SaveStateReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[SaveStateBuilder]: ...
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
        ) -> SaveStateReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> SaveStateReader: ...

    type SaveStateReader = _SaveStateModule.Reader
    type SaveStateBuilder = _SaveStateModule.Builder
    SaveState: _SaveStateModule
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
            mgmt: Sequence[EventBuilder | EventReader]

        class ManagementatResultTuple(NamedTuple):
            mgmt: Sequence[EventBuilder | EventReader]

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
        ) -> Awaitable[
            Sequence[_EventModule]
            | _ServiceModule.Server.ManagementatResultTuple
            | None
        ]: ...
        def managementAt_context(
            self, context: _ServiceModule.Server.ManagementatCallContext
        ) -> Awaitable[None]: ...

    class ServiceClient(_IdentifiableModule.IdentifiableClient):
        class ManagementatResult(Awaitable[ManagementatResult], Protocol):
            mgmt: Sequence[EventReader]

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
type DailyWeatherBuilder = _ParamsModule._DailyWeatherModule.Builder
type DailyWeatherReader = _ParamsModule._DailyWeatherModule.Reader
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
        "setValue",
        "saveState",
        "weather",
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
type HarvestBuilder = _ParamsModule._HarvestModule.Builder
type HarvestReader = _ParamsModule._HarvestModule.Reader
type ILRDatesBuilder = _ILRDatesModule.Builder
type ILRDatesReader = _ILRDatesModule.Reader
type IrrigationBuilder = _ParamsModule._IrrigationModule.Builder
type IrrigationReader = _ParamsModule._IrrigationModule.Reader
type KVBuilder = _ParamsModule._DailyWeatherModule._KVModule.Builder
type KVReader = _ParamsModule._DailyWeatherModule._KVModule.Reader
type ManagementatResult = _ServiceModule.ServiceClient.ManagementatResult
type MineralFertilizationBuilder = _ParamsModule._MineralFertilizationModule.Builder
type MineralFertilizationReader = _ParamsModule._MineralFertilizationModule.Reader
type NDemandFertilizationBuilder = _ParamsModule._NDemandFertilizationModule.Builder
type NDemandFertilizationReader = _ParamsModule._NDemandFertilizationModule.Reader
type OptCarbonMgmtDataBuilder = (
    _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Builder
)
type OptCarbonMgmtDataReader = (
    _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Reader
)
type OrganicFertilizationBuilder = _ParamsModule._OrganicFertilizationModule.Builder
type OrganicFertilizationReader = _ParamsModule._OrganicFertilizationModule.Reader
type OrganicMatterParametersBuilder = (
    _ParamsModule._OrganicFertilizationModule._OrganicMatterParametersModule.Builder
)
type OrganicMatterParametersReader = (
    _ParamsModule._OrganicFertilizationModule._OrganicMatterParametersModule.Reader
)
type ParametersBuilder = _ParamsModule._IrrigationModule._ParametersModule.Builder
type ParametersReader = _ParamsModule._IrrigationModule._ParametersModule.Reader
type ParamsBuilder = _ParamsModule.Builder
type ParamsCuttingCLEnum = int | Literal["cut", "left"]
type ParamsCuttingUnitEnum = int | Literal["percentage", "biomass", "lai"]
type ParamsHarvestCropUsageEnum = int | Literal["greenManure", "biomassProduction"]
type ParamsReader = _ParamsModule.Reader
type PlantOrganEnum = int | Literal["root", "leaf", "shoot", "fruit", "strukt", "sugar"]
type SaveStateBuilder = _ParamsModule._SaveStateModule.Builder
type SaveStateReader = _ParamsModule._SaveStateModule.Reader
type ServiceClient = _ServiceModule.ServiceClient
type SowingBuilder = _ParamsModule._SowingModule.Builder
type SowingReader = _ParamsModule._SowingModule.Reader
type SpecBuilder = _ParamsModule._CuttingModule._SpecModule.Builder
type SpecReader = _ParamsModule._CuttingModule._SpecModule.Reader
type TillageBuilder = _ParamsModule._TillageModule.Builder
type TillageReader = _ParamsModule._TillageModule.Reader
type TypeBuilder = _EventModule._TypeModule.Builder
type TypeReader = _EventModule._TypeModule.Reader
