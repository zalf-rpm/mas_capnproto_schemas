"""Schema helper types for `soil_params.capnp`."""

from mas.schema.soil.soil_params_capnp.types import modules as modules

type _CapillaryRiseRateDataSchema = (
    modules._CapillaryRiseRateStructModule._DataStructModule._DataSchema
)

type _CapillaryRiseRateSchema = (
    modules._CapillaryRiseRateStructModule._CapillaryRiseRateSchema
)

type _SoilCharacteristicDataDataSchema = (
    modules._SoilCharacteristicDataStructModule._DataStructModule._DataSchema
)

type _SoilCharacteristicDataSchema = (
    modules._SoilCharacteristicDataStructModule._SoilCharacteristicDataSchema
)

type _SoilCharacteristicModifierDataSchema = (
    modules._SoilCharacteristicModifierStructModule._DataStructModule._DataSchema
)

type _SoilCharacteristicModifierSchema = (
    modules._SoilCharacteristicModifierStructModule._SoilCharacteristicModifierSchema
)
