"""This is an automatically generated stub for `sim_setup.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.model.monica.sim_setup_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

Setup: types.modules._SetupStructModule

__all__ = ["Setup", "get_schema_by_id", "load_capnp_file", "types"]
