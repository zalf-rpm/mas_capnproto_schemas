"""Runtime placeholder module for module helper types of `yieldstat.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _StructModule


class _RestInputStructModule(_StructModule):
    pass


class _ResultStructModule(_StructModule):
    class _ResultToValueStructModule(_StructModule):
        pass


class _OutputStructModule(_StructModule):
    class _YearToResultStructModule(_StructModule):
        pass
