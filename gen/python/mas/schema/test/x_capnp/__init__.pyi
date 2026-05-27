"""This is an automatically generated stub for `x.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.test.x_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

X: types.modules._XInterfaceModule
S: types.modules._SStructModule
Y: types.modules._YInterfaceModule
Z: types.modules._ZInterfaceModule

__all__ = ["S", "X", "Y", "Z", "get_schema_by_id", "load_capnp_file", "types"]
