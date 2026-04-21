"""Runtime placeholder module for module helper types of `grid.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _GridInterfaceModule(_InterfaceModule):
    class _ValueStructModule(_StructModule):
        pass

    class _ResolutionStructModule(_StructModule):
        pass

    class _RowColStructModule(_StructModule):
        pass

    class _AggregationPartStructModule(_StructModule):
        pass

    class _LocationStructModule(_StructModule):
        pass

    class _CallbackInterfaceModule(_InterfaceModule):
        pass
