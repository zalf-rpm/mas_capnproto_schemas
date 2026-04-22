"""This is an automatically generated stub for `management.capnp`."""

from mas.schema.management.management_capnp import types as types

EventType: types.modules._EventTypeEnumModule
PlantOrgan: types.modules._PlantOrganEnumModule
Event: types.modules._EventStructModule
Nutrient: types.modules._NutrientStructModule

Fertilizer: types.modules._FertilizerInterfaceModule
Params: types.modules._ParamsStructModule
FertilizerService: types.modules._FertilizerServiceInterfaceModule
Service: types.modules._ServiceInterfaceModule

__all__ = [
    "Event",
    "EventType",
    "Fertilizer",
    "FertilizerService",
    "Nutrient",
    "Params",
    "PlantOrgan",
    "Service",
    "types",
]
