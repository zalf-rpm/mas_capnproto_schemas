# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `field_exp_data.capnp`."""

from __future__ import annotations

# Load schemas and build module structure
from importlib import import_module
from typing import cast

from capnp.lib.capnp import SchemaLoader, _StructModule


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

WeatherStation = _StructModule(
    _loader.get(0xBFA2D703516408B8).as_struct(),
    "WeatherStation",
)
SoilMetadata = _StructModule(
    _loader.get(0x86836F1366E5F73F).as_struct(),
    "SoilMetadata",
)
Field = _StructModule(
    _loader.get(0xC158BD732092CDE5).as_struct(),
    "Field",
)
ExperimentDescription = _StructModule(
    _loader.get(0x9D795A72A27F67D7).as_struct(),
    "ExperimentDescription",
)
Treatment = _StructModule(
    _loader.get(0xFF1381363C7ABD06).as_struct(),
    "Treatment",
)
Cultivar = _StructModule(
    _loader.get(0xAB7EA2BFA7965AF8).as_struct(),
    "Cultivar",
)
Plot = _StructModule(
    _loader.get(0xA7A2210FB1E289F2).as_struct(),
    "Plot",
)
InitialConditionsLayer = _StructModule(
    _loader.get(0xD1C0BC9F5B332A6E).as_struct(),
    "InitialConditionsLayer",
)
PlantingEvent = _StructModule(
    _loader.get(0xF6B17C769768D8FF).as_struct(),
    "PlantingEvent",
)
HarvestEvent = _StructModule(
    _loader.get(0x97EB30DBCF87911A).as_struct(),
    "HarvestEvent",
)
IrrigationEvent = _StructModule(
    _loader.get(0xCF2547B626594655).as_struct(),
    "IrrigationEvent",
)
FertilizerEvent = _StructModule(
    _loader.get(0xA5DF81BAE928E6DA).as_struct(),
    "FertilizerEvent",
)
Residue = _StructModule(
    _loader.get(0xE82432F4EF15A586).as_struct(),
    "Residue",
)
EnvironmentModification = _StructModule(
    _loader.get(0xB52867725B843050).as_struct(),
    "EnvironmentModification",
)
MixedType = _StructModule(
    _loader.get(0xA23434CC8F8D6A77).as_struct(),
    "MixedType",
)
