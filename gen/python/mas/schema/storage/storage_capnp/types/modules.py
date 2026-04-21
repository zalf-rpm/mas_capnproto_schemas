"""Runtime placeholder module for module helper types of `storage.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _StoreInterfaceModule(_InterfaceModule):
    class _ContainerInterfaceModule(_InterfaceModule):
        class _EntryInterfaceModule(_InterfaceModule):
            class _ValueStructModule(_StructModule):
                pass

        class _KeyAndEntryStructModule(_StructModule):
            pass

    class _InfoAndContainerStructModule(_StructModule):
        pass

    class _ImportExportDataStructModule(_StructModule):
        pass
