"""This is an automatically generated stub for `management.capnp`."""

from mas.schema.management.management_capnp import types as types

class _EventTypeEnumModule:
    sowing: int
    automaticSowing: int
    harvest: int
    automaticHarvest: int
    irrigation: int
    tillage: int
    organicFertilization: int
    mineralFertilization: int
    nDemandFertilization: int
    cutting: int
    setValue: int
    saveState: int

class _PlantOrganEnumModule:
    root: int
    leaf: int
    shoot: int
    fruit: int
    strukt: int
    sugar: int

Event: types.modules._EventStructModule
Nutrient: types.modules._NutrientStructModule

Fertilizer: types.modules._FertilizerInterfaceModule
Params: types.modules._ParamsStructModule
FertilizerService: types.modules._FertilizerServiceInterfaceModule
Service: types.modules._ServiceInterfaceModule

__all__ = [
    "Event",
    "Fertilizer",
    "FertilizerService",
    "Nutrient",
    "Params",
    "Service",
    "types",
]
