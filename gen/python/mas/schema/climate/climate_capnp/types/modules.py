"""Runtime placeholder module for module helper types of `climate.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _EnsembleMemberStructModule(_StructModule):
    pass


class _MetadataStructModule(_StructModule):
    class _SupportedInterfaceModule(_InterfaceModule):
        pass

    class _ValueStructModule(_StructModule):
        pass

    class _EntryStructModule(_StructModule):
        pass

    class _InformationInterfaceModule(_InterfaceModule):
        pass


class _DatasetInterfaceModule(_InterfaceModule):
    class _GetLocationsCallbackInterfaceModule(_InterfaceModule):
        pass


class _MetaPlusDataStructModule(_StructModule):
    pass


class _LocationStructModule(_StructModule):
    class _KVStructModule(_StructModule):
        pass


class _TimeSeriesInterfaceModule(_InterfaceModule):
    pass


class _TimeSeriesDataStructModule(_StructModule):
    pass


class _ServiceInterfaceModule(_InterfaceModule):
    pass


class _CSVTimeSeriesFactoryInterfaceModule(_InterfaceModule):
    class _CSVConfigStructModule(_StructModule):
        pass


class _AlterTimeSeriesWrapperInterfaceModule(_InterfaceModule):
    class _AlteredStructModule(_StructModule):
        pass


class _AlterTimeSeriesWrapperFactoryInterfaceModule(_InterfaceModule):
    pass
