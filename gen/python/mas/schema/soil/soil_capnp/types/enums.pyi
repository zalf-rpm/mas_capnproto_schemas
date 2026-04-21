"""Enum helper aliases for `soil.capnp`."""

from typing import Literal

type PropertyNameEnum = (
    int
    | Literal[
        "soilType",
        "sand",
        "clay",
        "silt",
        "pH",
        "sceleton",
        "organicCarbon",
        "organicMatter",
        "bulkDensity",
        "rawDensity",
        "fieldCapacity",
        "permanentWiltingPoint",
        "saturation",
        "soilMoisture",
        "soilWaterConductivityCoefficient",
        "ammonium",
        "nitrate",
        "cnRatio",
        "inGroundwater",
        "impenetrable",
    ]
)

type STypeEnum = int | Literal["unknown", "ka5"]
