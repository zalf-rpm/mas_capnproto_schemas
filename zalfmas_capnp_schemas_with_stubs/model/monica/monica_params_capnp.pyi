"""This is an automatically generated stub for `monica_params.capnp`."""

from __future__ import annotations
from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _DynamicListBuilder,
    _DynamicListReader,
    _StructModule,
)
from contextlib import AbstractContextManager
from .monica_management_capnp import _ParamsStructModule
from ...climate_capnp import RCPEnum
from ...date_capnp import DateReader, DateBuilder
from collections.abc import Iterator, Sequence, Callable
from typing import Literal, overload, override, Any, IO

class _Float64List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> float: ...
        @override
        def __iter__(self) -> Iterator[float]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> float: ...
        @override
        def __setitem__(self, key: int, value: float) -> None: ...
        @override
        def __iter__(self) -> Iterator[float]: ...

class _BoolList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> bool: ...
        @override
        def __iter__(self) -> Iterator[bool]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> bool: ...
        @override
        def __setitem__(self, key: int, value: bool) -> None: ...
        @override
        def __iter__(self) -> Iterator[bool]: ...

class _SpeciesParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def speciesId(self) -> str: ...
        @property
        def carboxylationPathway(self) -> int: ...
        @property
        def defaultRadiationUseEfficiency(self) -> float: ...
        @property
        def partBiologicalNFixation(self) -> float: ...
        @property
        def initialKcFactor(self) -> float: ...
        @property
        def luxuryNCoeff(self) -> float: ...
        @property
        def maxCropDiameter(self) -> float: ...
        @property
        def stageAtMaxHeight(self) -> float: ...
        @property
        def stageAtMaxDiameter(self) -> float: ...
        @property
        def minimumNConcentration(self) -> float: ...
        @property
        def minimumTemperatureForAssimilation(self) -> float: ...
        @property
        def optimumTemperatureForAssimilation(self) -> float: ...
        @property
        def maximumTemperatureForAssimilation(self) -> float: ...
        @property
        def nConcentrationAbovegroundBiomass(self) -> float: ...
        @property
        def nConcentrationB0(self) -> float: ...
        @property
        def nConcentrationPN(self) -> float: ...
        @property
        def nConcentrationRoot(self) -> float: ...
        @property
        def developmentAccelerationByNitrogenStress(self) -> int: ...
        @property
        def fieldConditionModifier(self) -> float: ...
        @property
        def assimilateReallocation(self) -> float: ...
        @property
        def baseTemperature(self) -> Float64ListReader: ...
        @property
        def organMaintenanceRespiration(self) -> Float64ListReader: ...
        @property
        def organGrowthRespiration(self) -> Float64ListReader: ...
        @property
        def stageMaxRootNConcentration(self) -> Float64ListReader: ...
        @property
        def initialOrganBiomass(self) -> Float64ListReader: ...
        @property
        def criticalOxygenContent(self) -> Float64ListReader: ...
        @property
        def stageMobilFromStorageCoeff(self) -> Float64ListReader: ...
        @property
        def abovegroundOrgan(self) -> BoolListReader: ...
        @property
        def storageOrgan(self) -> BoolListReader: ...
        @property
        def samplingDepth(self) -> float: ...
        @property
        def targetNSamplingDepth(self) -> float: ...
        @property
        def targetN30(self) -> float: ...
        @property
        def maxNUptakeParam(self) -> float: ...
        @property
        def rootDistributionParam(self) -> float: ...
        @property
        def plantDensity(self) -> int: ...
        @property
        def rootGrowthLag(self) -> float: ...
        @property
        def minimumTemperatureRootGrowth(self) -> float: ...
        @property
        def initialRootingDepth(self) -> float: ...
        @property
        def rootPenetrationRate(self) -> float: ...
        @property
        def rootFormFactor(self) -> float: ...
        @property
        def specificRootLength(self) -> float: ...
        @property
        def stageAfterCut(self) -> int: ...
        @property
        def limitingTemperatureHeatStress(self) -> float: ...
        @property
        def cuttingDelayDays(self) -> int: ...
        @property
        def droughtImpactOnFertilityFactor(self) -> float: ...
        @property
        def efMono(self) -> float: ...
        @property
        def efMonos(self) -> float: ...
        @property
        def efIso(self) -> float: ...
        @property
        def vcMax25(self) -> float: ...
        @property
        def aekc(self) -> float: ...
        @property
        def aeko(self) -> float: ...
        @property
        def aevc(self) -> float: ...
        @property
        def kc25(self) -> float: ...
        @property
        def ko25(self) -> float: ...
        @property
        def transitionStageLeafExp(self) -> int: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> SpeciesParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def speciesId(self) -> str: ...
        @speciesId.setter
        def speciesId(self, value: str) -> None: ...
        @property
        def carboxylationPathway(self) -> int: ...
        @carboxylationPathway.setter
        def carboxylationPathway(self, value: int) -> None: ...
        @property
        def defaultRadiationUseEfficiency(self) -> float: ...
        @defaultRadiationUseEfficiency.setter
        def defaultRadiationUseEfficiency(self, value: float) -> None: ...
        @property
        def partBiologicalNFixation(self) -> float: ...
        @partBiologicalNFixation.setter
        def partBiologicalNFixation(self, value: float) -> None: ...
        @property
        def initialKcFactor(self) -> float: ...
        @initialKcFactor.setter
        def initialKcFactor(self, value: float) -> None: ...
        @property
        def luxuryNCoeff(self) -> float: ...
        @luxuryNCoeff.setter
        def luxuryNCoeff(self, value: float) -> None: ...
        @property
        def maxCropDiameter(self) -> float: ...
        @maxCropDiameter.setter
        def maxCropDiameter(self, value: float) -> None: ...
        @property
        def stageAtMaxHeight(self) -> float: ...
        @stageAtMaxHeight.setter
        def stageAtMaxHeight(self, value: float) -> None: ...
        @property
        def stageAtMaxDiameter(self) -> float: ...
        @stageAtMaxDiameter.setter
        def stageAtMaxDiameter(self, value: float) -> None: ...
        @property
        def minimumNConcentration(self) -> float: ...
        @minimumNConcentration.setter
        def minimumNConcentration(self, value: float) -> None: ...
        @property
        def minimumTemperatureForAssimilation(self) -> float: ...
        @minimumTemperatureForAssimilation.setter
        def minimumTemperatureForAssimilation(self, value: float) -> None: ...
        @property
        def optimumTemperatureForAssimilation(self) -> float: ...
        @optimumTemperatureForAssimilation.setter
        def optimumTemperatureForAssimilation(self, value: float) -> None: ...
        @property
        def maximumTemperatureForAssimilation(self) -> float: ...
        @maximumTemperatureForAssimilation.setter
        def maximumTemperatureForAssimilation(self, value: float) -> None: ...
        @property
        def nConcentrationAbovegroundBiomass(self) -> float: ...
        @nConcentrationAbovegroundBiomass.setter
        def nConcentrationAbovegroundBiomass(self, value: float) -> None: ...
        @property
        def nConcentrationB0(self) -> float: ...
        @nConcentrationB0.setter
        def nConcentrationB0(self, value: float) -> None: ...
        @property
        def nConcentrationPN(self) -> float: ...
        @nConcentrationPN.setter
        def nConcentrationPN(self, value: float) -> None: ...
        @property
        def nConcentrationRoot(self) -> float: ...
        @nConcentrationRoot.setter
        def nConcentrationRoot(self, value: float) -> None: ...
        @property
        def developmentAccelerationByNitrogenStress(self) -> int: ...
        @developmentAccelerationByNitrogenStress.setter
        def developmentAccelerationByNitrogenStress(self, value: int) -> None: ...
        @property
        def fieldConditionModifier(self) -> float: ...
        @fieldConditionModifier.setter
        def fieldConditionModifier(self, value: float) -> None: ...
        @property
        def assimilateReallocation(self) -> float: ...
        @assimilateReallocation.setter
        def assimilateReallocation(self, value: float) -> None: ...
        @property
        def baseTemperature(self) -> Float64ListBuilder: ...
        @baseTemperature.setter
        def baseTemperature(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def organMaintenanceRespiration(self) -> Float64ListBuilder: ...
        @organMaintenanceRespiration.setter
        def organMaintenanceRespiration(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def organGrowthRespiration(self) -> Float64ListBuilder: ...
        @organGrowthRespiration.setter
        def organGrowthRespiration(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def stageMaxRootNConcentration(self) -> Float64ListBuilder: ...
        @stageMaxRootNConcentration.setter
        def stageMaxRootNConcentration(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def initialOrganBiomass(self) -> Float64ListBuilder: ...
        @initialOrganBiomass.setter
        def initialOrganBiomass(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def criticalOxygenContent(self) -> Float64ListBuilder: ...
        @criticalOxygenContent.setter
        def criticalOxygenContent(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def stageMobilFromStorageCoeff(self) -> Float64ListBuilder: ...
        @stageMobilFromStorageCoeff.setter
        def stageMobilFromStorageCoeff(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def abovegroundOrgan(self) -> BoolListBuilder: ...
        @abovegroundOrgan.setter
        def abovegroundOrgan(
            self, value: BoolListBuilder | BoolListReader | dict[str, Any]
        ) -> None: ...
        @property
        def storageOrgan(self) -> BoolListBuilder: ...
        @storageOrgan.setter
        def storageOrgan(
            self, value: BoolListBuilder | BoolListReader | dict[str, Any]
        ) -> None: ...
        @property
        def samplingDepth(self) -> float: ...
        @samplingDepth.setter
        def samplingDepth(self, value: float) -> None: ...
        @property
        def targetNSamplingDepth(self) -> float: ...
        @targetNSamplingDepth.setter
        def targetNSamplingDepth(self, value: float) -> None: ...
        @property
        def targetN30(self) -> float: ...
        @targetN30.setter
        def targetN30(self, value: float) -> None: ...
        @property
        def maxNUptakeParam(self) -> float: ...
        @maxNUptakeParam.setter
        def maxNUptakeParam(self, value: float) -> None: ...
        @property
        def rootDistributionParam(self) -> float: ...
        @rootDistributionParam.setter
        def rootDistributionParam(self, value: float) -> None: ...
        @property
        def plantDensity(self) -> int: ...
        @plantDensity.setter
        def plantDensity(self, value: int) -> None: ...
        @property
        def rootGrowthLag(self) -> float: ...
        @rootGrowthLag.setter
        def rootGrowthLag(self, value: float) -> None: ...
        @property
        def minimumTemperatureRootGrowth(self) -> float: ...
        @minimumTemperatureRootGrowth.setter
        def minimumTemperatureRootGrowth(self, value: float) -> None: ...
        @property
        def initialRootingDepth(self) -> float: ...
        @initialRootingDepth.setter
        def initialRootingDepth(self, value: float) -> None: ...
        @property
        def rootPenetrationRate(self) -> float: ...
        @rootPenetrationRate.setter
        def rootPenetrationRate(self, value: float) -> None: ...
        @property
        def rootFormFactor(self) -> float: ...
        @rootFormFactor.setter
        def rootFormFactor(self, value: float) -> None: ...
        @property
        def specificRootLength(self) -> float: ...
        @specificRootLength.setter
        def specificRootLength(self, value: float) -> None: ...
        @property
        def stageAfterCut(self) -> int: ...
        @stageAfterCut.setter
        def stageAfterCut(self, value: int) -> None: ...
        @property
        def limitingTemperatureHeatStress(self) -> float: ...
        @limitingTemperatureHeatStress.setter
        def limitingTemperatureHeatStress(self, value: float) -> None: ...
        @property
        def cuttingDelayDays(self) -> int: ...
        @cuttingDelayDays.setter
        def cuttingDelayDays(self, value: int) -> None: ...
        @property
        def droughtImpactOnFertilityFactor(self) -> float: ...
        @droughtImpactOnFertilityFactor.setter
        def droughtImpactOnFertilityFactor(self, value: float) -> None: ...
        @property
        def efMono(self) -> float: ...
        @efMono.setter
        def efMono(self, value: float) -> None: ...
        @property
        def efMonos(self) -> float: ...
        @efMonos.setter
        def efMonos(self, value: float) -> None: ...
        @property
        def efIso(self) -> float: ...
        @efIso.setter
        def efIso(self, value: float) -> None: ...
        @property
        def vcMax25(self) -> float: ...
        @vcMax25.setter
        def vcMax25(self, value: float) -> None: ...
        @property
        def aekc(self) -> float: ...
        @aekc.setter
        def aekc(self, value: float) -> None: ...
        @property
        def aeko(self) -> float: ...
        @aeko.setter
        def aeko(self, value: float) -> None: ...
        @property
        def aevc(self) -> float: ...
        @aevc.setter
        def aevc(self, value: float) -> None: ...
        @property
        def kc25(self) -> float: ...
        @kc25.setter
        def kc25(self, value: float) -> None: ...
        @property
        def ko25(self) -> float: ...
        @ko25.setter
        def ko25(self, value: float) -> None: ...
        @property
        def transitionStageLeafExp(self) -> int: ...
        @transitionStageLeafExp.setter
        def transitionStageLeafExp(self, value: int) -> None: ...
        @override
        @overload
        def init(
            self, field: Literal["baseTemperature"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["organMaintenanceRespiration"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["organGrowthRespiration"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["stageMaxRootNConcentration"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["initialOrganBiomass"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["criticalOxygenContent"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["stageMobilFromStorageCoeff"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["abovegroundOrgan"], size: int | None = None
        ) -> BoolListBuilder: ...
        @overload
        def init(
            self, field: Literal["storageOrgan"], size: int | None = None
        ) -> BoolListBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> SpeciesParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        speciesId: str | None = None,
        carboxylationPathway: int | None = None,
        defaultRadiationUseEfficiency: float | None = None,
        partBiologicalNFixation: float | None = None,
        initialKcFactor: float | None = None,
        luxuryNCoeff: float | None = None,
        maxCropDiameter: float | None = None,
        stageAtMaxHeight: float | None = None,
        stageAtMaxDiameter: float | None = None,
        minimumNConcentration: float | None = None,
        minimumTemperatureForAssimilation: float | None = None,
        optimumTemperatureForAssimilation: float | None = None,
        maximumTemperatureForAssimilation: float | None = None,
        nConcentrationAbovegroundBiomass: float | None = None,
        nConcentrationB0: float | None = None,
        nConcentrationPN: float | None = None,
        nConcentrationRoot: float | None = None,
        developmentAccelerationByNitrogenStress: int | None = None,
        fieldConditionModifier: float | None = None,
        assimilateReallocation: float | None = None,
        baseTemperature: Float64ListBuilder | dict[str, Any] | None = None,
        organMaintenanceRespiration: Float64ListBuilder | dict[str, Any] | None = None,
        organGrowthRespiration: Float64ListBuilder | dict[str, Any] | None = None,
        stageMaxRootNConcentration: Float64ListBuilder | dict[str, Any] | None = None,
        initialOrganBiomass: Float64ListBuilder | dict[str, Any] | None = None,
        criticalOxygenContent: Float64ListBuilder | dict[str, Any] | None = None,
        stageMobilFromStorageCoeff: Float64ListBuilder | dict[str, Any] | None = None,
        abovegroundOrgan: BoolListBuilder | dict[str, Any] | None = None,
        storageOrgan: BoolListBuilder | dict[str, Any] | None = None,
        samplingDepth: float | None = None,
        targetNSamplingDepth: float | None = None,
        targetN30: float | None = None,
        maxNUptakeParam: float | None = None,
        rootDistributionParam: float | None = None,
        plantDensity: int | None = None,
        rootGrowthLag: float | None = None,
        minimumTemperatureRootGrowth: float | None = None,
        initialRootingDepth: float | None = None,
        rootPenetrationRate: float | None = None,
        rootFormFactor: float | None = None,
        specificRootLength: float | None = None,
        stageAfterCut: int | None = None,
        limitingTemperatureHeatStress: float | None = None,
        cuttingDelayDays: int | None = None,
        droughtImpactOnFertilityFactor: float | None = None,
        efMono: float | None = None,
        efMonos: float | None = None,
        efIso: float | None = None,
        vcMax25: float | None = None,
        aekc: float | None = None,
        aeko: float | None = None,
        aevc: float | None = None,
        kc25: float | None = None,
        ko25: float | None = None,
        transitionStageLeafExp: int | None = None,
        **kwargs: Any,
    ) -> SpeciesParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[SpeciesParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SpeciesParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SpeciesParametersBuilder]: ...
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
    ) -> SpeciesParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SpeciesParametersReader: ...

SpeciesParameters: _SpeciesParametersStructModule

class _Float64ListList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> Float64ListReader: ...
        @override
        def __iter__(self) -> Iterator[Float64ListReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> Float64ListBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: Float64ListReader | Float64ListBuilder | Sequence[Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[Float64ListBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> Float64ListBuilder: ...

class _YieldComponentStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def organId(self) -> int: ...
        @property
        def yieldPercentage(self) -> float: ...
        @property
        def yieldDryMatter(self) -> float: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> YieldComponentBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def organId(self) -> int: ...
        @organId.setter
        def organId(self, value: int) -> None: ...
        @property
        def yieldPercentage(self) -> float: ...
        @yieldPercentage.setter
        def yieldPercentage(self, value: float) -> None: ...
        @property
        def yieldDryMatter(self) -> float: ...
        @yieldDryMatter.setter
        def yieldDryMatter(self, value: float) -> None: ...
        @override
        def as_reader(self) -> YieldComponentReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        organId: int | None = None,
        yieldPercentage: float | None = None,
        yieldDryMatter: float | None = None,
        **kwargs: Any,
    ) -> YieldComponentBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[YieldComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[YieldComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[YieldComponentBuilder]: ...
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
    ) -> YieldComponentReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> YieldComponentReader: ...

YieldComponent: _YieldComponentStructModule

class _YieldComponentList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> YieldComponentReader: ...
        @override
        def __iter__(self) -> Iterator[YieldComponentReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> YieldComponentBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: YieldComponentReader | YieldComponentBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[YieldComponentBuilder]: ...
        @override
        def init(
            self, index: int, size: int | None = None
        ) -> YieldComponentBuilder: ...

class _CultivarParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def cultivarId(self) -> str: ...
        @property
        def description(self) -> str: ...
        @property
        def perennial(self) -> bool: ...
        @property
        def maxAssimilationRate(self) -> float: ...
        @property
        def maxCropHeight(self) -> float: ...
        @property
        def residueNRatio(self) -> float: ...
        @property
        def lt50cultivar(self) -> float: ...
        @property
        def cropHeightP1(self) -> float: ...
        @property
        def cropHeightP2(self) -> float: ...
        @property
        def cropSpecificMaxRootingDepth(self) -> float: ...
        @property
        def assimilatePartitioningCoeff(self) -> Float64ListListReader: ...
        @property
        def organSenescenceRate(self) -> Float64ListListReader: ...
        @property
        def baseDaylength(self) -> Float64ListReader: ...
        @property
        def optimumTemperature(self) -> Float64ListReader: ...
        @property
        def daylengthRequirement(self) -> Float64ListReader: ...
        @property
        def droughtStressThreshold(self) -> Float64ListReader: ...
        @property
        def specificLeafArea(self) -> Float64ListReader: ...
        @property
        def stageKcFactor(self) -> Float64ListReader: ...
        @property
        def stageTemperatureSum(self) -> Float64ListReader: ...
        @property
        def vernalisationRequirement(self) -> Float64ListReader: ...
        @property
        def heatSumIrrigationStart(self) -> float: ...
        @property
        def heatSumIrrigationEnd(self) -> float: ...
        @property
        def criticalTemperatureHeatStress(self) -> float: ...
        @property
        def beginSensitivePhaseHeatStress(self) -> float: ...
        @property
        def endSensitivePhaseHeatStress(self) -> float: ...
        @property
        def frostHardening(self) -> float: ...
        @property
        def frostDehardening(self) -> float: ...
        @property
        def lowTemperatureExposure(self) -> float: ...
        @property
        def respiratoryStress(self) -> float: ...
        @property
        def latestHarvestDoy(self) -> int: ...
        @property
        def organIdsForPrimaryYield(self) -> YieldComponentListReader: ...
        @property
        def organIdsForSecondaryYield(self) -> YieldComponentListReader: ...
        @property
        def organIdsForCutting(self) -> YieldComponentListReader: ...
        @property
        def earlyRefLeafExp(self) -> float: ...
        @property
        def refLeafExp(self) -> float: ...
        @property
        def minTempDevWE(self) -> float: ...
        @property
        def optTempDevWE(self) -> float: ...
        @property
        def maxTempDevWE(self) -> float: ...
        @property
        def winterCrop(self) -> bool: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> CultivarParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def cultivarId(self) -> str: ...
        @cultivarId.setter
        def cultivarId(self, value: str) -> None: ...
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str) -> None: ...
        @property
        def perennial(self) -> bool: ...
        @perennial.setter
        def perennial(self, value: bool) -> None: ...
        @property
        def maxAssimilationRate(self) -> float: ...
        @maxAssimilationRate.setter
        def maxAssimilationRate(self, value: float) -> None: ...
        @property
        def maxCropHeight(self) -> float: ...
        @maxCropHeight.setter
        def maxCropHeight(self, value: float) -> None: ...
        @property
        def residueNRatio(self) -> float: ...
        @residueNRatio.setter
        def residueNRatio(self, value: float) -> None: ...
        @property
        def lt50cultivar(self) -> float: ...
        @lt50cultivar.setter
        def lt50cultivar(self, value: float) -> None: ...
        @property
        def cropHeightP1(self) -> float: ...
        @cropHeightP1.setter
        def cropHeightP1(self, value: float) -> None: ...
        @property
        def cropHeightP2(self) -> float: ...
        @cropHeightP2.setter
        def cropHeightP2(self, value: float) -> None: ...
        @property
        def cropSpecificMaxRootingDepth(self) -> float: ...
        @cropSpecificMaxRootingDepth.setter
        def cropSpecificMaxRootingDepth(self, value: float) -> None: ...
        @property
        def assimilatePartitioningCoeff(self) -> Float64ListListBuilder: ...
        @assimilatePartitioningCoeff.setter
        def assimilatePartitioningCoeff(
            self, value: Float64ListListBuilder | Float64ListListReader | dict[str, Any]
        ) -> None: ...
        @property
        def organSenescenceRate(self) -> Float64ListListBuilder: ...
        @organSenescenceRate.setter
        def organSenescenceRate(
            self, value: Float64ListListBuilder | Float64ListListReader | dict[str, Any]
        ) -> None: ...
        @property
        def baseDaylength(self) -> Float64ListBuilder: ...
        @baseDaylength.setter
        def baseDaylength(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def optimumTemperature(self) -> Float64ListBuilder: ...
        @optimumTemperature.setter
        def optimumTemperature(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def daylengthRequirement(self) -> Float64ListBuilder: ...
        @daylengthRequirement.setter
        def daylengthRequirement(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def droughtStressThreshold(self) -> Float64ListBuilder: ...
        @droughtStressThreshold.setter
        def droughtStressThreshold(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def specificLeafArea(self) -> Float64ListBuilder: ...
        @specificLeafArea.setter
        def specificLeafArea(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def stageKcFactor(self) -> Float64ListBuilder: ...
        @stageKcFactor.setter
        def stageKcFactor(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def stageTemperatureSum(self) -> Float64ListBuilder: ...
        @stageTemperatureSum.setter
        def stageTemperatureSum(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def vernalisationRequirement(self) -> Float64ListBuilder: ...
        @vernalisationRequirement.setter
        def vernalisationRequirement(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def heatSumIrrigationStart(self) -> float: ...
        @heatSumIrrigationStart.setter
        def heatSumIrrigationStart(self, value: float) -> None: ...
        @property
        def heatSumIrrigationEnd(self) -> float: ...
        @heatSumIrrigationEnd.setter
        def heatSumIrrigationEnd(self, value: float) -> None: ...
        @property
        def criticalTemperatureHeatStress(self) -> float: ...
        @criticalTemperatureHeatStress.setter
        def criticalTemperatureHeatStress(self, value: float) -> None: ...
        @property
        def beginSensitivePhaseHeatStress(self) -> float: ...
        @beginSensitivePhaseHeatStress.setter
        def beginSensitivePhaseHeatStress(self, value: float) -> None: ...
        @property
        def endSensitivePhaseHeatStress(self) -> float: ...
        @endSensitivePhaseHeatStress.setter
        def endSensitivePhaseHeatStress(self, value: float) -> None: ...
        @property
        def frostHardening(self) -> float: ...
        @frostHardening.setter
        def frostHardening(self, value: float) -> None: ...
        @property
        def frostDehardening(self) -> float: ...
        @frostDehardening.setter
        def frostDehardening(self, value: float) -> None: ...
        @property
        def lowTemperatureExposure(self) -> float: ...
        @lowTemperatureExposure.setter
        def lowTemperatureExposure(self, value: float) -> None: ...
        @property
        def respiratoryStress(self) -> float: ...
        @respiratoryStress.setter
        def respiratoryStress(self, value: float) -> None: ...
        @property
        def latestHarvestDoy(self) -> int: ...
        @latestHarvestDoy.setter
        def latestHarvestDoy(self, value: int) -> None: ...
        @property
        def organIdsForPrimaryYield(self) -> YieldComponentListBuilder: ...
        @organIdsForPrimaryYield.setter
        def organIdsForPrimaryYield(
            self,
            value: YieldComponentListBuilder
            | YieldComponentListReader
            | dict[str, Any],
        ) -> None: ...
        @property
        def organIdsForSecondaryYield(self) -> YieldComponentListBuilder: ...
        @organIdsForSecondaryYield.setter
        def organIdsForSecondaryYield(
            self,
            value: YieldComponentListBuilder
            | YieldComponentListReader
            | dict[str, Any],
        ) -> None: ...
        @property
        def organIdsForCutting(self) -> YieldComponentListBuilder: ...
        @organIdsForCutting.setter
        def organIdsForCutting(
            self,
            value: YieldComponentListBuilder
            | YieldComponentListReader
            | dict[str, Any],
        ) -> None: ...
        @property
        def earlyRefLeafExp(self) -> float: ...
        @earlyRefLeafExp.setter
        def earlyRefLeafExp(self, value: float) -> None: ...
        @property
        def refLeafExp(self) -> float: ...
        @refLeafExp.setter
        def refLeafExp(self, value: float) -> None: ...
        @property
        def minTempDevWE(self) -> float: ...
        @minTempDevWE.setter
        def minTempDevWE(self, value: float) -> None: ...
        @property
        def optTempDevWE(self) -> float: ...
        @optTempDevWE.setter
        def optTempDevWE(self, value: float) -> None: ...
        @property
        def maxTempDevWE(self) -> float: ...
        @maxTempDevWE.setter
        def maxTempDevWE(self, value: float) -> None: ...
        @property
        def winterCrop(self) -> bool: ...
        @winterCrop.setter
        def winterCrop(self, value: bool) -> None: ...
        @override
        @overload
        def init(
            self, field: Literal["assimilatePartitioningCoeff"], size: int | None = None
        ) -> Float64ListListBuilder: ...
        @overload
        def init(
            self, field: Literal["organSenescenceRate"], size: int | None = None
        ) -> Float64ListListBuilder: ...
        @overload
        def init(
            self, field: Literal["baseDaylength"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["optimumTemperature"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["daylengthRequirement"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["droughtStressThreshold"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["specificLeafArea"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["stageKcFactor"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["stageTemperatureSum"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["vernalisationRequirement"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["organIdsForPrimaryYield"], size: int | None = None
        ) -> YieldComponentListBuilder: ...
        @overload
        def init(
            self, field: Literal["organIdsForSecondaryYield"], size: int | None = None
        ) -> YieldComponentListBuilder: ...
        @overload
        def init(
            self, field: Literal["organIdsForCutting"], size: int | None = None
        ) -> YieldComponentListBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> CultivarParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        cultivarId: str | None = None,
        description: str | None = None,
        perennial: bool | None = None,
        maxAssimilationRate: float | None = None,
        maxCropHeight: float | None = None,
        residueNRatio: float | None = None,
        lt50cultivar: float | None = None,
        cropHeightP1: float | None = None,
        cropHeightP2: float | None = None,
        cropSpecificMaxRootingDepth: float | None = None,
        assimilatePartitioningCoeff: Float64ListListBuilder
        | dict[str, Any]
        | None = None,
        organSenescenceRate: Float64ListListBuilder | dict[str, Any] | None = None,
        baseDaylength: Float64ListBuilder | dict[str, Any] | None = None,
        optimumTemperature: Float64ListBuilder | dict[str, Any] | None = None,
        daylengthRequirement: Float64ListBuilder | dict[str, Any] | None = None,
        droughtStressThreshold: Float64ListBuilder | dict[str, Any] | None = None,
        specificLeafArea: Float64ListBuilder | dict[str, Any] | None = None,
        stageKcFactor: Float64ListBuilder | dict[str, Any] | None = None,
        stageTemperatureSum: Float64ListBuilder | dict[str, Any] | None = None,
        vernalisationRequirement: Float64ListBuilder | dict[str, Any] | None = None,
        heatSumIrrigationStart: float | None = None,
        heatSumIrrigationEnd: float | None = None,
        criticalTemperatureHeatStress: float | None = None,
        beginSensitivePhaseHeatStress: float | None = None,
        endSensitivePhaseHeatStress: float | None = None,
        frostHardening: float | None = None,
        frostDehardening: float | None = None,
        lowTemperatureExposure: float | None = None,
        respiratoryStress: float | None = None,
        latestHarvestDoy: int | None = None,
        organIdsForPrimaryYield: YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        organIdsForSecondaryYield: YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        organIdsForCutting: YieldComponentListBuilder | dict[str, Any] | None = None,
        earlyRefLeafExp: float | None = None,
        refLeafExp: float | None = None,
        minTempDevWE: float | None = None,
        optTempDevWE: float | None = None,
        maxTempDevWE: float | None = None,
        winterCrop: bool | None = None,
        **kwargs: Any,
    ) -> CultivarParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[CultivarParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[CultivarParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[CultivarParametersBuilder]: ...
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
    ) -> CultivarParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> CultivarParametersReader: ...

CultivarParameters: _CultivarParametersStructModule

class _CropParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def speciesParams(self) -> SpeciesParametersReader: ...
        @property
        def cultivarParams(self) -> CultivarParametersReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> CropParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def speciesParams(self) -> SpeciesParametersBuilder: ...
        @speciesParams.setter
        def speciesParams(
            self,
            value: SpeciesParametersBuilder | SpeciesParametersReader | dict[str, Any],
        ) -> None: ...
        @property
        def cultivarParams(self) -> CultivarParametersBuilder: ...
        @cultivarParams.setter
        def cultivarParams(
            self,
            value: CultivarParametersBuilder
            | CultivarParametersReader
            | dict[str, Any],
        ) -> None: ...
        @override
        @overload
        def init(
            self, field: Literal["speciesParams"], size: int | None = None
        ) -> SpeciesParametersBuilder: ...
        @overload
        def init(
            self, field: Literal["cultivarParams"], size: int | None = None
        ) -> CultivarParametersBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> CropParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        speciesParams: SpeciesParametersBuilder | dict[str, Any] | None = None,
        cultivarParams: CultivarParametersBuilder | dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> CropParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[CropParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[CropParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[CropParametersBuilder]: ...
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
    ) -> CropParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> CropParametersReader: ...

CropParameters: _CropParametersStructModule

class _CropResidueParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def params(
            self,
        ) -> _ParamsStructModule._OrganicFertilizationStructModule._OrganicMatterParametersStructModule.Reader: ...
        @property
        def species(self) -> str: ...
        @property
        def residueType(self) -> str: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> CropResidueParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def params(
            self,
        ) -> _ParamsStructModule._OrganicFertilizationStructModule._OrganicMatterParametersStructModule.Builder: ...
        @params.setter
        def params(
            self,
            value: _ParamsStructModule._OrganicFertilizationStructModule._OrganicMatterParametersStructModule.Builder
            | _ParamsStructModule._OrganicFertilizationStructModule._OrganicMatterParametersStructModule.Reader
            | dict[str, Any],
        ) -> None: ...
        @property
        def species(self) -> str: ...
        @species.setter
        def species(self, value: str) -> None: ...
        @property
        def residueType(self) -> str: ...
        @residueType.setter
        def residueType(self, value: str) -> None: ...
        @override
        def init(
            self, field: Literal["params"], size: int | None = None
        ) -> _ParamsStructModule._OrganicFertilizationStructModule._OrganicMatterParametersStructModule.Builder: ...
        @override
        def as_reader(self) -> CropResidueParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        params: _ParamsStructModule._OrganicFertilizationStructModule._OrganicMatterParametersStructModule.Builder
        | dict[str, Any]
        | None = None,
        species: str | None = None,
        residueType: str | None = None,
        **kwargs: Any,
    ) -> CropResidueParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[CropResidueParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[CropResidueParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[CropResidueParametersBuilder]: ...
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
    ) -> CropResidueParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> CropResidueParametersReader: ...

CropResidueParameters: _CropResidueParametersStructModule

class _CropSpecStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def cropParams(self) -> CropParametersReader: ...
        @property
        def residueParams(self) -> CropResidueParametersReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> CropSpecBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def cropParams(self) -> CropParametersBuilder: ...
        @cropParams.setter
        def cropParams(
            self, value: CropParametersBuilder | CropParametersReader | dict[str, Any]
        ) -> None: ...
        @property
        def residueParams(self) -> CropResidueParametersBuilder: ...
        @residueParams.setter
        def residueParams(
            self,
            value: CropResidueParametersBuilder
            | CropResidueParametersReader
            | dict[str, Any],
        ) -> None: ...
        @override
        @overload
        def init(
            self, field: Literal["cropParams"], size: int | None = None
        ) -> CropParametersBuilder: ...
        @overload
        def init(
            self, field: Literal["residueParams"], size: int | None = None
        ) -> CropResidueParametersBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> CropSpecReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        cropParams: CropParametersBuilder | dict[str, Any] | None = None,
        residueParams: CropResidueParametersBuilder | dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> CropSpecBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[CropSpecReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[CropSpecReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[CropSpecBuilder]: ...
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
    ) -> CropSpecReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> CropSpecReader: ...

CropSpec: _CropSpecStructModule

class _AutomaticHarvestParametersStructModule(_StructModule):
    class _HarvestTimeEnumModule:
        maturity: int
        unknown: int

    HarvestTime: _HarvestTimeEnumModule
    class Reader(_DynamicStructReader):
        @property
        def harvestTime(self) -> AutomaticHarvestParametersHarvestTimeEnum: ...
        @property
        def latestHarvestDOY(self) -> int: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> AutomaticHarvestParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def harvestTime(self) -> AutomaticHarvestParametersHarvestTimeEnum: ...
        @harvestTime.setter
        def harvestTime(
            self, value: AutomaticHarvestParametersHarvestTimeEnum
        ) -> None: ...
        @property
        def latestHarvestDOY(self) -> int: ...
        @latestHarvestDOY.setter
        def latestHarvestDOY(self, value: int) -> None: ...
        @override
        def as_reader(self) -> AutomaticHarvestParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        harvestTime: AutomaticHarvestParametersHarvestTimeEnum | None = None,
        latestHarvestDOY: int | None = None,
        **kwargs: Any,
    ) -> AutomaticHarvestParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[AutomaticHarvestParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[AutomaticHarvestParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[AutomaticHarvestParametersBuilder]: ...
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
    ) -> AutomaticHarvestParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AutomaticHarvestParametersReader: ...

AutomaticHarvestParameters: _AutomaticHarvestParametersStructModule

class _NMinCropParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def samplingDepth(self) -> float: ...
        @property
        def nTarget(self) -> float: ...
        @property
        def nTarget30(self) -> float: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> NMinCropParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def samplingDepth(self) -> float: ...
        @samplingDepth.setter
        def samplingDepth(self, value: float) -> None: ...
        @property
        def nTarget(self) -> float: ...
        @nTarget.setter
        def nTarget(self, value: float) -> None: ...
        @property
        def nTarget30(self) -> float: ...
        @nTarget30.setter
        def nTarget30(self, value: float) -> None: ...
        @override
        def as_reader(self) -> NMinCropParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        samplingDepth: float | None = None,
        nTarget: float | None = None,
        nTarget30: float | None = None,
        **kwargs: Any,
    ) -> NMinCropParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[NMinCropParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[NMinCropParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[NMinCropParametersBuilder]: ...
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
    ) -> NMinCropParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> NMinCropParametersReader: ...

NMinCropParameters: _NMinCropParametersStructModule

class _NMinApplicationParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def min(self) -> float: ...
        @property
        def max(self) -> float: ...
        @property
        def delayInDays(self) -> int: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> NMinApplicationParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def min(self) -> float: ...
        @min.setter
        def min(self, value: float) -> None: ...
        @property
        def max(self) -> float: ...
        @max.setter
        def max(self, value: float) -> None: ...
        @property
        def delayInDays(self) -> int: ...
        @delayInDays.setter
        def delayInDays(self, value: int) -> None: ...
        @override
        def as_reader(self) -> NMinApplicationParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        min: float | None = None,
        max: float | None = None,
        delayInDays: int | None = None,
        **kwargs: Any,
    ) -> NMinApplicationParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[NMinApplicationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[NMinApplicationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[NMinApplicationParametersBuilder]: ...
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
    ) -> NMinApplicationParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> NMinApplicationParametersReader: ...

NMinApplicationParameters: _NMinApplicationParametersStructModule

class _SoilParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def soilSandContent(self) -> float: ...
        @property
        def soilClayContent(self) -> float: ...
        @property
        def soilpH(self) -> float: ...
        @property
        def soilStoneContent(self) -> float: ...
        @property
        def lambda_(self) -> float: ...
        @property
        def fieldCapacity(self) -> float: ...
        @property
        def saturation(self) -> float: ...
        @property
        def permanentWiltingPoint(self) -> float: ...
        @property
        def soilTexture(self) -> str: ...
        @property
        def soilAmmonium(self) -> float: ...
        @property
        def soilNitrate(self) -> float: ...
        @property
        def soilCNRatio(self) -> float: ...
        @property
        def soilMoisturePercentFC(self) -> float: ...
        @property
        def soilRawDensity(self) -> float: ...
        @property
        def soilBulkDensity(self) -> float: ...
        @property
        def soilOrganicCarbon(self) -> float: ...
        @property
        def soilOrganicMatter(self) -> float: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> SoilParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def soilSandContent(self) -> float: ...
        @soilSandContent.setter
        def soilSandContent(self, value: float) -> None: ...
        @property
        def soilClayContent(self) -> float: ...
        @soilClayContent.setter
        def soilClayContent(self, value: float) -> None: ...
        @property
        def soilpH(self) -> float: ...
        @soilpH.setter
        def soilpH(self, value: float) -> None: ...
        @property
        def soilStoneContent(self) -> float: ...
        @soilStoneContent.setter
        def soilStoneContent(self, value: float) -> None: ...
        @property
        def lambda_(self) -> float: ...
        @lambda_.setter
        def lambda_(self, value: float) -> None: ...
        @property
        def fieldCapacity(self) -> float: ...
        @fieldCapacity.setter
        def fieldCapacity(self, value: float) -> None: ...
        @property
        def saturation(self) -> float: ...
        @saturation.setter
        def saturation(self, value: float) -> None: ...
        @property
        def permanentWiltingPoint(self) -> float: ...
        @permanentWiltingPoint.setter
        def permanentWiltingPoint(self, value: float) -> None: ...
        @property
        def soilTexture(self) -> str: ...
        @soilTexture.setter
        def soilTexture(self, value: str) -> None: ...
        @property
        def soilAmmonium(self) -> float: ...
        @soilAmmonium.setter
        def soilAmmonium(self, value: float) -> None: ...
        @property
        def soilNitrate(self) -> float: ...
        @soilNitrate.setter
        def soilNitrate(self, value: float) -> None: ...
        @property
        def soilCNRatio(self) -> float: ...
        @soilCNRatio.setter
        def soilCNRatio(self, value: float) -> None: ...
        @property
        def soilMoisturePercentFC(self) -> float: ...
        @soilMoisturePercentFC.setter
        def soilMoisturePercentFC(self, value: float) -> None: ...
        @property
        def soilRawDensity(self) -> float: ...
        @soilRawDensity.setter
        def soilRawDensity(self, value: float) -> None: ...
        @property
        def soilBulkDensity(self) -> float: ...
        @soilBulkDensity.setter
        def soilBulkDensity(self, value: float) -> None: ...
        @property
        def soilOrganicCarbon(self) -> float: ...
        @soilOrganicCarbon.setter
        def soilOrganicCarbon(self, value: float) -> None: ...
        @property
        def soilOrganicMatter(self) -> float: ...
        @soilOrganicMatter.setter
        def soilOrganicMatter(self, value: float) -> None: ...
        @override
        def as_reader(self) -> SoilParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        soilSandContent: float | None = None,
        soilClayContent: float | None = None,
        soilpH: float | None = None,
        soilStoneContent: float | None = None,
        lambda_: float | None = None,
        fieldCapacity: float | None = None,
        saturation: float | None = None,
        permanentWiltingPoint: float | None = None,
        soilTexture: str | None = None,
        soilAmmonium: float | None = None,
        soilNitrate: float | None = None,
        soilCNRatio: float | None = None,
        soilMoisturePercentFC: float | None = None,
        soilRawDensity: float | None = None,
        soilBulkDensity: float | None = None,
        soilOrganicCarbon: float | None = None,
        soilOrganicMatter: float | None = None,
        **kwargs: Any,
    ) -> SoilParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[SoilParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SoilParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SoilParametersBuilder]: ...
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
    ) -> SoilParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SoilParametersReader: ...

SoilParameters: _SoilParametersStructModule

class _AutomaticIrrigationParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def params(
            self,
        ) -> (
            _ParamsStructModule._IrrigationStructModule._ParametersStructModule.Reader
        ): ...
        @property
        def amount(self) -> float: ...
        @property
        def threshold(self) -> float: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> AutomaticIrrigationParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
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
        @property
        def amount(self) -> float: ...
        @amount.setter
        def amount(self, value: float) -> None: ...
        @property
        def threshold(self) -> float: ...
        @threshold.setter
        def threshold(self, value: float) -> None: ...
        @override
        def init(
            self, field: Literal["params"], size: int | None = None
        ) -> (
            _ParamsStructModule._IrrigationStructModule._ParametersStructModule.Builder
        ): ...
        @override
        def as_reader(self) -> AutomaticIrrigationParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        params: _ParamsStructModule._IrrigationStructModule._ParametersStructModule.Builder
        | dict[str, Any]
        | None = None,
        amount: float | None = None,
        threshold: float | None = None,
        **kwargs: Any,
    ) -> AutomaticIrrigationParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[AutomaticIrrigationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[AutomaticIrrigationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[AutomaticIrrigationParametersBuilder]: ...
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
    ) -> AutomaticIrrigationParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AutomaticIrrigationParametersReader: ...

AutomaticIrrigationParameters: _AutomaticIrrigationParametersStructModule

class _SoilParametersList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> SoilParametersReader: ...
        @override
        def __iter__(self) -> Iterator[SoilParametersReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> SoilParametersBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: SoilParametersReader | SoilParametersBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[SoilParametersBuilder]: ...
        @override
        def init(
            self, index: int, size: int | None = None
        ) -> SoilParametersBuilder: ...

class _SiteParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def latitude(self) -> float: ...
        @property
        def slope(self) -> float: ...
        @property
        def heightNN(self) -> float: ...
        @property
        def groundwaterDepth(self) -> float: ...
        @property
        def soilCNRatio(self) -> float: ...
        @property
        def drainageCoeff(self) -> float: ...
        @property
        def vqNDeposition(self) -> float: ...
        @property
        def maxEffectiveRootingDepth(self) -> float: ...
        @property
        def impenetrableLayerDepth(self) -> float: ...
        @property
        def soilSpecificHumusBalanceCorrection(self) -> float: ...
        @property
        def soilParameters(self) -> SoilParametersListReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> SiteParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def latitude(self) -> float: ...
        @latitude.setter
        def latitude(self, value: float) -> None: ...
        @property
        def slope(self) -> float: ...
        @slope.setter
        def slope(self, value: float) -> None: ...
        @property
        def heightNN(self) -> float: ...
        @heightNN.setter
        def heightNN(self, value: float) -> None: ...
        @property
        def groundwaterDepth(self) -> float: ...
        @groundwaterDepth.setter
        def groundwaterDepth(self, value: float) -> None: ...
        @property
        def soilCNRatio(self) -> float: ...
        @soilCNRatio.setter
        def soilCNRatio(self, value: float) -> None: ...
        @property
        def drainageCoeff(self) -> float: ...
        @drainageCoeff.setter
        def drainageCoeff(self, value: float) -> None: ...
        @property
        def vqNDeposition(self) -> float: ...
        @vqNDeposition.setter
        def vqNDeposition(self, value: float) -> None: ...
        @property
        def maxEffectiveRootingDepth(self) -> float: ...
        @maxEffectiveRootingDepth.setter
        def maxEffectiveRootingDepth(self, value: float) -> None: ...
        @property
        def impenetrableLayerDepth(self) -> float: ...
        @impenetrableLayerDepth.setter
        def impenetrableLayerDepth(self, value: float) -> None: ...
        @property
        def soilSpecificHumusBalanceCorrection(self) -> float: ...
        @soilSpecificHumusBalanceCorrection.setter
        def soilSpecificHumusBalanceCorrection(self, value: float) -> None: ...
        @property
        def soilParameters(self) -> SoilParametersListBuilder: ...
        @soilParameters.setter
        def soilParameters(
            self,
            value: SoilParametersListBuilder
            | SoilParametersListReader
            | dict[str, Any],
        ) -> None: ...
        @override
        def init(
            self, field: Literal["soilParameters"], size: int | None = None
        ) -> SoilParametersListBuilder: ...
        @override
        def as_reader(self) -> SiteParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        latitude: float | None = None,
        slope: float | None = None,
        heightNN: float | None = None,
        groundwaterDepth: float | None = None,
        soilCNRatio: float | None = None,
        drainageCoeff: float | None = None,
        vqNDeposition: float | None = None,
        maxEffectiveRootingDepth: float | None = None,
        impenetrableLayerDepth: float | None = None,
        soilSpecificHumusBalanceCorrection: float | None = None,
        soilParameters: SoilParametersListBuilder | dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> SiteParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[SiteParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SiteParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SiteParametersBuilder]: ...
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
    ) -> SiteParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SiteParametersReader: ...

SiteParameters: _SiteParametersStructModule

class _YearToValueList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> YearToValueReader: ...
        @override
        def __iter__(self) -> Iterator[YearToValueReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> YearToValueBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: YearToValueReader | YearToValueBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[YearToValueBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> YearToValueBuilder: ...

class _EnvironmentParametersStructModule(_StructModule):
    class _YearToValueStructModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def year(self) -> int: ...
            @property
            def value(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
            ) -> YearToValueBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def year(self) -> int: ...
            @year.setter
            def year(self, value: int) -> None: ...
            @property
            def value(self) -> float: ...
            @value.setter
            def value(self, value: float) -> None: ...
            @override
            def as_reader(self) -> YearToValueReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            year: int | None = None,
            value: float | None = None,
            **kwargs: Any,
        ) -> YearToValueBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[YearToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[YearToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[YearToValueBuilder]: ...
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
        ) -> YearToValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> YearToValueReader: ...

    type YearToValueReader = _YearToValueStructModule.Reader
    type YearToValueBuilder = _YearToValueStructModule.Builder
    YearToValue: _YearToValueStructModule
    class Reader(_DynamicStructReader):
        @property
        def albedo(self) -> float: ...
        @property
        def atmosphericCO2(self) -> float: ...
        @property
        def atmosphericCO2s(self) -> YearToValueListReader: ...
        @property
        def atmosphericO3(self) -> float: ...
        @property
        def atmosphericO3s(self) -> YearToValueListReader: ...
        @property
        def windSpeedHeight(self) -> float: ...
        @property
        def leachingDepth(self) -> float: ...
        @property
        def timeStep(self) -> float: ...
        @property
        def maxGroundwaterDepth(self) -> float: ...
        @property
        def minGroundwaterDepth(self) -> float: ...
        @property
        def minGroundwaterDepthMonth(self) -> int: ...
        @property
        def rcp(self) -> RCPEnum: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> EnvironmentParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def albedo(self) -> float: ...
        @albedo.setter
        def albedo(self, value: float) -> None: ...
        @property
        def atmosphericCO2(self) -> float: ...
        @atmosphericCO2.setter
        def atmosphericCO2(self, value: float) -> None: ...
        @property
        def atmosphericCO2s(self) -> YearToValueListBuilder: ...
        @atmosphericCO2s.setter
        def atmosphericCO2s(
            self, value: YearToValueListBuilder | YearToValueListReader | dict[str, Any]
        ) -> None: ...
        @property
        def atmosphericO3(self) -> float: ...
        @atmosphericO3.setter
        def atmosphericO3(self, value: float) -> None: ...
        @property
        def atmosphericO3s(self) -> YearToValueListBuilder: ...
        @atmosphericO3s.setter
        def atmosphericO3s(
            self, value: YearToValueListBuilder | YearToValueListReader | dict[str, Any]
        ) -> None: ...
        @property
        def windSpeedHeight(self) -> float: ...
        @windSpeedHeight.setter
        def windSpeedHeight(self, value: float) -> None: ...
        @property
        def leachingDepth(self) -> float: ...
        @leachingDepth.setter
        def leachingDepth(self, value: float) -> None: ...
        @property
        def timeStep(self) -> float: ...
        @timeStep.setter
        def timeStep(self, value: float) -> None: ...
        @property
        def maxGroundwaterDepth(self) -> float: ...
        @maxGroundwaterDepth.setter
        def maxGroundwaterDepth(self, value: float) -> None: ...
        @property
        def minGroundwaterDepth(self) -> float: ...
        @minGroundwaterDepth.setter
        def minGroundwaterDepth(self, value: float) -> None: ...
        @property
        def minGroundwaterDepthMonth(self) -> int: ...
        @minGroundwaterDepthMonth.setter
        def minGroundwaterDepthMonth(self, value: int) -> None: ...
        @property
        def rcp(self) -> RCPEnum: ...
        @rcp.setter
        def rcp(self, value: RCPEnum) -> None: ...
        @override
        @overload
        def init(
            self, field: Literal["atmosphericCO2s"], size: int | None = None
        ) -> YearToValueListBuilder: ...
        @overload
        def init(
            self, field: Literal["atmosphericO3s"], size: int | None = None
        ) -> YearToValueListBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> EnvironmentParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        albedo: float | None = None,
        atmosphericCO2: float | None = None,
        atmosphericCO2s: YearToValueListBuilder | dict[str, Any] | None = None,
        atmosphericO3: float | None = None,
        atmosphericO3s: YearToValueListBuilder | dict[str, Any] | None = None,
        windSpeedHeight: float | None = None,
        leachingDepth: float | None = None,
        timeStep: float | None = None,
        maxGroundwaterDepth: float | None = None,
        minGroundwaterDepth: float | None = None,
        minGroundwaterDepthMonth: int | None = None,
        rcp: RCPEnum | None = None,
        **kwargs: Any,
    ) -> EnvironmentParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[EnvironmentParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[EnvironmentParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[EnvironmentParametersBuilder]: ...
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
    ) -> EnvironmentParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> EnvironmentParametersReader: ...

EnvironmentParameters: _EnvironmentParametersStructModule

class _DateToValueList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> DateToValueReader: ...
        @override
        def __iter__(self) -> Iterator[DateToValueReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> DateToValueBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: DateToValueReader | DateToValueBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[DateToValueBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> DateToValueBuilder: ...

class _MeasuredGroundwaterTableInformationStructModule(_StructModule):
    class _DateToValueStructModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def date(self) -> DateReader: ...
            @property
            def value(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
            ) -> DateToValueBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def date(self) -> DateBuilder: ...
            @date.setter
            def date(
                self, value: DateBuilder | DateReader | dict[str, Any]
            ) -> None: ...
            @property
            def value(self) -> float: ...
            @value.setter
            def value(self, value: float) -> None: ...
            @override
            def init(
                self, field: Literal["date"], size: int | None = None
            ) -> DateBuilder: ...
            @override
            def as_reader(self) -> DateToValueReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            date: DateBuilder | dict[str, Any] | None = None,
            value: float | None = None,
            **kwargs: Any,
        ) -> DateToValueBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[DateToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[DateToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[DateToValueBuilder]: ...
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
        ) -> DateToValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> DateToValueReader: ...

    type DateToValueReader = _DateToValueStructModule.Reader
    type DateToValueBuilder = _DateToValueStructModule.Builder
    DateToValue: _DateToValueStructModule
    class Reader(_DynamicStructReader):
        @property
        def groundwaterInformationAvailable(self) -> bool: ...
        @property
        def groundwaterInfo(self) -> DateToValueListReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> MeasuredGroundwaterTableInformationBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def groundwaterInformationAvailable(self) -> bool: ...
        @groundwaterInformationAvailable.setter
        def groundwaterInformationAvailable(self, value: bool) -> None: ...
        @property
        def groundwaterInfo(self) -> DateToValueListBuilder: ...
        @groundwaterInfo.setter
        def groundwaterInfo(
            self, value: DateToValueListBuilder | DateToValueListReader | dict[str, Any]
        ) -> None: ...
        @override
        def init(
            self, field: Literal["groundwaterInfo"], size: int | None = None
        ) -> DateToValueListBuilder: ...
        @override
        def as_reader(self) -> MeasuredGroundwaterTableInformationReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        groundwaterInformationAvailable: bool | None = None,
        groundwaterInfo: DateToValueListBuilder | dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> MeasuredGroundwaterTableInformationBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[MeasuredGroundwaterTableInformationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[MeasuredGroundwaterTableInformationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[MeasuredGroundwaterTableInformationBuilder]: ...
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
    ) -> MeasuredGroundwaterTableInformationReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> MeasuredGroundwaterTableInformationReader: ...

MeasuredGroundwaterTableInformation: _MeasuredGroundwaterTableInformationStructModule

class _SimulationParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def startDate(self) -> DateReader: ...
        @property
        def endDate(self) -> DateReader: ...
        @property
        def nitrogenResponseOn(self) -> bool: ...
        @property
        def waterDeficitResponseOn(self) -> bool: ...
        @property
        def emergenceFloodingControlOn(self) -> bool: ...
        @property
        def emergenceMoistureControlOn(self) -> bool: ...
        @property
        def frostKillOn(self) -> bool: ...
        @property
        def useAutomaticIrrigation(self) -> bool: ...
        @property
        def autoIrrigationParams(self) -> AutomaticIrrigationParametersReader: ...
        @property
        def useNMinMineralFertilisingMethod(self) -> bool: ...
        @property
        def nMinFertiliserPartition(
            self,
        ) -> _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Reader: ...
        @property
        def nMinApplicationParams(self) -> NMinApplicationParametersReader: ...
        @property
        def useSecondaryYields(self) -> bool: ...
        @property
        def useAutomaticHarvestTrigger(self) -> bool: ...
        @property
        def numberOfLayers(self) -> int: ...
        @property
        def layerThickness(self) -> float: ...
        @property
        def startPVIndex(self) -> int: ...
        @property
        def julianDayAutomaticFertilising(self) -> int: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> SimulationParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def startDate(self) -> DateBuilder: ...
        @startDate.setter
        def startDate(
            self, value: DateBuilder | DateReader | dict[str, Any]
        ) -> None: ...
        @property
        def endDate(self) -> DateBuilder: ...
        @endDate.setter
        def endDate(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
        @property
        def nitrogenResponseOn(self) -> bool: ...
        @nitrogenResponseOn.setter
        def nitrogenResponseOn(self, value: bool) -> None: ...
        @property
        def waterDeficitResponseOn(self) -> bool: ...
        @waterDeficitResponseOn.setter
        def waterDeficitResponseOn(self, value: bool) -> None: ...
        @property
        def emergenceFloodingControlOn(self) -> bool: ...
        @emergenceFloodingControlOn.setter
        def emergenceFloodingControlOn(self, value: bool) -> None: ...
        @property
        def emergenceMoistureControlOn(self) -> bool: ...
        @emergenceMoistureControlOn.setter
        def emergenceMoistureControlOn(self, value: bool) -> None: ...
        @property
        def frostKillOn(self) -> bool: ...
        @frostKillOn.setter
        def frostKillOn(self, value: bool) -> None: ...
        @property
        def useAutomaticIrrigation(self) -> bool: ...
        @useAutomaticIrrigation.setter
        def useAutomaticIrrigation(self, value: bool) -> None: ...
        @property
        def autoIrrigationParams(self) -> AutomaticIrrigationParametersBuilder: ...
        @autoIrrigationParams.setter
        def autoIrrigationParams(
            self,
            value: AutomaticIrrigationParametersBuilder
            | AutomaticIrrigationParametersReader
            | dict[str, Any],
        ) -> None: ...
        @property
        def useNMinMineralFertilisingMethod(self) -> bool: ...
        @useNMinMineralFertilisingMethod.setter
        def useNMinMineralFertilisingMethod(self, value: bool) -> None: ...
        @property
        def nMinFertiliserPartition(
            self,
        ) -> _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder: ...
        @nMinFertiliserPartition.setter
        def nMinFertiliserPartition(
            self,
            value: _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder
            | _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Reader
            | dict[str, Any],
        ) -> None: ...
        @property
        def nMinApplicationParams(self) -> NMinApplicationParametersBuilder: ...
        @nMinApplicationParams.setter
        def nMinApplicationParams(
            self,
            value: NMinApplicationParametersBuilder
            | NMinApplicationParametersReader
            | dict[str, Any],
        ) -> None: ...
        @property
        def useSecondaryYields(self) -> bool: ...
        @useSecondaryYields.setter
        def useSecondaryYields(self, value: bool) -> None: ...
        @property
        def useAutomaticHarvestTrigger(self) -> bool: ...
        @useAutomaticHarvestTrigger.setter
        def useAutomaticHarvestTrigger(self, value: bool) -> None: ...
        @property
        def numberOfLayers(self) -> int: ...
        @numberOfLayers.setter
        def numberOfLayers(self, value: int) -> None: ...
        @property
        def layerThickness(self) -> float: ...
        @layerThickness.setter
        def layerThickness(self, value: float) -> None: ...
        @property
        def startPVIndex(self) -> int: ...
        @startPVIndex.setter
        def startPVIndex(self, value: int) -> None: ...
        @property
        def julianDayAutomaticFertilising(self) -> int: ...
        @julianDayAutomaticFertilising.setter
        def julianDayAutomaticFertilising(self, value: int) -> None: ...
        @override
        @overload
        def init(
            self, field: Literal["startDate"], size: int | None = None
        ) -> DateBuilder: ...
        @overload
        def init(
            self, field: Literal["endDate"], size: int | None = None
        ) -> DateBuilder: ...
        @overload
        def init(
            self, field: Literal["autoIrrigationParams"], size: int | None = None
        ) -> AutomaticIrrigationParametersBuilder: ...
        @overload
        def init(
            self, field: Literal["nMinFertiliserPartition"], size: int | None = None
        ) -> _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder: ...
        @overload
        def init(
            self, field: Literal["nMinApplicationParams"], size: int | None = None
        ) -> NMinApplicationParametersBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> SimulationParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        startDate: DateBuilder | dict[str, Any] | None = None,
        endDate: DateBuilder | dict[str, Any] | None = None,
        nitrogenResponseOn: bool | None = None,
        waterDeficitResponseOn: bool | None = None,
        emergenceFloodingControlOn: bool | None = None,
        emergenceMoistureControlOn: bool | None = None,
        frostKillOn: bool | None = None,
        useAutomaticIrrigation: bool | None = None,
        autoIrrigationParams: AutomaticIrrigationParametersBuilder
        | dict[str, Any]
        | None = None,
        useNMinMineralFertilisingMethod: bool | None = None,
        nMinFertiliserPartition: _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder
        | dict[str, Any]
        | None = None,
        nMinApplicationParams: NMinApplicationParametersBuilder
        | dict[str, Any]
        | None = None,
        useSecondaryYields: bool | None = None,
        useAutomaticHarvestTrigger: bool | None = None,
        numberOfLayers: int | None = None,
        layerThickness: float | None = None,
        startPVIndex: int | None = None,
        julianDayAutomaticFertilising: int | None = None,
        **kwargs: Any,
    ) -> SimulationParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[SimulationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SimulationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SimulationParametersBuilder]: ...
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
    ) -> SimulationParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SimulationParametersReader: ...

SimulationParameters: _SimulationParametersStructModule

class _CropModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def canopyReflectionCoefficient(self) -> float: ...
        @property
        def referenceMaxAssimilationRate(self) -> float: ...
        @property
        def referenceLeafAreaIndex(self) -> float: ...
        @property
        def maintenanceRespirationParameter1(self) -> float: ...
        @property
        def maintenanceRespirationParameter2(self) -> float: ...
        @property
        def minimumNConcentrationRoot(self) -> float: ...
        @property
        def minimumAvailableN(self) -> float: ...
        @property
        def referenceAlbedo(self) -> float: ...
        @property
        def stomataConductanceAlpha(self) -> float: ...
        @property
        def saturationBeta(self) -> float: ...
        @property
        def growthRespirationRedux(self) -> float: ...
        @property
        def maxCropNDemand(self) -> float: ...
        @property
        def growthRespirationParameter1(self) -> float: ...
        @property
        def growthRespirationParameter2(self) -> float: ...
        @property
        def tortuosity(self) -> float: ...
        @property
        def adjustRootDepthForSoilProps(self) -> bool: ...
        @property
        def experimentalEnablePhenologyWangEngelTemperatureResponse(self) -> bool: ...
        @property
        def experimentalEnablePhotosynthesisWangEngelTemperatureResponse(
            self,
        ) -> bool: ...
        @property
        def experimentalEnableHourlyFvCBPhotosynthesis(self) -> bool: ...
        @property
        def experimentalEnableTResponseLeafExpansion(self) -> bool: ...
        @property
        def experimentalDisableDailyRootBiomassToSoil(self) -> bool: ...
        @property
        def enableVernalisationFactorFix(self) -> bool: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> CropModuleParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def canopyReflectionCoefficient(self) -> float: ...
        @canopyReflectionCoefficient.setter
        def canopyReflectionCoefficient(self, value: float) -> None: ...
        @property
        def referenceMaxAssimilationRate(self) -> float: ...
        @referenceMaxAssimilationRate.setter
        def referenceMaxAssimilationRate(self, value: float) -> None: ...
        @property
        def referenceLeafAreaIndex(self) -> float: ...
        @referenceLeafAreaIndex.setter
        def referenceLeafAreaIndex(self, value: float) -> None: ...
        @property
        def maintenanceRespirationParameter1(self) -> float: ...
        @maintenanceRespirationParameter1.setter
        def maintenanceRespirationParameter1(self, value: float) -> None: ...
        @property
        def maintenanceRespirationParameter2(self) -> float: ...
        @maintenanceRespirationParameter2.setter
        def maintenanceRespirationParameter2(self, value: float) -> None: ...
        @property
        def minimumNConcentrationRoot(self) -> float: ...
        @minimumNConcentrationRoot.setter
        def minimumNConcentrationRoot(self, value: float) -> None: ...
        @property
        def minimumAvailableN(self) -> float: ...
        @minimumAvailableN.setter
        def minimumAvailableN(self, value: float) -> None: ...
        @property
        def referenceAlbedo(self) -> float: ...
        @referenceAlbedo.setter
        def referenceAlbedo(self, value: float) -> None: ...
        @property
        def stomataConductanceAlpha(self) -> float: ...
        @stomataConductanceAlpha.setter
        def stomataConductanceAlpha(self, value: float) -> None: ...
        @property
        def saturationBeta(self) -> float: ...
        @saturationBeta.setter
        def saturationBeta(self, value: float) -> None: ...
        @property
        def growthRespirationRedux(self) -> float: ...
        @growthRespirationRedux.setter
        def growthRespirationRedux(self, value: float) -> None: ...
        @property
        def maxCropNDemand(self) -> float: ...
        @maxCropNDemand.setter
        def maxCropNDemand(self, value: float) -> None: ...
        @property
        def growthRespirationParameter1(self) -> float: ...
        @growthRespirationParameter1.setter
        def growthRespirationParameter1(self, value: float) -> None: ...
        @property
        def growthRespirationParameter2(self) -> float: ...
        @growthRespirationParameter2.setter
        def growthRespirationParameter2(self, value: float) -> None: ...
        @property
        def tortuosity(self) -> float: ...
        @tortuosity.setter
        def tortuosity(self, value: float) -> None: ...
        @property
        def adjustRootDepthForSoilProps(self) -> bool: ...
        @adjustRootDepthForSoilProps.setter
        def adjustRootDepthForSoilProps(self, value: bool) -> None: ...
        @property
        def experimentalEnablePhenologyWangEngelTemperatureResponse(self) -> bool: ...
        @experimentalEnablePhenologyWangEngelTemperatureResponse.setter
        def experimentalEnablePhenologyWangEngelTemperatureResponse(
            self, value: bool
        ) -> None: ...
        @property
        def experimentalEnablePhotosynthesisWangEngelTemperatureResponse(
            self,
        ) -> bool: ...
        @experimentalEnablePhotosynthesisWangEngelTemperatureResponse.setter
        def experimentalEnablePhotosynthesisWangEngelTemperatureResponse(
            self, value: bool
        ) -> None: ...
        @property
        def experimentalEnableHourlyFvCBPhotosynthesis(self) -> bool: ...
        @experimentalEnableHourlyFvCBPhotosynthesis.setter
        def experimentalEnableHourlyFvCBPhotosynthesis(self, value: bool) -> None: ...
        @property
        def experimentalEnableTResponseLeafExpansion(self) -> bool: ...
        @experimentalEnableTResponseLeafExpansion.setter
        def experimentalEnableTResponseLeafExpansion(self, value: bool) -> None: ...
        @property
        def experimentalDisableDailyRootBiomassToSoil(self) -> bool: ...
        @experimentalDisableDailyRootBiomassToSoil.setter
        def experimentalDisableDailyRootBiomassToSoil(self, value: bool) -> None: ...
        @property
        def enableVernalisationFactorFix(self) -> bool: ...
        @enableVernalisationFactorFix.setter
        def enableVernalisationFactorFix(self, value: bool) -> None: ...
        @override
        def as_reader(self) -> CropModuleParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        canopyReflectionCoefficient: float | None = None,
        referenceMaxAssimilationRate: float | None = None,
        referenceLeafAreaIndex: float | None = None,
        maintenanceRespirationParameter1: float | None = None,
        maintenanceRespirationParameter2: float | None = None,
        minimumNConcentrationRoot: float | None = None,
        minimumAvailableN: float | None = None,
        referenceAlbedo: float | None = None,
        stomataConductanceAlpha: float | None = None,
        saturationBeta: float | None = None,
        growthRespirationRedux: float | None = None,
        maxCropNDemand: float | None = None,
        growthRespirationParameter1: float | None = None,
        growthRespirationParameter2: float | None = None,
        tortuosity: float | None = None,
        adjustRootDepthForSoilProps: bool | None = None,
        experimentalEnablePhenologyWangEngelTemperatureResponse: bool | None = None,
        experimentalEnablePhotosynthesisWangEngelTemperatureResponse: bool
        | None = None,
        experimentalEnableHourlyFvCBPhotosynthesis: bool | None = None,
        experimentalEnableTResponseLeafExpansion: bool | None = None,
        experimentalDisableDailyRootBiomassToSoil: bool | None = None,
        enableVernalisationFactorFix: bool | None = None,
        **kwargs: Any,
    ) -> CropModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[CropModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[CropModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[CropModuleParametersBuilder]: ...
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
    ) -> CropModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> CropModuleParametersReader: ...

CropModuleParameters: _CropModuleParametersStructModule

class _SoilMoistureModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def criticalMoistureDepth(self) -> float: ...
        @property
        def saturatedHydraulicConductivity(self) -> float: ...
        @property
        def surfaceRoughness(self) -> float: ...
        @property
        def groundwaterDischarge(self) -> float: ...
        @property
        def hydraulicConductivityRedux(self) -> float: ...
        @property
        def snowAccumulationTresholdTemperature(self) -> float: ...
        @property
        def kcFactor(self) -> float: ...
        @property
        def temperatureLimitForLiquidWater(self) -> float: ...
        @property
        def correctionSnow(self) -> float: ...
        @property
        def correctionRain(self) -> float: ...
        @property
        def snowMaxAdditionalDensity(self) -> float: ...
        @property
        def newSnowDensityMin(self) -> float: ...
        @property
        def snowRetentionCapacityMin(self) -> float: ...
        @property
        def refreezeParameter1(self) -> float: ...
        @property
        def refreezeParameter2(self) -> float: ...
        @property
        def refreezeTemperature(self) -> float: ...
        @property
        def snowMeltTemperature(self) -> float: ...
        @property
        def snowPacking(self) -> float: ...
        @property
        def snowRetentionCapacityMax(self) -> float: ...
        @property
        def evaporationZeta(self) -> float: ...
        @property
        def xsaCriticalSoilMoisture(self) -> float: ...
        @property
        def maximumEvaporationImpactDepth(self) -> float: ...
        @property
        def maxPercolationRate(self) -> float: ...
        @property
        def moistureInitValue(self) -> float: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> SoilMoistureModuleParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def criticalMoistureDepth(self) -> float: ...
        @criticalMoistureDepth.setter
        def criticalMoistureDepth(self, value: float) -> None: ...
        @property
        def saturatedHydraulicConductivity(self) -> float: ...
        @saturatedHydraulicConductivity.setter
        def saturatedHydraulicConductivity(self, value: float) -> None: ...
        @property
        def surfaceRoughness(self) -> float: ...
        @surfaceRoughness.setter
        def surfaceRoughness(self, value: float) -> None: ...
        @property
        def groundwaterDischarge(self) -> float: ...
        @groundwaterDischarge.setter
        def groundwaterDischarge(self, value: float) -> None: ...
        @property
        def hydraulicConductivityRedux(self) -> float: ...
        @hydraulicConductivityRedux.setter
        def hydraulicConductivityRedux(self, value: float) -> None: ...
        @property
        def snowAccumulationTresholdTemperature(self) -> float: ...
        @snowAccumulationTresholdTemperature.setter
        def snowAccumulationTresholdTemperature(self, value: float) -> None: ...
        @property
        def kcFactor(self) -> float: ...
        @kcFactor.setter
        def kcFactor(self, value: float) -> None: ...
        @property
        def temperatureLimitForLiquidWater(self) -> float: ...
        @temperatureLimitForLiquidWater.setter
        def temperatureLimitForLiquidWater(self, value: float) -> None: ...
        @property
        def correctionSnow(self) -> float: ...
        @correctionSnow.setter
        def correctionSnow(self, value: float) -> None: ...
        @property
        def correctionRain(self) -> float: ...
        @correctionRain.setter
        def correctionRain(self, value: float) -> None: ...
        @property
        def snowMaxAdditionalDensity(self) -> float: ...
        @snowMaxAdditionalDensity.setter
        def snowMaxAdditionalDensity(self, value: float) -> None: ...
        @property
        def newSnowDensityMin(self) -> float: ...
        @newSnowDensityMin.setter
        def newSnowDensityMin(self, value: float) -> None: ...
        @property
        def snowRetentionCapacityMin(self) -> float: ...
        @snowRetentionCapacityMin.setter
        def snowRetentionCapacityMin(self, value: float) -> None: ...
        @property
        def refreezeParameter1(self) -> float: ...
        @refreezeParameter1.setter
        def refreezeParameter1(self, value: float) -> None: ...
        @property
        def refreezeParameter2(self) -> float: ...
        @refreezeParameter2.setter
        def refreezeParameter2(self, value: float) -> None: ...
        @property
        def refreezeTemperature(self) -> float: ...
        @refreezeTemperature.setter
        def refreezeTemperature(self, value: float) -> None: ...
        @property
        def snowMeltTemperature(self) -> float: ...
        @snowMeltTemperature.setter
        def snowMeltTemperature(self, value: float) -> None: ...
        @property
        def snowPacking(self) -> float: ...
        @snowPacking.setter
        def snowPacking(self, value: float) -> None: ...
        @property
        def snowRetentionCapacityMax(self) -> float: ...
        @snowRetentionCapacityMax.setter
        def snowRetentionCapacityMax(self, value: float) -> None: ...
        @property
        def evaporationZeta(self) -> float: ...
        @evaporationZeta.setter
        def evaporationZeta(self, value: float) -> None: ...
        @property
        def xsaCriticalSoilMoisture(self) -> float: ...
        @xsaCriticalSoilMoisture.setter
        def xsaCriticalSoilMoisture(self, value: float) -> None: ...
        @property
        def maximumEvaporationImpactDepth(self) -> float: ...
        @maximumEvaporationImpactDepth.setter
        def maximumEvaporationImpactDepth(self, value: float) -> None: ...
        @property
        def maxPercolationRate(self) -> float: ...
        @maxPercolationRate.setter
        def maxPercolationRate(self, value: float) -> None: ...
        @property
        def moistureInitValue(self) -> float: ...
        @moistureInitValue.setter
        def moistureInitValue(self, value: float) -> None: ...
        @override
        def as_reader(self) -> SoilMoistureModuleParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        criticalMoistureDepth: float | None = None,
        saturatedHydraulicConductivity: float | None = None,
        surfaceRoughness: float | None = None,
        groundwaterDischarge: float | None = None,
        hydraulicConductivityRedux: float | None = None,
        snowAccumulationTresholdTemperature: float | None = None,
        kcFactor: float | None = None,
        temperatureLimitForLiquidWater: float | None = None,
        correctionSnow: float | None = None,
        correctionRain: float | None = None,
        snowMaxAdditionalDensity: float | None = None,
        newSnowDensityMin: float | None = None,
        snowRetentionCapacityMin: float | None = None,
        refreezeParameter1: float | None = None,
        refreezeParameter2: float | None = None,
        refreezeTemperature: float | None = None,
        snowMeltTemperature: float | None = None,
        snowPacking: float | None = None,
        snowRetentionCapacityMax: float | None = None,
        evaporationZeta: float | None = None,
        xsaCriticalSoilMoisture: float | None = None,
        maximumEvaporationImpactDepth: float | None = None,
        maxPercolationRate: float | None = None,
        moistureInitValue: float | None = None,
        **kwargs: Any,
    ) -> SoilMoistureModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[SoilMoistureModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SoilMoistureModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SoilMoistureModuleParametersBuilder]: ...
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
    ) -> SoilMoistureModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SoilMoistureModuleParametersReader: ...

SoilMoistureModuleParameters: _SoilMoistureModuleParametersStructModule

class _SticsParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def useN2O(self) -> bool: ...
        @property
        def useNit(self) -> bool: ...
        @property
        def useDenit(self) -> bool: ...
        @property
        def codeVnit(self) -> int: ...
        @property
        def codeTnit(self) -> int: ...
        @property
        def codeRationit(self) -> int: ...
        @property
        def codeHourlyWfpsNit(self) -> int: ...
        @property
        def codePdenit(self) -> int: ...
        @property
        def codeRatiodenit(self) -> int: ...
        @property
        def codeHourlyWfpsDenit(self) -> int: ...
        @property
        def hminn(self) -> float: ...
        @property
        def hoptn(self) -> float: ...
        @property
        def pHminnit(self) -> float: ...
        @property
        def pHmaxnit(self) -> float: ...
        @property
        def nh4Min(self) -> float: ...
        @property
        def pHminden(self) -> float: ...
        @property
        def pHmaxden(self) -> float: ...
        @property
        def wfpsc(self) -> float: ...
        @property
        def tdenitoptGauss(self) -> float: ...
        @property
        def scaleTdenitopt(self) -> float: ...
        @property
        def kd(self) -> float: ...
        @property
        def kDesat(self) -> float: ...
        @property
        def fnx(self) -> float: ...
        @property
        def vnitmax(self) -> float: ...
        @property
        def kamm(self) -> float: ...
        @property
        def tnitmin(self) -> float: ...
        @property
        def tnitopt(self) -> float: ...
        @property
        def tnitop2(self) -> float: ...
        @property
        def tnitmax(self) -> float: ...
        @property
        def tnitoptGauss(self) -> float: ...
        @property
        def scaleTnitopt(self) -> float: ...
        @property
        def rationit(self) -> float: ...
        @property
        def cminPdenit(self) -> float: ...
        @property
        def cmaxPdenit(self) -> float: ...
        @property
        def minPdenit(self) -> float: ...
        @property
        def maxPdenit(self) -> float: ...
        @property
        def ratiodenit(self) -> float: ...
        @property
        def profdenit(self) -> float: ...
        @property
        def vpotdenit(self) -> float: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> SticsParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def useN2O(self) -> bool: ...
        @useN2O.setter
        def useN2O(self, value: bool) -> None: ...
        @property
        def useNit(self) -> bool: ...
        @useNit.setter
        def useNit(self, value: bool) -> None: ...
        @property
        def useDenit(self) -> bool: ...
        @useDenit.setter
        def useDenit(self, value: bool) -> None: ...
        @property
        def codeVnit(self) -> int: ...
        @codeVnit.setter
        def codeVnit(self, value: int) -> None: ...
        @property
        def codeTnit(self) -> int: ...
        @codeTnit.setter
        def codeTnit(self, value: int) -> None: ...
        @property
        def codeRationit(self) -> int: ...
        @codeRationit.setter
        def codeRationit(self, value: int) -> None: ...
        @property
        def codeHourlyWfpsNit(self) -> int: ...
        @codeHourlyWfpsNit.setter
        def codeHourlyWfpsNit(self, value: int) -> None: ...
        @property
        def codePdenit(self) -> int: ...
        @codePdenit.setter
        def codePdenit(self, value: int) -> None: ...
        @property
        def codeRatiodenit(self) -> int: ...
        @codeRatiodenit.setter
        def codeRatiodenit(self, value: int) -> None: ...
        @property
        def codeHourlyWfpsDenit(self) -> int: ...
        @codeHourlyWfpsDenit.setter
        def codeHourlyWfpsDenit(self, value: int) -> None: ...
        @property
        def hminn(self) -> float: ...
        @hminn.setter
        def hminn(self, value: float) -> None: ...
        @property
        def hoptn(self) -> float: ...
        @hoptn.setter
        def hoptn(self, value: float) -> None: ...
        @property
        def pHminnit(self) -> float: ...
        @pHminnit.setter
        def pHminnit(self, value: float) -> None: ...
        @property
        def pHmaxnit(self) -> float: ...
        @pHmaxnit.setter
        def pHmaxnit(self, value: float) -> None: ...
        @property
        def nh4Min(self) -> float: ...
        @nh4Min.setter
        def nh4Min(self, value: float) -> None: ...
        @property
        def pHminden(self) -> float: ...
        @pHminden.setter
        def pHminden(self, value: float) -> None: ...
        @property
        def pHmaxden(self) -> float: ...
        @pHmaxden.setter
        def pHmaxden(self, value: float) -> None: ...
        @property
        def wfpsc(self) -> float: ...
        @wfpsc.setter
        def wfpsc(self, value: float) -> None: ...
        @property
        def tdenitoptGauss(self) -> float: ...
        @tdenitoptGauss.setter
        def tdenitoptGauss(self, value: float) -> None: ...
        @property
        def scaleTdenitopt(self) -> float: ...
        @scaleTdenitopt.setter
        def scaleTdenitopt(self, value: float) -> None: ...
        @property
        def kd(self) -> float: ...
        @kd.setter
        def kd(self, value: float) -> None: ...
        @property
        def kDesat(self) -> float: ...
        @kDesat.setter
        def kDesat(self, value: float) -> None: ...
        @property
        def fnx(self) -> float: ...
        @fnx.setter
        def fnx(self, value: float) -> None: ...
        @property
        def vnitmax(self) -> float: ...
        @vnitmax.setter
        def vnitmax(self, value: float) -> None: ...
        @property
        def kamm(self) -> float: ...
        @kamm.setter
        def kamm(self, value: float) -> None: ...
        @property
        def tnitmin(self) -> float: ...
        @tnitmin.setter
        def tnitmin(self, value: float) -> None: ...
        @property
        def tnitopt(self) -> float: ...
        @tnitopt.setter
        def tnitopt(self, value: float) -> None: ...
        @property
        def tnitop2(self) -> float: ...
        @tnitop2.setter
        def tnitop2(self, value: float) -> None: ...
        @property
        def tnitmax(self) -> float: ...
        @tnitmax.setter
        def tnitmax(self, value: float) -> None: ...
        @property
        def tnitoptGauss(self) -> float: ...
        @tnitoptGauss.setter
        def tnitoptGauss(self, value: float) -> None: ...
        @property
        def scaleTnitopt(self) -> float: ...
        @scaleTnitopt.setter
        def scaleTnitopt(self, value: float) -> None: ...
        @property
        def rationit(self) -> float: ...
        @rationit.setter
        def rationit(self, value: float) -> None: ...
        @property
        def cminPdenit(self) -> float: ...
        @cminPdenit.setter
        def cminPdenit(self, value: float) -> None: ...
        @property
        def cmaxPdenit(self) -> float: ...
        @cmaxPdenit.setter
        def cmaxPdenit(self, value: float) -> None: ...
        @property
        def minPdenit(self) -> float: ...
        @minPdenit.setter
        def minPdenit(self, value: float) -> None: ...
        @property
        def maxPdenit(self) -> float: ...
        @maxPdenit.setter
        def maxPdenit(self, value: float) -> None: ...
        @property
        def ratiodenit(self) -> float: ...
        @ratiodenit.setter
        def ratiodenit(self, value: float) -> None: ...
        @property
        def profdenit(self) -> float: ...
        @profdenit.setter
        def profdenit(self, value: float) -> None: ...
        @property
        def vpotdenit(self) -> float: ...
        @vpotdenit.setter
        def vpotdenit(self, value: float) -> None: ...
        @override
        def as_reader(self) -> SticsParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        useN2O: bool | None = None,
        useNit: bool | None = None,
        useDenit: bool | None = None,
        codeVnit: int | None = None,
        codeTnit: int | None = None,
        codeRationit: int | None = None,
        codeHourlyWfpsNit: int | None = None,
        codePdenit: int | None = None,
        codeRatiodenit: int | None = None,
        codeHourlyWfpsDenit: int | None = None,
        hminn: float | None = None,
        hoptn: float | None = None,
        pHminnit: float | None = None,
        pHmaxnit: float | None = None,
        nh4Min: float | None = None,
        pHminden: float | None = None,
        pHmaxden: float | None = None,
        wfpsc: float | None = None,
        tdenitoptGauss: float | None = None,
        scaleTdenitopt: float | None = None,
        kd: float | None = None,
        kDesat: float | None = None,
        fnx: float | None = None,
        vnitmax: float | None = None,
        kamm: float | None = None,
        tnitmin: float | None = None,
        tnitopt: float | None = None,
        tnitop2: float | None = None,
        tnitmax: float | None = None,
        tnitoptGauss: float | None = None,
        scaleTnitopt: float | None = None,
        rationit: float | None = None,
        cminPdenit: float | None = None,
        cmaxPdenit: float | None = None,
        minPdenit: float | None = None,
        maxPdenit: float | None = None,
        ratiodenit: float | None = None,
        profdenit: float | None = None,
        vpotdenit: float | None = None,
        **kwargs: Any,
    ) -> SticsParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[SticsParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SticsParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SticsParametersBuilder]: ...
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
    ) -> SticsParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SticsParametersReader: ...

SticsParameters: _SticsParametersStructModule

class _SoilOrganicModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def somSlowDecCoeffStandard(self) -> float: ...
        @property
        def somFastDecCoeffStandard(self) -> float: ...
        @property
        def smbSlowMaintRateStandard(self) -> float: ...
        @property
        def smbFastMaintRateStandard(self) -> float: ...
        @property
        def smbSlowDeathRateStandard(self) -> float: ...
        @property
        def smbFastDeathRateStandard(self) -> float: ...
        @property
        def smbUtilizationEfficiency(self) -> float: ...
        @property
        def somSlowUtilizationEfficiency(self) -> float: ...
        @property
        def somFastUtilizationEfficiency(self) -> float: ...
        @property
        def aomSlowUtilizationEfficiency(self) -> float: ...
        @property
        def aomFastUtilizationEfficiency(self) -> float: ...
        @property
        def aomFastMaxCtoN(self) -> float: ...
        @property
        def partSOMFastToSOMSlow(self) -> float: ...
        @property
        def partSMBSlowToSOMFast(self) -> float: ...
        @property
        def partSMBFastToSOMFast(self) -> float: ...
        @property
        def partSOMToSMBSlow(self) -> float: ...
        @property
        def partSOMToSMBFast(self) -> float: ...
        @property
        def cnRatioSMB(self) -> float: ...
        @property
        def limitClayEffect(self) -> float: ...
        @property
        def ammoniaOxidationRateCoeffStandard(self) -> float: ...
        @property
        def nitriteOxidationRateCoeffStandard(self) -> float: ...
        @property
        def transportRateCoeff(self) -> float: ...
        @property
        def specAnaerobDenitrification(self) -> float: ...
        @property
        def immobilisationRateCoeffNO3(self) -> float: ...
        @property
        def immobilisationRateCoeffNH4(self) -> float: ...
        @property
        def denit1(self) -> float: ...
        @property
        def denit2(self) -> float: ...
        @property
        def denit3(self) -> float: ...
        @property
        def hydrolysisKM(self) -> float: ...
        @property
        def activationEnergy(self) -> float: ...
        @property
        def hydrolysisP1(self) -> float: ...
        @property
        def hydrolysisP2(self) -> float: ...
        @property
        def atmosphericResistance(self) -> float: ...
        @property
        def n2oProductionRate(self) -> float: ...
        @property
        def inhibitorNH3(self) -> float: ...
        @property
        def psMaxMineralisationDepth(self) -> float: ...
        @property
        def sticsParams(self) -> SticsParametersReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> SoilOrganicModuleParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def somSlowDecCoeffStandard(self) -> float: ...
        @somSlowDecCoeffStandard.setter
        def somSlowDecCoeffStandard(self, value: float) -> None: ...
        @property
        def somFastDecCoeffStandard(self) -> float: ...
        @somFastDecCoeffStandard.setter
        def somFastDecCoeffStandard(self, value: float) -> None: ...
        @property
        def smbSlowMaintRateStandard(self) -> float: ...
        @smbSlowMaintRateStandard.setter
        def smbSlowMaintRateStandard(self, value: float) -> None: ...
        @property
        def smbFastMaintRateStandard(self) -> float: ...
        @smbFastMaintRateStandard.setter
        def smbFastMaintRateStandard(self, value: float) -> None: ...
        @property
        def smbSlowDeathRateStandard(self) -> float: ...
        @smbSlowDeathRateStandard.setter
        def smbSlowDeathRateStandard(self, value: float) -> None: ...
        @property
        def smbFastDeathRateStandard(self) -> float: ...
        @smbFastDeathRateStandard.setter
        def smbFastDeathRateStandard(self, value: float) -> None: ...
        @property
        def smbUtilizationEfficiency(self) -> float: ...
        @smbUtilizationEfficiency.setter
        def smbUtilizationEfficiency(self, value: float) -> None: ...
        @property
        def somSlowUtilizationEfficiency(self) -> float: ...
        @somSlowUtilizationEfficiency.setter
        def somSlowUtilizationEfficiency(self, value: float) -> None: ...
        @property
        def somFastUtilizationEfficiency(self) -> float: ...
        @somFastUtilizationEfficiency.setter
        def somFastUtilizationEfficiency(self, value: float) -> None: ...
        @property
        def aomSlowUtilizationEfficiency(self) -> float: ...
        @aomSlowUtilizationEfficiency.setter
        def aomSlowUtilizationEfficiency(self, value: float) -> None: ...
        @property
        def aomFastUtilizationEfficiency(self) -> float: ...
        @aomFastUtilizationEfficiency.setter
        def aomFastUtilizationEfficiency(self, value: float) -> None: ...
        @property
        def aomFastMaxCtoN(self) -> float: ...
        @aomFastMaxCtoN.setter
        def aomFastMaxCtoN(self, value: float) -> None: ...
        @property
        def partSOMFastToSOMSlow(self) -> float: ...
        @partSOMFastToSOMSlow.setter
        def partSOMFastToSOMSlow(self, value: float) -> None: ...
        @property
        def partSMBSlowToSOMFast(self) -> float: ...
        @partSMBSlowToSOMFast.setter
        def partSMBSlowToSOMFast(self, value: float) -> None: ...
        @property
        def partSMBFastToSOMFast(self) -> float: ...
        @partSMBFastToSOMFast.setter
        def partSMBFastToSOMFast(self, value: float) -> None: ...
        @property
        def partSOMToSMBSlow(self) -> float: ...
        @partSOMToSMBSlow.setter
        def partSOMToSMBSlow(self, value: float) -> None: ...
        @property
        def partSOMToSMBFast(self) -> float: ...
        @partSOMToSMBFast.setter
        def partSOMToSMBFast(self, value: float) -> None: ...
        @property
        def cnRatioSMB(self) -> float: ...
        @cnRatioSMB.setter
        def cnRatioSMB(self, value: float) -> None: ...
        @property
        def limitClayEffect(self) -> float: ...
        @limitClayEffect.setter
        def limitClayEffect(self, value: float) -> None: ...
        @property
        def ammoniaOxidationRateCoeffStandard(self) -> float: ...
        @ammoniaOxidationRateCoeffStandard.setter
        def ammoniaOxidationRateCoeffStandard(self, value: float) -> None: ...
        @property
        def nitriteOxidationRateCoeffStandard(self) -> float: ...
        @nitriteOxidationRateCoeffStandard.setter
        def nitriteOxidationRateCoeffStandard(self, value: float) -> None: ...
        @property
        def transportRateCoeff(self) -> float: ...
        @transportRateCoeff.setter
        def transportRateCoeff(self, value: float) -> None: ...
        @property
        def specAnaerobDenitrification(self) -> float: ...
        @specAnaerobDenitrification.setter
        def specAnaerobDenitrification(self, value: float) -> None: ...
        @property
        def immobilisationRateCoeffNO3(self) -> float: ...
        @immobilisationRateCoeffNO3.setter
        def immobilisationRateCoeffNO3(self, value: float) -> None: ...
        @property
        def immobilisationRateCoeffNH4(self) -> float: ...
        @immobilisationRateCoeffNH4.setter
        def immobilisationRateCoeffNH4(self, value: float) -> None: ...
        @property
        def denit1(self) -> float: ...
        @denit1.setter
        def denit1(self, value: float) -> None: ...
        @property
        def denit2(self) -> float: ...
        @denit2.setter
        def denit2(self, value: float) -> None: ...
        @property
        def denit3(self) -> float: ...
        @denit3.setter
        def denit3(self, value: float) -> None: ...
        @property
        def hydrolysisKM(self) -> float: ...
        @hydrolysisKM.setter
        def hydrolysisKM(self, value: float) -> None: ...
        @property
        def activationEnergy(self) -> float: ...
        @activationEnergy.setter
        def activationEnergy(self, value: float) -> None: ...
        @property
        def hydrolysisP1(self) -> float: ...
        @hydrolysisP1.setter
        def hydrolysisP1(self, value: float) -> None: ...
        @property
        def hydrolysisP2(self) -> float: ...
        @hydrolysisP2.setter
        def hydrolysisP2(self, value: float) -> None: ...
        @property
        def atmosphericResistance(self) -> float: ...
        @atmosphericResistance.setter
        def atmosphericResistance(self, value: float) -> None: ...
        @property
        def n2oProductionRate(self) -> float: ...
        @n2oProductionRate.setter
        def n2oProductionRate(self, value: float) -> None: ...
        @property
        def inhibitorNH3(self) -> float: ...
        @inhibitorNH3.setter
        def inhibitorNH3(self, value: float) -> None: ...
        @property
        def psMaxMineralisationDepth(self) -> float: ...
        @psMaxMineralisationDepth.setter
        def psMaxMineralisationDepth(self, value: float) -> None: ...
        @property
        def sticsParams(self) -> SticsParametersBuilder: ...
        @sticsParams.setter
        def sticsParams(
            self, value: SticsParametersBuilder | SticsParametersReader | dict[str, Any]
        ) -> None: ...
        @override
        def init(
            self, field: Literal["sticsParams"], size: int | None = None
        ) -> SticsParametersBuilder: ...
        @override
        def as_reader(self) -> SoilOrganicModuleParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        somSlowDecCoeffStandard: float | None = None,
        somFastDecCoeffStandard: float | None = None,
        smbSlowMaintRateStandard: float | None = None,
        smbFastMaintRateStandard: float | None = None,
        smbSlowDeathRateStandard: float | None = None,
        smbFastDeathRateStandard: float | None = None,
        smbUtilizationEfficiency: float | None = None,
        somSlowUtilizationEfficiency: float | None = None,
        somFastUtilizationEfficiency: float | None = None,
        aomSlowUtilizationEfficiency: float | None = None,
        aomFastUtilizationEfficiency: float | None = None,
        aomFastMaxCtoN: float | None = None,
        partSOMFastToSOMSlow: float | None = None,
        partSMBSlowToSOMFast: float | None = None,
        partSMBFastToSOMFast: float | None = None,
        partSOMToSMBSlow: float | None = None,
        partSOMToSMBFast: float | None = None,
        cnRatioSMB: float | None = None,
        limitClayEffect: float | None = None,
        ammoniaOxidationRateCoeffStandard: float | None = None,
        nitriteOxidationRateCoeffStandard: float | None = None,
        transportRateCoeff: float | None = None,
        specAnaerobDenitrification: float | None = None,
        immobilisationRateCoeffNO3: float | None = None,
        immobilisationRateCoeffNH4: float | None = None,
        denit1: float | None = None,
        denit2: float | None = None,
        denit3: float | None = None,
        hydrolysisKM: float | None = None,
        activationEnergy: float | None = None,
        hydrolysisP1: float | None = None,
        hydrolysisP2: float | None = None,
        atmosphericResistance: float | None = None,
        n2oProductionRate: float | None = None,
        inhibitorNH3: float | None = None,
        psMaxMineralisationDepth: float | None = None,
        sticsParams: SticsParametersBuilder | dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> SoilOrganicModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[SoilOrganicModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SoilOrganicModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SoilOrganicModuleParametersBuilder]: ...
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
    ) -> SoilOrganicModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SoilOrganicModuleParametersReader: ...

SoilOrganicModuleParameters: _SoilOrganicModuleParametersStructModule

class _SoilTemperatureModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def nTau(self) -> float: ...
        @property
        def initialSurfaceTemperature(self) -> float: ...
        @property
        def baseTemperature(self) -> float: ...
        @property
        def quartzRawDensity(self) -> float: ...
        @property
        def densityAir(self) -> float: ...
        @property
        def densityWater(self) -> float: ...
        @property
        def densityHumus(self) -> float: ...
        @property
        def specificHeatCapacityAir(self) -> float: ...
        @property
        def specificHeatCapacityQuartz(self) -> float: ...
        @property
        def specificHeatCapacityWater(self) -> float: ...
        @property
        def specificHeatCapacityHumus(self) -> float: ...
        @property
        def soilAlbedo(self) -> float: ...
        @property
        def soilMoisture(self) -> float: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> SoilTemperatureModuleParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def nTau(self) -> float: ...
        @nTau.setter
        def nTau(self, value: float) -> None: ...
        @property
        def initialSurfaceTemperature(self) -> float: ...
        @initialSurfaceTemperature.setter
        def initialSurfaceTemperature(self, value: float) -> None: ...
        @property
        def baseTemperature(self) -> float: ...
        @baseTemperature.setter
        def baseTemperature(self, value: float) -> None: ...
        @property
        def quartzRawDensity(self) -> float: ...
        @quartzRawDensity.setter
        def quartzRawDensity(self, value: float) -> None: ...
        @property
        def densityAir(self) -> float: ...
        @densityAir.setter
        def densityAir(self, value: float) -> None: ...
        @property
        def densityWater(self) -> float: ...
        @densityWater.setter
        def densityWater(self, value: float) -> None: ...
        @property
        def densityHumus(self) -> float: ...
        @densityHumus.setter
        def densityHumus(self, value: float) -> None: ...
        @property
        def specificHeatCapacityAir(self) -> float: ...
        @specificHeatCapacityAir.setter
        def specificHeatCapacityAir(self, value: float) -> None: ...
        @property
        def specificHeatCapacityQuartz(self) -> float: ...
        @specificHeatCapacityQuartz.setter
        def specificHeatCapacityQuartz(self, value: float) -> None: ...
        @property
        def specificHeatCapacityWater(self) -> float: ...
        @specificHeatCapacityWater.setter
        def specificHeatCapacityWater(self, value: float) -> None: ...
        @property
        def specificHeatCapacityHumus(self) -> float: ...
        @specificHeatCapacityHumus.setter
        def specificHeatCapacityHumus(self, value: float) -> None: ...
        @property
        def soilAlbedo(self) -> float: ...
        @soilAlbedo.setter
        def soilAlbedo(self, value: float) -> None: ...
        @property
        def soilMoisture(self) -> float: ...
        @soilMoisture.setter
        def soilMoisture(self, value: float) -> None: ...
        @override
        def as_reader(self) -> SoilTemperatureModuleParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        nTau: float | None = None,
        initialSurfaceTemperature: float | None = None,
        baseTemperature: float | None = None,
        quartzRawDensity: float | None = None,
        densityAir: float | None = None,
        densityWater: float | None = None,
        densityHumus: float | None = None,
        specificHeatCapacityAir: float | None = None,
        specificHeatCapacityQuartz: float | None = None,
        specificHeatCapacityWater: float | None = None,
        specificHeatCapacityHumus: float | None = None,
        soilAlbedo: float | None = None,
        soilMoisture: float | None = None,
        **kwargs: Any,
    ) -> SoilTemperatureModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[SoilTemperatureModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SoilTemperatureModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SoilTemperatureModuleParametersBuilder]: ...
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
    ) -> SoilTemperatureModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SoilTemperatureModuleParametersReader: ...

SoilTemperatureModuleParameters: _SoilTemperatureModuleParametersStructModule

class _SoilTransportModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def dispersionLength(self) -> float: ...
        @property
        def ad(self) -> float: ...
        @property
        def diffusionCoefficientStandard(self) -> float: ...
        @property
        def nDeposition(self) -> float: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> SoilTransportModuleParametersBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def dispersionLength(self) -> float: ...
        @dispersionLength.setter
        def dispersionLength(self, value: float) -> None: ...
        @property
        def ad(self) -> float: ...
        @ad.setter
        def ad(self, value: float) -> None: ...
        @property
        def diffusionCoefficientStandard(self) -> float: ...
        @diffusionCoefficientStandard.setter
        def diffusionCoefficientStandard(self, value: float) -> None: ...
        @property
        def nDeposition(self) -> float: ...
        @nDeposition.setter
        def nDeposition(self, value: float) -> None: ...
        @override
        def as_reader(self) -> SoilTransportModuleParametersReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        dispersionLength: float | None = None,
        ad: float | None = None,
        diffusionCoefficientStandard: float | None = None,
        nDeposition: float | None = None,
        **kwargs: Any,
    ) -> SoilTransportModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[SoilTransportModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SoilTransportModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SoilTransportModuleParametersBuilder]: ...
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
    ) -> SoilTransportModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SoilTransportModuleParametersReader: ...

SoilTransportModuleParameters: _SoilTransportModuleParametersStructModule

class _SpeciesIdToEmissionList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> SpeciesIdToEmissionReader: ...
        @override
        def __iter__(self) -> Iterator[SpeciesIdToEmissionReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> SpeciesIdToEmissionBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: SpeciesIdToEmissionReader
            | SpeciesIdToEmissionBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[SpeciesIdToEmissionBuilder]: ...
        @override
        def init(
            self, index: int, size: int | None = None
        ) -> SpeciesIdToEmissionBuilder: ...

class _VocStructModule(_StructModule):
    class _EmissionsStructModule(_StructModule):
        class _SpeciesIdToEmissionStructModule(_StructModule):
            class Reader(_DynamicStructReader):
                @property
                def speciesId(self) -> int: ...
                @property
                def emission(self) -> float: ...
                @override
                def as_builder(
                    self,
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Callable[[int], bytearray] | None = None,
                ) -> SpeciesIdToEmissionBuilder: ...

            class Builder(_DynamicStructBuilder):
                @property
                def speciesId(self) -> int: ...
                @speciesId.setter
                def speciesId(self, value: int) -> None: ...
                @property
                def emission(self) -> float: ...
                @emission.setter
                def emission(self, value: float) -> None: ...
                @override
                def as_reader(self) -> SpeciesIdToEmissionReader: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                speciesId: int | None = None,
                emission: float | None = None,
                **kwargs: Any,
            ) -> SpeciesIdToEmissionBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[SpeciesIdToEmissionReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[SpeciesIdToEmissionReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[SpeciesIdToEmissionBuilder]: ...
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
            ) -> SpeciesIdToEmissionReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> SpeciesIdToEmissionReader: ...

        type SpeciesIdToEmissionReader = _SpeciesIdToEmissionStructModule.Reader
        type SpeciesIdToEmissionBuilder = _SpeciesIdToEmissionStructModule.Builder
        SpeciesIdToEmission: _SpeciesIdToEmissionStructModule
        class Reader(_DynamicStructReader):
            @property
            def speciesIdToIsopreneEmission(self) -> SpeciesIdToEmissionListReader: ...
            @property
            def speciesIdToMonoterpeneEmission(
                self,
            ) -> SpeciesIdToEmissionListReader: ...
            @property
            def isopreneEmission(self) -> float: ...
            @property
            def monoterpeneEmission(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
            ) -> EmissionsBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def speciesIdToIsopreneEmission(self) -> SpeciesIdToEmissionListBuilder: ...
            @speciesIdToIsopreneEmission.setter
            def speciesIdToIsopreneEmission(
                self,
                value: SpeciesIdToEmissionListBuilder
                | SpeciesIdToEmissionListReader
                | dict[str, Any],
            ) -> None: ...
            @property
            def speciesIdToMonoterpeneEmission(
                self,
            ) -> SpeciesIdToEmissionListBuilder: ...
            @speciesIdToMonoterpeneEmission.setter
            def speciesIdToMonoterpeneEmission(
                self,
                value: SpeciesIdToEmissionListBuilder
                | SpeciesIdToEmissionListReader
                | dict[str, Any],
            ) -> None: ...
            @property
            def isopreneEmission(self) -> float: ...
            @isopreneEmission.setter
            def isopreneEmission(self, value: float) -> None: ...
            @property
            def monoterpeneEmission(self) -> float: ...
            @monoterpeneEmission.setter
            def monoterpeneEmission(self, value: float) -> None: ...
            @override
            @overload
            def init(
                self,
                field: Literal["speciesIdToIsopreneEmission"],
                size: int | None = None,
            ) -> SpeciesIdToEmissionListBuilder: ...
            @overload
            def init(
                self,
                field: Literal["speciesIdToMonoterpeneEmission"],
                size: int | None = None,
            ) -> SpeciesIdToEmissionListBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> EmissionsReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            speciesIdToIsopreneEmission: SpeciesIdToEmissionListBuilder
            | dict[str, Any]
            | None = None,
            speciesIdToMonoterpeneEmission: SpeciesIdToEmissionListBuilder
            | dict[str, Any]
            | None = None,
            isopreneEmission: float | None = None,
            monoterpeneEmission: float | None = None,
            **kwargs: Any,
        ) -> EmissionsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[EmissionsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[EmissionsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[EmissionsBuilder]: ...
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
        ) -> EmissionsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> EmissionsReader: ...

    type EmissionsReader = _EmissionsStructModule.Reader
    type EmissionsBuilder = _EmissionsStructModule.Builder
    Emissions: _EmissionsStructModule
    class _SpeciesDataStructModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def id(self) -> int: ...
            @property
            def efMonos(self) -> float: ...
            @property
            def efMono(self) -> float: ...
            @property
            def efIso(self) -> float: ...
            @property
            def theta(self) -> float: ...
            @property
            def fage(self) -> float: ...
            @property
            def ctIs(self) -> float: ...
            @property
            def ctMt(self) -> float: ...
            @property
            def haIs(self) -> float: ...
            @property
            def haMt(self) -> float: ...
            @property
            def dsIs(self) -> float: ...
            @property
            def dsMt(self) -> float: ...
            @property
            def hdIs(self) -> float: ...
            @property
            def hdMt(self) -> float: ...
            @property
            def hdj(self) -> float: ...
            @property
            def sdj(self) -> float: ...
            @property
            def kc25(self) -> float: ...
            @property
            def ko25(self) -> float: ...
            @property
            def vcMax25(self) -> float: ...
            @property
            def qjvc(self) -> float: ...
            @property
            def aekc(self) -> float: ...
            @property
            def aeko(self) -> float: ...
            @property
            def aejm(self) -> float: ...
            @property
            def aevc(self) -> float: ...
            @property
            def slaMin(self) -> float: ...
            @property
            def scaleI(self) -> float: ...
            @property
            def scaleM(self) -> float: ...
            @property
            def mFol(self) -> float: ...
            @property
            def lai(self) -> float: ...
            @property
            def sla(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
            ) -> SpeciesDataBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def id(self) -> int: ...
            @id.setter
            def id(self, value: int) -> None: ...
            @property
            def efMonos(self) -> float: ...
            @efMonos.setter
            def efMonos(self, value: float) -> None: ...
            @property
            def efMono(self) -> float: ...
            @efMono.setter
            def efMono(self, value: float) -> None: ...
            @property
            def efIso(self) -> float: ...
            @efIso.setter
            def efIso(self, value: float) -> None: ...
            @property
            def theta(self) -> float: ...
            @theta.setter
            def theta(self, value: float) -> None: ...
            @property
            def fage(self) -> float: ...
            @fage.setter
            def fage(self, value: float) -> None: ...
            @property
            def ctIs(self) -> float: ...
            @ctIs.setter
            def ctIs(self, value: float) -> None: ...
            @property
            def ctMt(self) -> float: ...
            @ctMt.setter
            def ctMt(self, value: float) -> None: ...
            @property
            def haIs(self) -> float: ...
            @haIs.setter
            def haIs(self, value: float) -> None: ...
            @property
            def haMt(self) -> float: ...
            @haMt.setter
            def haMt(self, value: float) -> None: ...
            @property
            def dsIs(self) -> float: ...
            @dsIs.setter
            def dsIs(self, value: float) -> None: ...
            @property
            def dsMt(self) -> float: ...
            @dsMt.setter
            def dsMt(self, value: float) -> None: ...
            @property
            def hdIs(self) -> float: ...
            @hdIs.setter
            def hdIs(self, value: float) -> None: ...
            @property
            def hdMt(self) -> float: ...
            @hdMt.setter
            def hdMt(self, value: float) -> None: ...
            @property
            def hdj(self) -> float: ...
            @hdj.setter
            def hdj(self, value: float) -> None: ...
            @property
            def sdj(self) -> float: ...
            @sdj.setter
            def sdj(self, value: float) -> None: ...
            @property
            def kc25(self) -> float: ...
            @kc25.setter
            def kc25(self, value: float) -> None: ...
            @property
            def ko25(self) -> float: ...
            @ko25.setter
            def ko25(self, value: float) -> None: ...
            @property
            def vcMax25(self) -> float: ...
            @vcMax25.setter
            def vcMax25(self, value: float) -> None: ...
            @property
            def qjvc(self) -> float: ...
            @qjvc.setter
            def qjvc(self, value: float) -> None: ...
            @property
            def aekc(self) -> float: ...
            @aekc.setter
            def aekc(self, value: float) -> None: ...
            @property
            def aeko(self) -> float: ...
            @aeko.setter
            def aeko(self, value: float) -> None: ...
            @property
            def aejm(self) -> float: ...
            @aejm.setter
            def aejm(self, value: float) -> None: ...
            @property
            def aevc(self) -> float: ...
            @aevc.setter
            def aevc(self, value: float) -> None: ...
            @property
            def slaMin(self) -> float: ...
            @slaMin.setter
            def slaMin(self, value: float) -> None: ...
            @property
            def scaleI(self) -> float: ...
            @scaleI.setter
            def scaleI(self, value: float) -> None: ...
            @property
            def scaleM(self) -> float: ...
            @scaleM.setter
            def scaleM(self, value: float) -> None: ...
            @property
            def mFol(self) -> float: ...
            @mFol.setter
            def mFol(self, value: float) -> None: ...
            @property
            def lai(self) -> float: ...
            @lai.setter
            def lai(self, value: float) -> None: ...
            @property
            def sla(self) -> float: ...
            @sla.setter
            def sla(self, value: float) -> None: ...
            @override
            def as_reader(self) -> SpeciesDataReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            id: int | None = None,
            efMonos: float | None = None,
            efMono: float | None = None,
            efIso: float | None = None,
            theta: float | None = None,
            fage: float | None = None,
            ctIs: float | None = None,
            ctMt: float | None = None,
            haIs: float | None = None,
            haMt: float | None = None,
            dsIs: float | None = None,
            dsMt: float | None = None,
            hdIs: float | None = None,
            hdMt: float | None = None,
            hdj: float | None = None,
            sdj: float | None = None,
            kc25: float | None = None,
            ko25: float | None = None,
            vcMax25: float | None = None,
            qjvc: float | None = None,
            aekc: float | None = None,
            aeko: float | None = None,
            aejm: float | None = None,
            aevc: float | None = None,
            slaMin: float | None = None,
            scaleI: float | None = None,
            scaleM: float | None = None,
            mFol: float | None = None,
            lai: float | None = None,
            sla: float | None = None,
            **kwargs: Any,
        ) -> SpeciesDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[SpeciesDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[SpeciesDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[SpeciesDataBuilder]: ...
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
        ) -> SpeciesDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> SpeciesDataReader: ...

    type SpeciesDataReader = _SpeciesDataStructModule.Reader
    type SpeciesDataBuilder = _SpeciesDataStructModule.Builder
    SpeciesData: _SpeciesDataStructModule
    class _CPDataStructModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def kc(self) -> float: ...
            @property
            def ko(self) -> float: ...
            @property
            def oi(self) -> float: ...
            @property
            def ci(self) -> float: ...
            @property
            def comp(self) -> float: ...
            @property
            def vcMax(self) -> float: ...
            @property
            def jMax(self) -> float: ...
            @property
            def jj(self) -> float: ...
            @property
            def jj1000(self) -> float: ...
            @property
            def jv(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
            ) -> CPDataBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def kc(self) -> float: ...
            @kc.setter
            def kc(self, value: float) -> None: ...
            @property
            def ko(self) -> float: ...
            @ko.setter
            def ko(self, value: float) -> None: ...
            @property
            def oi(self) -> float: ...
            @oi.setter
            def oi(self, value: float) -> None: ...
            @property
            def ci(self) -> float: ...
            @ci.setter
            def ci(self, value: float) -> None: ...
            @property
            def comp(self) -> float: ...
            @comp.setter
            def comp(self, value: float) -> None: ...
            @property
            def vcMax(self) -> float: ...
            @vcMax.setter
            def vcMax(self, value: float) -> None: ...
            @property
            def jMax(self) -> float: ...
            @jMax.setter
            def jMax(self, value: float) -> None: ...
            @property
            def jj(self) -> float: ...
            @jj.setter
            def jj(self, value: float) -> None: ...
            @property
            def jj1000(self) -> float: ...
            @jj1000.setter
            def jj1000(self, value: float) -> None: ...
            @property
            def jv(self) -> float: ...
            @jv.setter
            def jv(self, value: float) -> None: ...
            @override
            def as_reader(self) -> CPDataReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            kc: float | None = None,
            ko: float | None = None,
            oi: float | None = None,
            ci: float | None = None,
            comp: float | None = None,
            vcMax: float | None = None,
            jMax: float | None = None,
            jj: float | None = None,
            jj1000: float | None = None,
            jv: float | None = None,
            **kwargs: Any,
        ) -> CPDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[CPDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[CPDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[CPDataBuilder]: ...
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
        ) -> CPDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> CPDataReader: ...

    type CPDataReader = _CPDataStructModule.Reader
    type CPDataBuilder = _CPDataStructModule.Builder
    CPData: _CPDataStructModule
    class _MicroClimateDataStructModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def rad(self) -> float: ...
            @property
            def rad24(self) -> float: ...
            @property
            def rad240(self) -> float: ...
            @property
            def tFol(self) -> float: ...
            @property
            def tFol24(self) -> float: ...
            @property
            def tFol240(self) -> float: ...
            @property
            def sunlitfoliagefraction(self) -> float: ...
            @property
            def sunlitfoliagefraction24(self) -> float: ...
            @property
            def co2concentration(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
            ) -> MicroClimateDataBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def rad(self) -> float: ...
            @rad.setter
            def rad(self, value: float) -> None: ...
            @property
            def rad24(self) -> float: ...
            @rad24.setter
            def rad24(self, value: float) -> None: ...
            @property
            def rad240(self) -> float: ...
            @rad240.setter
            def rad240(self, value: float) -> None: ...
            @property
            def tFol(self) -> float: ...
            @tFol.setter
            def tFol(self, value: float) -> None: ...
            @property
            def tFol24(self) -> float: ...
            @tFol24.setter
            def tFol24(self, value: float) -> None: ...
            @property
            def tFol240(self) -> float: ...
            @tFol240.setter
            def tFol240(self, value: float) -> None: ...
            @property
            def sunlitfoliagefraction(self) -> float: ...
            @sunlitfoliagefraction.setter
            def sunlitfoliagefraction(self, value: float) -> None: ...
            @property
            def sunlitfoliagefraction24(self) -> float: ...
            @sunlitfoliagefraction24.setter
            def sunlitfoliagefraction24(self, value: float) -> None: ...
            @property
            def co2concentration(self) -> float: ...
            @co2concentration.setter
            def co2concentration(self, value: float) -> None: ...
            @override
            def as_reader(self) -> MicroClimateDataReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            rad: float | None = None,
            rad24: float | None = None,
            rad240: float | None = None,
            tFol: float | None = None,
            tFol24: float | None = None,
            tFol240: float | None = None,
            sunlitfoliagefraction: float | None = None,
            sunlitfoliagefraction24: float | None = None,
            co2concentration: float | None = None,
            **kwargs: Any,
        ) -> MicroClimateDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[MicroClimateDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[MicroClimateDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[MicroClimateDataBuilder]: ...
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
        ) -> MicroClimateDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> MicroClimateDataReader: ...

    type MicroClimateDataReader = _MicroClimateDataStructModule.Reader
    type MicroClimateDataBuilder = _MicroClimateDataStructModule.Builder
    MicroClimateData: _MicroClimateDataStructModule
    class _PhotosynthTStructModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def par(self) -> float: ...
            @property
            def par24(self) -> float: ...
            @property
            def par240(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
            ) -> PhotosynthTBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def par(self) -> float: ...
            @par.setter
            def par(self, value: float) -> None: ...
            @property
            def par24(self) -> float: ...
            @par24.setter
            def par24(self, value: float) -> None: ...
            @property
            def par240(self) -> float: ...
            @par240.setter
            def par240(self, value: float) -> None: ...
            @override
            def as_reader(self) -> PhotosynthTReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            par: float | None = None,
            par24: float | None = None,
            par240: float | None = None,
            **kwargs: Any,
        ) -> PhotosynthTBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[PhotosynthTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[PhotosynthTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[PhotosynthTBuilder]: ...
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
        ) -> PhotosynthTReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> PhotosynthTReader: ...

    type PhotosynthTReader = _PhotosynthTStructModule.Reader
    type PhotosynthTBuilder = _PhotosynthTStructModule.Builder
    PhotosynthT: _PhotosynthTStructModule
    class _FoliageTStructModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def tempK(self) -> float: ...
            @property
            def tempK24(self) -> float: ...
            @property
            def tempK240(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
            ) -> FoliageTBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def tempK(self) -> float: ...
            @tempK.setter
            def tempK(self, value: float) -> None: ...
            @property
            def tempK24(self) -> float: ...
            @tempK24.setter
            def tempK24(self, value: float) -> None: ...
            @property
            def tempK240(self) -> float: ...
            @tempK240.setter
            def tempK240(self, value: float) -> None: ...
            @override
            def as_reader(self) -> FoliageTReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            tempK: float | None = None,
            tempK24: float | None = None,
            tempK240: float | None = None,
            **kwargs: Any,
        ) -> FoliageTBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[FoliageTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[FoliageTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[FoliageTBuilder]: ...
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
        ) -> FoliageTReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> FoliageTReader: ...

    type FoliageTReader = _FoliageTStructModule.Reader
    type FoliageTBuilder = _FoliageTStructModule.Builder
    FoliageT: _FoliageTStructModule
    class _EnzymeActivityTStructModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def efIso(self) -> float: ...
            @property
            def efMono(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
            ) -> EnzymeActivityTBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def efIso(self) -> float: ...
            @efIso.setter
            def efIso(self, value: float) -> None: ...
            @property
            def efMono(self) -> float: ...
            @efMono.setter
            def efMono(self, value: float) -> None: ...
            @override
            def as_reader(self) -> EnzymeActivityTReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            efIso: float | None = None,
            efMono: float | None = None,
            **kwargs: Any,
        ) -> EnzymeActivityTBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[EnzymeActivityTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[EnzymeActivityTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[EnzymeActivityTBuilder]: ...
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
        ) -> EnzymeActivityTReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> EnzymeActivityTReader: ...

    type EnzymeActivityTReader = _EnzymeActivityTStructModule.Reader
    type EnzymeActivityTBuilder = _EnzymeActivityTStructModule.Builder
    EnzymeActivityT: _EnzymeActivityTStructModule
    class _LeafEmissionTStructModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def foliageLayer(self) -> int: ...
            @property
            def pho(self) -> PhotosynthTReader: ...
            @property
            def fol(self) -> FoliageTReader: ...
            @property
            def enzAct(self) -> EnzymeActivityTReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
            ) -> LeafEmissionTBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def foliageLayer(self) -> int: ...
            @foliageLayer.setter
            def foliageLayer(self, value: int) -> None: ...
            @property
            def pho(self) -> PhotosynthTBuilder: ...
            @pho.setter
            def pho(
                self, value: PhotosynthTBuilder | PhotosynthTReader | dict[str, Any]
            ) -> None: ...
            @property
            def fol(self) -> FoliageTBuilder: ...
            @fol.setter
            def fol(
                self, value: FoliageTBuilder | FoliageTReader | dict[str, Any]
            ) -> None: ...
            @property
            def enzAct(self) -> EnzymeActivityTBuilder: ...
            @enzAct.setter
            def enzAct(
                self,
                value: EnzymeActivityTBuilder | EnzymeActivityTReader | dict[str, Any],
            ) -> None: ...
            @override
            @overload
            def init(
                self, field: Literal["pho"], size: int | None = None
            ) -> PhotosynthTBuilder: ...
            @overload
            def init(
                self, field: Literal["fol"], size: int | None = None
            ) -> FoliageTBuilder: ...
            @overload
            def init(
                self, field: Literal["enzAct"], size: int | None = None
            ) -> EnzymeActivityTBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> LeafEmissionTReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            foliageLayer: int | None = None,
            pho: PhotosynthTBuilder | dict[str, Any] | None = None,
            fol: FoliageTBuilder | dict[str, Any] | None = None,
            enzAct: EnzymeActivityTBuilder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> LeafEmissionTBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[LeafEmissionTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[LeafEmissionTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[LeafEmissionTBuilder]: ...
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
        ) -> LeafEmissionTReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> LeafEmissionTReader: ...

    type LeafEmissionTReader = _LeafEmissionTStructModule.Reader
    type LeafEmissionTBuilder = _LeafEmissionTStructModule.Builder
    LeafEmissionT: _LeafEmissionTStructModule
    class _LeafEmissionsStructModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def isoprene(self) -> float: ...
            @property
            def monoterp(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
            ) -> LeafEmissionsBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def isoprene(self) -> float: ...
            @isoprene.setter
            def isoprene(self, value: float) -> None: ...
            @property
            def monoterp(self) -> float: ...
            @monoterp.setter
            def monoterp(self, value: float) -> None: ...
            @override
            def as_reader(self) -> LeafEmissionsReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            isoprene: float | None = None,
            monoterp: float | None = None,
            **kwargs: Any,
        ) -> LeafEmissionsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[LeafEmissionsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[LeafEmissionsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[LeafEmissionsBuilder]: ...
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
        ) -> LeafEmissionsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> LeafEmissionsReader: ...

    type LeafEmissionsReader = _LeafEmissionsStructModule.Reader
    type LeafEmissionsBuilder = _LeafEmissionsStructModule.Builder
    LeafEmissions: _LeafEmissionsStructModule
    class Reader(_DynamicStructReader):
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> VocBuilder: ...

    class Builder(_DynamicStructBuilder):
        @override
        def as_reader(self) -> VocReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        **kwargs: Any,
    ) -> VocBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[VocReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[VocReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[VocBuilder]: ...
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
    ) -> VocReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> VocReader: ...

Voc: _VocStructModule

# Top-level type aliases for use in type annotations
type AutomaticHarvestParametersBuilder = _AutomaticHarvestParametersStructModule.Builder
type AutomaticHarvestParametersHarvestTimeEnum = int | Literal["maturity", "unknown"]
type AutomaticHarvestParametersReader = _AutomaticHarvestParametersStructModule.Reader
type AutomaticIrrigationParametersBuilder = (
    _AutomaticIrrigationParametersStructModule.Builder
)
type AutomaticIrrigationParametersReader = (
    _AutomaticIrrigationParametersStructModule.Reader
)
type BoolListBuilder = _BoolList.Builder
type BoolListReader = _BoolList.Reader
type CPDataBuilder = _VocStructModule._CPDataStructModule.Builder
type CPDataReader = _VocStructModule._CPDataStructModule.Reader
type CropModuleParametersBuilder = _CropModuleParametersStructModule.Builder
type CropModuleParametersReader = _CropModuleParametersStructModule.Reader
type CropParametersBuilder = _CropParametersStructModule.Builder
type CropParametersReader = _CropParametersStructModule.Reader
type CropResidueParametersBuilder = _CropResidueParametersStructModule.Builder
type CropResidueParametersReader = _CropResidueParametersStructModule.Reader
type CropSpecBuilder = _CropSpecStructModule.Builder
type CropSpecReader = _CropSpecStructModule.Reader
type CultivarParametersBuilder = _CultivarParametersStructModule.Builder
type CultivarParametersReader = _CultivarParametersStructModule.Reader
type DateToValueBuilder = (
    _MeasuredGroundwaterTableInformationStructModule._DateToValueStructModule.Builder
)
type DateToValueListBuilder = _DateToValueList.Builder
type DateToValueListReader = _DateToValueList.Reader
type DateToValueReader = (
    _MeasuredGroundwaterTableInformationStructModule._DateToValueStructModule.Reader
)
type EmissionsBuilder = _VocStructModule._EmissionsStructModule.Builder
type EmissionsReader = _VocStructModule._EmissionsStructModule.Reader
type EnvironmentParametersBuilder = _EnvironmentParametersStructModule.Builder
type EnvironmentParametersReader = _EnvironmentParametersStructModule.Reader
type EnzymeActivityTBuilder = _VocStructModule._EnzymeActivityTStructModule.Builder
type EnzymeActivityTReader = _VocStructModule._EnzymeActivityTStructModule.Reader
type Float64ListBuilder = _Float64List.Builder
type Float64ListListBuilder = _Float64ListList.Builder
type Float64ListListReader = _Float64ListList.Reader
type Float64ListReader = _Float64List.Reader
type FoliageTBuilder = _VocStructModule._FoliageTStructModule.Builder
type FoliageTReader = _VocStructModule._FoliageTStructModule.Reader
type LeafEmissionTBuilder = _VocStructModule._LeafEmissionTStructModule.Builder
type LeafEmissionTReader = _VocStructModule._LeafEmissionTStructModule.Reader
type LeafEmissionsBuilder = _VocStructModule._LeafEmissionsStructModule.Builder
type LeafEmissionsReader = _VocStructModule._LeafEmissionsStructModule.Reader
type MeasuredGroundwaterTableInformationBuilder = (
    _MeasuredGroundwaterTableInformationStructModule.Builder
)
type MeasuredGroundwaterTableInformationReader = (
    _MeasuredGroundwaterTableInformationStructModule.Reader
)
type MicroClimateDataBuilder = _VocStructModule._MicroClimateDataStructModule.Builder
type MicroClimateDataReader = _VocStructModule._MicroClimateDataStructModule.Reader
type NMinApplicationParametersBuilder = _NMinApplicationParametersStructModule.Builder
type NMinApplicationParametersReader = _NMinApplicationParametersStructModule.Reader
type NMinCropParametersBuilder = _NMinCropParametersStructModule.Builder
type NMinCropParametersReader = _NMinCropParametersStructModule.Reader
type PhotosynthTBuilder = _VocStructModule._PhotosynthTStructModule.Builder
type PhotosynthTReader = _VocStructModule._PhotosynthTStructModule.Reader
type SimulationParametersBuilder = _SimulationParametersStructModule.Builder
type SimulationParametersReader = _SimulationParametersStructModule.Reader
type SiteParametersBuilder = _SiteParametersStructModule.Builder
type SiteParametersReader = _SiteParametersStructModule.Reader
type SoilMoistureModuleParametersBuilder = (
    _SoilMoistureModuleParametersStructModule.Builder
)
type SoilMoistureModuleParametersReader = (
    _SoilMoistureModuleParametersStructModule.Reader
)
type SoilOrganicModuleParametersBuilder = (
    _SoilOrganicModuleParametersStructModule.Builder
)
type SoilOrganicModuleParametersReader = _SoilOrganicModuleParametersStructModule.Reader
type SoilParametersBuilder = _SoilParametersStructModule.Builder
type SoilParametersListBuilder = _SoilParametersList.Builder
type SoilParametersListReader = _SoilParametersList.Reader
type SoilParametersReader = _SoilParametersStructModule.Reader
type SoilTemperatureModuleParametersBuilder = (
    _SoilTemperatureModuleParametersStructModule.Builder
)
type SoilTemperatureModuleParametersReader = (
    _SoilTemperatureModuleParametersStructModule.Reader
)
type SoilTransportModuleParametersBuilder = (
    _SoilTransportModuleParametersStructModule.Builder
)
type SoilTransportModuleParametersReader = (
    _SoilTransportModuleParametersStructModule.Reader
)
type SpeciesDataBuilder = _VocStructModule._SpeciesDataStructModule.Builder
type SpeciesDataReader = _VocStructModule._SpeciesDataStructModule.Reader
type SpeciesIdToEmissionBuilder = (
    _VocStructModule._EmissionsStructModule._SpeciesIdToEmissionStructModule.Builder
)
type SpeciesIdToEmissionListBuilder = _SpeciesIdToEmissionList.Builder
type SpeciesIdToEmissionListReader = _SpeciesIdToEmissionList.Reader
type SpeciesIdToEmissionReader = (
    _VocStructModule._EmissionsStructModule._SpeciesIdToEmissionStructModule.Reader
)
type SpeciesParametersBuilder = _SpeciesParametersStructModule.Builder
type SpeciesParametersReader = _SpeciesParametersStructModule.Reader
type SticsParametersBuilder = _SticsParametersStructModule.Builder
type SticsParametersReader = _SticsParametersStructModule.Reader
type VocBuilder = _VocStructModule.Builder
type VocReader = _VocStructModule.Reader
type YearToValueBuilder = (
    _EnvironmentParametersStructModule._YearToValueStructModule.Builder
)
type YearToValueListBuilder = _YearToValueList.Builder
type YearToValueListReader = _YearToValueList.Reader
type YearToValueReader = (
    _EnvironmentParametersStructModule._YearToValueStructModule.Reader
)
type YieldComponentBuilder = _YieldComponentStructModule.Builder
type YieldComponentListBuilder = _YieldComponentList.Builder
type YieldComponentListReader = _YieldComponentList.Reader
type YieldComponentReader = _YieldComponentStructModule.Reader
