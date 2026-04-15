"""This is an automatically generated stub for `management.capnp`."""

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

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.crop.crop_capnp.types.clients import CropClient
from mas.schema.crop.crop_capnp.types.modules import _CropInterfaceModule
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)
from mas.schema.registry.registry_capnp.types.clients import RegistryClient
from mas.schema.registry.registry_capnp.types.modules import _RegistryInterfaceModule

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

class _FertilizerInterfaceModule(
    _IdentifiableInterfaceModule,
    _PersistentInterfaceModule,
):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> FertilizerClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def nutrients(
            self,
            _context: NutrientsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            NutrientListBuilder
            | NutrientListReader
            | Sequence[Any]
            | NutrientsResultTuple
            | None
        ]: ...
        def nutrients_context(
            self,
            context: NutrientsCallContext,
        ) -> Awaitable[None]: ...
        def parameters(
            self,
            _context: ParametersCallContext,
            **kwargs: object,
        ) -> Awaitable[AnyPointer | ParametersResultTuple | None]: ...
        def parameters_context(
            self,
            context: ParametersCallContext,
        ) -> Awaitable[None]: ...

class NutrientsRequest(Protocol):
    def send(self) -> NutrientsResult: ...

class _NutrientStructModule(_StructModule):
    class _NameEnumModule:
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

    Name: _NameEnumModule
    class _UnitEnumModule:
        none: int
        fraction: int
        percent: int

    Unit: _UnitEnumModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        nutrient: NutrientNameEnum | None = None,
        value: float | None = None,
        unit: NutrientUnitEnum | None = None,
        **kwargs: object,
    ) -> NutrientBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[NutrientReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[NutrientReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[NutrientBuilder]: ...
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
    ) -> NutrientReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> NutrientReader: ...

class NutrientReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> NutrientBuilder: ...

class NutrientBuilder(_DynamicStructBuilder):
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

Nutrient: _NutrientStructModule

class _NutrientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> NutrientReader: ...
        @override
        def __iter__(self) -> Iterator[NutrientReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> NutrientBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: NutrientReader | NutrientBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[NutrientBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> NutrientBuilder: ...

class NutrientsResult(Awaitable[NutrientsResult], Protocol):
    nutrients: NutrientListReader

class NutrientsServerResult(_DynamicStructBuilder):
    @property
    def nutrients(self) -> NutrientListBuilder: ...
    @nutrients.setter
    def nutrients(
        self,
        value: NutrientListBuilder | NutrientListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["nutrients"],
        size: int | None = None,
    ) -> NutrientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class NutrientsParams(Protocol): ...

class NutrientsCallContext(Protocol):
    params: NutrientsParams
    @property
    def results(self) -> NutrientsServerResult: ...

class NutrientsResultTuple(NamedTuple):
    nutrients: NutrientListBuilder | NutrientListReader | Sequence[Any]

class ParametersRequest(Protocol):
    def send(self) -> ParametersResult: ...

class ParametersResult(Awaitable[ParametersResult], Protocol):
    params: _DynamicObjectReader

class ParametersServerResult(_DynamicStructBuilder):
    @property
    def params(self) -> AnyPointer: ...
    @params.setter
    def params(self, value: AnyPointer) -> None: ...

class ParametersParams(Protocol): ...

class ParametersCallContext(Protocol):
    params: ParametersParams
    @property
    def results(self) -> ParametersServerResult: ...

class ParametersResultTuple(NamedTuple):
    params: AnyPointer

class FertilizerClient(IdentifiableClient, PersistentClient):
    def nutrients(self) -> NutrientsResult: ...
    def parameters(self) -> ParametersResult: ...
    def nutrients_request(self) -> NutrientsRequest: ...
    def parameters_request(self) -> ParametersRequest: ...

Fertilizer: _FertilizerInterfaceModule

class MineralFertilizationReader(_DynamicStructReader):
    @property
    def fertilizer(self) -> FertilizerClient: ...
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
    def fertilizer(self) -> FertilizerClient: ...
    @fertilizer.setter
    def fertilizer(
        self,
        value: FertilizerClient | _FertilizerInterfaceModule.Server,
    ) -> None: ...
    @property
    def amount(self) -> float: ...
    @amount.setter
    def amount(self, value: float) -> None: ...
    @override
    def as_reader(self) -> MineralFertilizationReader: ...

class NDemandFertilizationReader(_DynamicStructReader):
    @property
    def nDemand(self) -> float: ...
    @property
    def fertilizer(self) -> FertilizerClient: ...
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
    def fertilizer(self) -> FertilizerClient: ...
    @fertilizer.setter
    def fertilizer(
        self,
        value: FertilizerClient | _FertilizerInterfaceModule.Server,
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

class OrganicFertilizationReader(_DynamicStructReader):
    @property
    def fertilizer(self) -> FertilizerClient: ...
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
    def fertilizer(self) -> FertilizerClient: ...
    @fertilizer.setter
    def fertilizer(
        self,
        value: FertilizerClient | _FertilizerInterfaceModule.Server,
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

class IrrigationReader(_DynamicStructReader):
    @property
    def amount(self) -> float: ...
    @property
    def nutrientConcentrations(self) -> NutrientListReader: ...
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
    def nutrientConcentrations(self) -> NutrientListBuilder: ...
    @nutrientConcentrations.setter
    def nutrientConcentrations(
        self,
        value: NutrientListBuilder | NutrientListReader | dict[str, Any],
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["nutrientConcentrations"],
        size: int | None = None,
    ) -> NutrientListBuilder: ...
    @override
    def as_reader(self) -> IrrigationReader: ...

class _ParamsStructModule(_StructModule):
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
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            fertilizer: FertilizerClient
            | _FertilizerInterfaceModule.Server
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
            fertilizer: FertilizerClient
            | _FertilizerInterfaceModule.Server
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
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            fertilizer: FertilizerClient
            | _FertilizerInterfaceModule.Server
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
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            amount: float | None = None,
            nutrientConcentrations: NutrientListBuilder | dict[str, Any] | None = None,
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

class _FertilizerServiceInterfaceModule(_RegistryInterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> FertilizerServiceClient: ...
    class Server(_RegistryInterfaceModule.Server): ...

class FertilizerServiceClient(RegistryClient): ...

FertilizerService: _FertilizerServiceInterfaceModule

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
FertilizerServer = _FertilizerInterfaceModule.Server
FertilizerServiceServer = _FertilizerServiceInterfaceModule.Server
type NutrientListBuilder = _NutrientList.Builder
type NutrientListReader = _NutrientList.Reader
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
type NutrientUnitEnum = int | Literal["none", "fraction", "percent"]
type ParamsCuttingCLEnum = int | Literal["cut", "left"]
type ParamsCuttingUnitEnum = int | Literal["percentage", "biomass", "lai"]
type ParamsHarvestCropUsageEnum = int | Literal["greenManure", "biomassProduction"]
type PlantOrganEnum = int | Literal["root", "leaf", "shoot", "fruit", "strukt", "sugar"]
ServiceServer = _ServiceInterfaceModule.Server
type SpecListBuilder = _SpecList.Builder
type SpecListReader = _SpecList.Reader
