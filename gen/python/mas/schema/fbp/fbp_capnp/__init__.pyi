"""This is an automatically generated stub for `fbp.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.fbp.fbp_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

IP: types.modules._IPStructModule
IIP: types.modules._IIPStructModule
Channel: types.modules._ChannelInterfaceModule
StartChannelsService: types.modules._StartChannelsServiceInterfaceModule
PortInfos: types.modules._PortInfosStructModule
Runnable: types.modules._RunnableInterfaceModule
Process: types.modules._ProcessInterfaceModule
Component: types.modules._ComponentStructModule

__all__ = [
    "IIP",
    "IP",
    "Channel",
    "Component",
    "PortInfos",
    "Process",
    "Runnable",
    "StartChannelsService",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
