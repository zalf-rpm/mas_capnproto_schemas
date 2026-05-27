"""This is an automatically generated stub for `web_berest_data_import.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.model.weberest.web_berest_data_import_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

DWLABImport: types.modules._DWLABImportInterfaceModule

__all__ = ["DWLABImport", "get_schema_by_id", "load_capnp_file", "types"]
