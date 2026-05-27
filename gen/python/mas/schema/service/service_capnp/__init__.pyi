"""This is an automatically generated stub for `service.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.service.service_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

Admin: types.modules._AdminInterfaceModule
SimpleFactory: types.modules._SimpleFactoryInterfaceModule
Factory: types.modules._FactoryInterfaceModule
Stoppable: types.modules._StoppableInterfaceModule

__all__ = [
    "Admin",
    "Factory",
    "SimpleFactory",
    "Stoppable",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
