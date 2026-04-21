"""Server helper types for `common.capnp`."""

from mas.schema.common.common_capnp.types import modules as modules

FactoryServer = modules._FactoryInterfaceModule.Server

HolderServer = modules._HolderInterfaceModule.Server

IOFactoryServer = modules._IOFactoryInterfaceModule.Server

IdentifiableHolderServer = modules._IdentifiableHolderInterfaceModule.Server

IdentifiableServer = modules._IdentifiableInterfaceModule.Server
