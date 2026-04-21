"""Runtime placeholder module for result tuple helpers of `soil.capnp`."""

# pyright: reportUnusedClass=none

from typing import NamedTuple


class DataResultTuple(NamedTuple):
    layers: object
    percentageOfArea: object


class GeolocationResultTuple(NamedTuple):
    lat: object
    lon: object


class CheckavailableparametersResultTuple(NamedTuple):
    failed: object
    mandatory: object
    optional: object


class ClosestprofilesatResultTuple(NamedTuple):
    profiles: object


class GetallavailableparametersResultTuple(NamedTuple):
    mandatory: object
    optional: object


class StreamallprofilesResultTuple(NamedTuple):
    allProfiles: object


class NextprofilesResultTuple(NamedTuple):
    profiles: object


__all__ = [
    "CheckavailableparametersResultTuple",
    "ClosestprofilesatResultTuple",
    "DataResultTuple",
    "GeolocationResultTuple",
    "GetallavailableparametersResultTuple",
    "NextprofilesResultTuple",
    "StreamallprofilesResultTuple",
]
