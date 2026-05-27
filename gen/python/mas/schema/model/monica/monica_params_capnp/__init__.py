# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `monica_params.capnp`."""

from __future__ import annotations

# Load schemas and build module structure
from importlib import import_module
from typing import cast

from capnp.lib.capnp import SchemaLoader, _EnumModule, _StructModule


def _import_schema_bundle() -> object:
    bundle_module_name = "_capnp_schema_bundle_65374570872b"
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

CropSpec = _StructModule(
    _loader.get(0xA74F5574681F9D55).as_struct(),
    "CropSpec",
)
CropParameters = _StructModule(
    _loader.get(0x8AC5CFB21988C168).as_struct(),
    "CropParameters",
)
SpeciesParameters = _StructModule(
    _loader.get(0xD2D587C796186E8B).as_struct(),
    "SpeciesParameters",
)
CultivarParameters = _StructModule(
    _loader.get(0xF206F12E39AB7F9B).as_struct(),
    "CultivarParameters",
)
YieldComponent = _StructModule(
    _loader.get(0xDBFE301C0DDEFE4E).as_struct(),
    "YieldComponent",
)
AutomaticHarvestParameters = _StructModule(
    _loader.get(0xC5F724BD00C2F628).as_struct(),
    "AutomaticHarvestParameters",
)
AutomaticHarvestParameters.HarvestTime = _EnumModule(
    AutomaticHarvestParameters.schema.fields["harvestTime"].schema,
    "HarvestTime",
)
NMinCropParameters = _StructModule(
    _loader.get(0xEA9236083718FDC2).as_struct(),
    "NMinCropParameters",
)
NMinApplicationParameters = _StructModule(
    _loader.get(0xDE7576C640B5AD18).as_struct(),
    "NMinApplicationParameters",
)
CropResidueParameters = _StructModule(
    _loader.get(0x8491DC2C2F94F1D1).as_struct(),
    "CropResidueParameters",
)
SoilParameters = _StructModule(
    _loader.get(0xB42137D4B8BA3EF6).as_struct(),
    "SoilParameters",
)
AutomaticIrrigationParameters = _StructModule(
    _loader.get(0x8890F17A143C6896).as_struct(),
    "AutomaticIrrigationParameters",
)
SiteParameters = _StructModule(
    _loader.get(0xB599BBD2F1465F9C).as_struct(),
    "SiteParameters",
)
EnvironmentParameters = _StructModule(
    _loader.get(0xC0FF4A277CA4BE0A).as_struct(),
    "EnvironmentParameters",
)
EnvironmentParameters.YearToValue = _StructModule(
    EnvironmentParameters.schema.fields["atmosphericCO2s"].schema.elementType,
    "YearToValue",
)
MeasuredGroundwaterTableInformation = _StructModule(
    _loader.get(0xC1092D6C4C110E29).as_struct(),
    "MeasuredGroundwaterTableInformation",
)
MeasuredGroundwaterTableInformation.DateToValue = _StructModule(
    MeasuredGroundwaterTableInformation.schema.fields[
        "groundwaterInfo"
    ].schema.elementType,
    "DateToValue",
)
SimulationParameters = _StructModule(
    _loader.get(0xFFAC0FA5C7156A5D).as_struct(),
    "SimulationParameters",
)
CropModuleParameters = _StructModule(
    _loader.get(0xE4D6D0D9AE1553DA).as_struct(),
    "CropModuleParameters",
)
SoilMoistureModuleParameters = _StructModule(
    _loader.get(0xCDFF1B0306EA58CF).as_struct(),
    "SoilMoistureModuleParameters",
)
SoilOrganicModuleParameters = _StructModule(
    _loader.get(0xB3E73F8C19AFD787).as_struct(),
    "SoilOrganicModuleParameters",
)
SoilTemperatureModuleParameters = _StructModule(
    _loader.get(0xF0C41D021228D929).as_struct(),
    "SoilTemperatureModuleParameters",
)
SoilTransportModuleParameters = _StructModule(
    _loader.get(0xC5CB65E585742338).as_struct(),
    "SoilTransportModuleParameters",
)
Voc = _StructModule(
    _loader.get(0xB87956E2953771DB).as_struct(),
    "Voc",
)
Voc.Emissions = _StructModule(
    _loader.get(0xD9ED2C1C754D683E).as_struct(),
    "Emissions",
)
Voc.Emissions.SpeciesIdToEmission = _StructModule(
    Voc.Emissions.schema.fields["speciesIdToIsopreneEmission"].schema.elementType,
    "SpeciesIdToEmission",
)
Voc.SpeciesData = _StructModule(
    _loader.get(0x80D5A7B782142E87).as_struct(),
    "SpeciesData",
)
Voc.CPData = _StructModule(
    _loader.get(0xCF0F425C8BD69FA2).as_struct(),
    "CPData",
)
Voc.MicroClimateData = _StructModule(
    _loader.get(0xF246442C7AEE0AF5).as_struct(),
    "MicroClimateData",
)
Voc.PhotosynthT = _StructModule(
    _loader.get(0xF95DB11410E33EFC).as_struct(),
    "PhotosynthT",
)
Voc.FoliageT = _StructModule(
    _loader.get(0xEE0B04CC3F52F33C).as_struct(),
    "FoliageT",
)
Voc.EnzymeActivityT = _StructModule(
    _loader.get(0xC281C6E5BE483337).as_struct(),
    "EnzymeActivityT",
)
Voc.LeafEmissionT = _StructModule(
    _loader.get(0xE82D760B257DADDB).as_struct(),
    "LeafEmissionT",
)
Voc.LeafEmissions = _StructModule(
    _loader.get(0xC8AEB5222AC5EF40).as_struct(),
    "LeafEmissions",
)
SticsParameters = _StructModule(
    _loader.get(0xCE5B0091FD9ACB21).as_struct(),
    "SticsParameters",
)
