"""Server helper types for `service.capnp`."""

from mas.schema.service.service_capnp.types import modules as modules

AdminServer = modules._AdminInterfaceModule.Server

FactoryServer = modules._FactoryInterfaceModule.Server

SimpleFactoryServer = modules._SimpleFactoryInterfaceModule.Server

StoppableServer = modules._StoppableInterfaceModule.Server
