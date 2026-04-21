"""Runtime placeholder module for module helper types of `fbp.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _IPStructModule(_StructModule):
    class _KVStructModule(_StructModule):
        pass


class _IIPStructModule(_StructModule):
    pass


class _ChannelInterfaceModule(_InterfaceModule):
    class _MsgStructModule(_StructModule):
        pass

    class _StartupInfoStructModule(_StructModule):
        pass

    class _ReaderInterfaceModule(_InterfaceModule):
        pass

    class _WriterInterfaceModule(_InterfaceModule):
        pass

    class _StatsCallbackInterfaceModule(_InterfaceModule):
        class _StatsStructModule(_StructModule):
            pass

        class _UnregisterInterfaceModule(_InterfaceModule):
            pass


class _StartChannelsServiceInterfaceModule(_InterfaceModule):
    class _ParamsStructModule(_StructModule):
        pass


class _PortInfosStructModule(_StructModule):
    class _NameAndSRStructModule(_StructModule):
        pass


class _ComponentStructModule(_StructModule):
    class _PortStructModule(_StructModule):
        pass


class _RunnableInterfaceModule(_InterfaceModule):
    class _FactoryInterfaceModule(_InterfaceModule):
        pass

    class _StoppedCallbackInterfaceModule(_InterfaceModule):
        pass


class _ProcessInterfaceModule(_InterfaceModule):
    class _FactoryInterfaceModule(_InterfaceModule):
        pass

    class _ConfigEntryStructModule(_StructModule):
        pass

    class _StateTransitionInterfaceModule(_InterfaceModule):
        pass
