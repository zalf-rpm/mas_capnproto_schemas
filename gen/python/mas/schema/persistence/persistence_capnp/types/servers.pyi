"""Server helper types for `persistence.capnp`."""

from mas.schema.persistence.persistence_capnp.types import modules as modules

GatewayRegistrableServer = modules._GatewayRegistrableInterfaceModule.Server

GatewayServer = modules._GatewayInterfaceModule.Server

HeartbeatServer = modules._HeartbeatInterfaceModule.Server

HostPortResolverServer = modules._HostPortResolverInterfaceModule.Server

PersistentServer = modules._PersistentInterfaceModule.Server

RegistrarServer = (
    modules._HostPortResolverInterfaceModule._RegistrarInterfaceModule.Server
)

ReleaseSturdyRefServer = (
    modules._PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule.Server
)

RestorerServer = modules._RestorerInterfaceModule.Server
