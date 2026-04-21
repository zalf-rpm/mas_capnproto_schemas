"""Runtime placeholder module for server helpers of `common.capnp`."""

# pyright: reportUnusedClass=none

from .. import Factory, Holder, Identifiable, IdentifiableHolder, IOFactory

FactoryServer = Factory.Server
HolderServer = Holder.Server
IOFactoryServer = IOFactory.Server
IdentifiableHolderServer = IdentifiableHolder.Server
IdentifiableServer = Identifiable.Server
