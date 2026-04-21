"""Runtime placeholder module for module helper types of `monica_state.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _StructModule


class _MaybeBoolStructModule(_StructModule):
    pass


class _RuntimeStateStructModule(_StructModule):
    pass


class _CropStateStructModule(_StructModule):
    pass


class _AOMPropertiesStructModule(_StructModule):
    pass


class _SoilColumnStateStructModule(_StructModule):
    class _DelayedNMinApplicationParamsStructModule(_StructModule):
        pass


class _SoilLayerStateStructModule(_StructModule):
    pass


class _MonicaModelStateStructModule(_StructModule):
    class _ACDToValueStructModule(_StructModule):
        pass


class _CropModuleStateStructModule(_StructModule):
    pass


class _SnowModuleStateStructModule(_StructModule):
    pass


class _FrostModuleStateStructModule(_StructModule):
    pass


class _SoilMoistureModuleStateStructModule(_StructModule):
    pass


class _SoilOrganicModuleStateStructModule(_StructModule):
    pass


class _SoilTemperatureModuleStateStructModule(_StructModule):
    pass


class _SoilTransportModuleStateStructModule(_StructModule):
    pass


class _ICDataStructModule(_StructModule):
    pass
