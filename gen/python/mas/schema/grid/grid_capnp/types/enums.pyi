"""Enum helper aliases for `grid.capnp`."""

from typing import Literal

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
