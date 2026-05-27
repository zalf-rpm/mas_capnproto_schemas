"""This is an automatically generated stub for `registry.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.registry.registry_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

Registry: types.modules._RegistryInterfaceModule

Admin: types.modules._AdminInterfaceModule
Registrar: types.modules._RegistrarInterfaceModule

__all__ = [
    "Admin",
    "Registrar",
    "Registry",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
