"""This is an automatically generated stub for `monica_management.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.model.monica.monica_management_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

ILRDates: types.modules._ILRDatesStructModule
EventType: types.modules._EventTypeEnumModule
PlantOrgan: types.modules._PlantOrganEnumModule
Event: types.modules._EventStructModule
Params: types.modules._ParamsStructModule
Service: types.modules._ServiceInterfaceModule

__all__ = [
    "Event",
    "EventType",
    "ILRDates",
    "Params",
    "PlantOrgan",
    "Service",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
