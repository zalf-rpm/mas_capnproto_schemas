"""This is an automatically generated stub for `jobs.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.jobs.jobs_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

Job: types.modules._JobStructModule
Service: types.modules._ServiceInterfaceModule

__all__ = ["Job", "Service", "get_schema_by_id", "load_capnp_file", "types"]
