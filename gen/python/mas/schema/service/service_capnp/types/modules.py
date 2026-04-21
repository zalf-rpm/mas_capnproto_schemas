"""Runtime placeholder module for module helper types of `service.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _AdminInterfaceModule(_InterfaceModule):
    pass


class _SimpleFactoryInterfaceModule(_InterfaceModule):
    pass


class _FactoryInterfaceModule(_InterfaceModule):
    class _CreateParamsStructModule(_StructModule):
        pass

    class _AccessInfoStructModule(_StructModule):
        pass


class _StoppableInterfaceModule(_InterfaceModule):
    pass
