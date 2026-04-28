"""Module helper types for `agmip.capnp`."""

from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.climate.climate_capnp.types.clients import TimeSeriesClient
from mas.schema.climate.climate_capnp.types.modules import _TimeSeriesInterfaceModule
from mas.schema.common.common_capnp.types import (
    schemas as _mas_schema_common_common_capnp_schemas,
)
from mas.schema.common.common_capnp.types.builders import StructuredTextBuilder
from mas.schema.model.agmip.agmip_capnp.types import builders as builders
from mas.schema.model.agmip.agmip_capnp.types import readers as readers
from mas.schema.model.agmip.agmip_capnp.types import schemas as schemas
from mas.schema.soil.soil_capnp.types import (
    schemas as _mas_schema_soil_soil_capnp_schemas,
)
from mas.schema.soil.soil_capnp.types.clients import ProfileClient
from mas.schema.soil.soil_capnp.types.modules import _ProfileInterfaceModule

class _FieldExperimentDataTemplateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _FieldExperimentDataTemplateSchema(_StructSchema):
        class _SoilProfileField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_soil_soil_capnp_schemas._ProfileSchema: ...

        class _SoilField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_common_common_capnp_schemas._StructuredTextSchema: ...

        class _PlotField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_common_common_capnp_schemas._StructuredTextSchema: ...

        class _TimeseriesField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _InterfaceSchema: ...

        class _TreatmentField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_common_common_capnp_schemas._StructuredTextSchema: ...

        class _ExperimentField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_common_common_capnp_schemas._StructuredTextSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["soilProfile"],
            ) -> _FieldExperimentDataTemplateStructModule._FieldExperimentDataTemplateSchema._SoilProfileField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soil"],
            ) -> _FieldExperimentDataTemplateStructModule._FieldExperimentDataTemplateSchema._SoilField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["plot"],
            ) -> _FieldExperimentDataTemplateStructModule._FieldExperimentDataTemplateSchema._PlotField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["timeseries"],
            ) -> _FieldExperimentDataTemplateStructModule._FieldExperimentDataTemplateSchema._TimeseriesField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["treatment"],
            ) -> _FieldExperimentDataTemplateStructModule._FieldExperimentDataTemplateSchema._TreatmentField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["experiment"],
            ) -> _FieldExperimentDataTemplateStructModule._FieldExperimentDataTemplateSchema._ExperimentField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _FieldExperimentDataTemplateStructModule._FieldExperimentDataTemplateSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._FieldExperimentDataTemplateSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        soilProfile: ProfileClient | _ProfileInterfaceModule.Server | None = None,
        soil: StructuredTextBuilder | dict[str, Any] | None = None,
        plot: StructuredTextBuilder | dict[str, Any] | None = None,
        timeseries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server | None = None,
        treatment: StructuredTextBuilder | dict[str, Any] | None = None,
        experiment: StructuredTextBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.FieldExperimentDataTemplateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.FieldExperimentDataTemplateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.FieldExperimentDataTemplateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.FieldExperimentDataTemplateBuilder]: ...
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
    ) -> readers.FieldExperimentDataTemplateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.FieldExperimentDataTemplateReader: ...
