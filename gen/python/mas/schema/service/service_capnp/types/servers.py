"""Runtime placeholder module for server helpers of `service.capnp`."""

from .. import Admin, Factory, SimpleFactory, Stoppable

AdminServer = Admin.Server
FactoryServer = Factory.Server
SimpleFactoryServer = SimpleFactory.Server
StoppableServer = Stoppable.Server
