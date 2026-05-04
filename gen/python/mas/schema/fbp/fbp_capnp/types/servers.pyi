"""Server helper types for `fbp.capnp`."""

from mas.schema.fbp.fbp_capnp.types import modules as modules

ChannelServer = modules._ChannelInterfaceModule.Server

DisconnectServer = modules._ProcessInterfaceModule._DisconnectInterfaceModule.Server

FactoryServer = modules._ProcessInterfaceModule._FactoryInterfaceModule.Server

ProcessServer = modules._ProcessInterfaceModule.Server

ReaderServer = modules._ChannelInterfaceModule._ReaderInterfaceModule.Server

RunnableServer = modules._RunnableInterfaceModule.Server

StartChannelsServiceServer = modules._StartChannelsServiceInterfaceModule.Server

StateTransitionServer = (
    modules._ProcessInterfaceModule._StateTransitionInterfaceModule.Server
)

StatsCallbackServer = (
    modules._ChannelInterfaceModule._StatsCallbackInterfaceModule.Server
)

StoppedCallbackServer = (
    modules._RunnableInterfaceModule._StoppedCallbackInterfaceModule.Server
)

UnregisterServer = modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server

WriterServer = modules._ChannelInterfaceModule._WriterInterfaceModule.Server
