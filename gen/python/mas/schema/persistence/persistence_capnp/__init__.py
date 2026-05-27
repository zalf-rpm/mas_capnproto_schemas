# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `persistence.capnp`."""

from __future__ import annotations

# Load schemas and build module structure
from importlib import import_module
from typing import cast

from capnp.lib.capnp import SchemaLoader, _InterfaceModule, _StructModule


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

VatId = _StructModule(
    _loader.get(0xE10A5D74D58BD18D).as_struct(),
    "VatId",
)
Address = _StructModule(
    _loader.get(0xFB47810671A05B0D).as_struct(),
    "Address",
)
VatPath = _StructModule(
    _loader.get(0xD9ECCDF2DBC48087).as_struct(),
    "VatPath",
)
SturdyRef = _StructModule(
    _loader.get(0x886D68271D83DE4D).as_struct(),
    "SturdyRef",
)
SturdyRef.Owner = _StructModule(
    _loader.get(0xFDD799ED60C87723).as_struct(),
    "Owner",
)
SturdyRef.Token = _StructModule(
    SturdyRef.schema.fields["localRef"].schema,
    "Token",
)
Heartbeat = _InterfaceModule(
    _loader.get(0x9FB3BDFAD147CA3A).as_interface(),
    "Heartbeat",
)
Persistent = _InterfaceModule(
    _loader.get(0xC1A7DAA0DC36CB65).as_interface(),
    "Persistent",
)
Persistent.SaveParams = _StructModule(
    _loader.get(0xD5E0AAC4225E0343).as_struct(),
    "SaveParams",
)
Persistent.SaveResults = _StructModule(
    _loader.get(0xDC5BD1EF982CEC13).as_struct(),
    "SaveResults",
)
Persistent.ReleaseSturdyRef = _InterfaceModule(
    _loader.get(0x8F700F81169F2E52).as_interface(),
    "ReleaseSturdyRef",
)
Restorer = _InterfaceModule(
    _loader.get(0x9FB6218427D92E3C).as_interface(),
    "Restorer",
)
Restorer.RestoreParams = _StructModule(
    _loader.get(0xC541E5764A37D73A).as_struct(),
    "RestoreParams",
)
HostPortResolver = _InterfaceModule(
    _loader.get(0xAA8D91FAB6D01D9F).as_interface(),
    "HostPortResolver",
)
HostPortResolver.Registrar = _InterfaceModule(
    _loader.get(0xB0CAF775704690B2).as_interface(),
    "Registrar",
)
HostPortResolver.Registrar.RegisterParams = _StructModule(
    HostPortResolver.Registrar.schema.methods["register"].param_type,  # pyright: ignore[reportUnknownArgumentType]
    "RegisterParams",
)
Gateway = _InterfaceModule(
    _loader.get(0x8F9C2C0A602F27ED).as_interface(),
    "Gateway",
)
Gateway.RegResults = _StructModule(
    Gateway.schema.methods["register"].result_type,  # pyright: ignore[reportUnknownArgumentType]
    "RegResults",
)
GatewayRegistrable = _InterfaceModule(
    _loader.get(0x8253222FDF37608D).as_interface(),
    "GatewayRegistrable",
)
