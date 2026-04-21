"""Schema helper types for `service.capnp`."""

from mas.schema.service.service_capnp.types import modules as modules

type _AdminSchema = modules._AdminInterfaceModule._AdminSchema

type _FactoryAccessInfoSchema = (
    modules._FactoryInterfaceModule._AccessInfoStructModule._AccessInfoSchema
)

type _FactoryCreateParamsSchema = (
    modules._FactoryInterfaceModule._CreateParamsStructModule._CreateParamsSchema
)

type _FactorySchema = modules._FactoryInterfaceModule._FactorySchema

type _SimpleFactorySchema = modules._SimpleFactoryInterfaceModule._SimpleFactorySchema
