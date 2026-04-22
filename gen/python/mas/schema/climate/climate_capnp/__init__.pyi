"""This is an automatically generated stub for `climate.capnp`."""

from mas.schema.climate.climate_capnp import types as types

GCM: types.modules._GCMEnumModule
RCM: types.modules._RCMEnumModule
SSP: types.modules._SSPEnumModule
RCP: types.modules._RCPEnumModule
EnsembleMember: types.modules._EnsembleMemberStructModule

Metadata: types.modules._MetadataStructModule
Element: types.modules._ElementEnumModule
TimeSeries: types.modules._TimeSeriesInterfaceModule
Location: types.modules._LocationStructModule

Dataset: types.modules._DatasetInterfaceModule
MetaPlusData: types.modules._MetaPlusDataStructModule
TimeSeriesData: types.modules._TimeSeriesDataStructModule
Service: types.modules._ServiceInterfaceModule
CSVTimeSeriesFactory: types.modules._CSVTimeSeriesFactoryInterfaceModule
AlterTimeSeriesWrapper: types.modules._AlterTimeSeriesWrapperInterfaceModule
AlterTimeSeriesWrapperFactory: (
    types.modules._AlterTimeSeriesWrapperFactoryInterfaceModule
)

__all__ = [
    "GCM",
    "RCM",
    "RCP",
    "SSP",
    "AlterTimeSeriesWrapper",
    "AlterTimeSeriesWrapperFactory",
    "CSVTimeSeriesFactory",
    "Dataset",
    "Element",
    "EnsembleMember",
    "Location",
    "MetaPlusData",
    "Metadata",
    "Service",
    "TimeSeries",
    "TimeSeriesData",
    "types",
]
