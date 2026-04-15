"""This is an automatically generated stub for `climate.capnp`."""

from . import types as types

class _GCMEnumModule:
    cccmaCanEsm2: int
    ichecEcEarth: int
    ipslIpslCm5AMr: int
    mirocMiroc5: int
    mpiMMpiEsmLr: int
    gfdlEsm4: int
    ipslCm6aLr: int
    mpiEsm12Hr: int
    mriEsm20: int
    ukesm10Ll: int
    gswp3W5E5: int
    mohcHadGem2Es: int

class _RCMEnumModule:
    clmcomCclm4817: int
    gericsRemo2015: int
    knmiRacmo22E: int
    smhiRca4: int
    clmcomBtuCclm4817: int
    mpiCscRemo2009: int
    uhohWrf361H: int

class _SSPEnumModule:
    ssp1: int
    ssp2: int
    ssp3: int
    ssp4: int
    ssp5: int

class _RCPEnumModule:
    rcp19: int
    rcp26: int
    rcp34: int
    rcp45: int
    rcp60: int
    rcp70: int
    rcp85: int

EnsembleMember: types.modules._EnsembleMemberStructModule

Metadata: types.modules._MetadataStructModule

class _ElementEnumModule:
    tmin: int
    tavg: int
    tmax: int
    precip: int
    globrad: int
    wind: int
    sunhours: int
    cloudamount: int
    relhumid: int
    airpress: int
    vaporpress: int
    co2: int
    o3: int
    et0: int
    dewpointTemp: int
    specificHumidity: int
    snowfallFlux: int
    surfaceDownwellingLongwaveRadiation: int
    potET: int

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
    "AlterTimeSeriesWrapper",
    "AlterTimeSeriesWrapperFactory",
    "CSVTimeSeriesFactory",
    "Dataset",
    "EnsembleMember",
    "Location",
    "MetaPlusData",
    "Metadata",
    "Service",
    "TimeSeries",
    "TimeSeriesData",
    "types",
]
