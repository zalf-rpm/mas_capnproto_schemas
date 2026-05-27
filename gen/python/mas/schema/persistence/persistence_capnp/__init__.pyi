"""This is an automatically generated stub for `persistence.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.persistence.persistence_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

VatId: types.modules._VatIdStructModule
Address: types.modules._AddressStructModule
VatPath: types.modules._VatPathStructModule
SturdyRef: types.modules._SturdyRefStructModule
Heartbeat: types.modules._HeartbeatInterfaceModule
Persistent: types.modules._PersistentInterfaceModule
Restorer: types.modules._RestorerInterfaceModule
HostPortResolver: types.modules._HostPortResolverInterfaceModule
Gateway: types.modules._GatewayInterfaceModule
GatewayRegistrable: types.modules._GatewayRegistrableInterfaceModule

__all__ = [
    "Address",
    "Gateway",
    "GatewayRegistrable",
    "Heartbeat",
    "HostPortResolver",
    "Persistent",
    "Restorer",
    "SturdyRef",
    "VatId",
    "VatPath",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
