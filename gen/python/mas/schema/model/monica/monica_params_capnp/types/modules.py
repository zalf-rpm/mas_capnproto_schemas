"""Runtime placeholder module for module helper types of `monica_params.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _StructModule


class _CropSpecStructModule(_StructModule):
    pass


class _CropParametersStructModule(_StructModule):
    pass


class _SpeciesParametersStructModule(_StructModule):
    pass


class _CultivarParametersStructModule(_StructModule):
    pass


class _YieldComponentStructModule(_StructModule):
    pass


class _AutomaticHarvestParametersStructModule(_StructModule):
    pass


class _NMinCropParametersStructModule(_StructModule):
    pass


class _NMinApplicationParametersStructModule(_StructModule):
    pass


class _CropResidueParametersStructModule(_StructModule):
    pass


class _SoilParametersStructModule(_StructModule):
    pass


class _AutomaticIrrigationParametersStructModule(_StructModule):
    pass


class _SiteParametersStructModule(_StructModule):
    pass


class _EnvironmentParametersStructModule(_StructModule):
    class _YearToValueStructModule(_StructModule):
        pass


class _MeasuredGroundwaterTableInformationStructModule(_StructModule):
    class _DateToValueStructModule(_StructModule):
        pass


class _SimulationParametersStructModule(_StructModule):
    pass


class _CropModuleParametersStructModule(_StructModule):
    pass


class _SoilMoistureModuleParametersStructModule(_StructModule):
    pass


class _SoilOrganicModuleParametersStructModule(_StructModule):
    pass


class _SoilTemperatureModuleParametersStructModule(_StructModule):
    pass


class _SoilTransportModuleParametersStructModule(_StructModule):
    pass


class _VocStructModule(_StructModule):
    class _EmissionsStructModule(_StructModule):
        class _SpeciesIdToEmissionStructModule(_StructModule):
            pass

    class _SpeciesDataStructModule(_StructModule):
        pass

    class _CPDataStructModule(_StructModule):
        pass

    class _MicroClimateDataStructModule(_StructModule):
        pass

    class _PhotosynthTStructModule(_StructModule):
        pass

    class _FoliageTStructModule(_StructModule):
        pass

    class _EnzymeActivityTStructModule(_StructModule):
        pass

    class _LeafEmissionTStructModule(_StructModule):
        pass

    class _LeafEmissionsStructModule(_StructModule):
        pass


class _SticsParametersStructModule(_StructModule):
    pass
