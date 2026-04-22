"""Schema helper types for `climate.capnp`."""

from mas.schema.climate.climate_capnp.types import modules as modules

type _AlterTimeSeriesWrapperAlterTypeEnumSchema = (
    modules._AlterTimeSeriesWrapperInterfaceModule._AlterTypeEnumModule._AlterTypeSchema
)

type _AlterTimeSeriesWrapperAlteredSchema = (
    modules._AlterTimeSeriesWrapperInterfaceModule._AlteredStructModule._AlteredSchema
)

type _AlterTimeSeriesWrapperFactorySchema = modules._AlterTimeSeriesWrapperFactoryInterfaceModule._AlterTimeSeriesWrapperFactorySchema

type _AlterTimeSeriesWrapperSchema = (
    modules._AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema
)

type _CSVTimeSeriesFactoryCSVConfigSchema = (
    modules._CSVTimeSeriesFactoryInterfaceModule._CSVConfigStructModule._CSVConfigSchema
)

type _CSVTimeSeriesFactorySchema = (
    modules._CSVTimeSeriesFactoryInterfaceModule._CSVTimeSeriesFactorySchema
)

type _DatasetGetLocationsCallbackSchema = modules._DatasetInterfaceModule._GetLocationsCallbackInterfaceModule._GetLocationsCallbackSchema

type _DatasetSchema = modules._DatasetInterfaceModule._DatasetSchema

type _ElementEnumSchema = modules._ElementEnumModule._ElementSchema

type _EnsembleMemberSchema = modules._EnsembleMemberStructModule._EnsembleMemberSchema

type _GCMEnumSchema = modules._GCMEnumModule._GCMSchema

type _LocationKVSchema = modules._LocationStructModule._KVStructModule._KVSchema

type _LocationSchema = modules._LocationStructModule._LocationSchema

type _MetaPlusDataSchema = modules._MetaPlusDataStructModule._MetaPlusDataSchema

type _MetadataEntrySchema = (
    modules._MetadataStructModule._EntryStructModule._EntrySchema
)

type _MetadataInformationSchema = (
    modules._MetadataStructModule._InformationInterfaceModule._InformationSchema
)

type _MetadataSchema = modules._MetadataStructModule._MetadataSchema

type _MetadataSupportedSchema = (
    modules._MetadataStructModule._SupportedInterfaceModule._SupportedSchema
)

type _MetadataValueSchema = (
    modules._MetadataStructModule._ValueStructModule._ValueSchema
)

type _RCMEnumSchema = modules._RCMEnumModule._RCMSchema

type _RCPEnumSchema = modules._RCPEnumModule._RCPSchema

type _SSPEnumSchema = modules._SSPEnumModule._SSPSchema

type _ServiceSchema = modules._ServiceInterfaceModule._ServiceSchema

type _TimeSeriesDataSchema = modules._TimeSeriesDataStructModule._TimeSeriesDataSchema

type _TimeSeriesResolutionEnumSchema = (
    modules._TimeSeriesInterfaceModule._ResolutionEnumModule._ResolutionSchema
)
