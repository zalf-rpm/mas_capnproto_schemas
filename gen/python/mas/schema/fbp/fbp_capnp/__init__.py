# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `fbp.capnp`."""

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

IP = _StructModule(
    _loader.get(0xAF0A1DC4709A5CCF).as_struct(),
    "IP",
)
IP.KV = _StructModule(
    IP.schema.fields["attributes"].schema.elementType,
    "KV",
)
IP.Type = _EnumModule(
    IP.schema.fields["type"].schema,
    "Type",
)
IP.ChunkedData = _StructModule(
    _loader.get(0xD9377FA82178A561).as_struct(),
    "ChunkedData",
)
IP.SysAttributes = _StructModule(
    IP.schema.fields["sysAttributes"].schema,
    "SysAttributes",
)
IIP = _StructModule(
    _loader.get(0xF3705FB36D44A21F).as_struct(),
    "IIP",
)
Channel = _InterfaceModule(
    _loader.get(0x9C62C32B2FF2B1E8).as_interface(),
    "Channel",
)
Channel.CloseSemantics = _EnumModule(
    Channel.schema.methods["setAutoCloseSemantics"].param_type.fields["cs"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "CloseSemantics",
)
Channel.Msg = _StructModule(
    Channel.schema.methods["reader"]
    .result_type.fields["r"]
    .schema.methods["read"]
    .result_type,  # pyright: ignore[reportUnknownArgumentType]
    "Msg",
)
Channel.StartupInfo = _StructModule(
    _loader.get(0xE3D7A3237F175028).as_struct(),
    "StartupInfo",
)
Channel.Reader = _InterfaceModule(
    Channel.schema.methods["reader"].result_type.fields["r"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "Reader",
)
Channel.Writer = _InterfaceModule(
    Channel.schema.methods["writer"].result_type.fields["w"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "Writer",
)
Channel.StatsCallback = _InterfaceModule(
    Channel.schema.methods["registerStatsCallback"]
    .param_type.fields["callback"]
    .schema,  # pyright: ignore[reportUnknownArgumentType]
    "StatsCallback",
)
Channel.StatsCallback.Stats = _StructModule(
    Channel.StatsCallback.schema.methods["status"].param_type.fields["stats"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "Stats",
)
Channel.StatsCallback.Unregister = _InterfaceModule(
    Channel.schema.methods["registerStatsCallback"]
    .result_type.fields["unregisterCallback"]
    .schema,  # pyright: ignore[reportUnknownArgumentType]
    "Unregister",
)
StartChannelsService = _InterfaceModule(
    _loader.get(0xD0CD6D829B810229).as_interface(),
    "StartChannelsService",
)
StartChannelsService.Params = _StructModule(
    StartChannelsService.schema.methods["start"].param_type,  # pyright: ignore[reportUnknownArgumentType]
    "Params",
)
PortInfos = _StructModule(
    _loader.get(0xECE0EFA9A922D4A8).as_struct(),
    "PortInfos",
)
PortInfos.NameAndSR = _StructModule(
    PortInfos.schema.fields["inPorts"].schema.elementType,
    "NameAndSR",
)
Component = _StructModule(
    _loader.get(0xD717FF7D6815A6B0).as_struct(),
    "Component",
)
Component.ComponentType = _EnumModule(
    Component.schema.fields["type"].schema,
    "ComponentType",
)
Component.Port = _StructModule(
    Component.schema.fields["inPorts"].schema.elementType,
    "Port",
)
Component.Port.PortType = _EnumModule(
    Component.Port.schema.fields["type"].schema,
    "PortType",
)
Runnable = _InterfaceModule(
    _loader.get(0xBDE616D300754FF0).as_interface(),
    "Runnable",
)
Runnable.Factory = _InterfaceModule(
    _loader.get(0xF5694DB406AA9975).as_interface(),
    "Factory",
)
Runnable.StoppedCallback = _InterfaceModule(
    Runnable.schema.methods["start"].param_type.fields["stoppedCb"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "StoppedCallback",
)
Process = _InterfaceModule(
    _loader.get(0xBBAD56943A039783).as_interface(),
    "Process",
)
Process.Factory = _InterfaceModule(
    _loader.get(0xB01652AB8F1AC0D3).as_interface(),
    "Factory",
)
Process.ProcessHandle = _InterfaceModule(
    _loader.get(0xE6869481A867614F).as_interface(),
    "ProcessHandle",
)
Process.Disconnect = _InterfaceModule(
    Process.schema.methods["connectInPort"].result_type.fields["disconnect"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "Disconnect",
)
Process.ConfigEntry = _StructModule(
    Process.schema.methods["configEntries"]
    .result_type.fields["config"]
    .schema.elementType,  # pyright: ignore[reportUnknownArgumentType]
    "ConfigEntry",
)
Process.State = _EnumModule(
    Process.schema.methods["state"]
    .param_type.fields["transitionCallback"]
    .schema.methods["stateChanged"]
    .param_type.fields["old"]
    .schema,  # pyright: ignore[reportUnknownArgumentType]
    "State",
)
Process.StateTransition = _InterfaceModule(
    Process.schema.methods["state"].param_type.fields["transitionCallback"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "StateTransition",
)
Process.ActivityState = _EnumModule(
    Process.schema.methods["activity"]
    .param_type.fields["transitionCallback"]
    .schema.methods["activityChanged"]
    .param_type.fields["old"]
    .schema.fields["state"]
    .schema,  # pyright: ignore[reportUnknownArgumentType]
    "ActivityState",
)
Process.ActivityInfo = _StructModule(
    Process.schema.methods["activity"]
    .param_type.fields["transitionCallback"]
    .schema.methods["activityChanged"]
    .param_type.fields["old"]
    .schema,  # pyright: ignore[reportUnknownArgumentType]
    "ActivityInfo",
)
Process.ActivityTransition = _InterfaceModule(
    Process.schema.methods["activity"].param_type.fields["transitionCallback"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "ActivityTransition",
)
Process.RunInfo = _StructModule(
    Process.schema.methods["lastRun"].result_type.fields["info"].schema,  # pyright: ignore[reportUnknownArgumentType]
    "RunInfo",
)
Process.RunInfo.Outcome = _EnumModule(
    Process.RunInfo.schema.fields["outcome"].schema,
    "Outcome",
)
Process.RunInfo.Phase = _EnumModule(
    Process.RunInfo.schema.fields["phase"].schema,
    "Phase",
)
