"""Runtime placeholder module for module helper types of `monica_management.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _ILRDatesStructModule(_StructModule):
    pass


class _EventStructModule(_StructModule):
    class _TypeStructModule(_StructModule):
        pass


class _ParamsStructModule(_StructModule):
    class _DailyWeatherStructModule(_StructModule):
        class _KVStructModule(_StructModule):
            pass

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
        class _ParametersStructModule(_StructModule):
            pass

    class _NDemandFertilizationStructModule(_StructModule):
        pass

    class _OrganicFertilizationStructModule(_StructModule):
        class _OrganicMatterParametersStructModule(_StructModule):
            pass

        class _ParametersStructModule(_StructModule):
            pass

    class _TillageStructModule(_StructModule):
        pass

    class _IrrigationStructModule(_StructModule):
        class _ParametersStructModule(_StructModule):
            pass

    class _SaveStateStructModule(_StructModule):
        pass


class _ServiceInterfaceModule(_InterfaceModule):
    pass
