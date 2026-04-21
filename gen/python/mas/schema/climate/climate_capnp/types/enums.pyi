"""Enum helper aliases for `climate.capnp`."""

from typing import Literal

type AlterTimeSeriesWrapperAlterTypeEnum = int | Literal["add", "mul"]

type ElementEnum = (
    int
    | Literal[
        "tmin",
        "tavg",
        "tmax",
        "precip",
        "globrad",
        "wind",
        "sunhours",
        "cloudamount",
        "relhumid",
        "airpress",
        "vaporpress",
        "co2",
        "o3",
        "et0",
        "dewpointTemp",
        "specificHumidity",
        "snowfallFlux",
        "surfaceDownwellingLongwaveRadiation",
        "potET",
    ]
)

type GCMEnum = (
    int
    | Literal[
        "cccmaCanEsm2",
        "ichecEcEarth",
        "ipslIpslCm5AMr",
        "mirocMiroc5",
        "mpiMMpiEsmLr",
        "gfdlEsm4",
        "ipslCm6aLr",
        "mpiEsm12Hr",
        "mriEsm20",
        "ukesm10Ll",
        "gswp3W5E5",
        "mohcHadGem2Es",
    ]
)

type RCMEnum = (
    int
    | Literal[
        "clmcomCclm4817",
        "gericsRemo2015",
        "knmiRacmo22E",
        "smhiRca4",
        "clmcomBtuCclm4817",
        "mpiCscRemo2009",
        "uhohWrf361H",
    ]
)

type RCPEnum = (
    int | Literal["rcp19", "rcp26", "rcp34", "rcp45", "rcp60", "rcp70", "rcp85"]
)

type SSPEnum = int | Literal["ssp1", "ssp2", "ssp3", "ssp4", "ssp5"]

type TimeSeriesResolutionEnum = int | Literal["daily", "hourly"]
