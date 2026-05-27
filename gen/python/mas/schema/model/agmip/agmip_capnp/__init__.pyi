"""This is an automatically generated stub for `agmip.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.model.agmip.agmip_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

FieldExperimentDataTemplate: types.modules._FieldExperimentDataTemplateStructModule

__all__ = [
    "FieldExperimentDataTemplate",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
