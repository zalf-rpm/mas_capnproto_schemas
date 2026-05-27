"""This is an automatically generated stub for `yieldstat.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.model.yieldstat.yieldstat_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

ResultId: types.modules._ResultIdEnumModule
RestInput: types.modules._RestInputStructModule
Result: types.modules._ResultStructModule
Output: types.modules._OutputStructModule

__all__ = [
    "Output",
    "RestInput",
    "Result",
    "ResultId",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
