"""This is an automatically generated stub for `monica_state.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.model.monica.monica_state_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

MaybeBool: types.modules._MaybeBoolStructModule
CropModuleState: types.modules._CropModuleStateStructModule
AOMProperties: types.modules._AOMPropertiesStructModule
SoilLayerState: types.modules._SoilLayerStateStructModule
SoilColumnState: types.modules._SoilColumnStateStructModule
SoilTemperatureModuleState: types.modules._SoilTemperatureModuleStateStructModule
FrostModuleState: types.modules._FrostModuleStateStructModule
SnowModuleState: types.modules._SnowModuleStateStructModule
SoilMoistureModuleState: types.modules._SoilMoistureModuleStateStructModule
SoilOrganicModuleState: types.modules._SoilOrganicModuleStateStructModule
SoilTransportModuleState: types.modules._SoilTransportModuleStateStructModule
MonicaModelState: types.modules._MonicaModelStateStructModule
RuntimeState: types.modules._RuntimeStateStructModule
CropState: types.modules._CropStateStructModule
ICData: types.modules._ICDataStructModule

__all__ = [
    "AOMProperties",
    "CropModuleState",
    "CropState",
    "FrostModuleState",
    "ICData",
    "MaybeBool",
    "MonicaModelState",
    "RuntimeState",
    "SnowModuleState",
    "SoilColumnState",
    "SoilLayerState",
    "SoilMoistureModuleState",
    "SoilOrganicModuleState",
    "SoilTemperatureModuleState",
    "SoilTransportModuleState",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
