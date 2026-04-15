"""Runtime placeholder module for result tuple helpers of `grid.capnp`."""

from typing import NamedTuple


class ClosestvalueatResultTuple(NamedTuple):
    val: object
    tl: object
    br: object
    aggParts: object


class DimensionResultTuple(NamedTuple):
    rows: object
    cols: object


class LatlonboundsResultTuple(NamedTuple):
    tl: object
    tr: object
    br: object
    bl: object


class NodatavalueResultTuple(NamedTuple):
    nodata: object


class ResolutionResultTuple(NamedTuple):
    res: object


class StreamcellsResultTuple(NamedTuple):
    callback: object


class UnitResultTuple(NamedTuple):
    unit: object


class ValueatResultTuple(NamedTuple):
    val: object
    aggParts: object


class SendcellsResultTuple(NamedTuple):
    locations: object


__all__ = [
    "ClosestvalueatResultTuple",
    "DimensionResultTuple",
    "LatlonboundsResultTuple",
    "NodatavalueResultTuple",
    "ResolutionResultTuple",
    "SendcellsResultTuple",
    "StreamcellsResultTuple",
    "UnitResultTuple",
    "ValueatResultTuple",
]
