"""Runtime placeholder module for server helpers of `registry.capnp`."""

# pyright: reportUnusedClass=none

from .. import Admin, Registrar, Registry

AdminServer = Admin.Server
RegistrarServer = Registrar.Server
RegistryServer = Registry.Server
UnregisterServer = Registrar.Unregister.Server
