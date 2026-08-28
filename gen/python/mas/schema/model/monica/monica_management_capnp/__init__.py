# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `monica_management.capnp`."""

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

ILRDates = _StructModule(
    _loader.get(0xA1F99F32EEA02590).as_struct(),
    "ILRDates",
)
EventType = _EnumModule(
    _loader.get(0xD0290DAF8DE9F2B0).as_enum(),
    "EventType",
)
PlantOrgan = _EnumModule(
    _loader.get(0xB33447204CDF022C).as_enum(),
    "PlantOrgan",
)
Event = _StructModule(
    _loader.get(0xCF672AB379467704).as_struct(),
    "Event",
)
Event.ExternalType = _EnumModule(
    Event.schema.fields["type"].schema,
    "ExternalType",
)
Event.PhenoStage = _EnumModule(
    _loader.get(0xB2BF3A5557791BC1).as_enum(),
    "PhenoStage",
)
Event.Type = _StructModule(
    _loader.get(0xB91010C363E568A4).as_struct(),
    "Type",
)
Params = _StructModule(
    _loader.get(0xCB20E21466098705).as_struct(),
    "Params",
)
Params.DailyWeather = _StructModule(
    _loader.get(0xA332CFE9735A304C).as_struct(),
    "DailyWeather",
)
Params.DailyWeather.KV = _StructModule(
    Params.DailyWeather.schema.fields["data"].schema.elementType,
    "KV",
)
Params.Sowing = _StructModule(
    _loader.get(0xC6880D1C13EC14DC).as_struct(),
    "Sowing",
)
Params.AutomaticSowing = _StructModule(
    _loader.get(0xD1BFC1C9617D9453).as_struct(),
    "AutomaticSowing",
)
Params.AutomaticSowing.AvgSoilTemp = _StructModule(
    Params.AutomaticSowing.schema.fields["avgSoilTemp"].schema,
    "AvgSoilTemp",
)
Params.Harvest = _StructModule(
    _loader.get(0x8FEB941D70F2A468).as_struct(),
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
    _loader.get(0xF805D22FABB80702).as_struct(),
    "AutomaticHarvest",
)
Params.Cutting = _StructModule(
    _loader.get(0x8460DAC6ABFF7ED9).as_struct(),
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
    _loader.get(0xA363D226E178DEBD).as_struct(),
    "MineralFertilization",
)
Params.MineralFertilization.Parameters = _StructModule(
    Params.MineralFertilization.schema.fields["partition"].schema,
    "Parameters",
)
Params.NDemandFertilization = _StructModule(
    _loader.get(0xC7C14E92E0CD461C).as_struct(),
    "NDemandFertilization",
)
Params.OrganicFertilization = _StructModule(
    _loader.get(0xB492838C7FED50B0).as_struct(),
    "OrganicFertilization",
)
Params.OrganicFertilization.OrganicMatterParameters = _StructModule(
    Params.OrganicFertilization.schema.fields["params"].schema.fields["params"].schema,
    "OrganicMatterParameters",
)
Params.OrganicFertilization.Parameters = _StructModule(
    Params.OrganicFertilization.schema.fields["params"].schema,
    "Parameters",
)
Params.Tillage = _StructModule(
    _loader.get(0xAA49811A4E3E2C59).as_struct(),
    "Tillage",
)
Params.Irrigation = _StructModule(
    _loader.get(0xD90939A58E404FF8).as_struct(),
    "Irrigation",
)
Params.Irrigation.Parameters = _StructModule(
    Params.Irrigation.schema.fields["params"].schema,
    "Parameters",
)
Params.SaveState = _StructModule(
    _loader.get(0xDD84803FC87AC648).as_struct(),
    "SaveState",
)
Service = _InterfaceModule(
    _loader.get(0xBFDA1920AFF38C07).as_interface(),
    "Service",
)
