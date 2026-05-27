"""This is an automatically generated stub for `grid.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.grid.grid_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

Aggregation: types.modules._AggregationEnumModule
Grid: types.modules._GridInterfaceModule

__all__ = ["Aggregation", "Grid", "get_schema_by_id", "load_capnp_file", "types"]
