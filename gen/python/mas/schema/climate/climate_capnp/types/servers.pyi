"""Server helper types for `climate.capnp`."""

from mas.schema.climate.climate_capnp.types import modules as modules

AlterTimeSeriesWrapperFactoryServer = (
    modules._AlterTimeSeriesWrapperFactoryInterfaceModule.Server
)

AlterTimeSeriesWrapperServer = modules._AlterTimeSeriesWrapperInterfaceModule.Server

CSVTimeSeriesFactoryServer = modules._CSVTimeSeriesFactoryInterfaceModule.Server

DatasetServer = modules._DatasetInterfaceModule.Server

GetLocationsCallbackServer = (
    modules._DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
)

InformationServer = modules._MetadataStructModule._InformationInterfaceModule.Server

ServiceServer = modules._ServiceInterfaceModule.Server

SupportedServer = modules._MetadataStructModule._SupportedInterfaceModule.Server

TimeSeriesServer = modules._TimeSeriesInterfaceModule.Server
