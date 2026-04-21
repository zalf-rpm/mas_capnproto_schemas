"""Runtime placeholder module for module helper types of `geo.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _StructModule


class _EPSGStructModule(_StructModule):
    pass


class _UTMCoordStructModule(_StructModule):
    pass


class _LatLonCoordStructModule(_StructModule):
    pass


class _GKCoordStructModule(_StructModule):
    pass


class _Point2DStructModule(_StructModule):
    pass


class _RowColStructModule(_StructModule):
    pass


class _CoordStructModule(_StructModule):
    pass


class _RectBoundsStructModule(_StructModule):
    pass
