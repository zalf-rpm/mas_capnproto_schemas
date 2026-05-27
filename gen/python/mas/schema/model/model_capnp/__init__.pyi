"""This is an automatically generated stub for `model.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.model.model_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

XYResult: types.modules._XYResultStructModule
Stat: types.modules._StatStructModule
XYPlusResult: types.modules._XYPlusResultStructModule
ClimateInstance: types.modules._ClimateInstanceInterfaceModule
Env: types.modules._EnvStructModule
EnvInstance: types.modules._EnvInstanceInterfaceModule
EnvInstanceProxy: types.modules._EnvInstanceProxyInterfaceModule
InstanceFactory: types.modules._InstanceFactoryInterfaceModule

__all__ = [
    "ClimateInstance",
    "Env",
    "EnvInstance",
    "EnvInstanceProxy",
    "InstanceFactory",
    "Stat",
    "XYPlusResult",
    "XYResult",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
