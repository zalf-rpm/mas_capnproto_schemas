"""Module helper types for `monica_state.capnp`."""

from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.model.monica.monica_management_capnp.types.modules import (
    _ParamsStructModule,
)
from mas.schema.model.monica.monica_params_capnp.types.builders import (
    AutomaticHarvestParametersBuilder,
    CropModuleParametersBuilder,
    CropParametersBuilder,
    CropResidueParametersBuilder,
    CultivarParametersBuilder,
    EnvironmentParametersBuilder,
    MeasuredGroundwaterTableInformationBuilder,
    SimulationParametersBuilder,
    SiteParametersBuilder,
    SoilMoistureModuleParametersBuilder,
    SoilOrganicModuleParametersBuilder,
    SoilParametersBuilder,
    SoilTemperatureModuleParametersBuilder,
    SoilTransportModuleParametersBuilder,
    SpeciesParametersBuilder,
)
from mas.schema.model.monica.monica_params_capnp.types.modules import _VocStructModule

from . import _all as _all

class _MaybeBoolStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        value: bool | None = None,
        **kwargs: object,
    ) -> _all.MaybeBoolBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.MaybeBoolReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.MaybeBoolReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.MaybeBoolBuilder]: ...
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
    ) -> _all.MaybeBoolReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.MaybeBoolReader: ...

class _CropModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        frostKillOn: bool | None = None,
        ktko: float | None = None,
        ktkc: float | None = None,
        assimilatePartCoeffsReduced: bool | None = None,
        o3WStomatalClosure: float | None = None,
        o3SumUptake: float | None = None,
        vsLatitude: float | None = None,
        abovegroundBiomass: float | None = None,
        abovegroundBiomassOld: float | None = None,
        pcAbovegroundOrgan: _all.BoolListBuilder | dict[str, Any] | None = None,
        actualTranspiration: float | None = None,
        pcAssimilatePartitioningCoeff: _all.Float64ListListBuilder
        | dict[str, Any]
        | None = None,
        pcAssimilateReallocation: float | None = None,
        assimilates: float | None = None,
        assimilationRate: float | None = None,
        astronomicDayLenght: float | None = None,
        pcBaseDaylength: _all.Float64ListBuilder | dict[str, Any] | None = None,
        pcBaseTemperature: _all.Float64ListBuilder | dict[str, Any] | None = None,
        pcBeginSensitivePhaseHeatStress: float | None = None,
        belowgroundBiomass: float | None = None,
        belowgroundBiomassOld: float | None = None,
        pcCarboxylationPathway: int | None = None,
        clearDayRadiation: float | None = None,
        pcCo2Method: int | None = None,
        criticalNConcentration: float | None = None,
        pcCriticalOxygenContent: _all.Float64ListBuilder | dict[str, Any] | None = None,
        pcCriticalTemperatureHeatStress: float | None = None,
        cropDiameter: float | None = None,
        cropFrostRedux: float | None = None,
        cropHeatRedux: float | None = None,
        cropHeight: float | None = None,
        pcCropHeightP1: float | None = None,
        pcCropHeightP2: float | None = None,
        pcCropName: str | None = None,
        cropNDemand: float | None = None,
        cropNRedux: float | None = None,
        pcCropSpecificMaxRootingDepth: float | None = None,
        cropWaterUptake: _all.Float64ListBuilder | dict[str, Any] | None = None,
        currentTemperatureSum: _all.Float64ListBuilder | dict[str, Any] | None = None,
        currentTotalTemperatureSum: float | None = None,
        currentTotalTemperatureSumRoot: float | None = None,
        pcCuttingDelayDays: int | None = None,
        daylengthFactor: float | None = None,
        pcDaylengthRequirement: _all.Float64ListBuilder | dict[str, Any] | None = None,
        daysAfterBeginFlowering: int | None = None,
        declination: float | None = None,
        pcDefaultRadiationUseEfficiency: float | None = None,
        vmDepthGroundwaterTable: int | None = None,
        pcDevelopmentAccelerationByNitrogenStress: int | None = None,
        developmentalStage: int | None = None,
        noOfCropSteps: int | None = None,
        droughtImpactOnFertility: float | None = None,
        pcDroughtImpactOnFertilityFactor: float | None = None,
        pcDroughtStressThreshold: _all.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        pcEmergenceFloodingControlOn: bool | None = None,
        pcEmergenceMoistureControlOn: bool | None = None,
        pcEndSensitivePhaseHeatStress: float | None = None,
        effectiveDayLength: float | None = None,
        errorStatus: bool | None = None,
        errorMessage: str | None = None,
        evaporatedFromIntercept: float | None = None,
        extraterrestrialRadiation: float | None = None,
        pcFieldConditionModifier: float | None = None,
        finalDevelopmentalStage: int | None = None,
        fixedN: float | None = None,
        pcFrostDehardening: float | None = None,
        pcFrostHardening: float | None = None,
        globalRadiation: float | None = None,
        greenAreaIndex: float | None = None,
        grossAssimilates: float | None = None,
        grossPhotosynthesis: float | None = None,
        grossPhotosynthesisMol: float | None = None,
        grossPhotosynthesisReferenceMol: float | None = None,
        grossPrimaryProduction: float | None = None,
        growthCycleEnded: bool | None = None,
        growthRespirationAS: float | None = None,
        pcHeatSumIrrigationStart: float | None = None,
        pcHeatSumIrrigationEnd: float | None = None,
        vsHeightNN: float | None = None,
        pcInitialKcFactor: float | None = None,
        pcInitialOrganBiomass: _all.Float64ListBuilder | dict[str, Any] | None = None,
        pcInitialRootingDepth: float | None = None,
        interceptionStorage: float | None = None,
        kcFactor: float | None = None,
        leafAreaIndex: float | None = None,
        sunlitLeafAreaIndex: _all.Float64ListBuilder | dict[str, Any] | None = None,
        shadedLeafAreaIndex: _all.Float64ListBuilder | dict[str, Any] | None = None,
        pcLowTemperatureExposure: float | None = None,
        pcLimitingTemperatureHeatStress: float | None = None,
        lt50: float | None = None,
        pcLt50cultivar: float | None = None,
        pcLuxuryNCoeff: float | None = None,
        maintenanceRespirationAS: float | None = None,
        pcMaxAssimilationRate: float | None = None,
        pcMaxCropDiameter: float | None = None,
        pcMaxCropHeight: float | None = None,
        maxNUptake: float | None = None,
        pcMaxNUptakeParam: float | None = None,
        pcMaxRootingDepth: float | None = None,
        pcMinimumNConcentration: float | None = None,
        pcMinimumTemperatureForAssimilation: float | None = None,
        pcOptimumTemperatureForAssimilation: float | None = None,
        pcMaximumTemperatureForAssimilation: float | None = None,
        pcMinimumTemperatureRootGrowth: float | None = None,
        netMaintenanceRespiration: float | None = None,
        netPhotosynthesis: float | None = None,
        netPrecipitation: float | None = None,
        netPrimaryProduction: float | None = None,
        pcNConcentrationAbovegroundBiomass: float | None = None,
        nConcentrationAbovegroundBiomass: float | None = None,
        nConcentrationAbovegroundBiomassOld: float | None = None,
        pcNConcentrationB0: float | None = None,
        nContentDeficit: float | None = None,
        pcNConcentrationPN: float | None = None,
        pcNConcentrationRoot: float | None = None,
        nConcentrationRoot: float | None = None,
        nConcentrationRootOld: float | None = None,
        pcNitrogenResponseOn: bool | None = None,
        pcNumberOfDevelopmentalStages: float | None = None,
        pcNumberOfOrgans: float | None = None,
        nUptakeFromLayer: _all.Float64ListBuilder | dict[str, Any] | None = None,
        pcOptimumTemperature: _all.Float64ListBuilder | dict[str, Any] | None = None,
        organBiomass: _all.Float64ListBuilder | dict[str, Any] | None = None,
        organDeadBiomass: _all.Float64ListBuilder | dict[str, Any] | None = None,
        organGreenBiomass: _all.Float64ListBuilder | dict[str, Any] | None = None,
        organGrowthIncrement: _all.Float64ListBuilder | dict[str, Any] | None = None,
        pcOrganGrowthRespiration: _all.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        pcOrganIdsForPrimaryYield: _all.YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        pcOrganIdsForSecondaryYield: _all.YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        pcOrganIdsForCutting: _all.YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        pcOrganMaintenanceRespiration: _all.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        organSenescenceIncrement: _all.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        pcOrganSenescenceRate: _all.Float64ListListBuilder
        | dict[str, Any]
        | None = None,
        overcastDayRadiation: float | None = None,
        oxygenDeficit: float | None = None,
        pcPartBiologicalNFixation: float | None = None,
        pcPerennial: bool | None = None,
        photoperiodicDaylength: float | None = None,
        photActRadiationMean: float | None = None,
        pcPlantDensity: float | None = None,
        potentialTranspiration: float | None = None,
        referenceEvapotranspiration: float | None = None,
        relativeTotalDevelopment: float | None = None,
        remainingEvapotranspiration: float | None = None,
        reserveAssimilatePool: float | None = None,
        pcResidueNRatio: float | None = None,
        pcRespiratoryStress: float | None = None,
        rootBiomass: float | None = None,
        rootBiomassOld: float | None = None,
        rootDensity: _all.Float64ListBuilder | dict[str, Any] | None = None,
        rootDiameter: _all.Float64ListBuilder | dict[str, Any] | None = None,
        pcRootDistributionParam: float | None = None,
        rootEffectivity: _all.Float64ListBuilder | dict[str, Any] | None = None,
        pcRootFormFactor: float | None = None,
        pcRootGrowthLag: float | None = None,
        rootingDepth: int | None = None,
        rootingDepthM: float | None = None,
        rootingZone: int | None = None,
        pcRootPenetrationRate: float | None = None,
        vmSaturationDeficit: float | None = None,
        soilCoverage: float | None = None,
        vsSoilMineralNContent: _all.Float64ListBuilder | dict[str, Any] | None = None,
        soilSpecificMaxRootingDepth: float | None = None,
        vsSoilSpecificMaxRootingDepth: float | None = None,
        pcSpecificLeafArea: _all.Float64ListBuilder | dict[str, Any] | None = None,
        pcSpecificRootLength: float | None = None,
        pcStageAfterCut: int | None = None,
        pcStageAtMaxDiameter: float | None = None,
        pcStageAtMaxHeight: float | None = None,
        pcStageMaxRootNConcentration: _all.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        pcStageKcFactor: _all.Float64ListBuilder | dict[str, Any] | None = None,
        pcStageTemperatureSum: _all.Float64ListBuilder | dict[str, Any] | None = None,
        stomataResistance: float | None = None,
        pcStorageOrgan: _all.BoolListBuilder | dict[str, Any] | None = None,
        storageOrgan: int | None = None,
        targetNConcentration: float | None = None,
        timeStep: float | None = None,
        timeUnderAnoxia: int | None = None,
        vsTortuosity: float | None = None,
        totalBiomass: float | None = None,
        totalBiomassNContent: float | None = None,
        totalCropHeatImpact: float | None = None,
        totalNInput: float | None = None,
        totalNUptake: float | None = None,
        totalRespired: float | None = None,
        respiration: float | None = None,
        sumTotalNUptake: float | None = None,
        totalRootLength: float | None = None,
        totalTemperatureSum: float | None = None,
        temperatureSumToFlowering: float | None = None,
        transpiration: _all.Float64ListBuilder | dict[str, Any] | None = None,
        transpirationRedux: _all.Float64ListBuilder | dict[str, Any] | None = None,
        transpirationDeficit: float | None = None,
        vernalisationDays: float | None = None,
        vernalisationFactor: float | None = None,
        pcVernalisationRequirement: _all.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        pcWaterDeficitResponseOn: bool | None = None,
        o3Senescence: float | None = None,
        o3LongTermDamage: float | None = None,
        o3ShortTermDamage: float | None = None,
        dyingOut: bool | None = None,
        accumulatedETa: float | None = None,
        accumulatedTranspiration: float | None = None,
        accumulatedPrimaryCropYield: float | None = None,
        sumExportedCutBiomass: float | None = None,
        exportedCutBiomass: float | None = None,
        sumResidueCutBiomass: float | None = None,
        residueCutBiomass: float | None = None,
        cuttingDelayDays: int | None = None,
        vsMaxEffectiveRootingDepth: float | None = None,
        vsImpenetrableLayerDept: float | None = None,
        anthesisDay: int | None = None,
        maturityDay: int | None = None,
        maturityReached: bool | None = None,
        stepSize24: int | None = None,
        stepSize240: int | None = None,
        rad24: _all.Float64ListBuilder | dict[str, Any] | None = None,
        rad240: _all.Float64ListBuilder | dict[str, Any] | None = None,
        tfol24: _all.Float64ListBuilder | dict[str, Any] | None = None,
        tfol240: _all.Float64ListBuilder | dict[str, Any] | None = None,
        index24: int | None = None,
        index240: int | None = None,
        full24: bool | None = None,
        full240: bool | None = None,
        guentherEmissions: _VocStructModule._EmissionsStructModule.Builder
        | dict[str, Any]
        | None = None,
        jjvEmissions: _VocStructModule._EmissionsStructModule.Builder
        | dict[str, Any]
        | None = None,
        vocSpecies: _VocStructModule._SpeciesDataStructModule.Builder
        | dict[str, Any]
        | None = None,
        cropPhotosynthesisResults: _VocStructModule._CPDataStructModule.Builder
        | dict[str, Any]
        | None = None,
        speciesParams: SpeciesParametersBuilder | dict[str, Any] | None = None,
        cultivarParams: CultivarParametersBuilder | dict[str, Any] | None = None,
        residueParams: CropResidueParametersBuilder | dict[str, Any] | None = None,
        isWinterCrop: bool | None = None,
        stemElongationEventFired: bool | None = None,
        lt50m: float | None = None,
        **kwargs: object,
    ) -> _all.CropModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.CropModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.CropModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.CropModuleStateBuilder]: ...
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
    ) -> _all.CropModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.CropModuleStateReader: ...

class _AOMPropertiesStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        aomSlow: float | None = None,
        aomFast: float | None = None,
        aomSlowDecRatetoSMBSlow: float | None = None,
        aomSlowDecRatetoSMBFast: float | None = None,
        aomFastDecRatetoSMBSlow: float | None = None,
        aomFastDecRatetoSMBFast: float | None = None,
        aomSlowDecCoeff: float | None = None,
        aomFastDecCoeff: float | None = None,
        aomSlowDecCoeffStandard: float | None = None,
        aomFastDecCoeffStandard: float | None = None,
        partAOMSlowtoSMBSlow: float | None = None,
        partAOMSlowtoSMBFast: float | None = None,
        cnRatioAOMSlow: float | None = None,
        cnRatioAOMFast: float | None = None,
        daysAfterApplication: int | None = None,
        aomDryMatterContent: float | None = None,
        aomNH4Content: float | None = None,
        aomSlowDelta: float | None = None,
        aomFastDelta: float | None = None,
        incorporation: bool | None = None,
        noVolatilization: bool | None = None,
        **kwargs: object,
    ) -> _all.AOMPropertiesBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.AOMPropertiesReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.AOMPropertiesReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.AOMPropertiesBuilder]: ...
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
    ) -> _all.AOMPropertiesReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.AOMPropertiesReader: ...

class _SoilLayerStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        layerThickness: float | None = None,
        soilWaterFlux: float | None = None,
        voAOMPool: _all.AOMPropertiesListBuilder | dict[str, Any] | None = None,
        somSlow: float | None = None,
        somFast: float | None = None,
        smbSlow: float | None = None,
        smbFast: float | None = None,
        soilCarbamid: float | None = None,
        soilNH4: float | None = None,
        soilNO2: float | None = None,
        soilNO3: float | None = None,
        soilFrozen: bool | None = None,
        sps: SoilParametersBuilder | dict[str, Any] | None = None,
        soilMoistureM3: float | None = None,
        soilTemperature: float | None = None,
        **kwargs: object,
    ) -> _all.SoilLayerStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SoilLayerStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SoilLayerStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SoilLayerStateBuilder]: ...
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
    ) -> _all.SoilLayerStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SoilLayerStateReader: ...

class _SoilColumnStateStructModule(_StructModule):
    class _DelayedNMinApplicationParamsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            fp: _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder
            | dict[str, Any]
            | None = None,
            samplingDepth: float | None = None,
            cropNTarget: float | None = None,
            cropNTarget30: float | None = None,
            fertiliserMinApplication: float | None = None,
            fertiliserMaxApplication: float | None = None,
            topDressingDelay: float | None = None,
            **kwargs: object,
        ) -> _all.DelayedNMinApplicationParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.DelayedNMinApplicationParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.DelayedNMinApplicationParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.DelayedNMinApplicationParamsBuilder]: ...
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
        ) -> _all.DelayedNMinApplicationParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.DelayedNMinApplicationParamsReader: ...

    DelayedNMinApplicationParams: _DelayedNMinApplicationParamsStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        vsSurfaceWaterStorage: float | None = None,
        vsInterceptionStorage: float | None = None,
        vmGroundwaterTable: int | None = None,
        vsFluxAtLowerBoundary: float | None = None,
        vqCropNUptake: float | None = None,
        vtSoilSurfaceTemperature: float | None = None,
        vmSnowDepth: float | None = None,
        psMaxMineralisationDepth: float | None = None,
        vsNumberOfOrganicLayers: float | None = None,
        vfTopDressing: float | None = None,
        vfTopDressingPartition: _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder
        | dict[str, Any]
        | None = None,
        vfTopDressingDelay: int | None = None,
        cropModule: _all.CropModuleStateBuilder | dict[str, Any] | None = None,
        delayedNMinApplications: _all.DelayedNMinApplicationParamsListBuilder
        | dict[str, Any]
        | None = None,
        pmCriticalMoistureDepth: float | None = None,
        layers: _all.SoilLayerStateListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.SoilColumnStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SoilColumnStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SoilColumnStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SoilColumnStateBuilder]: ...
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
    ) -> _all.SoilColumnStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SoilColumnStateReader: ...

class _SoilTemperatureModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        soilSurfaceTemperature: float | None = None,
        moduleParams: SoilTemperatureModuleParametersBuilder
        | dict[str, Any]
        | None = None,
        dampingFactor: float | None = None,
        soilColumnVtGroundLayer: _all.SoilLayerStateBuilder
        | dict[str, Any]
        | None = None,
        soilColumnVtBottomLayer: _all.SoilLayerStateBuilder
        | dict[str, Any]
        | None = None,
        numberOfLayers: int | None = None,
        vsNumberOfLayers: int | None = None,
        vsSoilMoistureConst: _all.Float64ListBuilder | dict[str, Any] | None = None,
        soilTemperature: _all.Float64ListBuilder | dict[str, Any] | None = None,
        v: _all.Float64ListBuilder | dict[str, Any] | None = None,
        volumeMatrix: _all.Float64ListBuilder | dict[str, Any] | None = None,
        volumeMatrixOld: _all.Float64ListBuilder | dict[str, Any] | None = None,
        b: _all.Float64ListBuilder | dict[str, Any] | None = None,
        matrixPrimaryDiagonal: _all.Float64ListBuilder | dict[str, Any] | None = None,
        matrixSecundaryDiagonal: _all.Float64ListBuilder | dict[str, Any] | None = None,
        heatFlow: float | None = None,
        heatConductivity: _all.Float64ListBuilder | dict[str, Any] | None = None,
        heatConductivityMean: _all.Float64ListBuilder | dict[str, Any] | None = None,
        heatCapacity: _all.Float64ListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.SoilTemperatureModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SoilTemperatureModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SoilTemperatureModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SoilTemperatureModuleStateBuilder]: ...
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
    ) -> _all.SoilTemperatureModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SoilTemperatureModuleStateReader: ...

class _FrostModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        pmHydraulicConductivityRedux: float | None = None,
        frostDepth: float | None = None,
        accumulatedFrostDepth: float | None = None,
        negativeDegreeDays: float | None = None,
        thawDepth: float | None = None,
        frostDays: int | None = None,
        lambdaRedux: _all.Float64ListBuilder | dict[str, Any] | None = None,
        temperatureUnderSnow: float | None = None,
        hydraulicConductivityRedux: float | None = None,
        ptTimeStep: float | None = None,
        **kwargs: object,
    ) -> _all.FrostModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.FrostModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.FrostModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.FrostModuleStateBuilder]: ...
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
    ) -> _all.FrostModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.FrostModuleStateReader: ...

class _SnowModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        snowRetentionCapacityMax: float | None = None,
        snowDensity: float | None = None,
        snowDepth: float | None = None,
        frozenWaterInSnow: float | None = None,
        liquidWaterInSnow: float | None = None,
        waterToInfiltrate: float | None = None,
        maxSnowDepth: float | None = None,
        accumulatedSnowDepth: float | None = None,
        snowmeltTemperature: float | None = None,
        snowAccumulationThresholdTemperature: float | None = None,
        temperatureLimitForLiquidWater: float | None = None,
        correctionRain: float | None = None,
        correctionSnow: float | None = None,
        refreezeTemperature: float | None = None,
        refreezeP1: float | None = None,
        refreezeP2: float | None = None,
        newSnowDensityMin: float | None = None,
        snowMaxAdditionalDensity: float | None = None,
        snowPacking: float | None = None,
        snowRetentionCapacityMin: float | None = None,
        **kwargs: object,
    ) -> _all.SnowModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SnowModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SnowModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SnowModuleStateBuilder]: ...
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
    ) -> _all.SnowModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SnowModuleStateReader: ...

class _SoilMoistureModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        frostComponent: _all.FrostModuleStateBuilder | dict[str, Any] | None = None,
        snowComponent: _all.SnowModuleStateBuilder | dict[str, Any] | None = None,
        xSACriticalSoilMoisture: float | None = None,
        moduleParams: SoilMoistureModuleParametersBuilder
        | dict[str, Any]
        | None = None,
        vwWindSpeedHeight: float | None = None,
        vwWindSpeed: float | None = None,
        numberOfLayers: int | None = None,
        vsNumberOfLayers: int | None = None,
        actualEvaporation: float | None = None,
        actualEvapotranspiration: float | None = None,
        actualTranspiration: float | None = None,
        availableWater: _all.Float64ListBuilder | dict[str, Any] | None = None,
        capillaryRise: float | None = None,
        capillaryRiseRate: _all.Float64ListBuilder | dict[str, Any] | None = None,
        capillaryWater: _all.Float64ListBuilder | dict[str, Any] | None = None,
        capillaryWater70: _all.Float64ListBuilder | dict[str, Any] | None = None,
        evaporation: _all.Float64ListBuilder | dict[str, Any] | None = None,
        evapotranspiration: _all.Float64ListBuilder | dict[str, Any] | None = None,
        fieldCapacity: _all.Float64ListBuilder | dict[str, Any] | None = None,
        fluxAtLowerBoundary: float | None = None,
        gravitationalWater: _all.Float64ListBuilder | dict[str, Any] | None = None,
        grossPrecipitation: float | None = None,
        groundwaterAdded: float | None = None,
        groundwaterDischarge: float | None = None,
        groundwaterTable: int | None = None,
        heatConductivity: _all.Float64ListBuilder | dict[str, Any] | None = None,
        hydraulicConductivityRedux: float | None = None,
        infiltration: float | None = None,
        interception: float | None = None,
        vcKcFactor: float | None = None,
        lambda_: _all.Float64ListBuilder | dict[str, Any] | None = None,
        lambdaReduced: float | None = None,
        vsLatitude: float | None = None,
        layerThickness: _all.Float64ListBuilder | dict[str, Any] | None = None,
        pmLayerThickness: float | None = None,
        pmLeachingDepth: float | None = None,
        pmLeachingDepthLayer: int | None = None,
        vwMaxAirTemperature: float | None = None,
        pmMaxPercolationRate: float | None = None,
        vwMeanAirTemperature: float | None = None,
        vwMinAirTemperature: float | None = None,
        vcNetPrecipitation: float | None = None,
        vwNetRadiation: float | None = None,
        permanentWiltingPoint: _all.Float64ListBuilder | dict[str, Any] | None = None,
        vcPercentageSoilCoverage: float | None = None,
        percolationRate: _all.Float64ListBuilder | dict[str, Any] | None = None,
        vwPrecipitation: float | None = None,
        referenceEvapotranspiration: float | None = None,
        relativeHumidity: float | None = None,
        residualEvapotranspiration: _all.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        saturatedHydraulicConductivity: _all.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        soilMoisture: _all.Float64ListBuilder | dict[str, Any] | None = None,
        soilMoisturecrit: float | None = None,
        soilMoistureDeficit: float | None = None,
        soilPoreVolume: _all.Float64ListBuilder | dict[str, Any] | None = None,
        vcStomataResistance: float | None = None,
        surfaceRoughness: float | None = None,
        surfaceRunOff: float | None = None,
        sumSurfaceRunOff: float | None = None,
        surfaceWaterStorage: float | None = None,
        ptTimeStep: float | None = None,
        totalWaterRemoval: float | None = None,
        transpiration: _all.Float64ListBuilder | dict[str, Any] | None = None,
        transpirationDeficit: float | None = None,
        waterFlux: _all.Float64ListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.SoilMoistureModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SoilMoistureModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SoilMoistureModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SoilMoistureModuleStateBuilder]: ...
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
    ) -> _all.SoilMoistureModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SoilMoistureModuleStateReader: ...

class _SoilOrganicModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        incorporation: bool | None = None,
        totalDenitrification: float | None = None,
        moduleParams: SoilOrganicModuleParametersBuilder | dict[str, Any] | None = None,
        vsNumberOfLayers: int | None = None,
        vsNumberOfOrganicLayers: int | None = None,
        addedOrganicMatter: bool | None = None,
        irrigationAmount: float | None = None,
        actAmmoniaOxidationRate: _all.Float64ListBuilder | dict[str, Any] | None = None,
        actNitrificationRate: _all.Float64ListBuilder | dict[str, Any] | None = None,
        actDenitrificationRate: _all.Float64ListBuilder | dict[str, Any] | None = None,
        aomFastDeltaSum: _all.Float64ListBuilder | dict[str, Any] | None = None,
        aomFastInput: _all.Float64ListBuilder | dict[str, Any] | None = None,
        aomFastSum: _all.Float64ListBuilder | dict[str, Any] | None = None,
        aomSlowDeltaSum: _all.Float64ListBuilder | dict[str, Any] | None = None,
        aomSlowInput: _all.Float64ListBuilder | dict[str, Any] | None = None,
        aomSlowSum: _all.Float64ListBuilder | dict[str, Any] | None = None,
        cBalance: _all.Float64ListBuilder | dict[str, Any] | None = None,
        decomposerRespiration: float | None = None,
        errorMessage: str | None = None,
        inertSoilOrganicC: _all.Float64ListBuilder | dict[str, Any] | None = None,
        n2oProduced: float | None = None,
        n2oProducedNit: float | None = None,
        n2oProducedDenit: float | None = None,
        netEcosystemExchange: float | None = None,
        netEcosystemProduction: float | None = None,
        netNMineralisation: float | None = None,
        netNMineralisationRate: _all.Float64ListBuilder | dict[str, Any] | None = None,
        totalNH3Volatilised: float | None = None,
        nh3Volatilised: float | None = None,
        smbCO2EvolutionRate: _all.Float64ListBuilder | dict[str, Any] | None = None,
        smbFastDelta: _all.Float64ListBuilder | dict[str, Any] | None = None,
        smbSlowDelta: _all.Float64ListBuilder | dict[str, Any] | None = None,
        vsSoilMineralNContent: _all.Float64ListBuilder | dict[str, Any] | None = None,
        soilOrganicC: _all.Float64ListBuilder | dict[str, Any] | None = None,
        somFastDelta: _all.Float64ListBuilder | dict[str, Any] | None = None,
        somFastInput: _all.Float64ListBuilder | dict[str, Any] | None = None,
        somSlowDelta: _all.Float64ListBuilder | dict[str, Any] | None = None,
        sumDenitrification: float | None = None,
        sumNetNMineralisation: float | None = None,
        sumN2OProduced: float | None = None,
        sumNH3Volatilised: float | None = None,
        **kwargs: object,
    ) -> _all.SoilOrganicModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SoilOrganicModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SoilOrganicModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SoilOrganicModuleStateBuilder]: ...
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
    ) -> _all.SoilOrganicModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SoilOrganicModuleStateReader: ...

class _SoilTransportModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        pcMinimumAvailableN: float | None = None,
        moduleParams: SoilTransportModuleParametersBuilder
        | dict[str, Any]
        | None = None,
        convection: _all.Float64ListBuilder | dict[str, Any] | None = None,
        cropNUptake: float | None = None,
        diffusionCoeff: _all.Float64ListBuilder | dict[str, Any] | None = None,
        dispersion: _all.Float64ListBuilder | dict[str, Any] | None = None,
        dispersionCoeff: _all.Float64ListBuilder | dict[str, Any] | None = None,
        vsLeachingDepth: float | None = None,
        leachingAtBoundary: float | None = None,
        vsNDeposition: float | None = None,
        vcNUptakeFromLayer: _all.Float64ListBuilder | dict[str, Any] | None = None,
        poreWaterVelocity: _all.Float64ListBuilder | dict[str, Any] | None = None,
        vsSoilMineralNContent: _all.Float64ListBuilder | dict[str, Any] | None = None,
        soilNO3: _all.Float64ListBuilder | dict[str, Any] | None = None,
        soilNO3aq: _all.Float64ListBuilder | dict[str, Any] | None = None,
        timeStep: float | None = None,
        totalDispersion: _all.Float64ListBuilder | dict[str, Any] | None = None,
        percolationRate: _all.Float64ListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.SoilTransportModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SoilTransportModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SoilTransportModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SoilTransportModuleStateBuilder]: ...
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
    ) -> _all.SoilTransportModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SoilTransportModuleStateReader: ...

class _MonicaModelStateStructModule(_StructModule):
    class _ACDToValueStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            acd: int | None = None,
            value: float | None = None,
            **kwargs: object,
        ) -> _all.ACDToValueBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.ACDToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.ACDToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.ACDToValueBuilder]: ...
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
        ) -> _all.ACDToValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.ACDToValueReader: ...

    ACDToValue: _ACDToValueStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        sitePs: SiteParametersBuilder | dict[str, Any] | None = None,
        cultivationMethodCount: int | None = None,
        envPs: EnvironmentParametersBuilder | dict[str, Any] | None = None,
        cropPs: CropModuleParametersBuilder | dict[str, Any] | None = None,
        vsGroundwaterDepth: float | None = None,
        vwAtmosphericO3Concentration: float | None = None,
        vwAtmosphericCO2Concentration: float | None = None,
        simPs: SimulationParametersBuilder | dict[str, Any] | None = None,
        groundwaterInformation: MeasuredGroundwaterTableInformationBuilder
        | dict[str, Any]
        | None = None,
        soilColumn: _all.SoilColumnStateBuilder | dict[str, Any] | None = None,
        soilTemperature: _all.SoilTemperatureModuleStateBuilder
        | dict[str, Any]
        | None = None,
        soilMoisture: _all.SoilMoistureModuleStateBuilder
        | dict[str, Any]
        | None = None,
        soilOrganic: _all.SoilOrganicModuleStateBuilder | dict[str, Any] | None = None,
        soilTransport: _all.SoilTransportModuleStateBuilder
        | dict[str, Any]
        | None = None,
        accuOxygenStress: float | None = None,
        currentCropModule: _all.CropModuleStateBuilder | dict[str, Any] | None = None,
        sumFertiliser: float | None = None,
        sumOrgFertiliser: float | None = None,
        dailySumFertiliser: float | None = None,
        dailySumOrgFertiliser: float | None = None,
        dailySumOrganicFertilizerDM: float | None = None,
        sumOrganicFertilizerDM: float | None = None,
        humusBalanceCarryOver: float | None = None,
        dailySumIrrigationWater: float | None = None,
        optCarbonExportedResidues: float | None = None,
        optCarbonReturnedResidues: float | None = None,
        currentStepDate: DateBuilder | dict[str, Any] | None = None,
        climateData: _all.ACDToValueListListBuilder | dict[str, Any] | None = None,
        currentEvents: _all.TextListBuilder | dict[str, Any] | None = None,
        previousDaysEvents: _all.TextListBuilder | dict[str, Any] | None = None,
        clearCropUponNextDay: bool | None = None,
        daysWithCrop: int | None = None,
        accuNStress: float | None = None,
        accuWaterStress: float | None = None,
        accuHeatStress: float | None = None,
        **kwargs: object,
    ) -> _all.MonicaModelStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.MonicaModelStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.MonicaModelStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.MonicaModelStateBuilder]: ...
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
    ) -> _all.MonicaModelStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.MonicaModelStateReader: ...

class _RuntimeStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        modelState: _all.MonicaModelStateBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.RuntimeStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.RuntimeStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.RuntimeStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.RuntimeStateBuilder]: ...
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
    ) -> _all.RuntimeStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.RuntimeStateReader: ...

class _CropStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        automaticHarvestParams: AutomaticHarvestParametersBuilder
        | dict[str, Any]
        | None = None,
        speciesName: str | None = None,
        cultivarName: str | None = None,
        seedDate: DateBuilder | dict[str, Any] | None = None,
        harvestDate: DateBuilder | dict[str, Any] | None = None,
        isWinterCrop: _all.MaybeBoolBuilder | dict[str, Any] | None = None,
        isPerennialCrop: _all.MaybeBoolBuilder | dict[str, Any] | None = None,
        cuttingDates: _all.DateListBuilder | dict[str, Any] | None = None,
        cropParams: CropParametersBuilder | dict[str, Any] | None = None,
        perennialCropParams: CropParametersBuilder | dict[str, Any] | None = None,
        residueParams: CropResidueParametersBuilder | dict[str, Any] | None = None,
        crossCropAdaptionFactor: float | None = None,
        automaticHarvest: bool | None = None,
        **kwargs: object,
    ) -> _all.CropStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.CropStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.CropStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.CropStateBuilder]: ...
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
    ) -> _all.CropStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.CropStateReader: ...

class _ICDataStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        noCrop: None | None = None,
        height: float | None = None,
        lait: float | None = None,
        **kwargs: object,
    ) -> _all.ICDataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.ICDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.ICDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.ICDataBuilder]: ...
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
    ) -> _all.ICDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.ICDataReader: ...
