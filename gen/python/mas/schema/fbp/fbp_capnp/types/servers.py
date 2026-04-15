"""Runtime placeholder module for server helpers of `fbp.capnp`."""

from .. import Channel, Process, Runnable, StartChannelsService

ChannelServer = Channel.Server
FactoryServer = Process.Factory.Server
ProcessServer = Process.Server
ReaderServer = Channel.Reader.Server
RunnableServer = Runnable.Server
StartChannelsServiceServer = StartChannelsService.Server
StateTransitionServer = Process.StateTransition.Server
StatsCallbackServer = Channel.StatsCallback.Server
StoppedCallbackServer = Runnable.StoppedCallback.Server
UnregisterServer = Channel.StatsCallback.Unregister.Server
WriterServer = Channel.Writer.Server
