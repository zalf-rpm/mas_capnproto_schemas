# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `management.capnp`."""

from __future__ import annotations

# Load schemas and build module structure
from importlib import import_module
from typing import cast

from capnp.lib.capnp import SchemaLoader, _EnumModule, _InterfaceModule, _StructModule


def _import_schema_bundle() -> object:
    bundle_module_name = "_capnp_schema_bundle_b45e9cb539b9"
    try:
        return import_module(bundle_module_name)
    except ModuleNotFoundError as error:
        original_error = error
        package_name = __package__

    while package_name:
        try:
            return import_module(f"{package_name}.{bundle_module_name}")
        except ModuleNotFoundError:
            package_name = package_name.rpartition(".")[0]

    raise original_error


_schema_bundle = _import_schema_bundle()


def get_schema_by_id(schema_id: int) -> object:
    return cast("object", _schema_bundle.get_schema_by_id(schema_id))


def load_capnp_file(path: str, imports: list[str] | tuple[str, ...] = ()) -> object:
    return cast("object", _schema_bundle.load_capnp_file(path, imports))


_loader: SchemaLoader = cast("SchemaLoader", _schema_bundle.get_schema_loader())

# Build module structure inline

EventType = _EnumModule(
    _loader.get(0x82A74595175B71A3).as_enum(),
    "EventType",
)
PlantOrgan = _EnumModule(
    _loader.get(0xC2D50914B83D42DE).as_enum(),
    "PlantOrgan",
)
Event = _StructModule(
    _loader.get(0x9C5DEDFD679AC842).as_struct(),
    "Event",
)
Event.ExternalType = _EnumModule(
    Event.schema.fields["type"].schema,
    "ExternalType",
)
Event.PhenoStage = _EnumModule(
    _loader.get(0x8FA09457BC1BFC34).as_enum(),
    "PhenoStage",
)
Event.Type = _StructModule(
    _loader.get(0xE1ED73D59C8CE359).as_struct(),
    "Type",
)
Params = _StructModule(
    _loader.get(0x9D247C812334C917).as_struct(),
    "Params",
)
Params.Sowing = _StructModule(
    _loader.get(0x80CE153F3BC9A9E8).as_struct(),
    "Sowing",
)
Params.AutomaticSowing = _StructModule(
    _loader.get(0xCFCF44997E7CEAB4).as_struct(),
    "AutomaticSowing",
)
Params.AutomaticSowing.AvgSoilTemp = _StructModule(
    Params.AutomaticSowing.schema.fields["avgSoilTemp"].schema,
    "AvgSoilTemp",
)
Params.Harvest = _StructModule(
    _loader.get(0xEED4E55BB04289EF).as_struct(),
    "Harvest",
)
Params.Harvest.CropUsage = _EnumModule(
    Params.Harvest.schema.fields["optCarbMgmtData"].schema.fields["cropUsage"].schema,
    "CropUsage",
)
Params.Harvest.OptCarbonMgmtData = _StructModule(
    Params.Harvest.schema.fields["optCarbMgmtData"].schema,
    "OptCarbonMgmtData",
)
Params.AutomaticHarvest = _StructModule(
    _loader.get(0xE3A37E340F816CD1).as_struct(),
    "AutomaticHarvest",
)
Params.Cutting = _StructModule(
    _loader.get(0xFEC75F2DDD43431D).as_struct(),
    "Cutting",
)
Params.Cutting.CL = _EnumModule(
    Params.Cutting.schema.fields["cuttingSpec"]
    .schema.elementType.fields["cutOrLeft"]
    .schema,
    "CL",
)
Params.Cutting.Unit = _EnumModule(
    Params.Cutting.schema.fields["cuttingSpec"]
    .schema.elementType.fields["unit"]
    .schema,
    "Unit",
)
Params.Cutting.Spec = _StructModule(
    Params.Cutting.schema.fields["cuttingSpec"].schema.elementType,
    "Spec",
)
Params.MineralFertilization = _StructModule(
    _loader.get(0xD3DA30EA7B25D921).as_struct(),
    "MineralFertilization",
)
Params.NDemandFertilization = _StructModule(
    _loader.get(0x953375AC67D4F573).as_struct(),
    "NDemandFertilization",
)
Params.OrganicFertilization = _StructModule(
    _loader.get(0xE98C76FB0FB0B2CD).as_struct(),
    "OrganicFertilization",
)
Params.Tillage = _StructModule(
    _loader.get(0x88A5848EF8603554).as_struct(),
    "Tillage",
)
Params.Irrigation = _StructModule(
    _loader.get(0x87FEB816363FF43C).as_struct(),
    "Irrigation",
)
Nutrient = _StructModule(
    _loader.get(0xAAFE4332E17AA43E).as_struct(),
    "Nutrient",
)
Nutrient.Name = _EnumModule(
    Nutrient.schema.fields["nutrient"].schema,
    "Name",
)
Nutrient.Unit = _EnumModule(
    Nutrient.schema.fields["unit"].schema,
    "Unit",
)
Fertilizer = _InterfaceModule(
    _loader.get(0x8C4CB8D60AE5AEC7).as_interface(),
    "Fertilizer",
)
FertilizerService = _InterfaceModule(
    _loader.get(0xBBB7AEAE0D097E05).as_interface(),
    "FertilizerService",
)
Service = _InterfaceModule(
    _loader.get(0xC876B729B7D7F6D9).as_interface(),
    "Service",
)
