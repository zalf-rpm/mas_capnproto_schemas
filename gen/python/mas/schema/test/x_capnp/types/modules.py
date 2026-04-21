"""Runtime placeholder module for module helper types of `x.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _SStructModule(_StructModule):
    pass


class _XInterfaceModule(_InterfaceModule):
    pass


class _YInterfaceModule(_InterfaceModule):
    pass


class _ZInterfaceModule(_InterfaceModule):
    pass
