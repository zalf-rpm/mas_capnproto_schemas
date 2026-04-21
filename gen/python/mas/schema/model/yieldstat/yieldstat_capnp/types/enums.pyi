"""Enum helper aliases for `yieldstat.capnp`."""

from typing import Literal

type ResultIdEnum = (
    int
    | Literal[
        "primaryYield",
        "dryMatter",
        "carbonInAboveGroundBiomass",
        "sumFertilizer",
        "sumIrrigation",
        "primaryYieldCU",
    ]
)
