"""This is an automatically generated stub for `monica_management.capnp`."""

from collections.abc import Awaitable, Callable, Iterator, Sequence
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

from mas.schema.climate.climate_capnp.types.enums import ElementEnum
from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.crop.crop_capnp.types.clients import CropClient
from mas.schema.crop.crop_capnp.types.modules import _CropInterfaceModule
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader

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

class _ILRDatesStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        sowing: DateBuilder | dict[str, Any] | None = None,
        earliestSowing: DateBuilder | dict[str, Any] | None = None,
        latestSowing: DateBuilder | dict[str, Any] | None = None,
        harvest: DateBuilder | dict[str, Any] | None = None,
        latestHarvest: DateBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> ILRDatesBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[ILRDatesReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[ILRDatesReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[ILRDatesBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> ILRDatesReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> ILRDatesReader: ...

class ILRDatesReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ILRDatesBuilder: ...

class ILRDatesBuilder(_DynamicStructBuilder):
    @property
    def sowing(self) -> DateBuilder: ...
    @sowing.setter
    def sowing(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
    @property
    def earliestSowing(self) -> DateBuilder: ...
    @earliestSowing.setter
    def earliestSowing(
        self,
        value: DateBuilder | DateReader | dict[str, Any],
    ) -> None: ...
    @property
    def latestSowing(self) -> DateBuilder: ...
    @latestSowing.setter
    def latestSowing(
        self,
        value: DateBuilder | DateReader | dict[str, Any],
    ) -> None: ...
    @property
    def harvest(self) -> DateBuilder: ...
    @harvest.setter
    def harvest(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
    @property
    def latestHarvest(self) -> DateBuilder: ...
    @latestHarvest.setter
    def latestHarvest(
        self,
        value: DateBuilder | DateReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["sowing"],
        size: int | None = None,
    ) -> DateBuilder: ...
    @overload
    def init(
        self,
        field: Literal["earliestSowing"],
        size: int | None = None,
    ) -> DateBuilder: ...
    @overload
    def init(
        self,
        field: Literal["latestSowing"],
        size: int | None = None,
    ) -> DateBuilder: ...
    @overload
    def init(
        self,
        field: Literal["harvest"],
        size: int | None = None,
    ) -> DateBuilder: ...
    @overload
    def init(
        self,
        field: Literal["latestHarvest"],
        size: int | None = None,
    ) -> DateBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> ILRDatesReader: ...

ILRDates: _ILRDatesStructModule

class _EventTypeEnumModule:
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

class _PlantOrganEnumModule:
    root: int
    leaf: int
    shoot: int
    fruit: int
    strukt: int
    sugar: int

class TypeReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> TypeBuilder: ...

class TypeBuilder(_DynamicStructBuilder):
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

class EventAtReader(_DynamicStructReader):
    @property
    def date(self) -> DateReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> EventAtBuilder: ...

class EventAtBuilder(_DynamicStructBuilder):
    @property
    def date(self) -> DateBuilder: ...
    @date.setter
    def date(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
    @override
    def init(self, field: Literal["date"], size: int | None = None) -> DateBuilder: ...
    @override
    def as_reader(self) -> EventAtReader: ...

class EventBetweenReader(_DynamicStructReader):
    @property
    def earliest(self) -> DateReader: ...
    @property
    def latest(self) -> DateReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> EventBetweenBuilder: ...

class EventBetweenBuilder(_DynamicStructBuilder):
    @property
    def earliest(self) -> DateBuilder: ...
    @earliest.setter
    def earliest(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
    @property
    def latest(self) -> DateBuilder: ...
    @latest.setter
    def latest(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["earliest"],
        size: int | None = None,
    ) -> DateBuilder: ...
    @overload
    def init(
        self,
        field: Literal["latest"],
        size: int | None = None,
    ) -> DateBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> EventBetweenReader: ...

class EventAfterReader(_DynamicStructReader):
    @property
    def event(self) -> TypeReader: ...
    @property
    def days(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> EventAfterBuilder: ...

class EventAfterBuilder(_DynamicStructBuilder):
    @property
    def event(self) -> TypeBuilder: ...
    @event.setter
    def event(self, value: TypeBuilder | TypeReader | dict[str, Any]) -> None: ...
    @property
    def days(self) -> int: ...
    @days.setter
    def days(self, value: int) -> None: ...
    @override
    def init(self, field: Literal["event"], size: int | None = None) -> TypeBuilder: ...
    @override
    def as_reader(self) -> EventAfterReader: ...

class _EventStructModule(_StructModule):
    class _ExternalTypeEnumModule:
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

    ExternalType: _ExternalTypeEnumModule
    class _PhenoStageEnumModule:
        emergence: int
        flowering: int
        anthesis: int
        maturity: int

    PhenoStage: _PhenoStageEnumModule
    class _TypeStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            external: EventExternalTypeEnum | None = None,
            internal: EventPhenoStageEnum | None = None,
            **kwargs: object,
        ) -> TypeBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[TypeReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[TypeReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[TypeBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> TypeReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> TypeReader: ...

    Type: _TypeStructModule
    class _EventAtStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            date: DateBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> EventAtBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[EventAtReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[EventAtReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[EventAtBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> EventAtReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> EventAtReader: ...

    EventAt: _EventAtStructModule
    class _EventBetweenStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            earliest: DateBuilder | dict[str, Any] | None = None,
            latest: DateBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> EventBetweenBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[EventBetweenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[EventBetweenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[EventBetweenBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> EventBetweenReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> EventBetweenReader: ...

    EventBetween: _EventBetweenStructModule
    class _EventAfterStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            event: TypeBuilder | dict[str, Any] | None = None,
            days: int | None = None,
            **kwargs: object,
        ) -> EventAfterBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[EventAfterReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[EventAfterReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[EventAfterBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> EventAfterReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> EventAfterReader: ...

    EventAfter: _EventAfterStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        type: EventExternalTypeEnum | None = None,
        info: IdInformationBuilder | dict[str, Any] | None = None,
        at: EventAtBuilder | dict[str, Any] | None = None,
        between: EventBetweenBuilder | dict[str, Any] | None = None,
        after: EventAfterBuilder | dict[str, Any] | None = None,
        params: AnyPointer | None = None,
        runAtStartOfDay: bool | None = None,
        **kwargs: object,
    ) -> EventBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[EventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[EventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[EventBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> EventReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> EventReader: ...

class EventReader(_DynamicStructReader):
    @property
    def type(self) -> EventExternalTypeEnum: ...
    @property
    def info(self) -> IdInformationReader: ...
    @property
    def at(self) -> EventAtReader: ...
    @property
    def between(self) -> EventBetweenReader: ...
    @property
    def after(self) -> EventAfterReader: ...
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> EventBuilder: ...

class EventBuilder(_DynamicStructBuilder):
    @property
    def type(self) -> EventExternalTypeEnum: ...
    @type.setter
    def type(self, value: EventExternalTypeEnum) -> None: ...
    @property
    def info(self) -> IdInformationBuilder: ...
    @info.setter
    def info(
        self,
        value: IdInformationBuilder | IdInformationReader | dict[str, Any],
    ) -> None: ...
    @property
    def at(self) -> EventAtBuilder: ...
    @at.setter
    def at(self, value: EventAtBuilder | EventAtReader | dict[str, Any]) -> None: ...
    @property
    def between(self) -> EventBetweenBuilder: ...
    @between.setter
    def between(
        self,
        value: EventBetweenBuilder | EventBetweenReader | dict[str, Any],
    ) -> None: ...
    @property
    def after(self) -> EventAfterBuilder: ...
    @after.setter
    def after(
        self,
        value: EventAfterBuilder | EventAfterReader | dict[str, Any],
    ) -> None: ...
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
    @override
    @overload
    def init(
        self,
        field: Literal["info"],
        size: int | None = None,
    ) -> IdInformationBuilder: ...
    @overload
    def init(self, field: Literal["at"], size: int | None = None) -> EventAtBuilder: ...
    @overload
    def init(
        self,
        field: Literal["between"],
        size: int | None = None,
    ) -> EventBetweenBuilder: ...
    @overload
    def init(
        self,
        field: Literal["after"],
        size: int | None = None,
    ) -> EventAfterBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> EventReader: ...

Event: _EventStructModule

class KVReader(_DynamicStructReader):
    @property
    def key(self) -> ElementEnum: ...
    @property
    def value(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> KVBuilder: ...

class KVBuilder(_DynamicStructBuilder):
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

class _KVList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> KVReader: ...
        @override
        def __iter__(self) -> Iterator[KVReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> KVBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: KVReader | KVBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[KVBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> KVBuilder: ...

class DailyWeatherReader(_DynamicStructReader):
    @property
    def data(self) -> KVListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> DailyWeatherBuilder: ...

class DailyWeatherBuilder(_DynamicStructBuilder):
    @property
    def data(self) -> KVListBuilder: ...
    @data.setter
    def data(self, value: KVListBuilder | KVListReader | dict[str, Any]) -> None: ...
    @override
    def init(
        self,
        field: Literal["data"],
        size: int | None = None,
    ) -> KVListBuilder: ...
    @override
    def as_reader(self) -> DailyWeatherReader: ...

class SowingReader(_DynamicStructReader):
    @property
    def cultivar(self) -> str: ...
    @property
    def plantDensity(self) -> int: ...
    @property
    def crop(self) -> CropClient: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> SowingBuilder: ...

class SowingBuilder(_DynamicStructBuilder):
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
    def crop(self, value: CropClient | _CropInterfaceModule.Server) -> None: ...
    @override
    def as_reader(self) -> SowingReader: ...

class AvgSoilTempReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> AvgSoilTempBuilder: ...

class AvgSoilTempBuilder(_DynamicStructBuilder):
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

class AutomaticSowingReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> AutomaticSowingBuilder: ...

class AutomaticSowingBuilder(_DynamicStructBuilder):
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
        self,
        value: AvgSoilTempBuilder | AvgSoilTempReader | dict[str, Any],
    ) -> None: ...
    @property
    def sowing(self) -> SowingBuilder: ...
    @sowing.setter
    def sowing(self, value: SowingBuilder | SowingReader | dict[str, Any]) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["avgSoilTemp"],
        size: int | None = None,
    ) -> AvgSoilTempBuilder: ...
    @overload
    def init(
        self,
        field: Literal["sowing"],
        size: int | None = None,
    ) -> SowingBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> AutomaticSowingReader: ...

class OptCarbonMgmtDataReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> OptCarbonMgmtDataBuilder: ...

class OptCarbonMgmtDataBuilder(_DynamicStructBuilder):
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

class HarvestReader(_DynamicStructReader):
    @property
    def exported(self) -> bool: ...
    @property
    def optCarbMgmtData(self) -> OptCarbonMgmtDataReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> HarvestBuilder: ...

class HarvestBuilder(_DynamicStructBuilder):
    @property
    def exported(self) -> bool: ...
    @exported.setter
    def exported(self, value: bool) -> None: ...
    @property
    def optCarbMgmtData(self) -> OptCarbonMgmtDataBuilder: ...
    @optCarbMgmtData.setter
    def optCarbMgmtData(
        self,
        value: OptCarbonMgmtDataBuilder | OptCarbonMgmtDataReader | dict[str, Any],
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["optCarbMgmtData"],
        size: int | None = None,
    ) -> OptCarbonMgmtDataBuilder: ...
    @override
    def as_reader(self) -> HarvestReader: ...

class AutomaticHarvestReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> AutomaticHarvestBuilder: ...

class AutomaticHarvestBuilder(_DynamicStructBuilder):
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
        self,
        value: HarvestBuilder | HarvestReader | dict[str, Any],
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["harvest"],
        size: int | None = None,
    ) -> HarvestBuilder: ...
    @override
    def as_reader(self) -> AutomaticHarvestReader: ...

class SpecReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> SpecBuilder: ...

class SpecBuilder(_DynamicStructBuilder):
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

class _SpecList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> SpecReader: ...
        @override
        def __iter__(self) -> Iterator[SpecReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> SpecBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: SpecReader | SpecBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[SpecBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> SpecBuilder: ...

class CuttingReader(_DynamicStructReader):
    @property
    def cuttingSpec(self) -> SpecListReader: ...
    @property
    def cutMaxAssimilationRatePercentage(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> CuttingBuilder: ...

class CuttingBuilder(_DynamicStructBuilder):
    @property
    def cuttingSpec(self) -> SpecListBuilder: ...
    @cuttingSpec.setter
    def cuttingSpec(
        self,
        value: SpecListBuilder | SpecListReader | dict[str, Any],
    ) -> None: ...
    @property
    def cutMaxAssimilationRatePercentage(self) -> float: ...
    @cutMaxAssimilationRatePercentage.setter
    def cutMaxAssimilationRatePercentage(self, value: float) -> None: ...
    @override
    def init(
        self,
        field: Literal["cuttingSpec"],
        size: int | None = None,
    ) -> SpecListBuilder: ...
    @override
    def as_reader(self) -> CuttingReader: ...

class ParamsMineralFertilizationParametersReader(_DynamicStructReader):
    @property
    def id(self) -> str: ...
    @property
    def name(self) -> str: ...
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ParamsMineralFertilizationParametersBuilder: ...

class ParamsMineralFertilizationParametersBuilder(_DynamicStructBuilder):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> None: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
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
    def as_reader(self) -> ParamsMineralFertilizationParametersReader: ...

class MineralFertilizationReader(_DynamicStructReader):
    @property
    def partition(
        self,
    ) -> _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Reader: ...
    @property
    def amount(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> MineralFertilizationBuilder: ...

class MineralFertilizationBuilder(_DynamicStructBuilder):
    @property
    def partition(
        self,
    ) -> _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder: ...
    @partition.setter
    def partition(
        self,
        value: _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder
        | _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Reader
        | dict[str, Any],
    ) -> None: ...
    @property
    def amount(self) -> float: ...
    @amount.setter
    def amount(self, value: float) -> None: ...
    @override
    def init(
        self,
        field: Literal["partition"],
        size: int | None = None,
    ) -> _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder: ...
    @override
    def as_reader(self) -> MineralFertilizationReader: ...

class NDemandFertilizationReader(_DynamicStructReader):
    @property
    def nDemand(self) -> float: ...
    @property
    def partition(
        self,
    ) -> _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Reader: ...
    @property
    def depth(self) -> float: ...
    @property
    def stage(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> NDemandFertilizationBuilder: ...

class NDemandFertilizationBuilder(_DynamicStructBuilder):
    @property
    def nDemand(self) -> float: ...
    @nDemand.setter
    def nDemand(self, value: float) -> None: ...
    @property
    def partition(
        self,
    ) -> _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder: ...
    @partition.setter
    def partition(
        self,
        value: _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder
        | _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Reader
        | dict[str, Any],
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
    def init(
        self,
        field: Literal["partition"],
        size: int | None = None,
    ) -> _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder: ...
    @override
    def as_reader(self) -> NDemandFertilizationReader: ...

class OrganicMatterParametersReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> OrganicMatterParametersBuilder: ...

class OrganicMatterParametersBuilder(_DynamicStructBuilder):
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

class ParamsOrganicFertilizationParametersReader(_DynamicStructReader):
    @property
    def params(self) -> OrganicMatterParametersReader: ...
    @property
    def id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ParamsOrganicFertilizationParametersBuilder: ...

class ParamsOrganicFertilizationParametersBuilder(_DynamicStructBuilder):
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
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @override
    def init(
        self,
        field: Literal["params"],
        size: int | None = None,
    ) -> OrganicMatterParametersBuilder: ...
    @override
    def as_reader(self) -> ParamsOrganicFertilizationParametersReader: ...

class OrganicFertilizationReader(_DynamicStructReader):
    @property
    def params(
        self,
    ) -> _ParamsStructModule._OrganicFertilizationStructModule._ParametersStructModule.Reader: ...
    @property
    def amount(self) -> float: ...
    @property
    def incorporation(self) -> bool: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> OrganicFertilizationBuilder: ...

class OrganicFertilizationBuilder(_DynamicStructBuilder):
    @property
    def params(
        self,
    ) -> _ParamsStructModule._OrganicFertilizationStructModule._ParametersStructModule.Builder: ...
    @params.setter
    def params(
        self,
        value: _ParamsStructModule._OrganicFertilizationStructModule._ParametersStructModule.Builder
        | _ParamsStructModule._OrganicFertilizationStructModule._ParametersStructModule.Reader
        | dict[str, Any],
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
    def init(
        self,
        field: Literal["params"],
        size: int | None = None,
    ) -> _ParamsStructModule._OrganicFertilizationStructModule._ParametersStructModule.Builder: ...
    @override
    def as_reader(self) -> OrganicFertilizationReader: ...

class TillageReader(_DynamicStructReader):
    @property
    def depth(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> TillageBuilder: ...

class TillageBuilder(_DynamicStructBuilder):
    @property
    def depth(self) -> float: ...
    @depth.setter
    def depth(self, value: float) -> None: ...
    @override
    def as_reader(self) -> TillageReader: ...

class ParamsIrrigationParametersReader(_DynamicStructReader):
    @property
    def nitrateConcentration(self) -> float: ...
    @property
    def sulfateConcentration(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ParamsIrrigationParametersBuilder: ...

class ParamsIrrigationParametersBuilder(_DynamicStructBuilder):
    @property
    def nitrateConcentration(self) -> float: ...
    @nitrateConcentration.setter
    def nitrateConcentration(self, value: float) -> None: ...
    @property
    def sulfateConcentration(self) -> float: ...
    @sulfateConcentration.setter
    def sulfateConcentration(self, value: float) -> None: ...
    @override
    def as_reader(self) -> ParamsIrrigationParametersReader: ...

class IrrigationReader(_DynamicStructReader):
    @property
    def amount(self) -> float: ...
    @property
    def params(
        self,
    ) -> _ParamsStructModule._IrrigationStructModule._ParametersStructModule.Reader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> IrrigationBuilder: ...

class IrrigationBuilder(_DynamicStructBuilder):
    @property
    def amount(self) -> float: ...
    @amount.setter
    def amount(self, value: float) -> None: ...
    @property
    def params(
        self,
    ) -> (
        _ParamsStructModule._IrrigationStructModule._ParametersStructModule.Builder
    ): ...
    @params.setter
    def params(
        self,
        value: _ParamsStructModule._IrrigationStructModule._ParametersStructModule.Builder
        | _ParamsStructModule._IrrigationStructModule._ParametersStructModule.Reader
        | dict[str, Any],
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["params"],
        size: int | None = None,
    ) -> (
        _ParamsStructModule._IrrigationStructModule._ParametersStructModule.Builder
    ): ...
    @override
    def as_reader(self) -> IrrigationReader: ...

class SaveStateReader(_DynamicStructReader):
    @property
    def noOfPreviousDaysSerializedClimateData(self) -> int: ...
    @property
    def asJson(self) -> bool: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> SaveStateBuilder: ...

class SaveStateBuilder(_DynamicStructBuilder):
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

class _ParamsStructModule(_StructModule):
    class _DailyWeatherStructModule(_StructModule):
        class _KVStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                key: ElementEnum | None = None,
                value: float | None = None,
                **kwargs: object,
            ) -> KVBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[KVReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[KVReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[KVBuilder]: ...
            @override
            def from_bytes_packed(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _DynamicStructReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> KVReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> KVReader: ...

        KV: _KVStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            data: KVListBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> DailyWeatherBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[DailyWeatherReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[DailyWeatherReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[DailyWeatherBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> DailyWeatherReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> DailyWeatherReader: ...

    DailyWeather: _DailyWeatherStructModule
    class _SowingStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            cultivar: str | None = None,
            plantDensity: int | None = None,
            crop: CropClient | _CropInterfaceModule.Server | None = None,
            **kwargs: object,
        ) -> SowingBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[SowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[SowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[SowingBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> SowingReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> SowingReader: ...

    Sowing: _SowingStructModule
    class _AutomaticSowingStructModule(_StructModule):
        class _AvgSoilTempStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                soilDepthForAveraging: float | None = None,
                daysInSoilTempWindow: int | None = None,
                sowingIfAboveAvgSoilTemp: float | None = None,
                **kwargs: object,
            ) -> AvgSoilTempBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[AvgSoilTempReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[AvgSoilTempReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[AvgSoilTempBuilder]: ...
            @override
            def from_bytes_packed(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _DynamicStructReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AvgSoilTempReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AvgSoilTempReader: ...

        AvgSoilTemp: _AvgSoilTempStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
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
            **kwargs: object,
        ) -> AutomaticSowingBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[AutomaticSowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[AutomaticSowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[AutomaticSowingBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AutomaticSowingReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AutomaticSowingReader: ...

    AutomaticSowing: _AutomaticSowingStructModule
    class _HarvestStructModule(_StructModule):
        class _CropUsageEnumModule:
            greenManure: int
            biomassProduction: int

        CropUsage: _CropUsageEnumModule
        class _OptCarbonMgmtDataStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                optCarbonConservation: bool | None = None,
                cropImpactOnHumusBalance: float | None = None,
                cropUsage: ParamsHarvestCropUsageEnum | None = None,
                residueHeq: float | None = None,
                organicFertilizerHeq: float | None = None,
                maxResidueRecoverFraction: float | None = None,
                **kwargs: object,
            ) -> OptCarbonMgmtDataBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[OptCarbonMgmtDataReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[OptCarbonMgmtDataReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[OptCarbonMgmtDataBuilder]: ...
            @override
            def from_bytes_packed(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _DynamicStructReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> OptCarbonMgmtDataReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> OptCarbonMgmtDataReader: ...

        OptCarbonMgmtData: _OptCarbonMgmtDataStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            exported: bool | None = None,
            optCarbMgmtData: OptCarbonMgmtDataBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> HarvestBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[HarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[HarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[HarvestBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> HarvestReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> HarvestReader: ...

    Harvest: _HarvestStructModule
    class _AutomaticHarvestStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            minPercentASW: float | None = None,
            maxPercentASW: float | None = None,
            max3dayPrecipSum: float | None = None,
            maxCurrentDayPrecipSum: float | None = None,
            harvestTime: EventPhenoStageEnum | None = None,
            harvest: HarvestBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> AutomaticHarvestBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[AutomaticHarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[AutomaticHarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[AutomaticHarvestBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AutomaticHarvestReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AutomaticHarvestReader: ...

    AutomaticHarvest: _AutomaticHarvestStructModule
    class _CuttingStructModule(_StructModule):
        class _CLEnumModule:
            cut: int
            left: int

        CL: _CLEnumModule
        class _UnitEnumModule:
            percentage: int
            biomass: int
            lai: int

        Unit: _UnitEnumModule
        class _SpecStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                organ: PlantOrganEnum | None = None,
                value: float | None = None,
                unit: ParamsCuttingUnitEnum | None = None,
                cutOrLeft: ParamsCuttingCLEnum | None = None,
                exportPercentage: float | None = None,
                **kwargs: object,
            ) -> SpecBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[SpecReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[SpecReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[SpecBuilder]: ...
            @override
            def from_bytes_packed(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _DynamicStructReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> SpecReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> SpecReader: ...

        Spec: _SpecStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            cuttingSpec: SpecListBuilder | dict[str, Any] | None = None,
            cutMaxAssimilationRatePercentage: float | None = None,
            **kwargs: object,
        ) -> CuttingBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[CuttingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[CuttingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[CuttingBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> CuttingReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> CuttingReader: ...

    Cutting: _CuttingStructModule
    class _MineralFertilizationStructModule(_StructModule):
        class _ParametersStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                id: str | None = None,
                name: str | None = None,
                carbamid: float | None = None,
                nh4: float | None = None,
                no3: float | None = None,
                **kwargs: object,
            ) -> ParamsMineralFertilizationParametersBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[ParamsMineralFertilizationParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[ParamsMineralFertilizationParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[
                ParamsMineralFertilizationParametersBuilder
            ]: ...
            @override
            def from_bytes_packed(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _DynamicStructReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> ParamsMineralFertilizationParametersReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> ParamsMineralFertilizationParametersReader: ...

        Parameters: _ParametersStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            partition: _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder
            | dict[str, Any]
            | None = None,
            amount: float | None = None,
            **kwargs: object,
        ) -> MineralFertilizationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[MineralFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[MineralFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[MineralFertilizationBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> MineralFertilizationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> MineralFertilizationReader: ...

    MineralFertilization: _MineralFertilizationStructModule
    class _NDemandFertilizationStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            nDemand: float | None = None,
            partition: _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder
            | dict[str, Any]
            | None = None,
            depth: float | None = None,
            stage: int | None = None,
            **kwargs: object,
        ) -> NDemandFertilizationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[NDemandFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[NDemandFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[NDemandFertilizationBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> NDemandFertilizationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> NDemandFertilizationReader: ...

    NDemandFertilization: _NDemandFertilizationStructModule
    class _OrganicFertilizationStructModule(_StructModule):
        class _OrganicMatterParametersStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
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
                **kwargs: object,
            ) -> OrganicMatterParametersBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[OrganicMatterParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[OrganicMatterParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[OrganicMatterParametersBuilder]: ...
            @override
            def from_bytes_packed(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _DynamicStructReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> OrganicMatterParametersReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> OrganicMatterParametersReader: ...

        OrganicMatterParameters: _OrganicMatterParametersStructModule
        class _ParametersStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                params: OrganicMatterParametersBuilder | dict[str, Any] | None = None,
                id: str | None = None,
                name: str | None = None,
                **kwargs: object,
            ) -> ParamsOrganicFertilizationParametersBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[ParamsOrganicFertilizationParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[ParamsOrganicFertilizationParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[
                ParamsOrganicFertilizationParametersBuilder
            ]: ...
            @override
            def from_bytes_packed(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _DynamicStructReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> ParamsOrganicFertilizationParametersReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> ParamsOrganicFertilizationParametersReader: ...

        Parameters: _ParametersStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            params: _ParamsStructModule._OrganicFertilizationStructModule._ParametersStructModule.Builder
            | dict[str, Any]
            | None = None,
            amount: float | None = None,
            incorporation: bool | None = None,
            **kwargs: object,
        ) -> OrganicFertilizationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[OrganicFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[OrganicFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[OrganicFertilizationBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> OrganicFertilizationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> OrganicFertilizationReader: ...

    OrganicFertilization: _OrganicFertilizationStructModule
    class _TillageStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            depth: float | None = None,
            **kwargs: object,
        ) -> TillageBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[TillageReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[TillageReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[TillageBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> TillageReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> TillageReader: ...

    Tillage: _TillageStructModule
    class _IrrigationStructModule(_StructModule):
        class _ParametersStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                nitrateConcentration: float | None = None,
                sulfateConcentration: float | None = None,
                **kwargs: object,
            ) -> ParamsIrrigationParametersBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[ParamsIrrigationParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[ParamsIrrigationParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[ParamsIrrigationParametersBuilder]: ...
            @override
            def from_bytes_packed(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _DynamicStructReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> ParamsIrrigationParametersReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> ParamsIrrigationParametersReader: ...

        Parameters: _ParametersStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            amount: float | None = None,
            params: _ParamsStructModule._IrrigationStructModule._ParametersStructModule.Builder
            | dict[str, Any]
            | None = None,
            **kwargs: object,
        ) -> IrrigationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[IrrigationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[IrrigationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[IrrigationBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> IrrigationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> IrrigationReader: ...

    Irrigation: _IrrigationStructModule
    class _SaveStateStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            noOfPreviousDaysSerializedClimateData: int | None = None,
            asJson: bool | None = None,
            **kwargs: object,
        ) -> SaveStateBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[SaveStateReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[SaveStateReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[SaveStateBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> SaveStateReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> SaveStateReader: ...

    SaveState: _SaveStateStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        **kwargs: object,
    ) -> ParamsBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[ParamsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[ParamsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[ParamsBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> ParamsReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> ParamsReader: ...

class ParamsReader(_DynamicStructReader):
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ParamsBuilder: ...

class ParamsBuilder(_DynamicStructBuilder):
    @override
    def as_reader(self) -> ParamsReader: ...

Params: _ParamsStructModule

class _ServiceInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> ServiceClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def managementAt(
            self,
            lat: float,
            lon: float,
            _context: ManagementatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            EventListBuilder
            | EventListReader
            | Sequence[Any]
            | ManagementatResultTuple
            | None
        ]: ...
        def managementAt_context(
            self,
            context: ManagementatCallContext,
        ) -> Awaitable[None]: ...

class ManagementatRequest(Protocol):
    lat: float
    lon: float
    def send(self) -> ManagementatResult: ...

class _EventList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> EventReader: ...
        @override
        def __iter__(self) -> Iterator[EventReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> EventBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: EventReader | EventBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[EventBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> EventBuilder: ...

class ManagementatResult(Awaitable[ManagementatResult], Protocol):
    mgmt: EventListReader

class ManagementatServerResult(_DynamicStructBuilder):
    @property
    def mgmt(self) -> EventListBuilder: ...
    @mgmt.setter
    def mgmt(
        self,
        value: EventListBuilder | EventListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["mgmt"],
        size: int | None = None,
    ) -> EventListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ManagementatCallContext(Protocol):
    params: LatLonCoordReader
    @property
    def results(self) -> ManagementatServerResult: ...

class ManagementatResultTuple(NamedTuple):
    mgmt: EventListBuilder | EventListReader | Sequence[Any]

class ServiceClient(IdentifiableClient):
    def managementAt(
        self,
        lat: float | None = None,
        lon: float | None = None,
    ) -> ManagementatResult: ...
    def managementAt_request(
        self,
        lat: float | None = None,
        lon: float | None = None,
    ) -> ManagementatRequest: ...

Service: _ServiceInterfaceModule

# Top-level type aliases for use in type annotations
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
type EventListBuilder = _EventList.Builder
type EventListReader = _EventList.Reader
type EventPhenoStageEnum = (
    int | Literal["emergence", "flowering", "anthesis", "maturity"]
)
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
type KVListBuilder = _KVList.Builder
type KVListReader = _KVList.Reader
type ParamsCuttingCLEnum = int | Literal["cut", "left"]
type ParamsCuttingUnitEnum = int | Literal["percentage", "biomass", "lai"]
type ParamsHarvestCropUsageEnum = int | Literal["greenManure", "biomassProduction"]
type PlantOrganEnum = int | Literal["root", "leaf", "shoot", "fruit", "strukt", "sugar"]
ServiceServer = _ServiceInterfaceModule.Server
type SpecListBuilder = _SpecList.Builder
type SpecListReader = _SpecList.Reader
