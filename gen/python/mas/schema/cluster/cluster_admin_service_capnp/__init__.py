# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `cluster_admin_service.capnp`."""

from __future__ import annotations

# Load schemas and build module structure
from importlib import import_module
from typing import cast

from capnp.lib.capnp import SchemaLoader, _InterfaceModule, _StructModule


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

Cluster = _StructModule(
    _loader.get(0xF7485D56D6F20E7D).as_struct(),
    "Cluster",
)
Cluster.Unregister = _InterfaceModule(
    _loader.get(0xE8B1F7A192651BBE).as_interface(),
    "Unregister",
)
Cluster.AdminMaster = _InterfaceModule(
    _loader.get(0xBF24278C65F633CE).as_interface(),
    "AdminMaster",
)
Cluster.UserMaster = _InterfaceModule(
    _loader.get(0xEC42C6DF28354B60).as_interface(),
    "UserMaster",
)
Cluster.Runtime = _InterfaceModule(
    _loader.get(0xF849848FEA5C4776).as_interface(),
    "Runtime",
)
Cluster.ZmqPipelineAddresses = _StructModule(
    _loader.get(0xC9034BA2BECC2A64).as_struct(),
    "ZmqPipelineAddresses",
)
Cluster.ValueHolder = _InterfaceModule(
    _loader.get(0xD6ACF080DCF2B4C8).as_interface(),
    "ValueHolder",
)
Cluster.ModelInstanceFactory = _InterfaceModule(
    _loader.get(0xFD9959998F9F0EBE).as_interface(),
    "ModelInstanceFactory",
)
