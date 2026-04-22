"""Schema helper types for `management.capnp`."""

from mas.schema.management.management_capnp.types import modules as modules

type _EventEventAfterSchema = (
    modules._EventStructModule._EventAfterStructModule._EventAfterSchema
)

type _EventEventAtSchema = (
    modules._EventStructModule._EventAtStructModule._EventAtSchema
)

type _EventEventBetweenSchema = (
    modules._EventStructModule._EventBetweenStructModule._EventBetweenSchema
)

type _EventExternalTypeEnumSchema = (
    modules._EventStructModule._ExternalTypeEnumModule._ExternalTypeSchema
)

type _EventPhenoStageEnumSchema = (
    modules._EventStructModule._PhenoStageEnumModule._PhenoStageSchema
)

type _EventSchema = modules._EventStructModule._EventSchema

type _EventTypeEnumSchema = modules._EventTypeEnumModule._EventTypeSchema

type _EventTypeSchema = modules._EventStructModule._TypeStructModule._TypeSchema

type _FertilizerSchema = modules._FertilizerInterfaceModule._FertilizerSchema

type _FertilizerServiceSchema = (
    modules._FertilizerServiceInterfaceModule._FertilizerServiceSchema
)

type _NutrientNameEnumSchema = modules._NutrientStructModule._NameEnumModule._NameSchema

type _NutrientSchema = modules._NutrientStructModule._NutrientSchema

type _NutrientUnitEnumSchema = modules._NutrientStructModule._UnitEnumModule._UnitSchema

type _ParamsAutomaticHarvestSchema = (
    modules._ParamsStructModule._AutomaticHarvestStructModule._AutomaticHarvestSchema
)

type _ParamsAutomaticSowingAvgSoilTempSchema = modules._ParamsStructModule._AutomaticSowingStructModule._AvgSoilTempStructModule._AvgSoilTempSchema

type _ParamsAutomaticSowingSchema = (
    modules._ParamsStructModule._AutomaticSowingStructModule._AutomaticSowingSchema
)

type _ParamsCuttingCLEnumSchema = (
    modules._ParamsStructModule._CuttingStructModule._CLEnumModule._CLSchema
)

type _ParamsCuttingSchema = (
    modules._ParamsStructModule._CuttingStructModule._CuttingSchema
)

type _ParamsCuttingSpecSchema = (
    modules._ParamsStructModule._CuttingStructModule._SpecStructModule._SpecSchema
)

type _ParamsCuttingUnitEnumSchema = (
    modules._ParamsStructModule._CuttingStructModule._UnitEnumModule._UnitSchema
)

type _ParamsHarvestCropUsageEnumSchema = modules._ParamsStructModule._HarvestStructModule._CropUsageEnumModule._CropUsageSchema

type _ParamsHarvestOptCarbonMgmtDataSchema = modules._ParamsStructModule._HarvestStructModule._OptCarbonMgmtDataStructModule._OptCarbonMgmtDataSchema

type _ParamsHarvestSchema = (
    modules._ParamsStructModule._HarvestStructModule._HarvestSchema
)

type _ParamsIrrigationSchema = (
    modules._ParamsStructModule._IrrigationStructModule._IrrigationSchema
)

type _ParamsMineralFertilizationSchema = modules._ParamsStructModule._MineralFertilizationStructModule._MineralFertilizationSchema

type _ParamsNDemandFertilizationSchema = modules._ParamsStructModule._NDemandFertilizationStructModule._NDemandFertilizationSchema

type _ParamsOrganicFertilizationSchema = modules._ParamsStructModule._OrganicFertilizationStructModule._OrganicFertilizationSchema

type _ParamsSchema = modules._ParamsStructModule._ParamsSchema

type _ParamsSowingSchema = modules._ParamsStructModule._SowingStructModule._SowingSchema

type _ParamsTillageSchema = (
    modules._ParamsStructModule._TillageStructModule._TillageSchema
)

type _PlantOrganEnumSchema = modules._PlantOrganEnumModule._PlantOrganSchema

type _ServiceSchema = modules._ServiceInterfaceModule._ServiceSchema
