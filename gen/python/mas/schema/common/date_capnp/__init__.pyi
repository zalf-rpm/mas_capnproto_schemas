"""This is an automatically generated stub for `date.capnp`."""

from collections.abc import Sequence
from types import ModuleType as _ModuleType

from capnp.lib.capnp import _Schema

from mas.schema.common.date_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> _ModuleType: ...

Date: types.modules._DateStructModule

__all__ = ["Date", "get_schema_by_id", "load_capnp_file", "types"]
