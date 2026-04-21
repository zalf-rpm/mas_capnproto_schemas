"""Schema helper types for `monica_params.capnp`."""

from mas.schema.model.monica.monica_params_capnp.types import modules as modules

type _AutomaticHarvestParametersSchema = (
    modules._AutomaticHarvestParametersStructModule._AutomaticHarvestParametersSchema
)

type _AutomaticIrrigationParametersSchema = modules._AutomaticIrrigationParametersStructModule._AutomaticIrrigationParametersSchema

type _CropModuleParametersSchema = (
    modules._CropModuleParametersStructModule._CropModuleParametersSchema
)

type _CropParametersSchema = modules._CropParametersStructModule._CropParametersSchema

type _CropResidueParametersSchema = (
    modules._CropResidueParametersStructModule._CropResidueParametersSchema
)

type _CropSpecSchema = modules._CropSpecStructModule._CropSpecSchema

type _CultivarParametersSchema = (
    modules._CultivarParametersStructModule._CultivarParametersSchema
)

type _EnvironmentParametersSchema = (
    modules._EnvironmentParametersStructModule._EnvironmentParametersSchema
)

type _EnvironmentParametersYearToValueSchema = modules._EnvironmentParametersStructModule._YearToValueStructModule._YearToValueSchema

type _MeasuredGroundwaterTableInformationDateToValueSchema = modules._MeasuredGroundwaterTableInformationStructModule._DateToValueStructModule._DateToValueSchema

type _MeasuredGroundwaterTableInformationSchema = modules._MeasuredGroundwaterTableInformationStructModule._MeasuredGroundwaterTableInformationSchema

type _NMinApplicationParametersSchema = (
    modules._NMinApplicationParametersStructModule._NMinApplicationParametersSchema
)

type _NMinCropParametersSchema = (
    modules._NMinCropParametersStructModule._NMinCropParametersSchema
)

type _SimulationParametersSchema = (
    modules._SimulationParametersStructModule._SimulationParametersSchema
)

type _SiteParametersSchema = modules._SiteParametersStructModule._SiteParametersSchema

type _SoilMoistureModuleParametersSchema = modules._SoilMoistureModuleParametersStructModule._SoilMoistureModuleParametersSchema

type _SoilOrganicModuleParametersSchema = (
    modules._SoilOrganicModuleParametersStructModule._SoilOrganicModuleParametersSchema
)

type _SoilParametersSchema = modules._SoilParametersStructModule._SoilParametersSchema

type _SoilTemperatureModuleParametersSchema = modules._SoilTemperatureModuleParametersStructModule._SoilTemperatureModuleParametersSchema

type _SoilTransportModuleParametersSchema = modules._SoilTransportModuleParametersStructModule._SoilTransportModuleParametersSchema

type _SpeciesParametersSchema = (
    modules._SpeciesParametersStructModule._SpeciesParametersSchema
)

type _SticsParametersSchema = (
    modules._SticsParametersStructModule._SticsParametersSchema
)

type _VocCPDataSchema = modules._VocStructModule._CPDataStructModule._CPDataSchema

type _VocEmissionsSchema = (
    modules._VocStructModule._EmissionsStructModule._EmissionsSchema
)

type _VocEmissionsSpeciesIdToEmissionSchema = modules._VocStructModule._EmissionsStructModule._SpeciesIdToEmissionStructModule._SpeciesIdToEmissionSchema

type _VocEnzymeActivityTSchema = (
    modules._VocStructModule._EnzymeActivityTStructModule._EnzymeActivityTSchema
)

type _VocFoliageTSchema = modules._VocStructModule._FoliageTStructModule._FoliageTSchema

type _VocLeafEmissionTSchema = (
    modules._VocStructModule._LeafEmissionTStructModule._LeafEmissionTSchema
)

type _VocLeafEmissionsSchema = (
    modules._VocStructModule._LeafEmissionsStructModule._LeafEmissionsSchema
)

type _VocMicroClimateDataSchema = (
    modules._VocStructModule._MicroClimateDataStructModule._MicroClimateDataSchema
)

type _VocPhotosynthTSchema = (
    modules._VocStructModule._PhotosynthTStructModule._PhotosynthTSchema
)

type _VocSchema = modules._VocStructModule._VocSchema

type _VocSpeciesDataSchema = (
    modules._VocStructModule._SpeciesDataStructModule._SpeciesDataSchema
)

type _YieldComponentSchema = modules._YieldComponentStructModule._YieldComponentSchema
