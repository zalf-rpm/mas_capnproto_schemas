"""This is an automatically generated stub for `soil_params.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.soil.soil_params_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

SoilCharacteristicData: types.modules._SoilCharacteristicDataStructModule
SoilCharacteristicModifier: types.modules._SoilCharacteristicModifierStructModule
CapillaryRiseRate: types.modules._CapillaryRiseRateStructModule

__all__ = [
    "CapillaryRiseRate",
    "SoilCharacteristicData",
    "SoilCharacteristicModifier",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
