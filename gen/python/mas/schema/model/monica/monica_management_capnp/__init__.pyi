"""This is an automatically generated stub for `monica_management.capnp`."""

from mas.schema.model.monica.monica_management_capnp import types as types

ILRDates: types.modules._ILRDatesStructModule

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
Params: types.modules._ParamsStructModule
Service: types.modules._ServiceInterfaceModule

__all__ = ["Event", "ILRDates", "Params", "Service", "types"]
