"""This is an automatically generated stub for `crop.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.crop.crop_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

Crop: types.modules._CropInterfaceModule
Service: types.modules._ServiceInterfaceModule

__all__ = ["Crop", "Service", "get_schema_by_id", "load_capnp_file", "types"]
