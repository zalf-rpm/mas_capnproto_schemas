"""This is an automatically generated stub for `a.capnp`."""

from collections.abc import Sequence
from types import ModuleType as _ModuleType

from capnp.lib.capnp import _Schema

from mas.schema.test.a_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> _ModuleType: ...

A: types.modules._AInterfaceModule

__all__ = ["A", "get_schema_by_id", "load_capnp_file", "types"]
