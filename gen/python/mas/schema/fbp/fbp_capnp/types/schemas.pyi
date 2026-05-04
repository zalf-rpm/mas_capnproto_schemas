"""Schema helper types for `fbp.capnp`."""

from mas.schema.fbp.fbp_capnp.types import modules as modules

type _ChannelCloseSemanticsEnumSchema = (
    modules._ChannelInterfaceModule._CloseSemanticsEnumModule._CloseSemanticsSchema
)

type _ChannelMsgSchema = modules._ChannelInterfaceModule._MsgStructModule._MsgSchema

type _ChannelReaderSchema = (
    modules._ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema
)

type _ChannelSchema = modules._ChannelInterfaceModule._ChannelSchema

type _ChannelStartupInfoSchema = (
    modules._ChannelInterfaceModule._StartupInfoStructModule._StartupInfoSchema
)

type _ChannelStatsCallbackSchema = (
    modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._StatsCallbackSchema
)

type _ChannelStatsCallbackStatsSchema = modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._StatsStructModule._StatsSchema

type _ChannelStatsCallbackUnregisterSchema = modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule._UnregisterSchema

type _ChannelWriterSchema = (
    modules._ChannelInterfaceModule._WriterInterfaceModule._WriterSchema
)

type _ComponentComponentFactorySchema = (
    modules._ComponentStructModule._ComponentFactoryStructModule._ComponentFactorySchema
)

type _ComponentComponentTypeEnumSchema = (
    modules._ComponentStructModule._ComponentTypeEnumModule._ComponentTypeSchema
)

type _ComponentPortPortTypeEnumSchema = (
    modules._ComponentStructModule._PortStructModule._PortTypeEnumModule._PortTypeSchema
)

type _ComponentPortSchema = modules._ComponentStructModule._PortStructModule._PortSchema

type _ComponentSchema = modules._ComponentStructModule._ComponentSchema

type _IIPSchema = modules._IIPStructModule._IIPSchema

type _IPKVSchema = modules._IPStructModule._KVStructModule._KVSchema

type _IPSchema = modules._IPStructModule._IPSchema

type _IPTypeEnumSchema = modules._IPStructModule._TypeEnumModule._TypeSchema

type _PortInfosNameAndSRSchema = (
    modules._PortInfosStructModule._NameAndSRStructModule._NameAndSRSchema
)

type _PortInfosSchema = modules._PortInfosStructModule._PortInfosSchema

type _ProcessConfigEntrySchema = (
    modules._ProcessInterfaceModule._ConfigEntryStructModule._ConfigEntrySchema
)

type _ProcessDisconnectSchema = (
    modules._ProcessInterfaceModule._DisconnectInterfaceModule._DisconnectSchema
)

type _ProcessFactorySchema = (
    modules._ProcessInterfaceModule._FactoryInterfaceModule._FactorySchema
)

type _ProcessSchema = modules._ProcessInterfaceModule._ProcessSchema

type _ProcessStateEnumSchema = (
    modules._ProcessInterfaceModule._StateEnumModule._StateSchema
)

type _ProcessStateTransitionSchema = modules._ProcessInterfaceModule._StateTransitionInterfaceModule._StateTransitionSchema

type _ProcessStopModeEnumSchema = (
    modules._ProcessInterfaceModule._StopModeEnumModule._StopModeSchema
)

type _RunnableFactorySchema = (
    modules._RunnableInterfaceModule._FactoryInterfaceModule._FactorySchema
)

type _RunnableSchema = modules._RunnableInterfaceModule._RunnableSchema

type _RunnableStoppedCallbackSchema = modules._RunnableInterfaceModule._StoppedCallbackInterfaceModule._StoppedCallbackSchema

type _StartChannelsServiceParamsSchema = (
    modules._StartChannelsServiceInterfaceModule._ParamsStructModule._ParamsSchema
)

type _StartChannelsServiceSchema = (
    modules._StartChannelsServiceInterfaceModule._StartChannelsServiceSchema
)
