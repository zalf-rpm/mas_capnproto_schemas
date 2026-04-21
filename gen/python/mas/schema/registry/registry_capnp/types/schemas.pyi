"""Schema helper types for `registry.capnp`."""

from mas.schema.registry.registry_capnp.types import modules as modules

type _AdminSchema = modules._AdminInterfaceModule._AdminSchema

type _RegistrarCrossDomainRestoreSchema = modules._RegistrarInterfaceModule._CrossDomainRestoreStructModule._CrossDomainRestoreSchema

type _RegistrarRegParamsSchema = (
    modules._RegistrarInterfaceModule._RegParamsStructModule._RegParamsSchema
)

type _RegistrarSchema = modules._RegistrarInterfaceModule._RegistrarSchema

type _RegistrarUnregisterSchema = (
    modules._RegistrarInterfaceModule._UnregisterInterfaceModule._UnregisterSchema
)

type _RegistryEntrySchema = (
    modules._RegistryInterfaceModule._EntryStructModule._EntrySchema
)
