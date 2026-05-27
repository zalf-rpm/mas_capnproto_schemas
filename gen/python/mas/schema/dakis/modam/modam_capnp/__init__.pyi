"""This is an automatically generated stub for `modam.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.dakis.modam.modam_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

ModamWrapperService: types.modules._ModamWrapperServiceInterfaceModule

__all__ = ["ModamWrapperService", "get_schema_by_id", "load_capnp_file", "types"]
