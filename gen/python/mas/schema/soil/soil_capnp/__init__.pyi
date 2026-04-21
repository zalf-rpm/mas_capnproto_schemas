"""This is an automatically generated stub for `soil.capnp`."""

from mas.schema.soil.soil_capnp import types as types

class _STypeEnumModule:
    unknown: int
    ka5: int

class _PropertyNameEnumModule:
    soilType: int
    sand: int
    clay: int
    silt: int
    pH: int
    sceleton: int
    organicCarbon: int
    organicMatter: int
    bulkDensity: int
    rawDensity: int
    fieldCapacity: int
    permanentWiltingPoint: int
    saturation: int
    soilMoisture: int
    soilWaterConductivityCoefficient: int
    ammonium: int
    nitrate: int
    cnRatio: int
    inGroundwater: int
    impenetrable: int

Layer: types.modules._LayerStructModule
Query: types.modules._QueryStructModule
ProfileData: types.modules._ProfileDataStructModule
Profile: types.modules._ProfileInterfaceModule
Service: types.modules._ServiceInterfaceModule

__all__ = ["Layer", "Profile", "ProfileData", "Query", "Service", "types"]
