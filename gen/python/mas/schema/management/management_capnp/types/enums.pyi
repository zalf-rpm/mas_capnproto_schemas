"""Enum helper aliases for `management.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import _DynamicEnum

class EventTypeValue(_DynamicEnum):
    @override
    def __str__(
        self,
    ) -> Literal[
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
    ]: ...

class PlantOrganValue(_DynamicEnum):
    @override
    def __str__(
        self,
    ) -> Literal["root", "leaf", "shoot", "fruit", "strukt", "sugar"]: ...

class EventExternalTypeValue(_DynamicEnum):
    @override
    def __str__(
        self,
    ) -> Literal[
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
    ]: ...

class EventPhenoStageValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["emergence", "flowering", "anthesis", "maturity"]: ...

class ParamsHarvestCropUsageValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["greenManure", "biomassProduction"]: ...

class ParamsCuttingCLValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["cut", "left"]: ...

class ParamsCuttingUnitValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["percentage", "biomass", "lai"]: ...

class NutrientNameValue(_DynamicEnum):
    @override
    def __str__(
        self,
    ) -> Literal[
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
    ]: ...

class NutrientUnitValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["none", "fraction", "percent"]: ...

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
