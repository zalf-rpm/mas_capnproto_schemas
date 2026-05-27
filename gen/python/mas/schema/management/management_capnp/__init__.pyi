"""This is an automatically generated stub for `management.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.management.management_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

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
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
