"""Module helper types for `monica_state.capnp`."""

from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _ListSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.common.date_capnp.types import (
    schemas as _mas_schema_common_date_capnp_schemas,
)
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.model.monica.monica_management_capnp.types import (
    schemas as _mas_schema_model_monica_monica_management_capnp_schemas,
)
from mas.schema.model.monica.monica_management_capnp.types.modules import (
    _ParamsStructModule,
)
from mas.schema.model.monica.monica_params_capnp.types import (
    schemas as _mas_schema_model_monica_monica_params_capnp_schemas,
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
from mas.schema.model.monica.monica_state_capnp.types import builders as builders
from mas.schema.model.monica.monica_state_capnp.types import readers as readers
from mas.schema.model.monica.monica_state_capnp.types import schemas as schemas

class _MaybeBoolStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _MaybeBoolSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["value"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _MaybeBoolStructModule._MaybeBoolSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._MaybeBoolSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        value: bool | None = None,
        **kwargs: object,
    ) -> builders.MaybeBoolBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.MaybeBoolReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.MaybeBoolReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.MaybeBoolBuilder]: ...
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
    ) -> readers.MaybeBoolReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.MaybeBoolReader: ...

class _CropModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _CropModuleStateSchema(_StructSchema):
        class _PcAbovegroundOrganField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcAssimilatePartitioningCoeffField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> _ListSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcAssimilatePartitioningCoeffField._Schema: ...

        class _PcBaseDaylengthField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcBaseTemperatureField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcCriticalOxygenContentField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _CropWaterUptakeField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _CurrentTemperatureSumField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcDaylengthRequirementField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcDroughtStressThresholdField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcInitialOrganBiomassField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SunlitLeafAreaIndexField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _ShadedLeafAreaIndexField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _NUptakeFromLayerField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcOptimumTemperatureField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _OrganBiomassField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _OrganDeadBiomassField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _OrganGreenBiomassField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _OrganGrowthIncrementField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcOrganGrowthRespirationField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcOrganIdsForPrimaryYieldField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(
                    self,
                ) -> _mas_schema_model_monica_monica_params_capnp_schemas._YieldComponentSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcOrganIdsForPrimaryYieldField._Schema: ...

        class _PcOrganIdsForSecondaryYieldField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(
                    self,
                ) -> _mas_schema_model_monica_monica_params_capnp_schemas._YieldComponentSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcOrganIdsForSecondaryYieldField._Schema: ...

        class _PcOrganIdsForCuttingField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(
                    self,
                ) -> _mas_schema_model_monica_monica_params_capnp_schemas._YieldComponentSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcOrganIdsForCuttingField._Schema: ...

        class _PcOrganMaintenanceRespirationField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _OrganSenescenceIncrementField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcOrganSenescenceRateField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> _ListSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcOrganSenescenceRateField._Schema: ...

        class _RootDensityField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _RootDiameterField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _RootEffectivityField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _VsSoilMineralNContentField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcSpecificLeafAreaField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcStageMaxRootNConcentrationField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcStageKcFactorField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcStageTemperatureSumField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcStorageOrganField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _TranspirationField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _TranspirationReduxField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PcVernalisationRequirementField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Rad24Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Rad240Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Tfol24Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Tfol240Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _GuentherEmissionsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> (
                _mas_schema_model_monica_monica_params_capnp_schemas._VocEmissionsSchema
            ): ...

        class _JjvEmissionsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> (
                _mas_schema_model_monica_monica_params_capnp_schemas._VocEmissionsSchema
            ): ...

        class _VocSpeciesField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._VocSpeciesDataSchema: ...

        class _CropPhotosynthesisResultsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> (
                _mas_schema_model_monica_monica_params_capnp_schemas._VocCPDataSchema
            ): ...

        class _SpeciesParamsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._SpeciesParametersSchema: ...

        class _CultivarParamsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._CultivarParametersSchema: ...

        class _ResidueParamsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._CropResidueParametersSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["frostKillOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["ktko"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["ktkc"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["assimilatePartCoeffsReduced"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["o3WStomatalClosure"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["o3SumUptake"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["vsLatitude"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["abovegroundBiomass"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["abovegroundBiomassOld"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcAbovegroundOrgan"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcAbovegroundOrganField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["actualTranspiration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcAssimilatePartitioningCoeff"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcAssimilatePartitioningCoeffField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcAssimilateReallocation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["assimilates"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["assimilationRate"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["astronomicDayLenght"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcBaseDaylength"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcBaseDaylengthField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcBaseTemperature"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcBaseTemperatureField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcBeginSensitivePhaseHeatStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["belowgroundBiomass"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["belowgroundBiomassOld"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcCarboxylationPathway"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["clearDayRadiation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcCo2Method"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["criticalNConcentration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcCriticalOxygenContent"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcCriticalOxygenContentField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcCriticalTemperatureHeatStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropDiameter"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropFrostRedux"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropHeatRedux"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["cropHeight"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcCropHeightP1"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcCropHeightP2"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["pcCropName"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropNDemand"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["cropNRedux"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcCropSpecificMaxRootingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropWaterUptake"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._CropWaterUptakeField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["currentTemperatureSum"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._CurrentTemperatureSumField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["currentTotalTemperatureSum"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["currentTotalTemperatureSumRoot"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcCuttingDelayDays"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["daylengthFactor"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcDaylengthRequirement"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcDaylengthRequirementField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["daysAfterBeginFlowering"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["declination"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcDefaultRadiationUseEfficiency"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vmDepthGroundwaterTable"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcDevelopmentAccelerationByNitrogenStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["developmentalStage"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["noOfCropSteps"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["droughtImpactOnFertility"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcDroughtImpactOnFertilityFactor"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcDroughtStressThreshold"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcDroughtStressThresholdField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcEmergenceFloodingControlOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcEmergenceMoistureControlOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcEndSensitivePhaseHeatStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["effectiveDayLength"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["errorStatus"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["errorMessage"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["evaporatedFromIntercept"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["extraterrestrialRadiation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcFieldConditionModifier"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["finalDevelopmentalStage"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["fixedN"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcFrostDehardening"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcFrostHardening"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["globalRadiation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["greenAreaIndex"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["grossAssimilates"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["grossPhotosynthesis"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["grossPhotosynthesisMol"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["grossPhotosynthesisReferenceMol"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["grossPrimaryProduction"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["growthCycleEnded"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["growthRespirationAS"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcHeatSumIrrigationStart"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcHeatSumIrrigationEnd"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["vsHeightNN"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcInitialKcFactor"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcInitialOrganBiomass"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcInitialOrganBiomassField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcInitialRootingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["interceptionStorage"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["kcFactor"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["leafAreaIndex"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sunlitLeafAreaIndex"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._SunlitLeafAreaIndexField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["shadedLeafAreaIndex"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._ShadedLeafAreaIndexField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcLowTemperatureExposure"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcLimitingTemperatureHeatStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["lt50"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcLt50cultivar"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcLuxuryNCoeff"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maintenanceRespirationAS"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcMaxAssimilationRate"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcMaxCropDiameter"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcMaxCropHeight"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["maxNUptake"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcMaxNUptakeParam"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcMaxRootingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcMinimumNConcentration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcMinimumTemperatureForAssimilation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcOptimumTemperatureForAssimilation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcMaximumTemperatureForAssimilation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcMinimumTemperatureRootGrowth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["netMaintenanceRespiration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["netPhotosynthesis"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["netPrecipitation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["netPrimaryProduction"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcNConcentrationAbovegroundBiomass"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nConcentrationAbovegroundBiomass"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nConcentrationAbovegroundBiomassOld"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcNConcentrationB0"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nContentDeficit"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcNConcentrationPN"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcNConcentrationRoot"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nConcentrationRoot"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nConcentrationRootOld"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcNitrogenResponseOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcNumberOfDevelopmentalStages"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcNumberOfOrgans"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nUptakeFromLayer"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._NUptakeFromLayerField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcOptimumTemperature"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcOptimumTemperatureField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["organBiomass"],
            ) -> (
                _CropModuleStateStructModule._CropModuleStateSchema._OrganBiomassField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["organDeadBiomass"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._OrganDeadBiomassField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["organGreenBiomass"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._OrganGreenBiomassField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["organGrowthIncrement"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._OrganGrowthIncrementField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcOrganGrowthRespiration"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcOrganGrowthRespirationField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcOrganIdsForPrimaryYield"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcOrganIdsForPrimaryYieldField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcOrganIdsForSecondaryYield"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcOrganIdsForSecondaryYieldField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcOrganIdsForCutting"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcOrganIdsForCuttingField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcOrganMaintenanceRespiration"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcOrganMaintenanceRespirationField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["organSenescenceIncrement"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._OrganSenescenceIncrementField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcOrganSenescenceRate"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcOrganSenescenceRateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["overcastDayRadiation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["oxygenDeficit"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcPartBiologicalNFixation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcPerennial"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["photoperiodicDaylength"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["photActRadiationMean"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcPlantDensity"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["potentialTranspiration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["referenceEvapotranspiration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["relativeTotalDevelopment"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["remainingEvapotranspiration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["reserveAssimilatePool"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcResidueNRatio"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcRespiratoryStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rootBiomass"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rootBiomassOld"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rootDensity"],
            ) -> (
                _CropModuleStateStructModule._CropModuleStateSchema._RootDensityField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["rootDiameter"],
            ) -> (
                _CropModuleStateStructModule._CropModuleStateSchema._RootDiameterField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcRootDistributionParam"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rootEffectivity"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._RootEffectivityField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcRootFormFactor"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcRootGrowthLag"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rootingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rootingDepthM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rootingZone"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcRootPenetrationRate"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vmSaturationDeficit"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilCoverage"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsSoilMineralNContent"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._VsSoilMineralNContentField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilSpecificMaxRootingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsSoilSpecificMaxRootingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcSpecificLeafArea"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcSpecificLeafAreaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcSpecificRootLength"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcStageAfterCut"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcStageAtMaxDiameter"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcStageAtMaxHeight"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcStageMaxRootNConcentration"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcStageMaxRootNConcentrationField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcStageKcFactor"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcStageKcFactorField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcStageTemperatureSum"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcStageTemperatureSumField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stomataResistance"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcStorageOrgan"],
            ) -> (
                _CropModuleStateStructModule._CropModuleStateSchema._PcStorageOrganField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["storageOrgan"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["targetNConcentration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["timeStep"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["timeUnderAnoxia"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsTortuosity"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["totalBiomass"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["totalBiomassNContent"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["totalCropHeatImpact"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["totalNInput"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["totalNUptake"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["totalRespired"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["respiration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sumTotalNUptake"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["totalRootLength"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["totalTemperatureSum"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["temperatureSumToFlowering"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["transpiration"],
            ) -> (
                _CropModuleStateStructModule._CropModuleStateSchema._TranspirationField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["transpirationRedux"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._TranspirationReduxField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["transpirationDeficit"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vernalisationDays"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vernalisationFactor"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcVernalisationRequirement"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._PcVernalisationRequirementField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pcWaterDeficitResponseOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["o3Senescence"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["o3LongTermDamage"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["o3ShortTermDamage"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["dyingOut"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["accumulatedETa"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["accumulatedTranspiration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["accumulatedPrimaryCropYield"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sumExportedCutBiomass"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["exportedCutBiomass"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sumResidueCutBiomass"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["residueCutBiomass"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cuttingDelayDays"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsMaxEffectiveRootingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsImpenetrableLayerDept"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["anthesisDay"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maturityDay"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maturityReached"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["stepSize24"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stepSize240"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rad24"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._Rad24Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rad240"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._Rad240Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["tfol24"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._Tfol24Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["tfol240"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._Tfol240Field: ...
            @overload
            def __getitem__(self, key: Literal["index24"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["index240"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["full24"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["full240"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["guentherEmissions"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._GuentherEmissionsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["jjvEmissions"],
            ) -> (
                _CropModuleStateStructModule._CropModuleStateSchema._JjvEmissionsField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["vocSpecies"],
            ) -> (
                _CropModuleStateStructModule._CropModuleStateSchema._VocSpeciesField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropPhotosynthesisResults"],
            ) -> _CropModuleStateStructModule._CropModuleStateSchema._CropPhotosynthesisResultsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["speciesParams"],
            ) -> (
                _CropModuleStateStructModule._CropModuleStateSchema._SpeciesParamsField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["cultivarParams"],
            ) -> (
                _CropModuleStateStructModule._CropModuleStateSchema._CultivarParamsField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["residueParams"],
            ) -> (
                _CropModuleStateStructModule._CropModuleStateSchema._ResidueParamsField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["isWinterCrop"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stemElongationEventFired"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["lt50m"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _CropModuleStateStructModule._CropModuleStateSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._CropModuleStateSchema: ...
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
        pcAbovegroundOrgan: builders.BoolListBuilder | dict[str, Any] | None = None,
        actualTranspiration: float | None = None,
        pcAssimilatePartitioningCoeff: builders.Float64ListListBuilder
        | dict[str, Any]
        | None = None,
        pcAssimilateReallocation: float | None = None,
        assimilates: float | None = None,
        assimilationRate: float | None = None,
        astronomicDayLenght: float | None = None,
        pcBaseDaylength: builders.Float64ListBuilder | dict[str, Any] | None = None,
        pcBaseTemperature: builders.Float64ListBuilder | dict[str, Any] | None = None,
        pcBeginSensitivePhaseHeatStress: float | None = None,
        belowgroundBiomass: float | None = None,
        belowgroundBiomassOld: float | None = None,
        pcCarboxylationPathway: int | None = None,
        clearDayRadiation: float | None = None,
        pcCo2Method: int | None = None,
        criticalNConcentration: float | None = None,
        pcCriticalOxygenContent: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
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
        cropWaterUptake: builders.Float64ListBuilder | dict[str, Any] | None = None,
        currentTemperatureSum: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        currentTotalTemperatureSum: float | None = None,
        currentTotalTemperatureSumRoot: float | None = None,
        pcCuttingDelayDays: int | None = None,
        daylengthFactor: float | None = None,
        pcDaylengthRequirement: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        daysAfterBeginFlowering: int | None = None,
        declination: float | None = None,
        pcDefaultRadiationUseEfficiency: float | None = None,
        vmDepthGroundwaterTable: int | None = None,
        pcDevelopmentAccelerationByNitrogenStress: int | None = None,
        developmentalStage: int | None = None,
        noOfCropSteps: int | None = None,
        droughtImpactOnFertility: float | None = None,
        pcDroughtImpactOnFertilityFactor: float | None = None,
        pcDroughtStressThreshold: builders.Float64ListBuilder
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
        pcInitialOrganBiomass: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        pcInitialRootingDepth: float | None = None,
        interceptionStorage: float | None = None,
        kcFactor: float | None = None,
        leafAreaIndex: float | None = None,
        sunlitLeafAreaIndex: builders.Float64ListBuilder | dict[str, Any] | None = None,
        shadedLeafAreaIndex: builders.Float64ListBuilder | dict[str, Any] | None = None,
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
        nUptakeFromLayer: builders.Float64ListBuilder | dict[str, Any] | None = None,
        pcOptimumTemperature: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        organBiomass: builders.Float64ListBuilder | dict[str, Any] | None = None,
        organDeadBiomass: builders.Float64ListBuilder | dict[str, Any] | None = None,
        organGreenBiomass: builders.Float64ListBuilder | dict[str, Any] | None = None,
        organGrowthIncrement: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        pcOrganGrowthRespiration: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        pcOrganIdsForPrimaryYield: builders.YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        pcOrganIdsForSecondaryYield: builders.YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        pcOrganIdsForCutting: builders.YieldComponentListBuilder
        | dict[str, Any]
        | None = None,
        pcOrganMaintenanceRespiration: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        organSenescenceIncrement: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        pcOrganSenescenceRate: builders.Float64ListListBuilder
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
        rootDensity: builders.Float64ListBuilder | dict[str, Any] | None = None,
        rootDiameter: builders.Float64ListBuilder | dict[str, Any] | None = None,
        pcRootDistributionParam: float | None = None,
        rootEffectivity: builders.Float64ListBuilder | dict[str, Any] | None = None,
        pcRootFormFactor: float | None = None,
        pcRootGrowthLag: float | None = None,
        rootingDepth: int | None = None,
        rootingDepthM: float | None = None,
        rootingZone: int | None = None,
        pcRootPenetrationRate: float | None = None,
        vmSaturationDeficit: float | None = None,
        soilCoverage: float | None = None,
        vsSoilMineralNContent: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        soilSpecificMaxRootingDepth: float | None = None,
        vsSoilSpecificMaxRootingDepth: float | None = None,
        pcSpecificLeafArea: builders.Float64ListBuilder | dict[str, Any] | None = None,
        pcSpecificRootLength: float | None = None,
        pcStageAfterCut: int | None = None,
        pcStageAtMaxDiameter: float | None = None,
        pcStageAtMaxHeight: float | None = None,
        pcStageMaxRootNConcentration: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        pcStageKcFactor: builders.Float64ListBuilder | dict[str, Any] | None = None,
        pcStageTemperatureSum: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        stomataResistance: float | None = None,
        pcStorageOrgan: builders.BoolListBuilder | dict[str, Any] | None = None,
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
        transpiration: builders.Float64ListBuilder | dict[str, Any] | None = None,
        transpirationRedux: builders.Float64ListBuilder | dict[str, Any] | None = None,
        transpirationDeficit: float | None = None,
        vernalisationDays: float | None = None,
        vernalisationFactor: float | None = None,
        pcVernalisationRequirement: builders.Float64ListBuilder
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
        rad24: builders.Float64ListBuilder | dict[str, Any] | None = None,
        rad240: builders.Float64ListBuilder | dict[str, Any] | None = None,
        tfol24: builders.Float64ListBuilder | dict[str, Any] | None = None,
        tfol240: builders.Float64ListBuilder | dict[str, Any] | None = None,
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
    ) -> builders.CropModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.CropModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.CropModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.CropModuleStateBuilder]: ...
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
    ) -> readers.CropModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CropModuleStateReader: ...

class _AOMPropertiesStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _AOMPropertiesSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["aomSlow"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["aomFast"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomSlowDecRatetoSMBSlow"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomSlowDecRatetoSMBFast"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomFastDecRatetoSMBSlow"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomFastDecRatetoSMBFast"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomSlowDecCoeff"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomFastDecCoeff"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomSlowDecCoeffStandard"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomFastDecCoeffStandard"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["partAOMSlowtoSMBSlow"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["partAOMSlowtoSMBFast"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cnRatioAOMSlow"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cnRatioAOMFast"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["daysAfterApplication"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomDryMatterContent"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomNH4Content"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomSlowDelta"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomFastDelta"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["incorporation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["noVolatilization"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _AOMPropertiesStructModule._AOMPropertiesSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._AOMPropertiesSchema: ...
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
    ) -> builders.AOMPropertiesBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.AOMPropertiesReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.AOMPropertiesReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.AOMPropertiesBuilder]: ...
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
    ) -> readers.AOMPropertiesReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.AOMPropertiesReader: ...

class _SoilLayerStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilLayerStateSchema(_StructSchema):
        class _VoAOMPoolField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._AOMPropertiesSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _SoilLayerStateStructModule._SoilLayerStateSchema._VoAOMPoolField._Schema: ...

        class _SpsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._SoilParametersSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["layerThickness"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilWaterFlux"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["voAOMPool"],
            ) -> _SoilLayerStateStructModule._SoilLayerStateSchema._VoAOMPoolField: ...
            @overload
            def __getitem__(self, key: Literal["somSlow"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["somFast"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["smbSlow"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["smbFast"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilCarbamid"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["soilNH4"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["soilNO2"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["soilNO3"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["soilFrozen"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sps"],
            ) -> _SoilLayerStateStructModule._SoilLayerStateSchema._SpsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilMoistureM3"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SoilLayerStateStructModule._SoilLayerStateSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SoilLayerStateSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        layerThickness: float | None = None,
        soilWaterFlux: float | None = None,
        voAOMPool: builders.AOMPropertiesListBuilder | dict[str, Any] | None = None,
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
    ) -> builders.SoilLayerStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilLayerStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SoilLayerStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilLayerStateBuilder]: ...
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
    ) -> readers.SoilLayerStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilLayerStateReader: ...

class _SoilColumnStateStructModule(_StructModule):
    class _DelayedNMinApplicationParamsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _DelayedNMinApplicationParamsSchema(_StructSchema):
            class _FpField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_model_monica_monica_management_capnp_schemas._ParamsMineralFertilizationParametersSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["fp"],
                ) -> _SoilColumnStateStructModule._DelayedNMinApplicationParamsStructModule._DelayedNMinApplicationParamsSchema._FpField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["samplingDepth"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["cropNTarget"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["cropNTarget30"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["fertiliserMinApplication"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["fertiliserMaxApplication"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["topDressingDelay"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _SoilColumnStateStructModule._DelayedNMinApplicationParamsStructModule._DelayedNMinApplicationParamsSchema._Fields: ...

        @property
        @override
        def schema(
            self,
        ) -> schemas._SoilColumnStateDelayedNMinApplicationParamsSchema: ...
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
        ) -> builders.DelayedNMinApplicationParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.DelayedNMinApplicationParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.DelayedNMinApplicationParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.DelayedNMinApplicationParamsBuilder]: ...
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
        ) -> readers.DelayedNMinApplicationParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.DelayedNMinApplicationParamsReader: ...

    DelayedNMinApplicationParams: _DelayedNMinApplicationParamsStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilColumnStateSchema(_StructSchema):
        class _VfTopDressingPartitionField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_management_capnp_schemas._ParamsMineralFertilizationParametersSchema: ...

        class _CropModuleField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._CropModuleStateSchema: ...

        class _DelayedNMinApplicationsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(
                    self,
                ) -> schemas._SoilColumnStateDelayedNMinApplicationParamsSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _SoilColumnStateStructModule._SoilColumnStateSchema._DelayedNMinApplicationsField._Schema: ...

        class _LayersField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._SoilLayerStateSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> (
                _SoilColumnStateStructModule._SoilColumnStateSchema._LayersField._Schema
            ): ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["vsSurfaceWaterStorage"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsInterceptionStorage"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vmGroundwaterTable"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsFluxAtLowerBoundary"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vqCropNUptake"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vtSoilSurfaceTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vmSnowDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["psMaxMineralisationDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsNumberOfOrganicLayers"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vfTopDressing"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vfTopDressingPartition"],
            ) -> _SoilColumnStateStructModule._SoilColumnStateSchema._VfTopDressingPartitionField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vfTopDressingDelay"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropModule"],
            ) -> (
                _SoilColumnStateStructModule._SoilColumnStateSchema._CropModuleField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["delayedNMinApplications"],
            ) -> _SoilColumnStateStructModule._SoilColumnStateSchema._DelayedNMinApplicationsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pmCriticalMoistureDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["layers"],
            ) -> _SoilColumnStateStructModule._SoilColumnStateSchema._LayersField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SoilColumnStateStructModule._SoilColumnStateSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SoilColumnStateSchema: ...
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
        cropModule: builders.CropModuleStateBuilder | dict[str, Any] | None = None,
        delayedNMinApplications: builders.DelayedNMinApplicationParamsListBuilder
        | dict[str, Any]
        | None = None,
        pmCriticalMoistureDepth: float | None = None,
        layers: builders.SoilLayerStateListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.SoilColumnStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilColumnStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SoilColumnStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilColumnStateBuilder]: ...
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
    ) -> readers.SoilColumnStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilColumnStateReader: ...

class _SoilTemperatureModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilTemperatureModuleStateSchema(_StructSchema):
        class _ModuleParamsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._SoilTemperatureModuleParametersSchema: ...

        class _SoilColumnVtGroundLayerField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._SoilLayerStateSchema: ...

        class _SoilColumnVtBottomLayerField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._SoilLayerStateSchema: ...

        class _VsSoilMoistureConstField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SoilTemperatureField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _VField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _VolumeMatrixField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _VolumeMatrixOldField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _BField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _MatrixPrimaryDiagonalField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _MatrixSecundaryDiagonalField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _HeatConductivityField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _HeatConductivityMeanField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _HeatCapacityField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["soilSurfaceTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["moduleParams"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._ModuleParamsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["dampingFactor"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilColumnVtGroundLayer"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._SoilColumnVtGroundLayerField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilColumnVtBottomLayer"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._SoilColumnVtBottomLayerField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["numberOfLayers"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsNumberOfLayers"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsSoilMoistureConst"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._VsSoilMoistureConstField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilTemperature"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._SoilTemperatureField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["v"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._VField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["volumeMatrix"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._VolumeMatrixField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["volumeMatrixOld"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._VolumeMatrixOldField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["b"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._BField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["matrixPrimaryDiagonal"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._MatrixPrimaryDiagonalField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["matrixSecundaryDiagonal"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._MatrixSecundaryDiagonalField: ...
            @overload
            def __getitem__(self, key: Literal["heatFlow"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["heatConductivity"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._HeatConductivityField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["heatConductivityMean"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._HeatConductivityMeanField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["heatCapacity"],
            ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._HeatCapacityField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SoilTemperatureModuleStateSchema: ...
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
        soilColumnVtGroundLayer: builders.SoilLayerStateBuilder
        | dict[str, Any]
        | None = None,
        soilColumnVtBottomLayer: builders.SoilLayerStateBuilder
        | dict[str, Any]
        | None = None,
        numberOfLayers: int | None = None,
        vsNumberOfLayers: int | None = None,
        vsSoilMoistureConst: builders.Float64ListBuilder | dict[str, Any] | None = None,
        soilTemperature: builders.Float64ListBuilder | dict[str, Any] | None = None,
        v: builders.Float64ListBuilder | dict[str, Any] | None = None,
        volumeMatrix: builders.Float64ListBuilder | dict[str, Any] | None = None,
        volumeMatrixOld: builders.Float64ListBuilder | dict[str, Any] | None = None,
        b: builders.Float64ListBuilder | dict[str, Any] | None = None,
        matrixPrimaryDiagonal: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        matrixSecundaryDiagonal: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        heatFlow: float | None = None,
        heatConductivity: builders.Float64ListBuilder | dict[str, Any] | None = None,
        heatConductivityMean: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        heatCapacity: builders.Float64ListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.SoilTemperatureModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilTemperatureModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SoilTemperatureModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilTemperatureModuleStateBuilder]: ...
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
    ) -> readers.SoilTemperatureModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilTemperatureModuleStateReader: ...

class _FrostModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _FrostModuleStateSchema(_StructSchema):
        class _LambdaReduxField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["pmHydraulicConductivityRedux"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["frostDepth"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["accumulatedFrostDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["negativeDegreeDays"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["thawDepth"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["frostDays"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lambdaRedux"],
            ) -> (
                _FrostModuleStateStructModule._FrostModuleStateSchema._LambdaReduxField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["temperatureUnderSnow"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["hydraulicConductivityRedux"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["ptTimeStep"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _FrostModuleStateStructModule._FrostModuleStateSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._FrostModuleStateSchema: ...
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
        lambdaRedux: builders.Float64ListBuilder | dict[str, Any] | None = None,
        temperatureUnderSnow: float | None = None,
        hydraulicConductivityRedux: float | None = None,
        ptTimeStep: float | None = None,
        **kwargs: object,
    ) -> builders.FrostModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.FrostModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.FrostModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.FrostModuleStateBuilder]: ...
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
    ) -> readers.FrostModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.FrostModuleStateReader: ...

class _SnowModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SnowModuleStateSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["snowRetentionCapacityMax"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["snowDensity"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["snowDepth"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["frozenWaterInSnow"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["liquidWaterInSnow"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["waterToInfiltrate"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["maxSnowDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["accumulatedSnowDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["snowmeltTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["snowAccumulationThresholdTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["temperatureLimitForLiquidWater"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["correctionRain"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["correctionSnow"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["refreezeTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["refreezeP1"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["refreezeP2"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["newSnowDensityMin"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["snowMaxAdditionalDensity"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["snowPacking"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["snowRetentionCapacityMin"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SnowModuleStateStructModule._SnowModuleStateSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SnowModuleStateSchema: ...
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
    ) -> builders.SnowModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SnowModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SnowModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SnowModuleStateBuilder]: ...
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
    ) -> readers.SnowModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SnowModuleStateReader: ...

class _SoilMoistureModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilMoistureModuleStateSchema(_StructSchema):
        class _FrostComponentField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._FrostModuleStateSchema: ...

        class _SnowComponentField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._SnowModuleStateSchema: ...

        class _ModuleParamsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._SoilMoistureModuleParametersSchema: ...

        class _AvailableWaterField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _CapillaryRiseRateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _CapillaryWaterField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _CapillaryWater70Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _EvaporationField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _EvapotranspirationField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _FieldCapacityField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _GravitationalWaterField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _HeatConductivityField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _LambdaField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _LayerThicknessField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PermanentWiltingPointField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PercolationRateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _ResidualEvapotranspirationField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SaturatedHydraulicConductivityField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SoilMoistureField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SoilPoreVolumeField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _TranspirationField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _WaterFluxField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["frostComponent"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._FrostComponentField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["snowComponent"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._SnowComponentField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["xSACriticalSoilMoisture"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["moduleParams"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._ModuleParamsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vwWindSpeedHeight"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vwWindSpeed"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["numberOfLayers"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsNumberOfLayers"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["actualEvaporation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["actualEvapotranspiration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["actualTranspiration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["availableWater"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._AvailableWaterField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["capillaryRise"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["capillaryRiseRate"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._CapillaryRiseRateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["capillaryWater"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._CapillaryWaterField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["capillaryWater70"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._CapillaryWater70Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["evaporation"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._EvaporationField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["evapotranspiration"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._EvapotranspirationField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["fieldCapacity"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._FieldCapacityField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["fluxAtLowerBoundary"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["gravitationalWater"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._GravitationalWaterField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["grossPrecipitation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["groundwaterAdded"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["groundwaterDischarge"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["groundwaterTable"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["heatConductivity"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._HeatConductivityField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["hydraulicConductivityRedux"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["infiltration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["interception"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["vcKcFactor"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lambda"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._LambdaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lambdaReduced"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["vsLatitude"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["layerThickness"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._LayerThicknessField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pmLayerThickness"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pmLeachingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pmLeachingDepthLayer"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vwMaxAirTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["pmMaxPercolationRate"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vwMeanAirTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vwMinAirTemperature"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vcNetPrecipitation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vwNetRadiation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["permanentWiltingPoint"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._PermanentWiltingPointField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vcPercentageSoilCoverage"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["percolationRate"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._PercolationRateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vwPrecipitation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["referenceEvapotranspiration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["relativeHumidity"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["residualEvapotranspiration"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._ResidualEvapotranspirationField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["saturatedHydraulicConductivity"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._SaturatedHydraulicConductivityField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilMoisture"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._SoilMoistureField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilMoisturecrit"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilMoistureDeficit"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilPoreVolume"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._SoilPoreVolumeField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vcStomataResistance"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["surfaceRoughness"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["surfaceRunOff"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sumSurfaceRunOff"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["surfaceWaterStorage"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["ptTimeStep"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["totalWaterRemoval"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["transpiration"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._TranspirationField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["transpirationDeficit"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["waterFlux"],
            ) -> _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._WaterFluxField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> (
            _SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema._Fields
        ): ...

    @property
    @override
    def schema(self) -> schemas._SoilMoistureModuleStateSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        frostComponent: builders.FrostModuleStateBuilder | dict[str, Any] | None = None,
        snowComponent: builders.SnowModuleStateBuilder | dict[str, Any] | None = None,
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
        availableWater: builders.Float64ListBuilder | dict[str, Any] | None = None,
        capillaryRise: float | None = None,
        capillaryRiseRate: builders.Float64ListBuilder | dict[str, Any] | None = None,
        capillaryWater: builders.Float64ListBuilder | dict[str, Any] | None = None,
        capillaryWater70: builders.Float64ListBuilder | dict[str, Any] | None = None,
        evaporation: builders.Float64ListBuilder | dict[str, Any] | None = None,
        evapotranspiration: builders.Float64ListBuilder | dict[str, Any] | None = None,
        fieldCapacity: builders.Float64ListBuilder | dict[str, Any] | None = None,
        fluxAtLowerBoundary: float | None = None,
        gravitationalWater: builders.Float64ListBuilder | dict[str, Any] | None = None,
        grossPrecipitation: float | None = None,
        groundwaterAdded: float | None = None,
        groundwaterDischarge: float | None = None,
        groundwaterTable: int | None = None,
        heatConductivity: builders.Float64ListBuilder | dict[str, Any] | None = None,
        hydraulicConductivityRedux: float | None = None,
        infiltration: float | None = None,
        interception: float | None = None,
        vcKcFactor: float | None = None,
        lambda_: builders.Float64ListBuilder | dict[str, Any] | None = None,
        lambdaReduced: float | None = None,
        vsLatitude: float | None = None,
        layerThickness: builders.Float64ListBuilder | dict[str, Any] | None = None,
        pmLayerThickness: float | None = None,
        pmLeachingDepth: float | None = None,
        pmLeachingDepthLayer: int | None = None,
        vwMaxAirTemperature: float | None = None,
        pmMaxPercolationRate: float | None = None,
        vwMeanAirTemperature: float | None = None,
        vwMinAirTemperature: float | None = None,
        vcNetPrecipitation: float | None = None,
        vwNetRadiation: float | None = None,
        permanentWiltingPoint: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        vcPercentageSoilCoverage: float | None = None,
        percolationRate: builders.Float64ListBuilder | dict[str, Any] | None = None,
        vwPrecipitation: float | None = None,
        referenceEvapotranspiration: float | None = None,
        relativeHumidity: float | None = None,
        residualEvapotranspiration: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        saturatedHydraulicConductivity: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        soilMoisture: builders.Float64ListBuilder | dict[str, Any] | None = None,
        soilMoisturecrit: float | None = None,
        soilMoistureDeficit: float | None = None,
        soilPoreVolume: builders.Float64ListBuilder | dict[str, Any] | None = None,
        vcStomataResistance: float | None = None,
        surfaceRoughness: float | None = None,
        surfaceRunOff: float | None = None,
        sumSurfaceRunOff: float | None = None,
        surfaceWaterStorage: float | None = None,
        ptTimeStep: float | None = None,
        totalWaterRemoval: float | None = None,
        transpiration: builders.Float64ListBuilder | dict[str, Any] | None = None,
        transpirationDeficit: float | None = None,
        waterFlux: builders.Float64ListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.SoilMoistureModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilMoistureModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SoilMoistureModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilMoistureModuleStateBuilder]: ...
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
    ) -> readers.SoilMoistureModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilMoistureModuleStateReader: ...

class _SoilOrganicModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilOrganicModuleStateSchema(_StructSchema):
        class _ModuleParamsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._SoilOrganicModuleParametersSchema: ...

        class _ActAmmoniaOxidationRateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _ActNitrificationRateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _ActDenitrificationRateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _AomFastDeltaSumField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _AomFastInputField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _AomFastSumField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _AomSlowDeltaSumField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _AomSlowInputField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _AomSlowSumField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _CBalanceField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _InertSoilOrganicCField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _NetNMineralisationRateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SmbCO2EvolutionRateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SmbFastDeltaField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SmbSlowDeltaField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _VsSoilMineralNContentField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SoilOrganicCField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SomFastDeltaField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SomFastInputField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SomSlowDeltaField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["incorporation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["totalDenitrification"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["moduleParams"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._ModuleParamsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsNumberOfLayers"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsNumberOfOrganicLayers"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["addedOrganicMatter"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["irrigationAmount"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["actAmmoniaOxidationRate"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._ActAmmoniaOxidationRateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["actNitrificationRate"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._ActNitrificationRateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["actDenitrificationRate"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._ActDenitrificationRateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomFastDeltaSum"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._AomFastDeltaSumField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomFastInput"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._AomFastInputField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomFastSum"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._AomFastSumField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomSlowDeltaSum"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._AomSlowDeltaSumField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomSlowInput"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._AomSlowInputField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aomSlowSum"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._AomSlowSumField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cBalance"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._CBalanceField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["decomposerRespiration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["errorMessage"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["inertSoilOrganicC"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._InertSoilOrganicCField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["n2oProduced"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["n2oProducedNit"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["n2oProducedDenit"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["netEcosystemExchange"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["netEcosystemProduction"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["netNMineralisation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["netNMineralisationRate"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._NetNMineralisationRateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["totalNH3Volatilised"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nh3Volatilised"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["smbCO2EvolutionRate"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._SmbCO2EvolutionRateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["smbFastDelta"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._SmbFastDeltaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["smbSlowDelta"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._SmbSlowDeltaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsSoilMineralNContent"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._VsSoilMineralNContentField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilOrganicC"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._SoilOrganicCField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["somFastDelta"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._SomFastDeltaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["somFastInput"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._SomFastInputField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["somSlowDelta"],
            ) -> _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._SomSlowDeltaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sumDenitrification"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sumNetNMineralisation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sumN2OProduced"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sumNH3Volatilised"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> (
            _SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema._Fields
        ): ...

    @property
    @override
    def schema(self) -> schemas._SoilOrganicModuleStateSchema: ...
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
        actAmmoniaOxidationRate: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        actNitrificationRate: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        actDenitrificationRate: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        aomFastDeltaSum: builders.Float64ListBuilder | dict[str, Any] | None = None,
        aomFastInput: builders.Float64ListBuilder | dict[str, Any] | None = None,
        aomFastSum: builders.Float64ListBuilder | dict[str, Any] | None = None,
        aomSlowDeltaSum: builders.Float64ListBuilder | dict[str, Any] | None = None,
        aomSlowInput: builders.Float64ListBuilder | dict[str, Any] | None = None,
        aomSlowSum: builders.Float64ListBuilder | dict[str, Any] | None = None,
        cBalance: builders.Float64ListBuilder | dict[str, Any] | None = None,
        decomposerRespiration: float | None = None,
        errorMessage: str | None = None,
        inertSoilOrganicC: builders.Float64ListBuilder | dict[str, Any] | None = None,
        n2oProduced: float | None = None,
        n2oProducedNit: float | None = None,
        n2oProducedDenit: float | None = None,
        netEcosystemExchange: float | None = None,
        netEcosystemProduction: float | None = None,
        netNMineralisation: float | None = None,
        netNMineralisationRate: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        totalNH3Volatilised: float | None = None,
        nh3Volatilised: float | None = None,
        smbCO2EvolutionRate: builders.Float64ListBuilder | dict[str, Any] | None = None,
        smbFastDelta: builders.Float64ListBuilder | dict[str, Any] | None = None,
        smbSlowDelta: builders.Float64ListBuilder | dict[str, Any] | None = None,
        vsSoilMineralNContent: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        soilOrganicC: builders.Float64ListBuilder | dict[str, Any] | None = None,
        somFastDelta: builders.Float64ListBuilder | dict[str, Any] | None = None,
        somFastInput: builders.Float64ListBuilder | dict[str, Any] | None = None,
        somSlowDelta: builders.Float64ListBuilder | dict[str, Any] | None = None,
        sumDenitrification: float | None = None,
        sumNetNMineralisation: float | None = None,
        sumN2OProduced: float | None = None,
        sumNH3Volatilised: float | None = None,
        **kwargs: object,
    ) -> builders.SoilOrganicModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilOrganicModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SoilOrganicModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilOrganicModuleStateBuilder]: ...
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
    ) -> readers.SoilOrganicModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilOrganicModuleStateReader: ...

class _SoilTransportModuleStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilTransportModuleStateSchema(_StructSchema):
        class _ModuleParamsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._SoilTransportModuleParametersSchema: ...

        class _ConvectionField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _DiffusionCoeffField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _DispersionField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _DispersionCoeffField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _VcNUptakeFromLayerField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PoreWaterVelocityField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _VsSoilMineralNContentField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SoilNO3Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _SoilNO3aqField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _TotalDispersionField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PercolationRateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["pcMinimumAvailableN"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["moduleParams"],
            ) -> _SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema._ModuleParamsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["convection"],
            ) -> _SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema._ConvectionField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropNUptake"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["diffusionCoeff"],
            ) -> _SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema._DiffusionCoeffField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["dispersion"],
            ) -> _SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema._DispersionField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["dispersionCoeff"],
            ) -> _SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema._DispersionCoeffField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsLeachingDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["leachingAtBoundary"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsNDeposition"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vcNUptakeFromLayer"],
            ) -> _SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema._VcNUptakeFromLayerField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["poreWaterVelocity"],
            ) -> _SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema._PoreWaterVelocityField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsSoilMineralNContent"],
            ) -> _SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema._VsSoilMineralNContentField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilNO3"],
            ) -> _SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema._SoilNO3Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilNO3aq"],
            ) -> _SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema._SoilNO3aqField: ...
            @overload
            def __getitem__(self, key: Literal["timeStep"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["totalDispersion"],
            ) -> _SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema._TotalDispersionField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["percolationRate"],
            ) -> _SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema._PercolationRateField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SoilTransportModuleStateSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        pcMinimumAvailableN: float | None = None,
        moduleParams: SoilTransportModuleParametersBuilder
        | dict[str, Any]
        | None = None,
        convection: builders.Float64ListBuilder | dict[str, Any] | None = None,
        cropNUptake: float | None = None,
        diffusionCoeff: builders.Float64ListBuilder | dict[str, Any] | None = None,
        dispersion: builders.Float64ListBuilder | dict[str, Any] | None = None,
        dispersionCoeff: builders.Float64ListBuilder | dict[str, Any] | None = None,
        vsLeachingDepth: float | None = None,
        leachingAtBoundary: float | None = None,
        vsNDeposition: float | None = None,
        vcNUptakeFromLayer: builders.Float64ListBuilder | dict[str, Any] | None = None,
        poreWaterVelocity: builders.Float64ListBuilder | dict[str, Any] | None = None,
        vsSoilMineralNContent: builders.Float64ListBuilder
        | dict[str, Any]
        | None = None,
        soilNO3: builders.Float64ListBuilder | dict[str, Any] | None = None,
        soilNO3aq: builders.Float64ListBuilder | dict[str, Any] | None = None,
        timeStep: float | None = None,
        totalDispersion: builders.Float64ListBuilder | dict[str, Any] | None = None,
        percolationRate: builders.Float64ListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.SoilTransportModuleStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilTransportModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SoilTransportModuleStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilTransportModuleStateBuilder]: ...
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
    ) -> readers.SoilTransportModuleStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilTransportModuleStateReader: ...

class _MonicaModelStateStructModule(_StructModule):
    class _ACDToValueStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _ACDToValueSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["acd"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["value"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _MonicaModelStateStructModule._ACDToValueStructModule._ACDToValueSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._MonicaModelStateACDToValueSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            acd: int | None = None,
            value: float | None = None,
            **kwargs: object,
        ) -> builders.ACDToValueBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.ACDToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.ACDToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.ACDToValueBuilder]: ...
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
        ) -> readers.ACDToValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.ACDToValueReader: ...

    ACDToValue: _ACDToValueStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _MonicaModelStateSchema(_StructSchema):
        class _SitePsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._SiteParametersSchema: ...

        class _EnvPsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._EnvironmentParametersSchema: ...

        class _CropPsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._CropModuleParametersSchema: ...

        class _SimPsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._SimulationParametersSchema: ...

        class _GroundwaterInformationField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._MeasuredGroundwaterTableInformationSchema: ...

        class _SoilColumnField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._SoilColumnStateSchema: ...

        class _SoilTemperatureField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._SoilTemperatureModuleStateSchema: ...

        class _SoilMoistureField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._SoilMoistureModuleStateSchema: ...

        class _SoilOrganicField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._SoilOrganicModuleStateSchema: ...

        class _SoilTransportField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._SoilTransportModuleStateSchema: ...

        class _CurrentCropModuleField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._CropModuleStateSchema: ...

        class _CurrentStepDateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _ClimateDataField(_StructSchemaField):
            class _Schema(_ListSchema):
                class _ElementSchema(_ListSchema):
                    @property
                    @override
                    def elementType(
                        self,
                    ) -> schemas._MonicaModelStateACDToValueSchema: ...

                @property
                @override
                def elementType(
                    self,
                ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._ClimateDataField._Schema._ElementSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._ClimateDataField._Schema: ...

        class _CurrentEventsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _PreviousDaysEventsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["sitePs"],
            ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._SitePsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cultivationMethodCount"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["envPs"],
            ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._EnvPsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropPs"],
            ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._CropPsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vsGroundwaterDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vwAtmosphericO3Concentration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vwAtmosphericCO2Concentration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["simPs"],
            ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._SimPsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["groundwaterInformation"],
            ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._GroundwaterInformationField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilColumn"],
            ) -> (
                _MonicaModelStateStructModule._MonicaModelStateSchema._SoilColumnField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilTemperature"],
            ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._SoilTemperatureField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilMoisture"],
            ) -> (
                _MonicaModelStateStructModule._MonicaModelStateSchema._SoilMoistureField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilOrganic"],
            ) -> (
                _MonicaModelStateStructModule._MonicaModelStateSchema._SoilOrganicField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilTransport"],
            ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._SoilTransportField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["accuOxygenStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["currentCropModule"],
            ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._CurrentCropModuleField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sumFertiliser"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sumOrgFertiliser"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["dailySumFertiliser"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["dailySumOrgFertiliser"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["dailySumOrganicFertilizerDM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sumOrganicFertilizerDM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["humusBalanceCarryOver"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["dailySumIrrigationWater"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["optCarbonExportedResidues"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["optCarbonReturnedResidues"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["currentStepDate"],
            ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._CurrentStepDateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["climateData"],
            ) -> (
                _MonicaModelStateStructModule._MonicaModelStateSchema._ClimateDataField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["currentEvents"],
            ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._CurrentEventsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["previousDaysEvents"],
            ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._PreviousDaysEventsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["clearCropUponNextDay"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["daysWithCrop"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["accuNStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["accuWaterStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["accuHeatStress"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _MonicaModelStateStructModule._MonicaModelStateSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._MonicaModelStateSchema: ...
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
        soilColumn: builders.SoilColumnStateBuilder | dict[str, Any] | None = None,
        soilTemperature: builders.SoilTemperatureModuleStateBuilder
        | dict[str, Any]
        | None = None,
        soilMoisture: builders.SoilMoistureModuleStateBuilder
        | dict[str, Any]
        | None = None,
        soilOrganic: builders.SoilOrganicModuleStateBuilder
        | dict[str, Any]
        | None = None,
        soilTransport: builders.SoilTransportModuleStateBuilder
        | dict[str, Any]
        | None = None,
        accuOxygenStress: float | None = None,
        currentCropModule: builders.CropModuleStateBuilder
        | dict[str, Any]
        | None = None,
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
        climateData: builders.ACDToValueListListBuilder | dict[str, Any] | None = None,
        currentEvents: builders.TextListBuilder | dict[str, Any] | None = None,
        previousDaysEvents: builders.TextListBuilder | dict[str, Any] | None = None,
        clearCropUponNextDay: bool | None = None,
        daysWithCrop: int | None = None,
        accuNStress: float | None = None,
        accuWaterStress: float | None = None,
        accuHeatStress: float | None = None,
        **kwargs: object,
    ) -> builders.MonicaModelStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.MonicaModelStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.MonicaModelStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.MonicaModelStateBuilder]: ...
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
    ) -> readers.MonicaModelStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.MonicaModelStateReader: ...

class _RuntimeStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _RuntimeStateSchema(_StructSchema):
        class _ModelStateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._MonicaModelStateSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["modelState"],
            ) -> _RuntimeStateStructModule._RuntimeStateSchema._ModelStateField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _RuntimeStateStructModule._RuntimeStateSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._RuntimeStateSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        modelState: builders.MonicaModelStateBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.RuntimeStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.RuntimeStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.RuntimeStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.RuntimeStateBuilder]: ...
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
    ) -> readers.RuntimeStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.RuntimeStateReader: ...

class _CropStateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _CropStateSchema(_StructSchema):
        class _AutomaticHarvestParamsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._AutomaticHarvestParametersSchema: ...

        class _SeedDateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _HarvestDateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _IsWinterCropField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._MaybeBoolSchema: ...

        class _IsPerennialCropField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._MaybeBoolSchema: ...

        class _CuttingDatesField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(
                    self,
                ) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _CropStateStructModule._CropStateSchema._CuttingDatesField._Schema: ...

        class _CropParamsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._CropParametersSchema: ...

        class _PerennialCropParamsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._CropParametersSchema: ...

        class _ResidueParamsField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_model_monica_monica_params_capnp_schemas._CropResidueParametersSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["automaticHarvestParams"],
            ) -> (
                _CropStateStructModule._CropStateSchema._AutomaticHarvestParamsField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["speciesName"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cultivarName"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["seedDate"],
            ) -> _CropStateStructModule._CropStateSchema._SeedDateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["harvestDate"],
            ) -> _CropStateStructModule._CropStateSchema._HarvestDateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["isWinterCrop"],
            ) -> _CropStateStructModule._CropStateSchema._IsWinterCropField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["isPerennialCrop"],
            ) -> _CropStateStructModule._CropStateSchema._IsPerennialCropField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cuttingDates"],
            ) -> _CropStateStructModule._CropStateSchema._CuttingDatesField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropParams"],
            ) -> _CropStateStructModule._CropStateSchema._CropParamsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["perennialCropParams"],
            ) -> _CropStateStructModule._CropStateSchema._PerennialCropParamsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["residueParams"],
            ) -> _CropStateStructModule._CropStateSchema._ResidueParamsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["crossCropAdaptionFactor"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["automaticHarvest"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _CropStateStructModule._CropStateSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._CropStateSchema: ...
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
        isWinterCrop: builders.MaybeBoolBuilder | dict[str, Any] | None = None,
        isPerennialCrop: builders.MaybeBoolBuilder | dict[str, Any] | None = None,
        cuttingDates: builders.DateListBuilder | dict[str, Any] | None = None,
        cropParams: CropParametersBuilder | dict[str, Any] | None = None,
        perennialCropParams: CropParametersBuilder | dict[str, Any] | None = None,
        residueParams: CropResidueParametersBuilder | dict[str, Any] | None = None,
        crossCropAdaptionFactor: float | None = None,
        automaticHarvest: bool | None = None,
        **kwargs: object,
    ) -> builders.CropStateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.CropStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.CropStateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.CropStateBuilder]: ...
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
    ) -> readers.CropStateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CropStateReader: ...

class _ICDataStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _ICDataSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["noCrop"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["height"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["lait"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _ICDataStructModule._ICDataSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._ICDataSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        noCrop: None | None = None,
        height: float | None = None,
        lait: float | None = None,
        **kwargs: object,
    ) -> builders.ICDataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.ICDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.ICDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.ICDataBuilder]: ...
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
    ) -> readers.ICDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.ICDataReader: ...
