"""Runtime placeholder module for server helpers of `persistence.capnp`."""

from .. import (
    Gateway,
    GatewayRegistrable,
    Heartbeat,
    HostPortResolver,
    Persistent,
    Restorer,
)

GatewayRegistrableServer = GatewayRegistrable.Server
GatewayServer = Gateway.Server
HeartbeatServer = Heartbeat.Server
HostPortResolverServer = HostPortResolver.Server
PersistentServer = Persistent.Server
RegistrarServer = HostPortResolver.Registrar.Server
ReleaseSturdyRefServer = Persistent.ReleaseSturdyRef.Server
RestorerServer = Restorer.Server
