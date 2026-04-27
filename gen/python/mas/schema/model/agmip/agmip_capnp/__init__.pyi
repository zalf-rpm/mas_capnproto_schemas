"""This is an automatically generated stub for `agmip.capnp`."""

from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

from mas.schema.climate.climate_capnp import (
    _TimeSeriesInterfaceModule,
)
from mas.schema.common.common_capnp import (
    StructuredTextBuilder,
    StructuredTextReader,
)
from mas.schema.soil.soil_capnp import _ProfileInterfaceModule

class _FieldExperimentDataTemplateStructModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def soilProfile(self) -> _ProfileInterfaceModule.ProfileClient: ...
        @property
        def soil(self) -> StructuredTextReader: ...
        @property
        def plot(self) -> StructuredTextReader: ...
        @property
        def timeseries(self) -> _TimeSeriesInterfaceModule.TimeSeriesClient: ...
        @property
        def treatment(self) -> StructuredTextReader: ...
        @property
        def experiment(self) -> StructuredTextReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ) -> FieldExperimentDataTemplateBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def soilProfile(self) -> _ProfileInterfaceModule.ProfileClient: ...
        @soilProfile.setter
        def soilProfile(
            self,
            value: _ProfileInterfaceModule.ProfileClient
            | _ProfileInterfaceModule.Server,
        ) -> None: ...
        @property
        def soil(self) -> StructuredTextBuilder: ...
        @soil.setter
        def soil(
            self,
            value: StructuredTextBuilder | StructuredTextReader | dict[str, Any],
        ) -> None: ...
        @property
        def plot(self) -> StructuredTextBuilder: ...
        @plot.setter
        def plot(
            self,
            value: StructuredTextBuilder | StructuredTextReader | dict[str, Any],
        ) -> None: ...
        @property
        def timeseries(self) -> _TimeSeriesInterfaceModule.TimeSeriesClient: ...
        @timeseries.setter
        def timeseries(
            self,
            value: _TimeSeriesInterfaceModule.TimeSeriesClient
            | _TimeSeriesInterfaceModule.Server,
        ) -> None: ...
        @property
        def treatment(self) -> StructuredTextBuilder: ...
        @treatment.setter
        def treatment(
            self,
            value: StructuredTextBuilder | StructuredTextReader | dict[str, Any],
        ) -> None: ...
        @property
        def experiment(self) -> StructuredTextBuilder: ...
        @experiment.setter
        def experiment(
            self,
            value: StructuredTextBuilder | StructuredTextReader | dict[str, Any],
        ) -> None: ...
        @override
        @overload
        def init(
            self,
            field: Literal["soil"],
            size: int | None = None,
        ) -> StructuredTextBuilder: ...
        @overload
        def init(
            self,
            field: Literal["plot"],
            size: int | None = None,
        ) -> StructuredTextBuilder: ...
        @overload
        def init(
            self,
            field: Literal["treatment"],
            size: int | None = None,
        ) -> StructuredTextBuilder: ...
        @overload
        def init(
            self,
            field: Literal["experiment"],
            size: int | None = None,
        ) -> StructuredTextBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> FieldExperimentDataTemplateReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        soilProfile: _ProfileInterfaceModule.ProfileClient
        | _ProfileInterfaceModule.Server
        | None = None,
        soil: StructuredTextBuilder | dict[str, Any] | None = None,
        plot: StructuredTextBuilder | dict[str, Any] | None = None,
        timeseries: _TimeSeriesInterfaceModule.TimeSeriesClient
        | _TimeSeriesInterfaceModule.Server
        | None = None,
        treatment: StructuredTextBuilder | dict[str, Any] | None = None,
        experiment: StructuredTextBuilder | dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> FieldExperimentDataTemplateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[FieldExperimentDataTemplateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[FieldExperimentDataTemplateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[FieldExperimentDataTemplateBuilder]: ...
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
    ) -> FieldExperimentDataTemplateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> FieldExperimentDataTemplateReader: ...

FieldExperimentDataTemplate: _FieldExperimentDataTemplateStructModule

# Top-level type aliases for use in type annotations
type FieldExperimentDataTemplateBuilder = (
    _FieldExperimentDataTemplateStructModule.Builder
)
type FieldExperimentDataTemplateReader = _FieldExperimentDataTemplateStructModule.Reader
