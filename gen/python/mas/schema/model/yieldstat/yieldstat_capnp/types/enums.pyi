"""Enum helper aliases for `yieldstat.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import _DynamicEnum

class ResultIdValue(_DynamicEnum):
    @override
    def __str__(
        self,
    ) -> Literal[
        "primaryYield",
        "dryMatter",
        "carbonInAboveGroundBiomass",
        "sumFertilizer",
        "sumIrrigation",
        "primaryYieldCU",
    ]: ...

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
