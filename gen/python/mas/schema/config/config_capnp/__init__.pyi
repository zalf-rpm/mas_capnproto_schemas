"""This is an automatically generated stub for `config.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.config.config_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

Service: types.modules._ServiceInterfaceModule

__all__ = ["Service", "get_schema_by_id", "load_capnp_file", "types"]
