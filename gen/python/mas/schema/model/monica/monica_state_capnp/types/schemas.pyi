"""Schema helper types for `monica_state.capnp`."""

from mas.schema.model.monica.monica_state_capnp.types import modules as modules

type _AOMPropertiesSchema = modules._AOMPropertiesStructModule._AOMPropertiesSchema

type _CropModuleStateSchema = (
    modules._CropModuleStateStructModule._CropModuleStateSchema
)

type _CropStateSchema = modules._CropStateStructModule._CropStateSchema

type _FrostModuleStateSchema = (
    modules._FrostModuleStateStructModule._FrostModuleStateSchema
)

type _ICDataSchema = modules._ICDataStructModule._ICDataSchema

type _MaybeBoolSchema = modules._MaybeBoolStructModule._MaybeBoolSchema

type _MonicaModelStateACDToValueSchema = (
    modules._MonicaModelStateStructModule._ACDToValueStructModule._ACDToValueSchema
)

type _MonicaModelStateSchema = (
    modules._MonicaModelStateStructModule._MonicaModelStateSchema
)

type _RuntimeStateSchema = modules._RuntimeStateStructModule._RuntimeStateSchema

type _SnowModuleStateSchema = (
    modules._SnowModuleStateStructModule._SnowModuleStateSchema
)

type _SoilColumnStateDelayedNMinApplicationParamsSchema = modules._SoilColumnStateStructModule._DelayedNMinApplicationParamsStructModule._DelayedNMinApplicationParamsSchema

type _SoilColumnStateSchema = (
    modules._SoilColumnStateStructModule._SoilColumnStateSchema
)

type _SoilLayerStateSchema = modules._SoilLayerStateStructModule._SoilLayerStateSchema

type _SoilMoistureModuleStateSchema = (
    modules._SoilMoistureModuleStateStructModule._SoilMoistureModuleStateSchema
)

type _SoilOrganicModuleStateSchema = (
    modules._SoilOrganicModuleStateStructModule._SoilOrganicModuleStateSchema
)

type _SoilTemperatureModuleStateSchema = (
    modules._SoilTemperatureModuleStateStructModule._SoilTemperatureModuleStateSchema
)

type _SoilTransportModuleStateSchema = (
    modules._SoilTransportModuleStateStructModule._SoilTransportModuleStateSchema
)
