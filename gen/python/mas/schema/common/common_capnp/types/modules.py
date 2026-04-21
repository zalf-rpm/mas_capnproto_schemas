"""Runtime placeholder module for module helper types of `common.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _IdInformationStructModule(_StructModule):
    pass


class _IdentifiableInterfaceModule(_InterfaceModule):
    pass


class _StructuredTextStructModule(_StructModule):
    pass


class _ValueStructModule(_StructModule):
    pass


class _FactoryInterfaceModule(_InterfaceModule):
    pass


class _IOFactoryInterfaceModule(_InterfaceModule):
    pass


class _PairStructModule(_StructModule):
    pass


class _HolderInterfaceModule(_InterfaceModule):
    pass


class _IdentifiableHolderInterfaceModule(_InterfaceModule):
    pass
