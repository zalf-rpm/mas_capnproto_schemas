"""Reader helper types for `monica_management.capnp`."""

from collections.abc import Callable
from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicObjectReader,
    _DynamicStructReader,
)

from mas.schema.climate.climate_capnp.types.enums import ElementEnum
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.crop.crop_capnp.types.clients import CropClient
from mas.schema.model.monica.monica_management_capnp.types import builders as builders
from mas.schema.model.monica.monica_management_capnp.types import enums as enums
from mas.schema.model.monica.monica_management_capnp.types import lists as lists
from mas.schema.model.monica.monica_management_capnp.types import modules as modules

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
    ) -> builders.ILRDatesBuilder: ...

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
    ) -> builders.KVBuilder: ...

class DailyWeatherReader(_DynamicStructReader):
    @property
    def data(self) -> KVListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.DailyWeatherBuilder: ...

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
    ) -> builders.ParamsMineralFertilizationParametersBuilder: ...

class MineralFertilizationReader(_DynamicStructReader):
    @property
    def partition(
        self,
    ) -> modules._ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Reader: ...
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
    def partition(
        self,
    ) -> modules._ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Reader: ...
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
    ) -> builders.OrganicMatterParametersBuilder: ...

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
    ) -> builders.ParamsOrganicFertilizationParametersBuilder: ...

class OrganicFertilizationReader(_DynamicStructReader):
    @property
    def params(
        self,
    ) -> modules._ParamsStructModule._OrganicFertilizationStructModule._ParametersStructModule.Reader: ...
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
    ) -> builders.ParamsIrrigationParametersBuilder: ...

class IrrigationReader(_DynamicStructReader):
    @property
    def amount(self) -> float: ...
    @property
    def params(
        self,
    ) -> modules._ParamsStructModule._IrrigationStructModule._ParametersStructModule.Reader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.IrrigationBuilder: ...

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
    ) -> builders.SaveStateBuilder: ...

class ParamsReader(_DynamicStructReader):
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ParamsBuilder: ...

type EventListReader = lists._EventList.Reader

type KVListReader = lists._KVList.Reader

type SpecListReader = lists._SpecList.Reader
