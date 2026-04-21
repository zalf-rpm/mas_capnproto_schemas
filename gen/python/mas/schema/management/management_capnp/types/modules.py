"""Runtime placeholder module for module helper types of `management.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _EventStructModule(_StructModule):
    class _TypeStructModule(_StructModule):
        pass


class _ParamsStructModule(_StructModule):
    class _SowingStructModule(_StructModule):
        pass

    class _AutomaticSowingStructModule(_StructModule):
        class _AvgSoilTempStructModule(_StructModule):
            pass

    class _HarvestStructModule(_StructModule):
        class _OptCarbonMgmtDataStructModule(_StructModule):
            pass

    class _AutomaticHarvestStructModule(_StructModule):
        pass

    class _CuttingStructModule(_StructModule):
        class _SpecStructModule(_StructModule):
            pass

    class _MineralFertilizationStructModule(_StructModule):
        pass

    class _NDemandFertilizationStructModule(_StructModule):
        pass

    class _OrganicFertilizationStructModule(_StructModule):
        pass

    class _TillageStructModule(_StructModule):
        pass

    class _IrrigationStructModule(_StructModule):
        pass


class _NutrientStructModule(_StructModule):
    pass


class _FertilizerInterfaceModule(_InterfaceModule):
    pass


class _FertilizerServiceInterfaceModule(_InterfaceModule):
    pass


class _ServiceInterfaceModule(_InterfaceModule):
    pass
