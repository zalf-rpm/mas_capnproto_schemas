"""Runtime placeholder module for module helper types of `soil.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _LayerStructModule(_StructModule):
    class _PropertyStructModule(_StructModule):
        pass


class _QueryStructModule(_StructModule):
    class _ResultStructModule(_StructModule):
        pass


class _ProfileDataStructModule(_StructModule):
    pass


class _ProfileInterfaceModule(_InterfaceModule):
    pass


class _ServiceInterfaceModule(_InterfaceModule):
    class _StreamInterfaceModule(_InterfaceModule):
        pass
