"""Runtime placeholder module for server helpers of `storage.capnp`."""

# pyright: reportUnusedClass=none

from .. import Store

ContainerServer = Store.Container.Server
EntryServer = Store.Container.Entry.Server
StoreServer = Store.Server
