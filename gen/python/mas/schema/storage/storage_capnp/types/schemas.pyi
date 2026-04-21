"""Schema helper types for `storage.capnp`."""

from mas.schema.storage.storage_capnp.types import modules as modules

type _StoreContainerEntrySchema = modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema

type _StoreContainerEntryValueSchema = modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema

type _StoreContainerKeyAndEntrySchema = modules._StoreInterfaceModule._ContainerInterfaceModule._KeyAndEntryStructModule._KeyAndEntrySchema

type _StoreContainerSchema = (
    modules._StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema
)

type _StoreImportExportDataSchema = (
    modules._StoreInterfaceModule._ImportExportDataStructModule._ImportExportDataSchema
)

type _StoreInfoAndContainerSchema = (
    modules._StoreInterfaceModule._InfoAndContainerStructModule._InfoAndContainerSchema
)

type _StoreSchema = modules._StoreInterfaceModule._StoreSchema
