"""Module helper types for `field_exp_data.capnp`."""

from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

from mas.schema.climate.climate_capnp.types.clients import TimeSeriesClient
from mas.schema.climate.climate_capnp.types.modules import _TimeSeriesInterfaceModule
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.soil.soil_capnp.types.clients import ProfileClient
from mas.schema.soil.soil_capnp.types.modules import _ProfileInterfaceModule

from . import _all as _all

class _WeatherStationStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: str | None = None,
        name: str | None = None,
        instituteName: str | None = None,
        site: str | None = None,
        country: str | None = None,
        location2ndLevel: str | None = None,
        location3rdLevel: str | None = None,
        latitudeInDecDeg: float | None = None,
        longitudeInDecDeg: float | None = None,
        elevationM: float | None = None,
        yearlyAvgTempInDegC: float | None = None,
        amplitudeOfMonthlyAvgTempsInDegC: float | None = None,
        tempSensorHeightInM: float | None = None,
        refHeightWeatherMeasurementInM: float | None = None,
        refHeightWindspeedMeasurementInM: float | None = None,
        annualCO2ConcentrationInPPM: float | None = None,
        notes: str | None = None,
        **kwargs: object,
    ) -> _all.WeatherStationBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.WeatherStationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.WeatherStationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.WeatherStationBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.WeatherStationReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.WeatherStationReader: ...

class _SoilMetadataStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: str | None = None,
        name: str | None = None,
        source: str | None = None,
        depthInCM: int | None = None,
        obstableDepthInCM: int | None = None,
        depthOfTopsoilInCM: int | None = None,
        drainageRatePerDay: float | None = None,
        runoffCureNoSCS: float | None = None,
        soilAvailableWaterContentInCM: float | None = None,
        surfaceStoneCoverAsFraction: float | None = None,
        soilAlbedo: float | None = None,
        soilEvaporationLimitInMM: float | None = None,
        mineralizationFactor: float | None = None,
        soilFertilityOnFoto: float | None = None,
        soilClassificationSystem: str | None = None,
        soilTexture: str | None = None,
        classification: str | None = None,
        notes: str | None = None,
        profile: ProfileClient | _ProfileInterfaceModule.Server | None = None,
        **kwargs: object,
    ) -> _all.SoilMetadataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SoilMetadataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SoilMetadataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SoilMetadataBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SoilMetadataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SoilMetadataReader: ...

class _FieldStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: str | None = None,
        name: str | None = None,
        latitudeInDecDeg: float | None = None,
        longitudeInDecDeg: float | None = None,
        elevationInM: float | None = None,
        slopeDegreeInDeg: float | None = None,
        drainageType: str | None = None,
        distanceToWeatherStationInKM: float | None = None,
        country: str | None = None,
        subCountry: str | None = None,
        subSubCountry: str | None = None,
        notes: str | None = None,
        **kwargs: object,
    ) -> _all.FieldBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.FieldReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.FieldReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.FieldBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.FieldReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.FieldReader: ...

class _CultivarStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: str | None = None,
        name: str | None = None,
        accessionId: str | None = None,
        accessionLocation: str | None = None,
        cropIdentifierICASA: str | None = None,
        seedLot: str | None = None,
        breedingProgram: str | None = None,
        originalName: str | None = None,
        releaseYear: int | None = None,
        synonym: str | None = None,
        notes: str | None = None,
        **kwargs: object,
    ) -> _all.CultivarBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.CultivarReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.CultivarReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.CultivarBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.CultivarReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.CultivarReader: ...

class _PlotStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: str | None = None,
        cultivar: _all.CultivarBuilder | dict[str, Any] | None = None,
        soil: _all.SoilMetadataBuilder | dict[str, Any] | None = None,
        blockNumber: int | None = None,
        plotNumber: int | None = None,
        replicateNumber: int | None = None,
        rowNumber: int | None = None,
        columnNumber: int | None = None,
        harvestMethod: str | None = None,
        notes: str | None = None,
        experimentId: str | None = None,
        treatmentId: str | None = None,
        cultivarId: str | None = None,
        soilId: str | None = None,
        **kwargs: object,
    ) -> _all.PlotBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.PlotReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.PlotReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.PlotBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.PlotReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.PlotReader: ...

class _ResidueStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        initialMeasureDate: DateBuilder | dict[str, Any] | None = None,
        incorporationDepth: int | None = None,
        percentIncorporated: float | None = None,
        prevCropCode: str | None = None,
        aboveGroundWeight: float | None = None,
        aboveGroundNConcentrationInPerc: float | None = None,
        rootWeightPreviousCrop: float | None = None,
        experimentId: str | None = None,
        treatmentId: str | None = None,
        **kwargs: object,
    ) -> _all.ResidueBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.ResidueReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.ResidueReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.ResidueBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.ResidueReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.ResidueReader: ...

class _InitialConditionsLayerStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        date: DateBuilder | dict[str, Any] | None = None,
        soilLayerTopDepthInCM: int | None = None,
        soilLayerBaseDepthInCM: int | None = None,
        waterConcentration: float | None = None,
        totalNInKGperHA: float | None = None,
        massNH4InKGperHA: float | None = None,
        massNO3InKGperHA: float | None = None,
        concNH4InPPM: float | None = None,
        concNO3InPPM: float | None = None,
        experimentId: str | None = None,
        treatmentId: str | None = None,
        **kwargs: object,
    ) -> _all.InitialConditionsLayerBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.InitialConditionsLayerReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.InitialConditionsLayerReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.InitialConditionsLayerBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.InitialConditionsLayerReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.InitialConditionsLayerReader: ...

class _PlantingEventStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        plantingDistribution: str | None = None,
        rowSpacingInCM: float | None = None,
        rowDirectionInArcDeg: float | None = None,
        plantingDepthInMM: int | None = None,
        plotLayout: str | None = None,
        plantingDate: DateBuilder | dict[str, Any] | None = None,
        plantPopulationAtPlantingInNoPerM2: int | None = None,
        averageEmergenceDate: DateBuilder | dict[str, Any] | None = None,
        averagePlantPopulationAtEmergenceInNoPerM2: int | None = None,
        notes: str | None = None,
        experimentId: str | None = None,
        treatmentId: str | None = None,
        **kwargs: object,
    ) -> _all.PlantingEventBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.PlantingEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.PlantingEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.PlantingEventBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.PlantingEventReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.PlantingEventReader: ...

class _HarvestEventStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        date: DateBuilder | dict[str, Any] | None = None,
        harvestMethod: str | None = None,
        harvestArea: float | None = None,
        notes: str | None = None,
        comments: str | None = None,
        experimentId: str | None = None,
        treatmentId: str | None = None,
        **kwargs: object,
    ) -> _all.HarvestEventBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.HarvestEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.HarvestEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.HarvestEventBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.HarvestEventReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.HarvestEventReader: ...

class _IrrigationEventStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        date: DateBuilder | dict[str, Any] | None = None,
        operation: str | None = None,
        applicationDepth: int | None = None,
        amount: int | None = None,
        waterNConcentrationInPerc: float | None = None,
        notes: str | None = None,
        experimentId: str | None = None,
        treatmentId: str | None = None,
        **kwargs: object,
    ) -> _all.IrrigationEventBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.IrrigationEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.IrrigationEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.IrrigationEventBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.IrrigationEventReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.IrrigationEventReader: ...

class _FertilizerEventStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        date: DateBuilder | dict[str, Any] | None = None,
        applicationMethod: str | None = None,
        applicationDepthInCM: int | None = None,
        material: str | None = None,
        appliedNInKGNPerHA: int | None = None,
        appliedNO3InKGNperHA: int | None = None,
        appliedNH4InKGNperHA: int | None = None,
        notes: str | None = None,
        experimentId: str | None = None,
        treatmentId: str | None = None,
        **kwargs: object,
    ) -> _all.FertilizerEventBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.FertilizerEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.FertilizerEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.FertilizerEventBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.FertilizerEventReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.FertilizerEventReader: ...

class _EnvironmentModificationStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        date: DateBuilder | dict[str, Any] | None = None,
        codeCO2: str | None = None,
        valueCO2: int | None = None,
        notes: str | None = None,
        experimentId: str | None = None,
        treatmentId: str | None = None,
        **kwargs: object,
    ) -> _all.EnvironmentModificationBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.EnvironmentModificationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.EnvironmentModificationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.EnvironmentModificationBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.EnvironmentModificationReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.EnvironmentModificationReader: ...

class _TreatmentStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: str | None = None,
        field: _all.FieldBuilder | dict[str, Any] | None = None,
        weatherStation: _all.WeatherStationBuilder | dict[str, Any] | None = None,
        weatherStationTimeseries: TimeSeriesClient
        | _TimeSeriesInterfaceModule.Server
        | None = None,
        name: str | None = None,
        simulationStartDate: DateBuilder | dict[str, Any] | None = None,
        simulationEndDate: DateBuilder | dict[str, Any] | None = None,
        irrigationApplied: bool | None = None,
        fertilizerApplied: bool | None = None,
        irrigationLevel: int | None = None,
        fertilizerLevel: int | None = None,
        plantingDateLevel: int | None = None,
        environmentalModificationsLevel: int | None = None,
        initialConditionsLevel: int | None = None,
        plantingDensityLevel: int | None = None,
        numberOfBlocksOrReplicates: int | None = None,
        notes: str | None = None,
        plots: _all.PlotListBuilder | dict[str, Any] | None = None,
        residue: _all.ResidueBuilder | dict[str, Any] | None = None,
        initialConditionsLayers: _all.InitialConditionsLayerListBuilder
        | dict[str, Any]
        | None = None,
        plantingEvents: _all.PlantingEventListBuilder | dict[str, Any] | None = None,
        harvestEvents: _all.HarvestEventListBuilder | dict[str, Any] | None = None,
        irrigationEvents: _all.IrrigationEventListBuilder
        | dict[str, Any]
        | None = None,
        fertilizerEvents: _all.FertilizerEventListBuilder
        | dict[str, Any]
        | None = None,
        environmentModifications: _all.EnvironmentModificationListBuilder
        | dict[str, Any]
        | None = None,
        experimentId: str | None = None,
        fieldId: str | None = None,
        weatherStationId: str | None = None,
        weatherStationDataset: str | None = None,
        **kwargs: object,
    ) -> _all.TreatmentBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.TreatmentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.TreatmentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.TreatmentBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.TreatmentReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.TreatmentReader: ...

class _ExperimentDescriptionStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: str | None = None,
        suiteId: str | None = None,
        name: str | None = None,
        researchInfrastructureName: str | None = None,
        instituteName: str | None = None,
        researchUnitName: str | None = None,
        experimentalFacilityName: str | None = None,
        siteName: str | None = None,
        siteType: str | None = None,
        mainExperimentFactor: str | None = None,
        experimentalFactorCombinations: str | None = None,
        experimentType: str | None = None,
        managementType: str | None = None,
        croppingSystem: str | None = None,
        plantingYear: int | None = None,
        harvestOperationYear: int | None = None,
        notes: str | None = None,
        treatments: _all.TreatmentListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.ExperimentDescriptionBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.ExperimentDescriptionReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.ExperimentDescriptionReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.ExperimentDescriptionBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.ExperimentDescriptionReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.ExperimentDescriptionReader: ...
