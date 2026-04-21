"""Enum helper aliases for `management.capnp`."""

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

type NutrientNameEnum = (
    int
    | Literal[
        "urea",
        "ammonia",
        "nitrate",
        "phosphorus",
        "potassium",
        "sulfate",
        "organicC",
        "organicN",
        "organicP",
        "organicNFast",
        "organicNSlow",
    ]
)

type NutrientUnitEnum = int | Literal["none", "fraction", "percent"]

type ParamsCuttingCLEnum = int | Literal["cut", "left"]

type ParamsCuttingUnitEnum = int | Literal["percentage", "biomass", "lai"]

type ParamsHarvestCropUsageEnum = int | Literal["greenManure", "biomassProduction"]

type PlantOrganEnum = int | Literal["root", "leaf", "shoot", "fruit", "strukt", "sugar"]
