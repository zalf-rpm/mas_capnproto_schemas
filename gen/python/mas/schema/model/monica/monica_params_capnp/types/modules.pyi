"""Module helper types for `monica_params.capnp`."""

from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _EnumSchema,
    _ListSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.climate.climate_capnp.types.enums import RCPEnum
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.model.monica.monica_management_capnp.types.modules import (
    _ParamsStructModule,
)
from mas.schema.model.monica.monica_params_capnp.types import builders as builders
from mas.schema.model.monica.monica_params_capnp.types import enums as enums
from mas.schema.model.monica.monica_params_capnp.types import readers as readers
from mas.schema.model.monica.monica_params_capnp.types import schemas as schemas

class _SpeciesParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SpeciesParametersSchema(_StructSchema):
        class _BaseTemperatureField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _OrganMaintenanceRespirationField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _OrganGrowthRespirationField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _StageMaxRootNConcentrationField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _InitialOrganBiomassField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _CriticalOxygenContentField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _StageMobilFromStorageCoeffField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _AbovegroundOrganField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _StorageOrganField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["speciesId"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["carboxylationPathway"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["defaultRadiationUseEfficiency"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["partBiologicalNFixation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["initialKcFactor"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["luxuryNCoeff"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maxCropDiameter"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stageAtMaxHeight"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stageAtMaxDiameter"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["minimumNConcentration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["minimumTemperatureForAssimilation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["optimumTemperatureForAssimilation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maximumTemperatureForAssimilation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nConcentrationAbovegroundBiomass"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nConcentrationB0"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nConcentrationPN"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nConcentrationRoot"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["developmentAccelerationByNitrogenStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["fieldConditionModifier"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["assimilateReallocation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["baseTemperature"],
            ) -> _SpeciesParametersStructModule._SpeciesParametersSchema._BaseTemperatureField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["organMaintenanceRespiration"],
            ) -> _SpeciesParametersStructModule._SpeciesParametersSchema._OrganMaintenanceRespirationField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["organGrowthRespiration"],
            ) -> _SpeciesParametersStructModule._SpeciesParametersSchema._OrganGrowthRespirationField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stageMaxRootNConcentration"],
            ) -> _SpeciesParametersStructModule._SpeciesParametersSchema._StageMaxRootNConcentrationField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["initialOrganBiomass"],
            ) -> _SpeciesParametersStructModule._SpeciesParametersSchema._InitialOrganBiomassField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["criticalOxygenContent"],
            ) -> _SpeciesParametersStructModule._SpeciesParametersSchema._CriticalOxygenContentField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stageMobilFromStorageCoeff"],
            ) -> _SpeciesParametersStructModule._SpeciesParametersSchema._StageMobilFromStorageCoeffField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["abovegroundOrgan"],
            ) -> _SpeciesParametersStructModule._SpeciesParametersSchema._AbovegroundOrganField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["storageOrgan"],
            ) -> _SpeciesParametersStructModule._SpeciesParametersSchema._StorageOrganField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["samplingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["targetNSamplingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["targetN30"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maxNUptakeParam"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rootDistributionParam"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["plantDensity"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rootGrowthLag"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["minimumTemperatureRootGrowth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["initialRootingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rootPenetrationRate"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rootFormFactor"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["specificRootLength"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stageAfterCut"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["limitingTemperatureHeatStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cuttingDelayDays"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["droughtImpactOnFertilityFactor"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["efMono"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["efMonos"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["efIso"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["vcMax25"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["aekc"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["aeko"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["aevc"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["kc25"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["ko25"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["transitionStageLeafExp"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SpeciesParametersStructModule._SpeciesParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SpeciesParametersSchema: ...
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
        baseTemperature: builders.Float64ListBuilder | dict[str, Any] | None = None,
        organMaintenanceRespiration: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        organGrowthRespiration: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        stageMaxRootNConcentration: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        initialOrganBiomass: builders.Float64ListBuilder | dict[str, Any] | None = None,
        criticalOxygenContent: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        stageMobilFromStorageCoeff: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        abovegroundOrgan: builders.BoolListBuilder | dict[str, Any] | None = None,
        storageOrgan: builders.BoolListBuilder | dict[str, Any] | None = None,
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
    ) -> builders.SpeciesParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SpeciesParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SpeciesParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SpeciesParametersBuilder]: ...
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
    ) -> readers.SpeciesParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SpeciesParametersReader: ...

class _YieldComponentStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _YieldComponentSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["organId"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["yieldPercentage"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["yieldDryMatter"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _YieldComponentStructModule._YieldComponentSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._YieldComponentSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        organId: int | None = None,
        yieldPercentage: float | None = None,
        yieldDryMatter: float | None = None,
        **kwargs: object,
    ) -> builders.YieldComponentBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.YieldComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.YieldComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.YieldComponentBuilder]: ...
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
    ) -> readers.YieldComponentReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.YieldComponentReader: ...

class _CultivarParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _CultivarParametersSchema(_StructSchema):
        class _AssimilatePartitioningCoeffField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> _ListSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._AssimilatePartitioningCoeffField._Schema: ...

        class _OrganSenescenceRateField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> _ListSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._OrganSenescenceRateField._Schema: ...

        class _BaseDaylengthField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _OptimumTemperatureField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _DaylengthRequirementField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _DroughtStressThresholdField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SpecificLeafAreaField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _StageKcFactorField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _StageTemperatureSumField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _VernalisationRequirementField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _OrganIdsForPrimaryYieldField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._YieldComponentSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._OrganIdsForPrimaryYieldField._Schema: ...

        class _OrganIdsForSecondaryYieldField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._YieldComponentSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._OrganIdsForSecondaryYieldField._Schema: ...

        class _OrganIdsForCuttingField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._YieldComponentSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._OrganIdsForCuttingField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["cultivarId"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["description"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["perennial"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maxAssimilationRate"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maxCropHeight"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["residueNRatio"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lt50cultivar"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropHeightP1"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropHeightP2"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropSpecificMaxRootingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["assimilatePartitioningCoeff"],
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._AssimilatePartitioningCoeffField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["organSenescenceRate"],
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._OrganSenescenceRateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["baseDaylength"],
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._BaseDaylengthField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["optimumTemperature"],
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._OptimumTemperatureField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["daylengthRequirement"],
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._DaylengthRequirementField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["droughtStressThreshold"],
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._DroughtStressThresholdField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["specificLeafArea"],
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._SpecificLeafAreaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stageKcFactor"],
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._StageKcFactorField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stageTemperatureSum"],
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._StageTemperatureSumField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vernalisationRequirement"],
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._VernalisationRequirementField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["heatSumIrrigationStart"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["heatSumIrrigationEnd"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["criticalTemperatureHeatStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["beginSensitivePhaseHeatStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["endSensitivePhaseHeatStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["frostHardening"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["frostDehardening"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lowTemperatureExposure"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["respiratoryStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["latestHarvestDoy"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["organIdsForPrimaryYield"],
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._OrganIdsForPrimaryYieldField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["organIdsForSecondaryYield"],
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._OrganIdsForSecondaryYieldField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["organIdsForCutting"],
            ) -> _CultivarParametersStructModule._CultivarParametersSchema._OrganIdsForCuttingField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["earlyRefLeafExp"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["refLeafExp"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["minTempDevWE"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["optTempDevWE"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maxTempDevWE"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["winterCrop"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _CultivarParametersStructModule._CultivarParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._CultivarParametersSchema: ...
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
        assimilatePartitioningCoeff: builders.Float64ListListBuilder
        | dict[str, Any]
        | None = None,
        organSenescenceRate: builders.Float64ListListBuilder
        | dict[str, Any]
        | None = None,
        baseDaylength: builders.Float64ListBuilder | dict[str, Any] | None = None,
        optimumTemperature: builders.Float64ListBuilder | dict[str, Any] | None = None,
        daylengthRequirement: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        droughtStressThreshold: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        specificLeafArea: builders.Float64ListBuilder | dict[str, Any] | None = None,
        stageKcFactor: builders.Float64ListBuilder | dict[str, Any] | None = None,
        stageTemperatureSum: builders.Float64ListBuilder | dict[str, Any] | None = None,
        vernalisationRequirement: builders.Float64ListBuilder
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
        organIdsForPrimaryYield: builders.YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        organIdsForSecondaryYield: builders.YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        organIdsForCutting: builders.YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        earlyRefLeafExp: float | None = None,
        refLeafExp: float | None = None,
        minTempDevWE: float | None = None,
        optTempDevWE: float | None = None,
        maxTempDevWE: float | None = None,
        winterCrop: bool | None = None,
        **kwargs: object,
    ) -> builders.CultivarParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.CultivarParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.CultivarParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.CultivarParametersBuilder]: ...
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
    ) -> readers.CultivarParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CultivarParametersReader: ...

class _CropParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _CropParametersSchema(_StructSchema):
        class _SpeciesParamsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._SpeciesParametersSchema: ...

        class _CultivarParamsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._CultivarParametersSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["speciesParams"],
            ) -> (
                _CropParametersStructModule._CropParametersSchema._SpeciesParamsField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["cultivarParams"],
            ) -> (
                _CropParametersStructModule._CropParametersSchema._CultivarParamsField
            ): ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _CropParametersStructModule._CropParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._CropParametersSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        speciesParams: builders.SpeciesParametersBuilder | dict[str, Any] | None = None,
        cultivarParams: builders.CultivarParametersBuilder
        | dict[str, Any]
        | None = None,
        **kwargs: object,
    ) -> builders.CropParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.CropParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.CropParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.CropParametersBuilder]: ...
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
    ) -> readers.CropParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CropParametersReader: ...

class _CropResidueParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _CropResidueParametersSchema(_StructSchema):
        class _ParamsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _StructSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["params"],
            ) -> _CropResidueParametersStructModule._CropResidueParametersSchema._ParamsField: ...
            @overload
            def __getitem__(self, key: Literal["species"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["residueType"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> (
            _CropResidueParametersStructModule._CropResidueParametersSchema._Fields
        ): ...

    @property
    @override
    def schema(self) -> schemas._CropResidueParametersSchema: ...
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
    ) -> builders.CropResidueParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.CropResidueParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.CropResidueParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.CropResidueParametersBuilder]: ...
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
    ) -> readers.CropResidueParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CropResidueParametersReader: ...

class _CropSpecStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _CropSpecSchema(_StructSchema):
        class _CropParamsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._CropParametersSchema: ...

        class _ResidueParamsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._CropResidueParametersSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["cropParams"],
            ) -> _CropSpecStructModule._CropSpecSchema._CropParamsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["residueParams"],
            ) -> _CropSpecStructModule._CropSpecSchema._ResidueParamsField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _CropSpecStructModule._CropSpecSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._CropSpecSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        cropParams: builders.CropParametersBuilder | dict[str, Any] | None = None,
        residueParams: builders.CropResidueParametersBuilder
        | dict[str, Any]
        | None = None,
        **kwargs: object,
    ) -> builders.CropSpecBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.CropSpecReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.CropSpecReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.CropSpecBuilder]: ...
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
    ) -> readers.CropSpecReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CropSpecReader: ...

class _AutomaticHarvestParametersStructModule(_StructModule):
    class _HarvestTimeEnumModule:
        maturity: int
        unknown: int

    HarvestTime: _HarvestTimeEnumModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _AutomaticHarvestParametersSchema(_StructSchema):
        class _HarvestTimeField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _EnumSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["harvestTime"],
            ) -> _AutomaticHarvestParametersStructModule._AutomaticHarvestParametersSchema._HarvestTimeField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["latestHarvestDOY"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _AutomaticHarvestParametersStructModule._AutomaticHarvestParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._AutomaticHarvestParametersSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        harvestTime: enums.AutomaticHarvestParametersHarvestTimeEnum | None = None,
        latestHarvestDOY: int | None = None,
        **kwargs: object,
    ) -> builders.AutomaticHarvestParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.AutomaticHarvestParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.AutomaticHarvestParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.AutomaticHarvestParametersBuilder]: ...
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
    ) -> readers.AutomaticHarvestParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.AutomaticHarvestParametersReader: ...

class _NMinCropParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _NMinCropParametersSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["samplingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["nTarget"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["nTarget30"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _NMinCropParametersStructModule._NMinCropParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._NMinCropParametersSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        samplingDepth: float | None = None,
        nTarget: float | None = None,
        nTarget30: float | None = None,
        **kwargs: object,
    ) -> builders.NMinCropParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.NMinCropParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.NMinCropParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.NMinCropParametersBuilder]: ...
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
    ) -> readers.NMinCropParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.NMinCropParametersReader: ...

class _NMinApplicationParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _NMinApplicationParametersSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["min"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["max"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["delayInDays"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _NMinApplicationParametersStructModule._NMinApplicationParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._NMinApplicationParametersSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        min: float | None = None,
        max: float | None = None,
        delayInDays: int | None = None,
        **kwargs: object,
    ) -> builders.NMinApplicationParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.NMinApplicationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.NMinApplicationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.NMinApplicationParametersBuilder]: ...
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
    ) -> readers.NMinApplicationParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.NMinApplicationParametersReader: ...

class _SoilParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilParametersSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["soilSandContent"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilClayContent"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["soilpH"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilStoneContent"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["lambda"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["fieldCapacity"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["saturation"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["permanentWiltingPoint"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilTexture"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilAmmonium"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilNitrate"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilCNRatio"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilMoisturePercentFC"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilRawDensity"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilBulkDensity"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilOrganicCarbon"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilOrganicMatter"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SoilParametersStructModule._SoilParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SoilParametersSchema: ...
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
    ) -> builders.SoilParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SoilParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilParametersBuilder]: ...
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
    ) -> readers.SoilParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilParametersReader: ...

class _AutomaticIrrigationParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _AutomaticIrrigationParametersSchema(_StructSchema):
        class _ParamsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _StructSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["params"],
            ) -> _AutomaticIrrigationParametersStructModule._AutomaticIrrigationParametersSchema._ParamsField: ...
            @overload
            def __getitem__(self, key: Literal["amount"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["threshold"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _AutomaticIrrigationParametersStructModule._AutomaticIrrigationParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._AutomaticIrrigationParametersSchema: ...
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
    ) -> builders.AutomaticIrrigationParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.AutomaticIrrigationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.AutomaticIrrigationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.AutomaticIrrigationParametersBuilder]: ...
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
    ) -> readers.AutomaticIrrigationParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.AutomaticIrrigationParametersReader: ...

class _SiteParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SiteParametersSchema(_StructSchema):
        class _SoilParametersField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._SoilParametersSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _SiteParametersStructModule._SiteParametersSchema._SoilParametersField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["latitude"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["slope"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["heightNN"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["groundwaterDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilCNRatio"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["drainageCoeff"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vqNDeposition"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maxEffectiveRootingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["impenetrableLayerDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilSpecificHumusBalanceCorrection"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilParameters"],
            ) -> (
                _SiteParametersStructModule._SiteParametersSchema._SoilParametersField
            ): ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SiteParametersStructModule._SiteParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SiteParametersSchema: ...
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
        soilParameters: builders.SoilParametersListBuilder
        | dict[str, Any]
        | None = None,
        **kwargs: object,
    ) -> builders.SiteParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SiteParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SiteParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SiteParametersBuilder]: ...
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
    ) -> readers.SiteParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SiteParametersReader: ...

class _EnvironmentParametersStructModule(_StructModule):
    class _YearToValueStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _YearToValueSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["year"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["value"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _EnvironmentParametersStructModule._YearToValueStructModule._YearToValueSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._EnvironmentParametersYearToValueSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            year: int | None = None,
            value: float | None = None,
            **kwargs: object,
        ) -> builders.YearToValueBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.YearToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.YearToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.YearToValueBuilder]: ...
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
        ) -> readers.YearToValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.YearToValueReader: ...

    YearToValue: _YearToValueStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _EnvironmentParametersSchema(_StructSchema):
        class _AtmosphericCO2sField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(
                    self,
                ) -> schemas._EnvironmentParametersYearToValueSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _EnvironmentParametersStructModule._EnvironmentParametersSchema._AtmosphericCO2sField._Schema: ...

        class _AtmosphericO3sField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(
                    self,
                ) -> schemas._EnvironmentParametersYearToValueSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _EnvironmentParametersStructModule._EnvironmentParametersSchema._AtmosphericO3sField._Schema: ...

        class _RcpField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _EnumSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["albedo"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["atmosphericCO2"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["atmosphericCO2s"],
            ) -> _EnvironmentParametersStructModule._EnvironmentParametersSchema._AtmosphericCO2sField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["atmosphericO3"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["atmosphericO3s"],
            ) -> _EnvironmentParametersStructModule._EnvironmentParametersSchema._AtmosphericO3sField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["windSpeedHeight"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["leachingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["timeStep"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maxGroundwaterDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["minGroundwaterDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["minGroundwaterDepthMonth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rcp"],
            ) -> _EnvironmentParametersStructModule._EnvironmentParametersSchema._RcpField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> (
            _EnvironmentParametersStructModule._EnvironmentParametersSchema._Fields
        ): ...

    @property
    @override
    def schema(self) -> schemas._EnvironmentParametersSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        albedo: float | None = None,
        atmosphericCO2: float | None = None,
        atmosphericCO2s: builders.YearToValueListBuilder | dict[str, Any] | None = None,
        atmosphericO3: float | None = None,
        atmosphericO3s: builders.YearToValueListBuilder | dict[str, Any] | None = None,
        windSpeedHeight: float | None = None,
        leachingDepth: float | None = None,
        timeStep: float | None = None,
        maxGroundwaterDepth: float | None = None,
        minGroundwaterDepth: float | None = None,
        minGroundwaterDepthMonth: int | None = None,
        rcp: RCPEnum | None = None,
        **kwargs: object,
    ) -> builders.EnvironmentParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.EnvironmentParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.EnvironmentParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.EnvironmentParametersBuilder]: ...
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
    ) -> readers.EnvironmentParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.EnvironmentParametersReader: ...

class _MeasuredGroundwaterTableInformationStructModule(_StructModule):
    class _DateToValueStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _DateToValueSchema(_StructSchema):
            class _DateField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _StructSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["date"],
                ) -> _MeasuredGroundwaterTableInformationStructModule._DateToValueStructModule._DateToValueSchema._DateField: ...
                @overload
                def __getitem__(self, key: Literal["value"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _MeasuredGroundwaterTableInformationStructModule._DateToValueStructModule._DateToValueSchema._Fields: ...

        @property
        @override
        def schema(
            self,
        ) -> schemas._MeasuredGroundwaterTableInformationDateToValueSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            date: DateBuilder | dict[str, Any] | None = None,
            value: float | None = None,
            **kwargs: object,
        ) -> builders.DateToValueBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.DateToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.DateToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.DateToValueBuilder]: ...
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
        ) -> readers.DateToValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.DateToValueReader: ...

    DateToValue: _DateToValueStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _MeasuredGroundwaterTableInformationSchema(_StructSchema):
        class _GroundwaterInfoField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(
                    self,
                ) -> schemas._MeasuredGroundwaterTableInformationDateToValueSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _MeasuredGroundwaterTableInformationStructModule._MeasuredGroundwaterTableInformationSchema._GroundwaterInfoField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["groundwaterInformationAvailable"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["groundwaterInfo"],
            ) -> _MeasuredGroundwaterTableInformationStructModule._MeasuredGroundwaterTableInformationSchema._GroundwaterInfoField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _MeasuredGroundwaterTableInformationStructModule._MeasuredGroundwaterTableInformationSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._MeasuredGroundwaterTableInformationSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        groundwaterInformationAvailable: bool | None = None,
        groundwaterInfo: builders.DateToValueListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.MeasuredGroundwaterTableInformationBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.MeasuredGroundwaterTableInformationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.MeasuredGroundwaterTableInformationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[
        builders.MeasuredGroundwaterTableInformationBuilder
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
    ) -> readers.MeasuredGroundwaterTableInformationReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.MeasuredGroundwaterTableInformationReader: ...

class _SimulationParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SimulationParametersSchema(_StructSchema):
        class _StartDateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _StructSchema: ...

        class _EndDateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _StructSchema: ...

        class _AutoIrrigationParamsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._AutomaticIrrigationParametersSchema: ...

        class _NMinFertiliserPartitionField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _StructSchema: ...

        class _NMinApplicationParamsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._NMinApplicationParametersSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["startDate"],
            ) -> _SimulationParametersStructModule._SimulationParametersSchema._StartDateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["endDate"],
            ) -> _SimulationParametersStructModule._SimulationParametersSchema._EndDateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nitrogenResponseOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["waterDeficitResponseOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["emergenceFloodingControlOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["emergenceMoistureControlOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["frostKillOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["useAutomaticIrrigation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["autoIrrigationParams"],
            ) -> _SimulationParametersStructModule._SimulationParametersSchema._AutoIrrigationParamsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["useNMinMineralFertilisingMethod"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nMinFertiliserPartition"],
            ) -> _SimulationParametersStructModule._SimulationParametersSchema._NMinFertiliserPartitionField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nMinApplicationParams"],
            ) -> _SimulationParametersStructModule._SimulationParametersSchema._NMinApplicationParamsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["useSecondaryYields"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["useAutomaticHarvestTrigger"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["numberOfLayers"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["layerThickness"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["startPVIndex"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["julianDayAutomaticFertilising"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SimulationParametersStructModule._SimulationParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SimulationParametersSchema: ...
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
        autoIrrigationParams: builders.AutomaticIrrigationParametersBuilder
        | dict[str, Any]
        | None = None,
        useNMinMineralFertilisingMethod: bool | None = None,
        nMinFertiliserPartition: _ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule.Builder
        | dict[str, Any]
        | None = None,
        nMinApplicationParams: builders.NMinApplicationParametersBuilder
        | dict[str, Any]
        | None = None,
        useSecondaryYields: bool | None = None,
        useAutomaticHarvestTrigger: bool | None = None,
        numberOfLayers: int | None = None,
        layerThickness: float | None = None,
        startPVIndex: int | None = None,
        julianDayAutomaticFertilising: int | None = None,
        **kwargs: object,
    ) -> builders.SimulationParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SimulationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SimulationParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SimulationParametersBuilder]: ...
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
    ) -> readers.SimulationParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SimulationParametersReader: ...

class _CropModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _CropModuleParametersSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["canopyReflectionCoefficient"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["referenceMaxAssimilationRate"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["referenceLeafAreaIndex"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maintenanceRespirationParameter1"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maintenanceRespirationParameter2"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["minimumNConcentrationRoot"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["minimumAvailableN"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["referenceAlbedo"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stomataConductanceAlpha"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["saturationBeta"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["growthRespirationRedux"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maxCropNDemand"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["growthRespirationParameter1"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["growthRespirationParameter2"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["tortuosity"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["adjustRootDepthForSoilProps"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentalEnablePhenologyWangEngelTemperatureResponse"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal[
                    "experimentalEnablePhotosynthesisWangEngelTemperatureResponse"
                ],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentalEnableHourlyFvCBPhotosynthesis"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentalEnableTResponseLeafExpansion"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentalDisableDailyRootBiomassToSoil"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["enableVernalisationFactorFix"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _CropModuleParametersStructModule._CropModuleParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._CropModuleParametersSchema: ...
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
    ) -> builders.CropModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.CropModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.CropModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.CropModuleParametersBuilder]: ...
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
    ) -> readers.CropModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CropModuleParametersReader: ...

class _SoilMoistureModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilMoistureModuleParametersSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["criticalMoistureDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["saturatedHydraulicConductivity"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["surfaceRoughness"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["groundwaterDischarge"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["hydraulicConductivityRedux"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["snowAccumulationTresholdTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["kcFactor"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["temperatureLimitForLiquidWater"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["correctionSnow"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["correctionRain"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["snowMaxAdditionalDensity"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["newSnowDensityMin"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["snowRetentionCapacityMin"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["refreezeParameter1"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["refreezeParameter2"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["refreezeTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["snowMeltTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["snowPacking"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["snowRetentionCapacityMax"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["evaporationZeta"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["xsaCriticalSoilMoisture"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maximumEvaporationImpactDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maxPercolationRate"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["moistureInitValue"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SoilMoistureModuleParametersStructModule._SoilMoistureModuleParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SoilMoistureModuleParametersSchema: ...
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
    ) -> builders.SoilMoistureModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilMoistureModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SoilMoistureModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilMoistureModuleParametersBuilder]: ...
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
    ) -> readers.SoilMoistureModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilMoistureModuleParametersReader: ...

class _SticsParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SticsParametersSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["useN2O"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["useNit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["useDenit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["codeVnit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["codeTnit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["codeRationit"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["codeHourlyWfpsNit"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["codePdenit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["codeRatiodenit"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["codeHourlyWfpsDenit"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["hminn"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["hoptn"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["pHminnit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["pHmaxnit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["nh4Min"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["pHminden"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["pHmaxden"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["wfpsc"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["tdenitoptGauss"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["scaleTdenitopt"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["kd"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["kDesat"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["fnx"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["vnitmax"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["kamm"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["tnitmin"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["tnitopt"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["tnitop2"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["tnitmax"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["tnitoptGauss"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["scaleTnitopt"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["rationit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["cminPdenit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["cmaxPdenit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["minPdenit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["maxPdenit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["ratiodenit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["profdenit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["vpotdenit"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SticsParametersStructModule._SticsParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SticsParametersSchema: ...
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
    ) -> builders.SticsParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SticsParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SticsParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SticsParametersBuilder]: ...
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
    ) -> readers.SticsParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SticsParametersReader: ...

class _SoilOrganicModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilOrganicModuleParametersSchema(_StructSchema):
        class _SticsParamsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._SticsParametersSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["somSlowDecCoeffStandard"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["somFastDecCoeffStandard"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["smbSlowMaintRateStandard"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["smbFastMaintRateStandard"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["smbSlowDeathRateStandard"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["smbFastDeathRateStandard"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["smbUtilizationEfficiency"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["somSlowUtilizationEfficiency"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["somFastUtilizationEfficiency"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomSlowUtilizationEfficiency"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomFastUtilizationEfficiency"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomFastMaxCtoN"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["partSOMFastToSOMSlow"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["partSMBSlowToSOMFast"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["partSMBFastToSOMFast"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["partSOMToSMBSlow"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["partSOMToSMBFast"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["cnRatioSMB"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["limitClayEffect"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["ammoniaOxidationRateCoeffStandard"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nitriteOxidationRateCoeffStandard"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["transportRateCoeff"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["specAnaerobDenitrification"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["immobilisationRateCoeffNO3"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["immobilisationRateCoeffNH4"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["denit1"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["denit2"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["denit3"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["hydrolysisKM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["activationEnergy"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["hydrolysisP1"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["hydrolysisP2"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["atmosphericResistance"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["n2oProductionRate"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["inhibitorNH3"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["psMaxMineralisationDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sticsParams"],
            ) -> _SoilOrganicModuleParametersStructModule._SoilOrganicModuleParametersSchema._SticsParamsField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SoilOrganicModuleParametersStructModule._SoilOrganicModuleParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SoilOrganicModuleParametersSchema: ...
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
        sticsParams: builders.SticsParametersBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.SoilOrganicModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilOrganicModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SoilOrganicModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilOrganicModuleParametersBuilder]: ...
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
    ) -> readers.SoilOrganicModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilOrganicModuleParametersReader: ...

class _SoilTemperatureModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilTemperatureModuleParametersSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["nTau"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["initialSurfaceTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["baseTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["quartzRawDensity"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["densityAir"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["densityWater"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["densityHumus"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["specificHeatCapacityAir"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["specificHeatCapacityQuartz"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["specificHeatCapacityWater"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["specificHeatCapacityHumus"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["soilAlbedo"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilMoisture"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SoilTemperatureModuleParametersStructModule._SoilTemperatureModuleParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SoilTemperatureModuleParametersSchema: ...
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
    ) -> builders.SoilTemperatureModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilTemperatureModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SoilTemperatureModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilTemperatureModuleParametersBuilder]: ...
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
    ) -> readers.SoilTemperatureModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilTemperatureModuleParametersReader: ...

class _SoilTransportModuleParametersStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilTransportModuleParametersSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["dispersionLength"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["ad"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["diffusionCoefficientStandard"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nDeposition"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SoilTransportModuleParametersStructModule._SoilTransportModuleParametersSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SoilTransportModuleParametersSchema: ...
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
    ) -> builders.SoilTransportModuleParametersBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilTransportModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SoilTransportModuleParametersReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilTransportModuleParametersBuilder]: ...
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
    ) -> readers.SoilTransportModuleParametersReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilTransportModuleParametersReader: ...

class _VocStructModule(_StructModule):
    class _EmissionsStructModule(_StructModule):
        class _SpeciesIdToEmissionStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            class _SpeciesIdToEmissionSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["speciesId"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["emission"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _VocStructModule._EmissionsStructModule._SpeciesIdToEmissionStructModule._SpeciesIdToEmissionSchema._Fields: ...

            @property
            @override
            def schema(self) -> schemas._VocEmissionsSpeciesIdToEmissionSchema: ...
            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                speciesId: int | None = None,
                emission: float | None = None,
                **kwargs: object,
            ) -> builders.SpeciesIdToEmissionBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[readers.SpeciesIdToEmissionReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[readers.SpeciesIdToEmissionReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[builders.SpeciesIdToEmissionBuilder]: ...
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
            ) -> readers.SpeciesIdToEmissionReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.SpeciesIdToEmissionReader: ...

        SpeciesIdToEmission: _SpeciesIdToEmissionStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _EmissionsSchema(_StructSchema):
            class _SpeciesIdToIsopreneEmissionField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(
                        self,
                    ) -> schemas._VocEmissionsSpeciesIdToEmissionSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _VocStructModule._EmissionsStructModule._EmissionsSchema._SpeciesIdToIsopreneEmissionField._Schema: ...

            class _SpeciesIdToMonoterpeneEmissionField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(
                        self,
                    ) -> schemas._VocEmissionsSpeciesIdToEmissionSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _VocStructModule._EmissionsStructModule._EmissionsSchema._SpeciesIdToMonoterpeneEmissionField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["speciesIdToIsopreneEmission"],
                ) -> _VocStructModule._EmissionsStructModule._EmissionsSchema._SpeciesIdToIsopreneEmissionField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["speciesIdToMonoterpeneEmission"],
                ) -> _VocStructModule._EmissionsStructModule._EmissionsSchema._SpeciesIdToMonoterpeneEmissionField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["isopreneEmission"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["monoterpeneEmission"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _VocStructModule._EmissionsStructModule._EmissionsSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._VocEmissionsSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            speciesIdToIsopreneEmission: builders.SpeciesIdToEmissionListBuilder
            | dict[str, Any]
            | None = None,
            speciesIdToMonoterpeneEmission: builders.SpeciesIdToEmissionListBuilder
            | dict[str, Any]
            | None = None,
            isopreneEmission: float | None = None,
            monoterpeneEmission: float | None = None,
            **kwargs: object,
        ) -> builders.EmissionsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.EmissionsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.EmissionsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.EmissionsBuilder]: ...
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
        ) -> readers.EmissionsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EmissionsReader: ...

    Emissions: _EmissionsStructModule
    class _SpeciesDataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _SpeciesDataSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["efMonos"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["efMono"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["efIso"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["theta"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["fage"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["ctIs"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["ctMt"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["haIs"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["haMt"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["dsIs"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["dsMt"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["hdIs"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["hdMt"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["hdj"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["sdj"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["kc25"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["ko25"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["vcMax25"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["qjvc"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["aekc"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["aeko"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["aejm"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["aevc"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["slaMin"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["scaleI"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["scaleM"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["mFol"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["lai"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["sla"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> (
                _VocStructModule._SpeciesDataStructModule._SpeciesDataSchema._Fields
            ): ...

        @property
        @override
        def schema(self) -> schemas._VocSpeciesDataSchema: ...
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
        ) -> builders.SpeciesDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.SpeciesDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.SpeciesDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.SpeciesDataBuilder]: ...
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
        ) -> readers.SpeciesDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SpeciesDataReader: ...

    SpeciesData: _SpeciesDataStructModule
    class _CPDataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _CPDataSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["kc"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["ko"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["oi"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["ci"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["comp"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["vcMax"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["jMax"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["jj"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["jj1000"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["jv"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _VocStructModule._CPDataStructModule._CPDataSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._VocCPDataSchema: ...
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
        ) -> builders.CPDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.CPDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.CPDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.CPDataBuilder]: ...
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
        ) -> readers.CPDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CPDataReader: ...

    CPData: _CPDataStructModule
    class _MicroClimateDataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _MicroClimateDataSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["rad"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["rad24"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["rad240"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["tFol"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["tFol24"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["tFol240"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["sunlitfoliagefraction"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["sunlitfoliagefraction24"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["co2concentration"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _VocStructModule._MicroClimateDataStructModule._MicroClimateDataSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._VocMicroClimateDataSchema: ...
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
        ) -> builders.MicroClimateDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.MicroClimateDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.MicroClimateDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.MicroClimateDataBuilder]: ...
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
        ) -> readers.MicroClimateDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.MicroClimateDataReader: ...

    MicroClimateData: _MicroClimateDataStructModule
    class _PhotosynthTStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _PhotosynthTSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["par"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["par24"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["par240"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> (
                _VocStructModule._PhotosynthTStructModule._PhotosynthTSchema._Fields
            ): ...

        @property
        @override
        def schema(self) -> schemas._VocPhotosynthTSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            par: float | None = None,
            par24: float | None = None,
            par240: float | None = None,
            **kwargs: object,
        ) -> builders.PhotosynthTBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.PhotosynthTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.PhotosynthTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.PhotosynthTBuilder]: ...
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
        ) -> readers.PhotosynthTReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.PhotosynthTReader: ...

    PhotosynthT: _PhotosynthTStructModule
    class _FoliageTStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _FoliageTSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["tempK"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["tempK24"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["tempK240"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _VocStructModule._FoliageTStructModule._FoliageTSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._VocFoliageTSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            tempK: float | None = None,
            tempK24: float | None = None,
            tempK240: float | None = None,
            **kwargs: object,
        ) -> builders.FoliageTBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.FoliageTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.FoliageTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.FoliageTBuilder]: ...
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
        ) -> readers.FoliageTReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.FoliageTReader: ...

    FoliageT: _FoliageTStructModule
    class _EnzymeActivityTStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _EnzymeActivityTSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["efIso"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["efMono"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _VocStructModule._EnzymeActivityTStructModule._EnzymeActivityTSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._VocEnzymeActivityTSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            efIso: float | None = None,
            efMono: float | None = None,
            **kwargs: object,
        ) -> builders.EnzymeActivityTBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.EnzymeActivityTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.EnzymeActivityTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.EnzymeActivityTBuilder]: ...
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
        ) -> readers.EnzymeActivityTReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EnzymeActivityTReader: ...

    EnzymeActivityT: _EnzymeActivityTStructModule
    class _LeafEmissionTStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _LeafEmissionTSchema(_StructSchema):
            class _PhoField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._VocPhotosynthTSchema: ...

            class _FolField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._VocFoliageTSchema: ...

            class _EnzActField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._VocEnzymeActivityTSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["foliageLayer"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["pho"],
                ) -> _VocStructModule._LeafEmissionTStructModule._LeafEmissionTSchema._PhoField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["fol"],
                ) -> _VocStructModule._LeafEmissionTStructModule._LeafEmissionTSchema._FolField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["enzAct"],
                ) -> _VocStructModule._LeafEmissionTStructModule._LeafEmissionTSchema._EnzActField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> (
                _VocStructModule._LeafEmissionTStructModule._LeafEmissionTSchema._Fields
            ): ...

        @property
        @override
        def schema(self) -> schemas._VocLeafEmissionTSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            foliageLayer: int | None = None,
            pho: builders.PhotosynthTBuilder | dict[str, Any] | None = None,
            fol: builders.FoliageTBuilder | dict[str, Any] | None = None,
            enzAct: builders.EnzymeActivityTBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> builders.LeafEmissionTBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.LeafEmissionTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.LeafEmissionTReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.LeafEmissionTBuilder]: ...
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
        ) -> readers.LeafEmissionTReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.LeafEmissionTReader: ...

    LeafEmissionT: _LeafEmissionTStructModule
    class _LeafEmissionsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _LeafEmissionsSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["isoprene"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["monoterp"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> (
                _VocStructModule._LeafEmissionsStructModule._LeafEmissionsSchema._Fields
            ): ...

        @property
        @override
        def schema(self) -> schemas._VocLeafEmissionsSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            isoprene: float | None = None,
            monoterp: float | None = None,
            **kwargs: object,
        ) -> builders.LeafEmissionsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.LeafEmissionsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.LeafEmissionsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.LeafEmissionsBuilder]: ...
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
        ) -> readers.LeafEmissionsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.LeafEmissionsReader: ...

    LeafEmissions: _LeafEmissionsStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _VocSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]): ...

        @property
        @override
        def fields(self) -> _VocStructModule._VocSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._VocSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        **kwargs: object,
    ) -> builders.VocBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.VocReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.VocReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.VocBuilder]: ...
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
    ) -> readers.VocReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.VocReader: ...
