"""Module helper types for `monica_params.capnp`."""

from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

from mas.schema.climate.climate_capnp.types.enums import RCPEnum
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.model.monica.monica_management_capnp.types.modules import (
    _ParamsStructModule,
)

from . import _all as _all

class _SpeciesParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
        baseTemperature: _all.Float64ListBuilder | dict[str, Any] | None = None,
        organMaintenanceRespiration: _all.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        organGrowthRespiration: _all.Float64ListBuilder | dict[str, Any] | None = None,
        stageMaxRootNConcentration: _all.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        initialOrganBiomass: _all.Float64ListBuilder | dict[str, Any] | None = None,
        criticalOxygenContent: _all.Float64ListBuilder | dict[str, Any] | None = None,
        stageMobilFromStorageCoeff: _all.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        abovegroundOrgan: _all.BoolListBuilder | dict[str, Any] | None = None,
        storageOrgan: _all.BoolListBuilder | dict[str, Any] | None = None,
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
        **kwargs: object,
    ) -> _all.SpeciesParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SpeciesParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SpeciesParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SpeciesParametersBuilder]: ...
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
    ) -> _all.SpeciesParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SpeciesParametersReader: ...

class _YieldComponentStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        organId: int | None = None,
        yieldPercentage: float | None = None,
        yieldDryMatter: float | None = None,
        **kwargs: object,
    ) -> _all.YieldComponentBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.YieldComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.YieldComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.YieldComponentBuilder]: ...
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
    ) -> _all.YieldComponentReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.YieldComponentReader: ...

class _CultivarParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
        assimilatePartitioningCoeff: _all.Float64ListListBuilder
        | dict[str, Any]
        | None = None,
        organSenescenceRate: _all.Float64ListListBuilder | dict[str, Any] | None = None,
        baseDaylength: _all.Float64ListBuilder | dict[str, Any] | None = None,
        optimumTemperature: _all.Float64ListBuilder | dict[str, Any] | None = None,
        daylengthRequirement: _all.Float64ListBuilder | dict[str, Any] | None = None,
        droughtStressThreshold: _all.Float64ListBuilder | dict[str, Any] | None = None,
        specificLeafArea: _all.Float64ListBuilder | dict[str, Any] | None = None,
        stageKcFactor: _all.Float64ListBuilder | dict[str, Any] | None = None,
        stageTemperatureSum: _all.Float64ListBuilder | dict[str, Any] | None = None,
        vernalisationRequirement: _all.Float64ListBuilder
        | dict[str, Any]
        | None = None,
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
        organIdsForPrimaryYield: _all.YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        organIdsForSecondaryYield: _all.YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        organIdsForCutting: _all.YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        earlyRefLeafExp: float | None = None,
        refLeafExp: float | None = None,
        minTempDevWE: float | None = None,
        optTempDevWE: float | None = None,
        maxTempDevWE: float | None = None,
        winterCrop: bool | None = None,
        **kwargs: object,
    ) -> _all.CultivarParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.CultivarParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.CultivarParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.CultivarParametersBuilder]: ...
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
    ) -> _all.CultivarParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.CultivarParametersReader: ...

class _CropParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        speciesParams: _all.SpeciesParametersBuilder | dict[str, Any] | None = None,
        cultivarParams: _all.CultivarParametersBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.CropParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.CropParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.CropParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.CropParametersBuilder]: ...
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
    ) -> _all.CropParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.CropParametersReader: ...

class _CropResidueParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
        **kwargs: object,
    ) -> _all.CropResidueParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.CropResidueParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.CropResidueParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.CropResidueParametersBuilder]: ...
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
    ) -> _all.CropResidueParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.CropResidueParametersReader: ...

class _CropSpecStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        cropParams: _all.CropParametersBuilder | dict[str, Any] | None = None,
        residueParams: _all.CropResidueParametersBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.CropSpecBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.CropSpecReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.CropSpecReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.CropSpecBuilder]: ...
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
    ) -> _all.CropSpecReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.CropSpecReader: ...

class _AutomaticHarvestParametersStructModule(_StructModule):
    class _HarvestTimeEnumModule:
        maturity: int
        unknown: int

    HarvestTime: _HarvestTimeEnumModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        harvestTime: _all.AutomaticHarvestParametersHarvestTimeEnum | None = None,
        latestHarvestDOY: int | None = None,
        **kwargs: object,
    ) -> _all.AutomaticHarvestParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.AutomaticHarvestParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.AutomaticHarvestParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.AutomaticHarvestParametersBuilder]: ...
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
    ) -> _all.AutomaticHarvestParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.AutomaticHarvestParametersReader: ...

class _NMinCropParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        samplingDepth: float | None = None,
        nTarget: float | None = None,
        nTarget30: float | None = None,
        **kwargs: object,
    ) -> _all.NMinCropParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.NMinCropParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.NMinCropParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.NMinCropParametersBuilder]: ...
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
    ) -> _all.NMinCropParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.NMinCropParametersReader: ...

class _NMinApplicationParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        min: float | None = None,
        max: float | None = None,
        delayInDays: int | None = None,
        **kwargs: object,
    ) -> _all.NMinApplicationParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.NMinApplicationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.NMinApplicationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.NMinApplicationParametersBuilder]: ...
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
    ) -> _all.NMinApplicationParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.NMinApplicationParametersReader: ...

class _SoilParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
        **kwargs: object,
    ) -> _all.SoilParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SoilParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SoilParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SoilParametersBuilder]: ...
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
    ) -> _all.SoilParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SoilParametersReader: ...

class _AutomaticIrrigationParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
        **kwargs: object,
    ) -> _all.AutomaticIrrigationParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.AutomaticIrrigationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.AutomaticIrrigationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.AutomaticIrrigationParametersBuilder]: ...
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
    ) -> _all.AutomaticIrrigationParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.AutomaticIrrigationParametersReader: ...

class _SiteParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
        soilParameters: _all.SoilParametersListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.SiteParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SiteParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SiteParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SiteParametersBuilder]: ...
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
    ) -> _all.SiteParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SiteParametersReader: ...

class _EnvironmentParametersStructModule(_StructModule):
    class _YearToValueStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            year: int | None = None,
            value: float | None = None,
            **kwargs: object,
        ) -> _all.YearToValueBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.YearToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.YearToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.YearToValueBuilder]: ...
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
        ) -> _all.YearToValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.YearToValueReader: ...

    YearToValue: _YearToValueStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        albedo: float | None = None,
        atmosphericCO2: float | None = None,
        atmosphericCO2s: _all.YearToValueListBuilder | dict[str, Any] | None = None,
        atmosphericO3: float | None = None,
        atmosphericO3s: _all.YearToValueListBuilder | dict[str, Any] | None = None,
        windSpeedHeight: float | None = None,
        leachingDepth: float | None = None,
        timeStep: float | None = None,
        maxGroundwaterDepth: float | None = None,
        minGroundwaterDepth: float | None = None,
        minGroundwaterDepthMonth: int | None = None,
        rcp: RCPEnum | None = None,
        **kwargs: object,
    ) -> _all.EnvironmentParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.EnvironmentParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.EnvironmentParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.EnvironmentParametersBuilder]: ...
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
    ) -> _all.EnvironmentParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.EnvironmentParametersReader: ...

class _MeasuredGroundwaterTableInformationStructModule(_StructModule):
    class _DateToValueStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            date: DateBuilder | dict[str, Any] | None = None,
            value: float | None = None,
            **kwargs: object,
        ) -> _all.DateToValueBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.DateToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.DateToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.DateToValueBuilder]: ...
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
        ) -> _all.DateToValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.DateToValueReader: ...

    DateToValue: _DateToValueStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        groundwaterInformationAvailable: bool | None = None,
        groundwaterInfo: _all.DateToValueListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.MeasuredGroundwaterTableInformationBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.MeasuredGroundwaterTableInformationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.MeasuredGroundwaterTableInformationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.MeasuredGroundwaterTableInformationBuilder]: ...
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
    ) -> _all.MeasuredGroundwaterTableInformationReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.MeasuredGroundwaterTableInformationReader: ...

class _SimulationParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
        autoIrrigationParams: _all.AutomaticIrrigationParametersBuilder
        | dict[str, Any]
        | None = None,
        useNMinMineralFertilisingMethod: bool | None = None,
        nMinFertiliserPartition: _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder
        | dict[str, Any]
        | None = None,
        nMinApplicationParams: _all.NMinApplicationParametersBuilder
        | dict[str, Any]
        | None = None,
        useSecondaryYields: bool | None = None,
        useAutomaticHarvestTrigger: bool | None = None,
        numberOfLayers: int | None = None,
        layerThickness: float | None = None,
        startPVIndex: int | None = None,
        julianDayAutomaticFertilising: int | None = None,
        **kwargs: object,
    ) -> _all.SimulationParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SimulationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SimulationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SimulationParametersBuilder]: ...
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
    ) -> _all.SimulationParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SimulationParametersReader: ...

class _CropModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
        **kwargs: object,
    ) -> _all.CropModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.CropModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.CropModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.CropModuleParametersBuilder]: ...
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
    ) -> _all.CropModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.CropModuleParametersReader: ...

class _SoilMoistureModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
        **kwargs: object,
    ) -> _all.SoilMoistureModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SoilMoistureModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SoilMoistureModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SoilMoistureModuleParametersBuilder]: ...
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
    ) -> _all.SoilMoistureModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SoilMoistureModuleParametersReader: ...

class _SticsParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
        **kwargs: object,
    ) -> _all.SticsParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SticsParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SticsParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SticsParametersBuilder]: ...
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
    ) -> _all.SticsParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SticsParametersReader: ...

class _SoilOrganicModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
        sticsParams: _all.SticsParametersBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.SoilOrganicModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SoilOrganicModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SoilOrganicModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SoilOrganicModuleParametersBuilder]: ...
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
    ) -> _all.SoilOrganicModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SoilOrganicModuleParametersReader: ...

class _SoilTemperatureModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
        **kwargs: object,
    ) -> _all.SoilTemperatureModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SoilTemperatureModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SoilTemperatureModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SoilTemperatureModuleParametersBuilder]: ...
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
    ) -> _all.SoilTemperatureModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SoilTemperatureModuleParametersReader: ...

class _SoilTransportModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        dispersionLength: float | None = None,
        ad: float | None = None,
        diffusionCoefficientStandard: float | None = None,
        nDeposition: float | None = None,
        **kwargs: object,
    ) -> _all.SoilTransportModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SoilTransportModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SoilTransportModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SoilTransportModuleParametersBuilder]: ...
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
    ) -> _all.SoilTransportModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SoilTransportModuleParametersReader: ...

class _VocStructModule(_StructModule):
    class _EmissionsStructModule(_StructModule):
        class _SpeciesIdToEmissionStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                speciesId: int | None = None,
                emission: float | None = None,
                **kwargs: object,
            ) -> _all.SpeciesIdToEmissionBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[_all.SpeciesIdToEmissionReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[_all.SpeciesIdToEmissionReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[_all.SpeciesIdToEmissionBuilder]: ...
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
            ) -> _all.SpeciesIdToEmissionReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _all.SpeciesIdToEmissionReader: ...

        SpeciesIdToEmission: _SpeciesIdToEmissionStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            speciesIdToIsopreneEmission: _all.SpeciesIdToEmissionListBuilder
            | dict[str, Any]
            | None = None,
            speciesIdToMonoterpeneEmission: _all.SpeciesIdToEmissionListBuilder
            | dict[str, Any]
            | None = None,
            isopreneEmission: float | None = None,
            monoterpeneEmission: float | None = None,
            **kwargs: object,
        ) -> _all.EmissionsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.EmissionsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.EmissionsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.EmissionsBuilder]: ...
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
        ) -> _all.EmissionsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.EmissionsReader: ...

    Emissions: _EmissionsStructModule
    class _SpeciesDataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

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
            **kwargs: object,
        ) -> _all.SpeciesDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.SpeciesDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.SpeciesDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.SpeciesDataBuilder]: ...
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
        ) -> _all.SpeciesDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.SpeciesDataReader: ...

    SpeciesData: _SpeciesDataStructModule
    class _CPDataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

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
            **kwargs: object,
        ) -> _all.CPDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.CPDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.CPDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.CPDataBuilder]: ...
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
        ) -> _all.CPDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.CPDataReader: ...

    CPData: _CPDataStructModule
    class _MicroClimateDataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

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
            **kwargs: object,
        ) -> _all.MicroClimateDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.MicroClimateDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.MicroClimateDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.MicroClimateDataBuilder]: ...
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
        ) -> _all.MicroClimateDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.MicroClimateDataReader: ...

    MicroClimateData: _MicroClimateDataStructModule
    class _PhotosynthTStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            par: float | None = None,
            par24: float | None = None,
            par240: float | None = None,
            **kwargs: object,
        ) -> _all.PhotosynthTBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.PhotosynthTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.PhotosynthTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.PhotosynthTBuilder]: ...
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
        ) -> _all.PhotosynthTReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.PhotosynthTReader: ...

    PhotosynthT: _PhotosynthTStructModule
    class _FoliageTStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            tempK: float | None = None,
            tempK24: float | None = None,
            tempK240: float | None = None,
            **kwargs: object,
        ) -> _all.FoliageTBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.FoliageTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.FoliageTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.FoliageTBuilder]: ...
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
        ) -> _all.FoliageTReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.FoliageTReader: ...

    FoliageT: _FoliageTStructModule
    class _EnzymeActivityTStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            efIso: float | None = None,
            efMono: float | None = None,
            **kwargs: object,
        ) -> _all.EnzymeActivityTBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.EnzymeActivityTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.EnzymeActivityTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.EnzymeActivityTBuilder]: ...
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
        ) -> _all.EnzymeActivityTReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.EnzymeActivityTReader: ...

    EnzymeActivityT: _EnzymeActivityTStructModule
    class _LeafEmissionTStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            foliageLayer: int | None = None,
            pho: _all.PhotosynthTBuilder | dict[str, Any] | None = None,
            fol: _all.FoliageTBuilder | dict[str, Any] | None = None,
            enzAct: _all.EnzymeActivityTBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> _all.LeafEmissionTBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.LeafEmissionTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.LeafEmissionTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.LeafEmissionTBuilder]: ...
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
        ) -> _all.LeafEmissionTReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.LeafEmissionTReader: ...

    LeafEmissionT: _LeafEmissionTStructModule
    class _LeafEmissionsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            isoprene: float | None = None,
            monoterp: float | None = None,
            **kwargs: object,
        ) -> _all.LeafEmissionsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.LeafEmissionsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.LeafEmissionsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.LeafEmissionsBuilder]: ...
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
        ) -> _all.LeafEmissionsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.LeafEmissionsReader: ...

    LeafEmissions: _LeafEmissionsStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        **kwargs: object,
    ) -> _all.VocBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.VocReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.VocReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.VocBuilder]: ...
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
    ) -> _all.VocReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.VocReader: ...
