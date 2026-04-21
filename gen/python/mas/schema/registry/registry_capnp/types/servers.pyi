"""Server helper types for `registry.capnp`."""

from mas.schema.registry.registry_capnp.types import modules as modules

AdminServer = modules._AdminInterfaceModule.Server

RegistrarServer = modules._RegistrarInterfaceModule.Server

RegistryServer = modules._RegistryInterfaceModule.Server

UnregisterServer = modules._RegistrarInterfaceModule._UnregisterInterfaceModule.Server
