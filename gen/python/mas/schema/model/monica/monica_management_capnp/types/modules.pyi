"""Module helper types for `monica_management.capnp`."""

from collections.abc import Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

from mas.schema.climate.climate_capnp.types.enums import ElementEnum
from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.crop.crop_capnp.types.clients import CropClient
from mas.schema.crop.crop_capnp.types.modules import _CropInterfaceModule

from . import _all as _all

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
    ) -> _all.ILRDatesBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.ILRDatesReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.ILRDatesReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.ILRDatesBuilder]: ...
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
    ) -> _all.ILRDatesReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.ILRDatesReader: ...

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
            external: _all.EventExternalTypeEnum | None = None,
            internal: _all.EventPhenoStageEnum | None = None,
            **kwargs: object,
        ) -> _all.TypeBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.TypeReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.TypeReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.TypeBuilder]: ...
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
        ) -> _all.TypeReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.TypeReader: ...

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
        ) -> _all.EventAtBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.EventAtReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.EventAtReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.EventAtBuilder]: ...
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
        ) -> _all.EventAtReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.EventAtReader: ...

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
        ) -> _all.EventBetweenBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.EventBetweenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.EventBetweenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.EventBetweenBuilder]: ...
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
        ) -> _all.EventBetweenReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.EventBetweenReader: ...

    EventBetween: _EventBetweenStructModule
    class _EventAfterStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            event: _all.TypeBuilder | dict[str, Any] | None = None,
            days: int | None = None,
            **kwargs: object,
        ) -> _all.EventAfterBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.EventAfterReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.EventAfterReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.EventAfterBuilder]: ...
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
        ) -> _all.EventAfterReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.EventAfterReader: ...

    EventAfter: _EventAfterStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        type: _all.EventExternalTypeEnum | None = None,
        info: IdInformationBuilder | dict[str, Any] | None = None,
        at: _all.EventAtBuilder | dict[str, Any] | None = None,
        between: _all.EventBetweenBuilder | dict[str, Any] | None = None,
        after: _all.EventAfterBuilder | dict[str, Any] | None = None,
        params: _all.AnyPointer | None = None,
        runAtStartOfDay: bool | None = None,
        **kwargs: object,
    ) -> _all.EventBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.EventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.EventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.EventBuilder]: ...
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
    ) -> _all.EventReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.EventReader: ...

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
            ) -> _all.KVBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[_all.KVReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[_all.KVReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[_all.KVBuilder]: ...
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
            ) -> _all.KVReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _all.KVReader: ...

        KV: _KVStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            data: _all.KVListBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> _all.DailyWeatherBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.DailyWeatherReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.DailyWeatherReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.DailyWeatherBuilder]: ...
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
        ) -> _all.DailyWeatherReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.DailyWeatherReader: ...

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
        ) -> _all.SowingBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.SowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.SowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.SowingBuilder]: ...
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
        ) -> _all.SowingReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.SowingReader: ...

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
            ) -> _all.AvgSoilTempBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[_all.AvgSoilTempReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[_all.AvgSoilTempReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[_all.AvgSoilTempBuilder]: ...
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
            ) -> _all.AvgSoilTempReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _all.AvgSoilTempReader: ...

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
            avgSoilTemp: _all.AvgSoilTempBuilder | dict[str, Any] | None = None,
            sowing: _all.SowingBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> _all.AutomaticSowingBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.AutomaticSowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.AutomaticSowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.AutomaticSowingBuilder]: ...
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
        ) -> _all.AutomaticSowingReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.AutomaticSowingReader: ...

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
                cropUsage: _all.ParamsHarvestCropUsageEnum | None = None,
                residueHeq: float | None = None,
                organicFertilizerHeq: float | None = None,
                maxResidueRecoverFraction: float | None = None,
                **kwargs: object,
            ) -> _all.OptCarbonMgmtDataBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[_all.OptCarbonMgmtDataReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[_all.OptCarbonMgmtDataReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[_all.OptCarbonMgmtDataBuilder]: ...
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
            ) -> _all.OptCarbonMgmtDataReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _all.OptCarbonMgmtDataReader: ...

        OptCarbonMgmtData: _OptCarbonMgmtDataStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            exported: bool | None = None,
            optCarbMgmtData: _all.OptCarbonMgmtDataBuilder
            | dict[str, Any]
            | None = None,
            **kwargs: object,
        ) -> _all.HarvestBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.HarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.HarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.HarvestBuilder]: ...
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
        ) -> _all.HarvestReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.HarvestReader: ...

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
            harvestTime: _all.EventPhenoStageEnum | None = None,
            harvest: _all.HarvestBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> _all.AutomaticHarvestBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.AutomaticHarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.AutomaticHarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.AutomaticHarvestBuilder]: ...
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
        ) -> _all.AutomaticHarvestReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.AutomaticHarvestReader: ...

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
                organ: _all.PlantOrganEnum | None = None,
                value: float | None = None,
                unit: _all.ParamsCuttingUnitEnum | None = None,
                cutOrLeft: _all.ParamsCuttingCLEnum | None = None,
                exportPercentage: float | None = None,
                **kwargs: object,
            ) -> _all.SpecBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[_all.SpecReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[_all.SpecReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[_all.SpecBuilder]: ...
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
            ) -> _all.SpecReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _all.SpecReader: ...

        Spec: _SpecStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            cuttingSpec: _all.SpecListBuilder | dict[str, Any] | None = None,
            cutMaxAssimilationRatePercentage: float | None = None,
            **kwargs: object,
        ) -> _all.CuttingBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.CuttingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.CuttingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.CuttingBuilder]: ...
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
        ) -> _all.CuttingReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.CuttingReader: ...

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
            ) -> _all.ParamsMineralFertilizationParametersBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[
                _all.ParamsMineralFertilizationParametersReader
            ]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[
                _all.ParamsMineralFertilizationParametersReader
            ]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[
                _all.ParamsMineralFertilizationParametersBuilder
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
            ) -> _all.ParamsMineralFertilizationParametersReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _all.ParamsMineralFertilizationParametersReader: ...

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
        ) -> _all.MineralFertilizationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.MineralFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.MineralFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.MineralFertilizationBuilder]: ...
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
        ) -> _all.MineralFertilizationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.MineralFertilizationReader: ...

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
        ) -> _all.NDemandFertilizationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.NDemandFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.NDemandFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.NDemandFertilizationBuilder]: ...
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
        ) -> _all.NDemandFertilizationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.NDemandFertilizationReader: ...

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
            ) -> _all.OrganicMatterParametersBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[_all.OrganicMatterParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[_all.OrganicMatterParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[_all.OrganicMatterParametersBuilder]: ...
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
            ) -> _all.OrganicMatterParametersReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _all.OrganicMatterParametersReader: ...

        OrganicMatterParameters: _OrganicMatterParametersStructModule
        class _ParametersStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                params: _all.OrganicMatterParametersBuilder
                | dict[str, Any]
                | None = None,
                id: str | None = None,
                name: str | None = None,
                **kwargs: object,
            ) -> _all.ParamsOrganicFertilizationParametersBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[
                _all.ParamsOrganicFertilizationParametersReader
            ]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[
                _all.ParamsOrganicFertilizationParametersReader
            ]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[
                _all.ParamsOrganicFertilizationParametersBuilder
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
            ) -> _all.ParamsOrganicFertilizationParametersReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _all.ParamsOrganicFertilizationParametersReader: ...

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
        ) -> _all.OrganicFertilizationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.OrganicFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.OrganicFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.OrganicFertilizationBuilder]: ...
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
        ) -> _all.OrganicFertilizationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.OrganicFertilizationReader: ...

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
        ) -> _all.TillageBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.TillageReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.TillageReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.TillageBuilder]: ...
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
        ) -> _all.TillageReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.TillageReader: ...

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
            ) -> _all.ParamsIrrigationParametersBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[_all.ParamsIrrigationParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[_all.ParamsIrrigationParametersReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[_all.ParamsIrrigationParametersBuilder]: ...
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
            ) -> _all.ParamsIrrigationParametersReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _all.ParamsIrrigationParametersReader: ...

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
        ) -> _all.IrrigationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.IrrigationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.IrrigationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.IrrigationBuilder]: ...
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
        ) -> _all.IrrigationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.IrrigationReader: ...

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
        ) -> _all.SaveStateBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.SaveStateReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.SaveStateReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.SaveStateBuilder]: ...
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
        ) -> _all.SaveStateReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.SaveStateReader: ...

    SaveState: _SaveStateStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        **kwargs: object,
    ) -> _all.ParamsBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.ParamsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.ParamsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.ParamsBuilder]: ...
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
    ) -> _all.ParamsReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.ParamsReader: ...

class _ServiceInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.ServiceClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def managementAt(
            self,
            lat: float,
            lon: float,
            _context: _all.ManagementatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.EventListBuilder
            | _all.EventListReader
            | Sequence[Any]
            | _all.ManagementatResultTuple
            | None
        ]: ...
        def managementAt_context(
            self,
            context: _all.ManagementatCallContext,
        ) -> Awaitable[None]: ...
