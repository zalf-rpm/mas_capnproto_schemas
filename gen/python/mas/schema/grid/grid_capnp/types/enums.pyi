"""Enum helper aliases for `grid.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import _DynamicEnum

class AggregationValue(_DynamicEnum):
    @override
    def __str__(
        self,
    ) -> Literal[
        "none",
        "wAvg",
        "wMedian",
        "min",
        "max",
        "sum",
        "iAvg",
        "iMedian",
        "avg",
        "median",
        "wSum",
        "iSum",
        "wMin",
        "iMin",
        "wMax",
        "iMax",
    ]: ...

type AggregationEnum = (
    int
    | Literal[
        "none",
        "wAvg",
        "wMedian",
        "min",
        "max",
        "sum",
        "iAvg",
        "iMedian",
        "avg",
        "median",
        "wSum",
        "iSum",
        "wMin",
        "iMin",
        "wMax",
        "iMax",
    ]
)
