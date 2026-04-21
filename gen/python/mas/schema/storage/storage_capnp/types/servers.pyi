"""Server helper types for `storage.capnp`."""

from mas.schema.storage.storage_capnp.types import modules as modules

ContainerServer = modules._StoreInterfaceModule._ContainerInterfaceModule.Server

EntryServer = (
    modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
)

StoreServer = modules._StoreInterfaceModule.Server
