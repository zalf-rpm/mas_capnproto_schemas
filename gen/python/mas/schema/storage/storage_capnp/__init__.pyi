"""This is an automatically generated stub for `storage.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.storage.storage_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

Store: types.modules._StoreInterfaceModule

__all__ = ["Store", "get_schema_by_id", "load_capnp_file", "types"]
