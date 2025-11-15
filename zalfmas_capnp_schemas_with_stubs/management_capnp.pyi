"""This is an automatically generated stub for `management.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, MutableSequence, Sequence
from enum import Enum
from typing import Any, Literal, NamedTuple, Protocol, TypeAlias, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _Request,
    _StructModule,
)

from .common_capnp import (
    Identifiable,
    IdentifiableClient,
    _IdentifiableModule,
    _IdInformationModule,
)
from .crop_capnp import Crop, CropClient, _CropModule
from .date_capnp import _DateModule
from .persistence_capnp import Persistent, PersistentClient, _PersistentModule
from .registry_capnp import Registry, RegistryClient, _RegistryModule

class _EventTypeModule(Enum):
    sowing = 0
    automaticSowing = 1
    harvest = 2
    automaticHarvest = 3
    irrigation = 4
    tillage = 5
    organicFertilization = 6
    mineralFertilization = 7
    nDemandFertilization = 8
    cutting = 9
    setValue = 10
    saveState = 11

EventType: TypeAlias = _EventTypeModule

class _PlantOrganModule(Enum):
    root = 0
    leaf = 1
    shoot = 2
    fruit = 3
    strukt = 4
    sugar = 5

PlantOrgan: TypeAlias = _PlantOrganModule

class _EventModule(_StructModule):
    class _ExternalTypeModule(Enum):
        sowing = 0
        automaticSowing = 1
        harvest = 2
        automaticHarvest = 3
        irrigation = 4
        tillage = 5
        organicFertilization = 6
        mineralFertilization = 7
        nDemandFertilization = 8
        cutting = 9

    ExternalType: TypeAlias = _ExternalTypeModule
    class _PhenoStageModule(Enum):
        emergence = 0
        flowering = 1
        anthesis = 2
        maturity = 3

    PhenoStage: TypeAlias = _PhenoStageModule
    class _TypeModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def external(self) -> _EventModule._ExternalTypeModule: ...
            @property
            def internal(self) -> _EventModule._PhenoStageModule: ...
            @override
            def which(self) -> Literal["external", "internal"]: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _EventModule._TypeModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def external(self) -> _EventModule._ExternalTypeModule: ...
            @external.setter
            def external(self, value: _EventModule._ExternalTypeModule | Literal["sowing", "automaticSowing", "harvest", "automaticHarvest", "irrigation", "tillage", "organicFertilization", "mineralFertilization", "nDemandFertilization", "cutting"]) -> None: ...
            @property
            def internal(self) -> _EventModule._PhenoStageModule: ...
            @internal.setter
            def internal(self, value: _EventModule._PhenoStageModule | Literal["emergence", "flowering", "anthesis", "maturity"]) -> None: ...
            @override
            def which(self) -> Literal["external", "internal"]: ...
            @override
            def as_reader(self) -> _EventModule._TypeModule.Reader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            external: _EventModule._ExternalTypeModule | Literal["sowing", "automaticSowing", "harvest", "automaticHarvest", "irrigation", "tillage", "organicFertilization", "mineralFertilization", "nDemandFertilization", "cutting"] | None = None,
            internal: _EventModule._PhenoStageModule | Literal["emergence", "flowering", "anthesis", "maturity"] | None = None,
        ) -> _EventModule._TypeModule.Builder: ...

    TypeReader: TypeAlias = _TypeModule.Reader
    TypeBuilder: TypeAlias = _TypeModule.Builder
    Type: _TypeModule
    class _AtModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def date(self) -> _DateModule.Reader: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _EventModule._AtModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def date(self) -> _DateModule.Builder: ...
            @date.setter
            def date(self, value: _DateModule.Builder | _DateModule.Reader | dict[str, Any]) -> None: ...
            def init(self, field: Literal["date"], size: int | None = None) -> _DateModule.Builder: ...
            @override
            def as_reader(self) -> _EventModule._AtModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, date: _DateModule.Builder | dict[str, Any] | None = None) -> _EventModule._AtModule.Builder: ...

    AtReader: TypeAlias = _AtModule.Reader
    AtBuilder: TypeAlias = _AtModule.Builder
    At: _AtModule
    class _BetweenModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def earliest(self) -> _DateModule.Reader: ...
            @property
            def latest(self) -> _DateModule.Reader: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _EventModule._BetweenModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def earliest(self) -> _DateModule.Builder: ...
            @earliest.setter
            def earliest(self, value: _DateModule.Builder | _DateModule.Reader | dict[str, Any]) -> None: ...
            @property
            def latest(self) -> _DateModule.Builder: ...
            @latest.setter
            def latest(self, value: _DateModule.Builder | _DateModule.Reader | dict[str, Any]) -> None: ...
            @overload
            def init(self, field: Literal["earliest"], size: int | None = None) -> _DateModule.Builder: ...
            @overload
            def init(self, field: Literal["latest"], size: int | None = None) -> _DateModule.Builder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> _EventModule._BetweenModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, earliest: _DateModule.Builder | dict[str, Any] | None = None, latest: _DateModule.Builder | dict[str, Any] | None = None) -> _EventModule._BetweenModule.Builder: ...

    BetweenReader: TypeAlias = _BetweenModule.Reader
    BetweenBuilder: TypeAlias = _BetweenModule.Builder
    Between: _BetweenModule
    class _AfterModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def event(self) -> _EventModule._TypeModule.Reader: ...
            @property
            def days(self) -> int: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _EventModule._AfterModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def event(self) -> _EventModule._TypeModule.Builder: ...
            @event.setter
            def event(self, value: _EventModule._TypeModule.Builder | _EventModule._TypeModule.Reader | dict[str, Any]) -> None: ...
            @property
            def days(self) -> int: ...
            @days.setter
            def days(self, value: int) -> None: ...
            def init(self, field: Literal["event"], size: int | None = None) -> _EventModule._TypeModule.Builder: ...
            @override
            def as_reader(self) -> _EventModule._AfterModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, event: _EventModule._TypeModule.Builder | dict[str, Any] | None = None, days: int | None = None) -> _EventModule._AfterModule.Builder: ...

    AfterReader: TypeAlias = _AfterModule.Reader
    AfterBuilder: TypeAlias = _AfterModule.Builder
    After: _AfterModule
    class Reader(_DynamicStructReader):
        @property
        def type(self) -> _EventModule._ExternalTypeModule: ...
        @property
        def info(self) -> _IdInformationModule.Reader: ...
        @property
        def at(self) -> _EventModule._AtModule.Reader: ...
        @property
        def between(self) -> _EventModule._BetweenModule.Reader: ...
        @property
        def after(self) -> _EventModule._AfterModule.Reader: ...
        @property
        def params(self) -> Any: ...
        @property
        def runAtStartOfDay(self) -> bool: ...
        @override
        def which(self) -> Literal["at", "between", "after"]: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _EventModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def type(self) -> _EventModule._ExternalTypeModule: ...
        @type.setter
        def type(self, value: _EventModule._ExternalTypeModule | Literal["sowing", "automaticSowing", "harvest", "automaticHarvest", "irrigation", "tillage", "organicFertilization", "mineralFertilization", "nDemandFertilization", "cutting"]) -> None: ...
        @property
        def info(self) -> _IdInformationModule.Builder: ...
        @info.setter
        def info(self, value: _IdInformationModule.Builder | _IdInformationModule.Reader | dict[str, Any]) -> None: ...
        @property
        def at(self) -> _EventModule._AtModule.Builder: ...
        @at.setter
        def at(self, value: _EventModule._AtModule.Builder | _EventModule._AtModule.Reader | dict[str, Any]) -> None: ...
        @property
        def between(self) -> _EventModule._BetweenModule.Builder: ...
        @between.setter
        def between(self, value: _EventModule._BetweenModule.Builder | _EventModule._BetweenModule.Reader | dict[str, Any]) -> None: ...
        @property
        def after(self) -> _EventModule._AfterModule.Builder: ...
        @after.setter
        def after(self, value: _EventModule._AfterModule.Builder | _EventModule._AfterModule.Reader | dict[str, Any]) -> None: ...
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
        def init(self, field: Literal["info"], size: int | None = None) -> _IdInformationModule.Builder: ...
        @overload
        def init(self, field: Literal["at"], size: int | None = None) -> _EventModule._AtModule.Builder: ...
        @overload
        def init(self, field: Literal["between"], size: int | None = None) -> _EventModule._BetweenModule.Builder: ...
        @overload
        def init(self, field: Literal["after"], size: int | None = None) -> _EventModule._AfterModule.Builder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> _EventModule.Reader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        type: _EventModule._ExternalTypeModule | Literal["sowing", "automaticSowing", "harvest", "automaticHarvest", "irrigation", "tillage", "organicFertilization", "mineralFertilization", "nDemandFertilization", "cutting"] | None = None,
        info: _IdInformationModule.Builder | dict[str, Any] | None = None,
        at: _EventModule._AtModule.Builder | dict[str, Any] | None = None,
        between: _EventModule._BetweenModule.Builder | dict[str, Any] | None = None,
        after: _EventModule._AfterModule.Builder | dict[str, Any] | None = None,
        params: Any | None = None,
        runAtStartOfDay: bool | None = None,
    ) -> _EventModule.Builder: ...

EventReader: TypeAlias = _EventModule.Reader
EventBuilder: TypeAlias = _EventModule.Builder
Event: _EventModule

class _FertilizerModule(_IdentifiableModule, _PersistentModule):
    NutrientReader: TypeAlias = _NutrientModule.Reader
    NutrientBuilder: TypeAlias = _NutrientModule.Builder
    Nutrient: _NutrientModule
    class NutrientsRequest(Protocol):
        def send(self) -> _FertilizerModule.FertilizerClient.NutrientsResult: ...

    class ParametersRequest(Protocol):
        def send(self) -> _FertilizerModule.FertilizerClient.ParametersResult: ...

    @classmethod
    def _new_client(cls, server: _FertilizerModule.Server | _IdentifiableModule.Server | _PersistentModule.Server) -> _FertilizerModule.FertilizerClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class NutrientsResult(Awaitable[NutrientsResult], Protocol):
            nutrients: Sequence[_NutrientModule.Builder | _NutrientModule.Reader]

        class ParametersResult(Awaitable[ParametersResult], Protocol):
            params: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

        class NutrientsResultTuple(NamedTuple):
            nutrients: Sequence[_NutrientModule]

        class ParametersResultTuple(NamedTuple):
            params: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

        class NutrientsCallContext(Protocol):
            params: _FertilizerModule.NutrientsRequest
            results: _FertilizerModule.Server.NutrientsResult

        class ParametersCallContext(Protocol):
            params: _FertilizerModule.ParametersRequest
            results: _FertilizerModule.Server.ParametersResult

        def nutrients(self, _context: _FertilizerModule.Server.NutrientsCallContext, **kwargs: Any) -> Awaitable[_FertilizerModule.Server.NutrientsResultTuple | None]: ...
        def nutrients_context(self, context: _FertilizerModule.Server.NutrientsCallContext) -> Awaitable[None]: ...
        def parameters(self, _context: _FertilizerModule.Server.ParametersCallContext, **kwargs: Any) -> Awaitable[_FertilizerModule.Server.ParametersResultTuple | None]: ...
        def parameters_context(self, context: _FertilizerModule.Server.ParametersCallContext) -> Awaitable[None]: ...

    class FertilizerClient(_IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient):
        class NutrientsResult(Awaitable[NutrientsResult], Protocol):
            nutrients: Sequence[_NutrientModule.Builder | _NutrientModule.Reader]

        class ParametersResult(Awaitable[ParametersResult], Protocol):
            params: _DynamicObjectReader

        def nutrients(self) -> _FertilizerModule.FertilizerClient.NutrientsResult: ...
        def parameters(self) -> _FertilizerModule.FertilizerClient.ParametersResult: ...
        def nutrients_request(self) -> _FertilizerModule.NutrientsRequest: ...
        def parameters_request(self) -> _FertilizerModule.ParametersRequest: ...

class _NutrientModule(_StructModule):
    class _NameModule(Enum):
        urea = 0
        ammonia = 1
        nitrate = 2
        phosphorus = 3
        potassium = 4
        sulfate = 5
        organicC = 6
        organicN = 7
        organicP = 8
        organicNFast = 9
        organicNSlow = 10

    Name: TypeAlias = _NameModule
    class _UnitModule(Enum):
        none = 0
        fraction = 1
        percent = 2

    Unit: TypeAlias = _UnitModule
    class Reader(_DynamicStructReader):
        @property
        def nutrient(self) -> _NutrientModule._NameModule: ...
        @property
        def value(self) -> float: ...
        @property
        def unit(self) -> _NutrientModule._UnitModule: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _NutrientModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def nutrient(self) -> _NutrientModule._NameModule: ...
        @nutrient.setter
        def nutrient(self, value: _NutrientModule._NameModule | Literal["urea", "ammonia", "nitrate", "phosphorus", "potassium", "sulfate", "organicC", "organicN", "organicP", "organicNFast", "organicNSlow"]) -> None: ...
        @property
        def value(self) -> float: ...
        @value.setter
        def value(self, value: float) -> None: ...
        @property
        def unit(self) -> _NutrientModule._UnitModule: ...
        @unit.setter
        def unit(self, value: _NutrientModule._UnitModule | Literal["none", "fraction", "percent"]) -> None: ...
        @override
        def as_reader(self) -> _NutrientModule.Reader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        nutrient: _NutrientModule._NameModule | Literal["urea", "ammonia", "nitrate", "phosphorus", "potassium", "sulfate", "organicC", "organicN", "organicP", "organicNFast", "organicNSlow"] | None = None,
        value: float | None = None,
        unit: _NutrientModule._UnitModule | Literal["none", "fraction", "percent"] | None = None,
    ) -> _NutrientModule.Builder: ...

Fertilizer: _FertilizerModule
FertilizerClient: TypeAlias = _FertilizerModule.FertilizerClient

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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule._SowingModule.Builder: ...

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
            def crop(self, value: _CropModule.CropClient | _CropModule.Server) -> None: ...
            @override
            def as_reader(self) -> _ParamsModule._SowingModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, cultivar: str | None = None, plantDensity: int | None = None, crop: _CropModule.CropClient | _CropModule.Server | None = None) -> _ParamsModule._SowingModule.Builder: ...

    SowingReader: TypeAlias = _SowingModule.Reader
    SowingBuilder: TypeAlias = _SowingModule.Builder
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
                def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule._AutomaticSowingModule._AvgSoilTempModule.Builder: ...

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
                def as_reader(self) -> _ParamsModule._AutomaticSowingModule._AvgSoilTempModule.Reader: ...

            @override
            def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, soilDepthForAveraging: float | None = None, daysInSoilTempWindow: int | None = None, sowingIfAboveAvgSoilTemp: float | None = None) -> _ParamsModule._AutomaticSowingModule._AvgSoilTempModule.Builder: ...

        AvgSoilTempReader: TypeAlias = _AvgSoilTempModule.Reader
        AvgSoilTempBuilder: TypeAlias = _AvgSoilTempModule.Builder
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
            def avgSoilTemp(self) -> _ParamsModule._AutomaticSowingModule._AvgSoilTempModule.Reader: ...
            @property
            def sowing(self) -> _ParamsModule._SowingModule.Reader: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule._AutomaticSowingModule.Builder: ...

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
            def avgSoilTemp(self) -> _ParamsModule._AutomaticSowingModule._AvgSoilTempModule.Builder: ...
            @avgSoilTemp.setter
            def avgSoilTemp(self, value: _ParamsModule._AutomaticSowingModule._AvgSoilTempModule.Builder | _ParamsModule._AutomaticSowingModule._AvgSoilTempModule.Reader | dict[str, Any]) -> None: ...
            @property
            def sowing(self) -> _ParamsModule._SowingModule.Builder: ...
            @sowing.setter
            def sowing(self, value: _ParamsModule._SowingModule.Builder | _ParamsModule._SowingModule.Reader | dict[str, Any]) -> None: ...
            @overload
            def init(self, field: Literal["avgSoilTemp"], size: int | None = None) -> _ParamsModule._AutomaticSowingModule._AvgSoilTempModule.Builder: ...
            @overload
            def init(self, field: Literal["sowing"], size: int | None = None) -> _ParamsModule._SowingModule.Builder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> _ParamsModule._AutomaticSowingModule.Reader: ...

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
            avgSoilTemp: _ParamsModule._AutomaticSowingModule._AvgSoilTempModule.Builder | dict[str, Any] | None = None,
            sowing: _ParamsModule._SowingModule.Builder | dict[str, Any] | None = None,
        ) -> _ParamsModule._AutomaticSowingModule.Builder: ...

    AutomaticSowingReader: TypeAlias = _AutomaticSowingModule.Reader
    AutomaticSowingBuilder: TypeAlias = _AutomaticSowingModule.Builder
    AutomaticSowing: _AutomaticSowingModule
    class _HarvestModule(_StructModule):
        class _CropUsageModule(Enum):
            greenManure = 0
            biomassProduction = 1

        CropUsage: TypeAlias = _CropUsageModule
        class _OptCarbonMgmtDataModule(_StructModule):
            class Reader(_DynamicStructReader):
                @property
                def optCarbonConservation(self) -> bool: ...
                @property
                def cropImpactOnHumusBalance(self) -> float: ...
                @property
                def cropUsage(self) -> _ParamsModule._HarvestModule._CropUsageModule: ...
                @property
                def residueHeq(self) -> float: ...
                @property
                def organicFertilizerHeq(self) -> float: ...
                @property
                def maxResidueRecoverFraction(self) -> float: ...
                @override
                def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Builder: ...

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
                def cropUsage(self) -> _ParamsModule._HarvestModule._CropUsageModule: ...
                @cropUsage.setter
                def cropUsage(self, value: _ParamsModule._HarvestModule._CropUsageModule | Literal["greenManure", "biomassProduction"]) -> None: ...
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
                def as_reader(self) -> _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Reader: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                optCarbonConservation: bool | None = None,
                cropImpactOnHumusBalance: float | None = None,
                cropUsage: _ParamsModule._HarvestModule._CropUsageModule | Literal["greenManure", "biomassProduction"] | None = None,
                residueHeq: float | None = None,
                organicFertilizerHeq: float | None = None,
                maxResidueRecoverFraction: float | None = None,
            ) -> _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Builder: ...

        OptCarbonMgmtDataReader: TypeAlias = _OptCarbonMgmtDataModule.Reader
        OptCarbonMgmtDataBuilder: TypeAlias = _OptCarbonMgmtDataModule.Builder
        OptCarbonMgmtData: _OptCarbonMgmtDataModule
        class Reader(_DynamicStructReader):
            @property
            def exported(self) -> bool: ...
            @property
            def optCarbMgmtData(self) -> _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Reader: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule._HarvestModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def exported(self) -> bool: ...
            @exported.setter
            def exported(self, value: bool) -> None: ...
            @property
            def optCarbMgmtData(self) -> _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Builder: ...
            @optCarbMgmtData.setter
            def optCarbMgmtData(self, value: _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Builder | _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Reader | dict[str, Any]) -> None: ...
            def init(self, field: Literal["optCarbMgmtData"], size: int | None = None) -> _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Builder: ...
            @override
            def as_reader(self) -> _ParamsModule._HarvestModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, exported: bool | None = None, optCarbMgmtData: _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Builder | dict[str, Any] | None = None) -> _ParamsModule._HarvestModule.Builder: ...

    HarvestReader: TypeAlias = _HarvestModule.Reader
    HarvestBuilder: TypeAlias = _HarvestModule.Builder
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
            def harvestTime(self) -> _EventModule._PhenoStageModule: ...
            @property
            def harvest(self) -> _ParamsModule._HarvestModule.Reader: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule._AutomaticHarvestModule.Builder: ...

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
            def harvestTime(self) -> _EventModule._PhenoStageModule: ...
            @harvestTime.setter
            def harvestTime(self, value: _EventModule._PhenoStageModule | Literal["emergence", "flowering", "anthesis", "maturity"]) -> None: ...
            @property
            def harvest(self) -> _ParamsModule._HarvestModule.Builder: ...
            @harvest.setter
            def harvest(self, value: _ParamsModule._HarvestModule.Builder | _ParamsModule._HarvestModule.Reader | dict[str, Any]) -> None: ...
            def init(self, field: Literal["harvest"], size: int | None = None) -> _ParamsModule._HarvestModule.Builder: ...
            @override
            def as_reader(self) -> _ParamsModule._AutomaticHarvestModule.Reader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            minPercentASW: float | None = None,
            maxPercentASW: float | None = None,
            max3dayPrecipSum: float | None = None,
            maxCurrentDayPrecipSum: float | None = None,
            harvestTime: _EventModule._PhenoStageModule | Literal["emergence", "flowering", "anthesis", "maturity"] | None = None,
            harvest: _ParamsModule._HarvestModule.Builder | dict[str, Any] | None = None,
        ) -> _ParamsModule._AutomaticHarvestModule.Builder: ...

    AutomaticHarvestReader: TypeAlias = _AutomaticHarvestModule.Reader
    AutomaticHarvestBuilder: TypeAlias = _AutomaticHarvestModule.Builder
    AutomaticHarvest: _AutomaticHarvestModule
    class _CuttingModule(_StructModule):
        class _CLModule(Enum):
            cut = 0
            left = 1

        CL: TypeAlias = _CLModule
        class _UnitModule(Enum):
            percentage = 0
            biomass = 1
            lai = 2

        Unit: TypeAlias = _UnitModule
        class _SpecModule(_StructModule):
            class Reader(_DynamicStructReader):
                @property
                def organ(self) -> _PlantOrganModule: ...
                @property
                def value(self) -> float: ...
                @property
                def unit(self) -> _ParamsModule._CuttingModule._UnitModule: ...
                @property
                def cutOrLeft(self) -> _ParamsModule._CuttingModule._CLModule: ...
                @property
                def exportPercentage(self) -> float: ...
                @override
                def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule._CuttingModule._SpecModule.Builder: ...

            class Builder(_DynamicStructBuilder):
                @property
                def organ(self) -> _PlantOrganModule: ...
                @organ.setter
                def organ(self, value: _PlantOrganModule | Literal["root", "leaf", "shoot", "fruit", "strukt", "sugar"]) -> None: ...
                @property
                def value(self) -> float: ...
                @value.setter
                def value(self, value: float) -> None: ...
                @property
                def unit(self) -> _ParamsModule._CuttingModule._UnitModule: ...
                @unit.setter
                def unit(self, value: _ParamsModule._CuttingModule._UnitModule | Literal["percentage", "biomass", "lai"]) -> None: ...
                @property
                def cutOrLeft(self) -> _ParamsModule._CuttingModule._CLModule: ...
                @cutOrLeft.setter
                def cutOrLeft(self, value: _ParamsModule._CuttingModule._CLModule | Literal["cut", "left"]) -> None: ...
                @property
                def exportPercentage(self) -> float: ...
                @exportPercentage.setter
                def exportPercentage(self, value: float) -> None: ...
                @override
                def as_reader(self) -> _ParamsModule._CuttingModule._SpecModule.Reader: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                organ: _PlantOrganModule | Literal["root", "leaf", "shoot", "fruit", "strukt", "sugar"] | None = None,
                value: float | None = None,
                unit: _ParamsModule._CuttingModule._UnitModule | Literal["percentage", "biomass", "lai"] | None = None,
                cutOrLeft: _ParamsModule._CuttingModule._CLModule | Literal["cut", "left"] | None = None,
                exportPercentage: float | None = None,
            ) -> _ParamsModule._CuttingModule._SpecModule.Builder: ...

        SpecReader: TypeAlias = _SpecModule.Reader
        SpecBuilder: TypeAlias = _SpecModule.Builder
        Spec: _SpecModule
        class Reader(_DynamicStructReader):
            @property
            def cuttingSpec(self) -> Sequence[_ParamsModule._CuttingModule._SpecModule.Reader]: ...
            @property
            def cutMaxAssimilationRatePercentage(self) -> float: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule._CuttingModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def cuttingSpec(self) -> MutableSequence[_ParamsModule._CuttingModule._SpecModule.Builder]: ...
            @cuttingSpec.setter
            def cuttingSpec(self, value: Sequence[_ParamsModule._CuttingModule._SpecModule.Builder | _ParamsModule._CuttingModule._SpecModule.Reader] | Sequence[dict[str, Any]]) -> None: ...
            @property
            def cutMaxAssimilationRatePercentage(self) -> float: ...
            @cutMaxAssimilationRatePercentage.setter
            def cutMaxAssimilationRatePercentage(self, value: float) -> None: ...
            def init(self, field: Literal["cuttingSpec"], size: int | None = None) -> MutableSequence[_ParamsModule._CuttingModule._SpecModule.Builder]: ...
            @override
            def as_reader(self) -> _ParamsModule._CuttingModule.Reader: ...

        @override
        def new_message(
            self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, cuttingSpec: Sequence[_ParamsModule._CuttingModule._SpecModule.Builder] | Sequence[dict[str, Any]] | None = None, cutMaxAssimilationRatePercentage: float | None = None
        ) -> _ParamsModule._CuttingModule.Builder: ...

    CuttingReader: TypeAlias = _CuttingModule.Reader
    CuttingBuilder: TypeAlias = _CuttingModule.Builder
    Cutting: _CuttingModule
    class _MineralFertilizationModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def fertilizer(self) -> _FertilizerModule.FertilizerClient: ...
            @property
            def amount(self) -> float: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule._MineralFertilizationModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def fertilizer(self) -> _FertilizerModule.FertilizerClient: ...
            @fertilizer.setter
            def fertilizer(self, value: _FertilizerModule.FertilizerClient | _FertilizerModule.Server) -> None: ...
            @property
            def amount(self) -> float: ...
            @amount.setter
            def amount(self, value: float) -> None: ...
            @override
            def as_reader(self) -> _ParamsModule._MineralFertilizationModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, fertilizer: _FertilizerModule.FertilizerClient | _FertilizerModule.Server | None = None, amount: float | None = None) -> _ParamsModule._MineralFertilizationModule.Builder: ...

    MineralFertilizationReader: TypeAlias = _MineralFertilizationModule.Reader
    MineralFertilizationBuilder: TypeAlias = _MineralFertilizationModule.Builder
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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule._NDemandFertilizationModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def nDemand(self) -> float: ...
            @nDemand.setter
            def nDemand(self, value: float) -> None: ...
            @property
            def fertilizer(self) -> _FertilizerModule.FertilizerClient: ...
            @fertilizer.setter
            def fertilizer(self, value: _FertilizerModule.FertilizerClient | _FertilizerModule.Server) -> None: ...
            @property
            def depth(self) -> float: ...
            @depth.setter
            def depth(self, value: float) -> None: ...
            @property
            def stage(self) -> int: ...
            @stage.setter
            def stage(self, value: int) -> None: ...
            @override
            def as_reader(self) -> _ParamsModule._NDemandFertilizationModule.Reader: ...

        @override
        def new_message(
            self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, nDemand: float | None = None, fertilizer: _FertilizerModule.FertilizerClient | _FertilizerModule.Server | None = None, depth: float | None = None, stage: int | None = None
        ) -> _ParamsModule._NDemandFertilizationModule.Builder: ...

    NDemandFertilizationReader: TypeAlias = _NDemandFertilizationModule.Reader
    NDemandFertilizationBuilder: TypeAlias = _NDemandFertilizationModule.Builder
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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule._OrganicFertilizationModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def fertilizer(self) -> _FertilizerModule.FertilizerClient: ...
            @fertilizer.setter
            def fertilizer(self, value: _FertilizerModule.FertilizerClient | _FertilizerModule.Server) -> None: ...
            @property
            def amount(self) -> float: ...
            @amount.setter
            def amount(self, value: float) -> None: ...
            @property
            def incorporation(self) -> bool: ...
            @incorporation.setter
            def incorporation(self, value: bool) -> None: ...
            @override
            def as_reader(self) -> _ParamsModule._OrganicFertilizationModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, fertilizer: _FertilizerModule.FertilizerClient | _FertilizerModule.Server | None = None, amount: float | None = None, incorporation: bool | None = None) -> _ParamsModule._OrganicFertilizationModule.Builder: ...

    OrganicFertilizationReader: TypeAlias = _OrganicFertilizationModule.Reader
    OrganicFertilizationBuilder: TypeAlias = _OrganicFertilizationModule.Builder
    OrganicFertilization: _OrganicFertilizationModule
    class _TillageModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def depth(self) -> float: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule._TillageModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def depth(self) -> float: ...
            @depth.setter
            def depth(self, value: float) -> None: ...
            @override
            def as_reader(self) -> _ParamsModule._TillageModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, depth: float | None = None) -> _ParamsModule._TillageModule.Builder: ...

    TillageReader: TypeAlias = _TillageModule.Reader
    TillageBuilder: TypeAlias = _TillageModule.Builder
    Tillage: _TillageModule
    class _IrrigationModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def amount(self) -> float: ...
            @property
            def nutrientConcentrations(self) -> Sequence[_NutrientModule.Reader]: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule._IrrigationModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def amount(self) -> float: ...
            @amount.setter
            def amount(self, value: float) -> None: ...
            @property
            def nutrientConcentrations(self) -> MutableSequence[_NutrientModule.Builder]: ...
            @nutrientConcentrations.setter
            def nutrientConcentrations(self, value: Sequence[_NutrientModule.Builder | _NutrientModule.Reader] | Sequence[dict[str, Any]]) -> None: ...
            def init(self, field: Literal["nutrientConcentrations"], size: int | None = None) -> MutableSequence[_NutrientModule.Builder]: ...
            @override
            def as_reader(self) -> _ParamsModule._IrrigationModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, amount: float | None = None, nutrientConcentrations: Sequence[_NutrientModule.Builder] | Sequence[dict[str, Any]] | None = None) -> _ParamsModule._IrrigationModule.Builder: ...

    IrrigationReader: TypeAlias = _IrrigationModule.Reader
    IrrigationBuilder: TypeAlias = _IrrigationModule.Builder
    Irrigation: _IrrigationModule
    class Reader(_DynamicStructReader):
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @override
        def as_reader(self) -> _ParamsModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ParamsModule.Builder: ...

ParamsReader: TypeAlias = _ParamsModule.Reader
ParamsBuilder: TypeAlias = _ParamsModule.Builder
Params: _ParamsModule

class _FertilizerServiceModule(_RegistryModule):
    @classmethod
    def _new_client(cls, server: _FertilizerServiceModule.Server | _IdentifiableModule.Server | _RegistryModule.Server) -> _FertilizerServiceModule.FertilizerServiceClient: ...
    class Server(_RegistryModule.Server): ...
    class FertilizerServiceClient(_RegistryModule.RegistryClient): ...

FertilizerService: _FertilizerServiceModule
FertilizerServiceClient: TypeAlias = _FertilizerServiceModule.FertilizerServiceClient

class _ServiceModule(_IdentifiableModule):
    class ManagementatRequest(Protocol):
        lat: float
        lon: float
        def send(self) -> _ServiceModule.ServiceClient.ManagementatResult: ...

    @classmethod
    def _new_client(cls, server: _ServiceModule.Server | _IdentifiableModule.Server) -> _ServiceModule.ServiceClient: ...
    class Server(_IdentifiableModule.Server):
        class ManagementatResult(Awaitable[ManagementatResult], Protocol):
            mgmt: Sequence[_EventModule.Builder | _EventModule.Reader]

        class ManagementatResultTuple(NamedTuple):
            mgmt: Sequence[_EventModule]

        class ManagementatCallContext(Protocol):
            params: _ServiceModule.ManagementatRequest
            results: _ServiceModule.Server.ManagementatResult

        def managementAt(self, lat: float, lon: float, _context: _ServiceModule.Server.ManagementatCallContext, **kwargs: Any) -> Awaitable[_ServiceModule.Server.ManagementatResultTuple | None]: ...
        def managementAt_context(self, context: _ServiceModule.Server.ManagementatCallContext) -> Awaitable[None]: ...

    class ServiceClient(_IdentifiableModule.IdentifiableClient):
        class ManagementatResult(Awaitable[ManagementatResult], Protocol):
            mgmt: Sequence[_EventModule.Builder | _EventModule.Reader]

        def managementAt(self, lat: float | None = None, lon: float | None = None) -> _ServiceModule.ServiceClient.ManagementatResult: ...
        def managementAt_request(self, lat: float | None = None, lon: float | None = None) -> _ServiceModule.ManagementatRequest: ...

Service: _ServiceModule
ServiceClient: TypeAlias = _ServiceModule.ServiceClient

# Top-level type aliases for use in type annotations
AfterBuilder: TypeAlias = _EventModule._AfterModule.Builder
AfterReader: TypeAlias = _EventModule._AfterModule.Reader
AtBuilder: TypeAlias = _EventModule._AtModule.Builder
AtReader: TypeAlias = _EventModule._AtModule.Reader
AutomaticHarvestBuilder: TypeAlias = _ParamsModule._AutomaticHarvestModule.Builder
AutomaticHarvestReader: TypeAlias = _ParamsModule._AutomaticHarvestModule.Reader
AutomaticSowingBuilder: TypeAlias = _ParamsModule._AutomaticSowingModule.Builder
AutomaticSowingReader: TypeAlias = _ParamsModule._AutomaticSowingModule.Reader
AvgSoilTempBuilder: TypeAlias = _ParamsModule._AutomaticSowingModule._AvgSoilTempModule.Builder
AvgSoilTempReader: TypeAlias = _ParamsModule._AutomaticSowingModule._AvgSoilTempModule.Reader
BetweenBuilder: TypeAlias = _EventModule._BetweenModule.Builder
BetweenReader: TypeAlias = _EventModule._BetweenModule.Reader
CuttingBuilder: TypeAlias = _ParamsModule._CuttingModule.Builder
CuttingReader: TypeAlias = _ParamsModule._CuttingModule.Reader
HarvestBuilder: TypeAlias = _ParamsModule._HarvestModule.Builder
HarvestReader: TypeAlias = _ParamsModule._HarvestModule.Reader
IrrigationBuilder: TypeAlias = _ParamsModule._IrrigationModule.Builder
IrrigationReader: TypeAlias = _ParamsModule._IrrigationModule.Reader
MineralFertilizationBuilder: TypeAlias = _ParamsModule._MineralFertilizationModule.Builder
MineralFertilizationReader: TypeAlias = _ParamsModule._MineralFertilizationModule.Reader
NDemandFertilizationBuilder: TypeAlias = _ParamsModule._NDemandFertilizationModule.Builder
NDemandFertilizationReader: TypeAlias = _ParamsModule._NDemandFertilizationModule.Reader
OptCarbonMgmtDataBuilder: TypeAlias = _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Builder
OptCarbonMgmtDataReader: TypeAlias = _ParamsModule._HarvestModule._OptCarbonMgmtDataModule.Reader
OrganicFertilizationBuilder: TypeAlias = _ParamsModule._OrganicFertilizationModule.Builder
OrganicFertilizationReader: TypeAlias = _ParamsModule._OrganicFertilizationModule.Reader
SowingBuilder: TypeAlias = _ParamsModule._SowingModule.Builder
SowingReader: TypeAlias = _ParamsModule._SowingModule.Reader
SpecBuilder: TypeAlias = _ParamsModule._CuttingModule._SpecModule.Builder
SpecReader: TypeAlias = _ParamsModule._CuttingModule._SpecModule.Reader
TillageBuilder: TypeAlias = _ParamsModule._TillageModule.Builder
TillageReader: TypeAlias = _ParamsModule._TillageModule.Reader
TypeBuilder: TypeAlias = _EventModule._TypeModule.Builder
TypeReader: TypeAlias = _EventModule._TypeModule.Reader
