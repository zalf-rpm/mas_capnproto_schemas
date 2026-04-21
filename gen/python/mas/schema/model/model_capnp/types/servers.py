"""Runtime placeholder module for server helpers of `model.capnp`."""

# pyright: reportUnusedClass=none

from .. import ClimateInstance, EnvInstance, EnvInstanceProxy, InstanceFactory

ClimateInstanceServer = ClimateInstance.Server
EnvInstanceProxyServer = EnvInstanceProxy.Server
EnvInstanceServer = EnvInstance.Server
InstanceFactoryServer = InstanceFactory.Server
UnregisterServer = EnvInstanceProxy.Unregister.Server
