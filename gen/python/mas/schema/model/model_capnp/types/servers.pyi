"""Server helper types for `model.capnp`."""

from mas.schema.model.model_capnp.types import modules as modules

ClimateInstanceServer = modules._ClimateInstanceInterfaceModule.Server

EnvInstanceProxyServer = modules._EnvInstanceProxyInterfaceModule.Server

EnvInstanceServer = modules._EnvInstanceInterfaceModule.Server

InstanceFactoryServer = modules._InstanceFactoryInterfaceModule.Server

UnregisterServer = (
    modules._EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
)
