"""Enum helper aliases for `monica_management.capnp`."""

from typing import Literal

type EventExternalTypeEnum = (
    int
    | Literal[
        "sowing",
        "automaticSowing",
        "harvest",
        "automaticHarvest",
        "irrigation",
        "tillage",
        "organicFertilization",
        "mineralFertilization",
        "nDemandFertilization",
        "cutting",
        "setValue",
        "saveState",
        "weather",
    ]
)

type EventPhenoStageEnum = (
    int | Literal["emergence", "flowering", "anthesis", "maturity"]
)

type EventTypeEnum = (
    int
    | Literal[
        "sowing",
        "automaticSowing",
        "harvest",
        "automaticHarvest",
        "irrigation",
        "tillage",
        "organicFertilization",
        "mineralFertilization",
        "nDemandFertilization",
        "cutting",
        "setValue",
        "saveState",
    ]
)

type ParamsCuttingCLEnum = int | Literal["cut", "left"]

type ParamsCuttingUnitEnum = int | Literal["percentage", "biomass", "lai"]

type ParamsHarvestCropUsageEnum = int | Literal["greenManure", "biomassProduction"]

type PlantOrganEnum = int | Literal["root", "leaf", "shoot", "fruit", "strukt", "sugar"]
