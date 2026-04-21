"""Runtime placeholder module for module helper types of `registry.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _AdminInterfaceModule(_InterfaceModule):
    pass


class _RegistryInterfaceModule(_InterfaceModule):
    class _EntryStructModule(_StructModule):
        pass


class _RegistrarInterfaceModule(_InterfaceModule):
    class _CrossDomainRestoreStructModule(_StructModule):
        pass

    class _RegParamsStructModule(_StructModule):
        pass

    class _UnregisterInterfaceModule(_InterfaceModule):
        pass
