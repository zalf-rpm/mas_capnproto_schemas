"""This is an automatically generated stub for `soil.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.soil.soil_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

SType: types.modules._STypeEnumModule
PropertyName: types.modules._PropertyNameEnumModule
Layer: types.modules._LayerStructModule
Query: types.modules._QueryStructModule
ProfileData: types.modules._ProfileDataStructModule
Profile: types.modules._ProfileInterfaceModule
Service: types.modules._ServiceInterfaceModule

__all__ = [
    "Layer",
    "Profile",
    "ProfileData",
    "PropertyName",
    "Query",
    "SType",
    "Service",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
