"""Runtime placeholder module for server helpers of `service.capnp`."""

# pyright: reportUnusedClass=none

from .. import Admin, Factory, SimpleFactory, Stoppable

AdminServer = Admin.Server
FactoryServer = Factory.Server
SimpleFactoryServer = SimpleFactory.Server
StoppableServer = Stoppable.Server
