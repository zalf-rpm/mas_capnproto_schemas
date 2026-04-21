"""Runtime placeholder module for module helper types of `model.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _XYResultStructModule(_StructModule):
    pass


class _StatStructModule(_StructModule):
    pass


class _XYPlusResultStructModule(_StructModule):
    pass


class _ClimateInstanceInterfaceModule(_InterfaceModule):
    pass


class _EnvStructModule(_StructModule):
    pass


class _EnvInstanceInterfaceModule(_InterfaceModule):
    pass


class _EnvInstanceProxyInterfaceModule(_InterfaceModule):
    class _UnregisterInterfaceModule(_InterfaceModule):
        pass


class _InstanceFactoryInterfaceModule(_InterfaceModule):
    pass
