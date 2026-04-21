"""Schema helper types for `model.capnp`."""

from mas.schema.model.model_capnp.types import modules as modules

type _ClimateInstanceSchema = (
    modules._ClimateInstanceInterfaceModule._ClimateInstanceSchema
)

type _EnvInstanceProxySchema = (
    modules._EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema
)

type _EnvInstanceProxyUnregisterSchema = modules._EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule._UnregisterSchema

type _EnvSchema = modules._EnvStructModule._EnvSchema

type _InstanceFactorySchema = (
    modules._InstanceFactoryInterfaceModule._InstanceFactorySchema
)

type _StatSchema = modules._StatStructModule._StatSchema

type _XYPlusResultSchema = modules._XYPlusResultStructModule._XYPlusResultSchema

type _XYResultSchema = modules._XYResultStructModule._XYResultSchema
