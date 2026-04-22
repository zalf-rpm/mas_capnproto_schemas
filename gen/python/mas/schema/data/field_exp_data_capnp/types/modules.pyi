"""Module helper types for `field_exp_data.capnp`."""

from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceSchema,
    _ListSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.climate.climate_capnp.types.clients import TimeSeriesClient
from mas.schema.climate.climate_capnp.types.modules import _TimeSeriesInterfaceModule
from mas.schema.common.date_capnp.types import (
    schemas as _mas_schema_common_date_capnp_schemas,
)
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.data.field_exp_data_capnp.types import builders as builders
from mas.schema.data.field_exp_data_capnp.types import readers as readers
from mas.schema.data.field_exp_data_capnp.types import schemas as schemas
from mas.schema.soil.soil_capnp.types import (
    schemas as _mas_schema_soil_soil_capnp_schemas,
)
from mas.schema.soil.soil_capnp.types.clients import ProfileClient
from mas.schema.soil.soil_capnp.types.modules import _ProfileInterfaceModule

class _WeatherStationStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _WeatherStationSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["instituteName"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["site"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["country"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["location2ndLevel"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["location3rdLevel"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["latitudeInDecDeg"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["longitudeInDecDeg"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["elevationM"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["yearlyAvgTempInDegC"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["amplitudeOfMonthlyAvgTempsInDegC"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["tempSensorHeightInM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["refHeightWeatherMeasurementInM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["refHeightWindspeedMeasurementInM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["annualCO2ConcentrationInPPM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["notes"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _WeatherStationStructModule._WeatherStationSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._WeatherStationSchema: ...
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
    ) -> builders.WeatherStationBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.WeatherStationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.WeatherStationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.WeatherStationBuilder]: ...
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
    ) -> readers.WeatherStationReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.WeatherStationReader: ...

class _SoilMetadataStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilMetadataSchema(_StructSchema):
        class _ProfileField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_soil_soil_capnp_schemas._ProfileSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["source"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["depthInCM"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["obstableDepthInCM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["depthOfTopsoilInCM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["drainageRatePerDay"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["runoffCureNoSCS"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilAvailableWaterContentInCM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["surfaceStoneCoverAsFraction"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["soilAlbedo"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilEvaporationLimitInMM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["mineralizationFactor"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilFertilityOnFoto"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilClassificationSystem"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilTexture"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["classification"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["notes"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["profile"],
            ) -> _SoilMetadataStructModule._SoilMetadataSchema._ProfileField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _SoilMetadataStructModule._SoilMetadataSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SoilMetadataSchema: ...
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
    ) -> builders.SoilMetadataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilMetadataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SoilMetadataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilMetadataBuilder]: ...
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
    ) -> readers.SoilMetadataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilMetadataReader: ...

class _FieldStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _FieldSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["latitudeInDecDeg"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["longitudeInDecDeg"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["elevationInM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["slopeDegreeInDeg"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["drainageType"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["distanceToWeatherStationInKM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["country"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["subCountry"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["subSubCountry"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["notes"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _FieldStructModule._FieldSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._FieldSchema: ...
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
    ) -> builders.FieldBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.FieldReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.FieldReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.FieldBuilder]: ...
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
    ) -> readers.FieldReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.FieldReader: ...

class _CultivarStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _CultivarSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["accessionId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["accessionLocation"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cropIdentifierICASA"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["seedLot"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["breedingProgram"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["originalName"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["releaseYear"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["synonym"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["notes"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _CultivarStructModule._CultivarSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._CultivarSchema: ...
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
    ) -> builders.CultivarBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.CultivarReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.CultivarReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.CultivarBuilder]: ...
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
    ) -> readers.CultivarReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CultivarReader: ...

class _PlotStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _PlotSchema(_StructSchema):
        class _CultivarField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._CultivarSchema: ...

        class _SoilField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._SoilMetadataSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["cultivar"],
            ) -> _PlotStructModule._PlotSchema._CultivarField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soil"],
            ) -> _PlotStructModule._PlotSchema._SoilField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["blockNumber"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["plotNumber"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["replicateNumber"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["rowNumber"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["columnNumber"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["harvestMethod"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["notes"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["treatmentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["cultivarId"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["soilId"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _PlotStructModule._PlotSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._PlotSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: str | None = None,
        cultivar: builders.CultivarBuilder | dict[str, Any] | None = None,
        soil: builders.SoilMetadataBuilder | dict[str, Any] | None = None,
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
    ) -> builders.PlotBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.PlotReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.PlotReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.PlotBuilder]: ...
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
    ) -> readers.PlotReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.PlotReader: ...

class _ResidueStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _ResidueSchema(_StructSchema):
        class _InitialMeasureDateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["initialMeasureDate"],
            ) -> _ResidueStructModule._ResidueSchema._InitialMeasureDateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["incorporationDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["percentIncorporated"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["prevCropCode"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aboveGroundWeight"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["aboveGroundNConcentrationInPerc"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rootWeightPreviousCrop"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["treatmentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _ResidueStructModule._ResidueSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._ResidueSchema: ...
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
    ) -> builders.ResidueBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.ResidueReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.ResidueReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.ResidueBuilder]: ...
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
    ) -> readers.ResidueReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.ResidueReader: ...

class _InitialConditionsLayerStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _InitialConditionsLayerSchema(_StructSchema):
        class _DateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["date"],
            ) -> _InitialConditionsLayerStructModule._InitialConditionsLayerSchema._DateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilLayerTopDepthInCM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilLayerBaseDepthInCM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["waterConcentration"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["totalNInKGperHA"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["massNH4InKGperHA"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["massNO3InKGperHA"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["concNH4InPPM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["concNO3InPPM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["treatmentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> (
            _InitialConditionsLayerStructModule._InitialConditionsLayerSchema._Fields
        ): ...

    @property
    @override
    def schema(self) -> schemas._InitialConditionsLayerSchema: ...
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
    ) -> builders.InitialConditionsLayerBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.InitialConditionsLayerReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.InitialConditionsLayerReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.InitialConditionsLayerBuilder]: ...
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
    ) -> readers.InitialConditionsLayerReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.InitialConditionsLayerReader: ...

class _PlantingEventStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _PlantingEventSchema(_StructSchema):
        class _PlantingDateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _AverageEmergenceDateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["plantingDistribution"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rowSpacingInCM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rowDirectionInArcDeg"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["plantingDepthInMM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["plotLayout"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["plantingDate"],
            ) -> _PlantingEventStructModule._PlantingEventSchema._PlantingDateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["plantPopulationAtPlantingInNoPerM2"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["averageEmergenceDate"],
            ) -> _PlantingEventStructModule._PlantingEventSchema._AverageEmergenceDateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["averagePlantPopulationAtEmergenceInNoPerM2"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["notes"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["treatmentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _PlantingEventStructModule._PlantingEventSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._PlantingEventSchema: ...
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
    ) -> builders.PlantingEventBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.PlantingEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.PlantingEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.PlantingEventBuilder]: ...
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
    ) -> readers.PlantingEventReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.PlantingEventReader: ...

class _HarvestEventStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _HarvestEventSchema(_StructSchema):
        class _DateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["date"],
            ) -> _HarvestEventStructModule._HarvestEventSchema._DateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["harvestMethod"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["harvestArea"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["notes"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["comments"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["treatmentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _HarvestEventStructModule._HarvestEventSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._HarvestEventSchema: ...
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
    ) -> builders.HarvestEventBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.HarvestEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.HarvestEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.HarvestEventBuilder]: ...
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
    ) -> readers.HarvestEventReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.HarvestEventReader: ...

class _IrrigationEventStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _IrrigationEventSchema(_StructSchema):
        class _DateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["date"],
            ) -> _IrrigationEventStructModule._IrrigationEventSchema._DateField: ...
            @overload
            def __getitem__(self, key: Literal["operation"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["applicationDepth"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["amount"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["waterNConcentrationInPerc"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["notes"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["treatmentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _IrrigationEventStructModule._IrrigationEventSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._IrrigationEventSchema: ...
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
    ) -> builders.IrrigationEventBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.IrrigationEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.IrrigationEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.IrrigationEventBuilder]: ...
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
    ) -> readers.IrrigationEventReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.IrrigationEventReader: ...

class _FertilizerEventStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _FertilizerEventSchema(_StructSchema):
        class _DateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["date"],
            ) -> _FertilizerEventStructModule._FertilizerEventSchema._DateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["applicationMethod"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["applicationDepthInCM"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["material"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["appliedNInKGNPerHA"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["appliedNO3InKGNperHA"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["appliedNH4InKGNperHA"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["notes"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["treatmentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _FertilizerEventStructModule._FertilizerEventSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._FertilizerEventSchema: ...
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
    ) -> builders.FertilizerEventBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.FertilizerEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.FertilizerEventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.FertilizerEventBuilder]: ...
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
    ) -> readers.FertilizerEventReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.FertilizerEventReader: ...

class _EnvironmentModificationStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _EnvironmentModificationSchema(_StructSchema):
        class _DateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["date"],
            ) -> _EnvironmentModificationStructModule._EnvironmentModificationSchema._DateField: ...
            @overload
            def __getitem__(self, key: Literal["codeCO2"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["valueCO2"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["notes"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["treatmentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> (
            _EnvironmentModificationStructModule._EnvironmentModificationSchema._Fields
        ): ...

    @property
    @override
    def schema(self) -> schemas._EnvironmentModificationSchema: ...
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
    ) -> builders.EnvironmentModificationBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.EnvironmentModificationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.EnvironmentModificationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.EnvironmentModificationBuilder]: ...
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
    ) -> readers.EnvironmentModificationReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.EnvironmentModificationReader: ...

class _TreatmentStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _TreatmentSchema(_StructSchema):
        class _FieldField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._FieldSchema: ...

        class _WeatherStationField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._WeatherStationSchema: ...

        class _WeatherStationTimeseriesField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _InterfaceSchema: ...

        class _SimulationStartDateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _SimulationEndDateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _PlotsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._PlotSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _TreatmentStructModule._TreatmentSchema._PlotsField._Schema: ...

        class _ResidueField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._ResidueSchema: ...

        class _InitialConditionsLayersField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._InitialConditionsLayerSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _TreatmentStructModule._TreatmentSchema._InitialConditionsLayersField._Schema: ...

        class _PlantingEventsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._PlantingEventSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> (
                _TreatmentStructModule._TreatmentSchema._PlantingEventsField._Schema
            ): ...

        class _HarvestEventsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._HarvestEventSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> (
                _TreatmentStructModule._TreatmentSchema._HarvestEventsField._Schema
            ): ...

        class _IrrigationEventsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._IrrigationEventSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> (
                _TreatmentStructModule._TreatmentSchema._IrrigationEventsField._Schema
            ): ...

        class _FertilizerEventsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._FertilizerEventSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> (
                _TreatmentStructModule._TreatmentSchema._FertilizerEventsField._Schema
            ): ...

        class _EnvironmentModificationsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._EnvironmentModificationSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _TreatmentStructModule._TreatmentSchema._EnvironmentModificationsField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["field"],
            ) -> _TreatmentStructModule._TreatmentSchema._FieldField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["weatherStation"],
            ) -> _TreatmentStructModule._TreatmentSchema._WeatherStationField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["weatherStationTimeseries"],
            ) -> (
                _TreatmentStructModule._TreatmentSchema._WeatherStationTimeseriesField
            ): ...
            @overload
            def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["simulationStartDate"],
            ) -> _TreatmentStructModule._TreatmentSchema._SimulationStartDateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["simulationEndDate"],
            ) -> _TreatmentStructModule._TreatmentSchema._SimulationEndDateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["irrigationApplied"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["fertilizerApplied"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["irrigationLevel"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["fertilizerLevel"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["plantingDateLevel"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["environmentalModificationsLevel"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["initialConditionsLevel"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["plantingDensityLevel"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["numberOfBlocksOrReplicates"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["notes"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["plots"],
            ) -> _TreatmentStructModule._TreatmentSchema._PlotsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["residue"],
            ) -> _TreatmentStructModule._TreatmentSchema._ResidueField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["initialConditionsLayers"],
            ) -> (
                _TreatmentStructModule._TreatmentSchema._InitialConditionsLayersField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["plantingEvents"],
            ) -> _TreatmentStructModule._TreatmentSchema._PlantingEventsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["harvestEvents"],
            ) -> _TreatmentStructModule._TreatmentSchema._HarvestEventsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["irrigationEvents"],
            ) -> _TreatmentStructModule._TreatmentSchema._IrrigationEventsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["fertilizerEvents"],
            ) -> _TreatmentStructModule._TreatmentSchema._FertilizerEventsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["environmentModifications"],
            ) -> (
                _TreatmentStructModule._TreatmentSchema._EnvironmentModificationsField
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["fieldId"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["weatherStationId"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["weatherStationDataset"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _TreatmentStructModule._TreatmentSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._TreatmentSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: str | None = None,
        field: builders.FieldBuilder | dict[str, Any] | None = None,
        weatherStation: builders.WeatherStationBuilder | dict[str, Any] | None = None,
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
        plots: builders.PlotListBuilder | dict[str, Any] | None = None,
        residue: builders.ResidueBuilder | dict[str, Any] | None = None,
        initialConditionsLayers: builders.InitialConditionsLayerListBuilder
        | dict[str, Any]
        | None = None,
        plantingEvents: builders.PlantingEventListBuilder
        | dict[str, Any]
        | None = None,
        harvestEvents: builders.HarvestEventListBuilder | dict[str, Any] | None = None,
        irrigationEvents: builders.IrrigationEventListBuilder
        | dict[str, Any]
        | None = None,
        fertilizerEvents: builders.FertilizerEventListBuilder
        | dict[str, Any]
        | None = None,
        environmentModifications: builders.EnvironmentModificationListBuilder
        | dict[str, Any]
        | None = None,
        experimentId: str | None = None,
        fieldId: str | None = None,
        weatherStationId: str | None = None,
        weatherStationDataset: str | None = None,
        **kwargs: object,
    ) -> builders.TreatmentBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.TreatmentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.TreatmentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.TreatmentBuilder]: ...
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
    ) -> readers.TreatmentReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.TreatmentReader: ...

class _ExperimentDescriptionStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _ExperimentDescriptionSchema(_StructSchema):
        class _TreatmentsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._TreatmentSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _ExperimentDescriptionStructModule._ExperimentDescriptionSchema._TreatmentsField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["suiteId"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["researchInfrastructureName"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["instituteName"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["researchUnitName"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentalFacilityName"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["siteName"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["siteType"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["mainExperimentFactor"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentalFactorCombinations"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experimentType"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["managementType"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["croppingSystem"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["plantingYear"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["harvestOperationYear"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["notes"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["treatments"],
            ) -> _ExperimentDescriptionStructModule._ExperimentDescriptionSchema._TreatmentsField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> (
            _ExperimentDescriptionStructModule._ExperimentDescriptionSchema._Fields
        ): ...

    @property
    @override
    def schema(self) -> schemas._ExperimentDescriptionSchema: ...
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
        treatments: builders.TreatmentListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.ExperimentDescriptionBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.ExperimentDescriptionReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.ExperimentDescriptionReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.ExperimentDescriptionBuilder]: ...
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
    ) -> readers.ExperimentDescriptionReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.ExperimentDescriptionReader: ...
