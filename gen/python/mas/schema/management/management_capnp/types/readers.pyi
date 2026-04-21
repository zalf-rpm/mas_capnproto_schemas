"""Reader helper types for `management.capnp`."""

from collections.abc import Callable
from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicObjectReader,
    _DynamicStructReader,
)

from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.crop.crop_capnp.types.clients import CropClient
from mas.schema.management.management_capnp.types import builders as builders
from mas.schema.management.management_capnp.types import clients as clients
from mas.schema.management.management_capnp.types import enums as enums
from mas.schema.management.management_capnp.types import lists as lists

class TypeReader(_DynamicStructReader):
    @property
    def external(self) -> enums.EventExternalTypeEnum: ...
    @property
    def internal(self) -> enums.EventPhenoStageEnum: ...
    @override
    def which(self) -> Literal["external", "internal"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.TypeBuilder: ...

class EventAtReader(_DynamicStructReader):
    @property
    def date(self) -> DateReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.EventAtBuilder: ...

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
    ) -> builders.EventBetweenBuilder: ...

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
    ) -> builders.EventAfterBuilder: ...

class EventReader(_DynamicStructReader):
    @property
    def type(self) -> enums.EventExternalTypeEnum: ...
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
    ) -> builders.EventBuilder: ...

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
    ) -> builders.SowingBuilder: ...

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
    ) -> builders.AvgSoilTempBuilder: ...

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
    ) -> builders.AutomaticSowingBuilder: ...

class OptCarbonMgmtDataReader(_DynamicStructReader):
    @property
    def optCarbonConservation(self) -> bool: ...
    @property
    def cropImpactOnHumusBalance(self) -> float: ...
    @property
    def cropUsage(self) -> enums.ParamsHarvestCropUsageEnum: ...
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
    ) -> builders.OptCarbonMgmtDataBuilder: ...

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
    ) -> builders.HarvestBuilder: ...

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
    def harvestTime(self) -> enums.EventPhenoStageEnum: ...
    @property
    def harvest(self) -> HarvestReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.AutomaticHarvestBuilder: ...

class SpecReader(_DynamicStructReader):
    @property
    def organ(self) -> enums.PlantOrganEnum: ...
    @property
    def value(self) -> float: ...
    @property
    def unit(self) -> enums.ParamsCuttingUnitEnum: ...
    @property
    def cutOrLeft(self) -> enums.ParamsCuttingCLEnum: ...
    @property
    def exportPercentage(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.SpecBuilder: ...

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
    ) -> builders.CuttingBuilder: ...

class NutrientReader(_DynamicStructReader):
    @property
    def nutrient(self) -> enums.NutrientNameEnum: ...
    @property
    def value(self) -> float: ...
    @property
    def unit(self) -> enums.NutrientUnitEnum: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.NutrientBuilder: ...

class MineralFertilizationReader(_DynamicStructReader):
    @property
    def fertilizer(self) -> clients.FertilizerClient: ...
    @property
    def amount(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.MineralFertilizationBuilder: ...

class NDemandFertilizationReader(_DynamicStructReader):
    @property
    def nDemand(self) -> float: ...
    @property
    def fertilizer(self) -> clients.FertilizerClient: ...
    @property
    def depth(self) -> float: ...
    @property
    def stage(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.NDemandFertilizationBuilder: ...

class OrganicFertilizationReader(_DynamicStructReader):
    @property
    def fertilizer(self) -> clients.FertilizerClient: ...
    @property
    def amount(self) -> float: ...
    @property
    def incorporation(self) -> bool: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.OrganicFertilizationBuilder: ...

class TillageReader(_DynamicStructReader):
    @property
    def depth(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.TillageBuilder: ...

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
    ) -> builders.IrrigationBuilder: ...

class ParamsReader(_DynamicStructReader):
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ParamsBuilder: ...

type EventListReader = lists._EventList.Reader

type NutrientListReader = lists._NutrientList.Reader

type SpecListReader = lists._SpecList.Reader
