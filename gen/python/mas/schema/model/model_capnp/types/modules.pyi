"""Module helper types for `model.capnp`."""

from collections.abc import Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _EnumModule,
    _EnumSchema,
    _InterfaceMethod,
    _InterfaceModule,
    _InterfaceSchema,
    _ListSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.climate.climate_capnp.types.clients import TimeSeriesClient
from mas.schema.climate.climate_capnp.types.modules import _TimeSeriesInterfaceModule
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.management.management_capnp.types import (
    schemas as _mas_schema_management_management_capnp_schemas,
)
from mas.schema.model.model_capnp.types import builders as builders
from mas.schema.model.model_capnp.types import clients as clients
from mas.schema.model.model_capnp.types import common as common
from mas.schema.model.model_capnp.types import contexts as contexts
from mas.schema.model.model_capnp.types import enums as enums
from mas.schema.model.model_capnp.types import readers as readers
from mas.schema.model.model_capnp.types import schemas as schemas
from mas.schema.model.model_capnp.types import servers as servers
from mas.schema.model.model_capnp.types.results import tuples as results_tuples
from mas.schema.persistence.persistence_capnp.types import (
    schemas as _mas_schema_persistence_persistence_capnp_schemas,
)
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)
from mas.schema.service.service_capnp.types.modules import _StoppableInterfaceModule
from mas.schema.soil.soil_capnp.types import (
    schemas as _mas_schema_soil_soil_capnp_schemas,
)
from mas.schema.soil.soil_capnp.types.clients import ProfileClient
from mas.schema.soil.soil_capnp.types.modules import _ProfileInterfaceModule

class _XYResultStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _XYResultSchema(_StructSchema):
        class _XsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _YsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["xs"],
            ) -> _XYResultStructModule._XYResultSchema._XsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["ys"],
            ) -> _XYResultStructModule._XYResultSchema._YsField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _XYResultStructModule._XYResultSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._XYResultSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        xs: builders.Float64ListBuilder | dict[str, Any] | None = None,
        ys: builders.Float64ListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.XYResultBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.XYResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.XYResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.XYResultBuilder]: ...
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
    ) -> readers.XYResultReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.XYResultReader: ...

class _StatStructModule(_StructModule):
    class _TypeEnumModule(_EnumModule):
        min: int
        max: int
        sd: int
        avg: int
        median: int

        class _TypeSchema(_EnumSchema): ...

        @property
        @override
        def schema(self) -> schemas._StatTypeEnumSchema: ...

    Type: _TypeEnumModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _StatSchema(_StructSchema):
        class _TypeField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._StatTypeEnumSchema: ...

        class _VsField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["type"],
            ) -> _StatStructModule._StatSchema._TypeField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["vs"],
            ) -> _StatStructModule._StatSchema._VsField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _StatStructModule._StatSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._StatSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        type: enums.StatTypeEnum | None = None,
        vs: builders.Float64ListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.StatBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.StatReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.StatReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.StatBuilder]: ...
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
    ) -> readers.StatReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.StatReader: ...

class _XYPlusResultStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _XYPlusResultSchema(_StructSchema):
        class _XyField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._XYResultSchema: ...

        class _StatsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._StatSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _XYPlusResultStructModule._XYPlusResultSchema._StatsField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["xy"],
            ) -> _XYPlusResultStructModule._XYPlusResultSchema._XyField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stats"],
            ) -> _XYPlusResultStructModule._XYPlusResultSchema._StatsField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _XYPlusResultStructModule._XYPlusResultSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._XYPlusResultSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        xy: builders.XYResultBuilder | dict[str, Any] | None = None,
        stats: builders.StatListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.XYPlusResultBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.XYPlusResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.XYPlusResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.XYPlusResultBuilder]: ...
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
    ) -> readers.XYPlusResultReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.XYPlusResultReader: ...

class _ClimateInstanceInterfaceModule(_IdentifiableInterfaceModule):
    class _ClimateInstanceSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["description"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _ClimateInstanceInterfaceModuleRunParamSchema(_StructSchema):
            class _TimeSeriesField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["timeSeries"],
                ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunParamSchema._TimeSeriesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunParamSchema._Fields: ...

        class _ClimateInstanceInterfaceModuleRunResultSchema(_StructSchema):
            class _ResultField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._XYResultSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["result"],
                ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunResultSchema._ResultField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunResultSchema._Fields: ...

        class _ClimateInstanceInterfaceModuleRunMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunResultSchema: ...

        class _ClimateInstanceInterfaceModuleRunSetParamSchema(_StructSchema):
            class _DatasetField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _InterfaceSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunSetParamSchema._DatasetField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["dataset"],
                ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunSetParamSchema._DatasetField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunSetParamSchema._Fields: ...

        class _ClimateInstanceInterfaceModuleRunSetResultSchema(_StructSchema):
            class _ResultField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._XYPlusResultSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["result"],
                ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunSetResultSchema._ResultField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunSetResultSchema._Fields: ...

        class _ClimateInstanceInterfaceModuleRunSetMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunSetParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunSetResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["run"],
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["runSet"],
            ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._ClimateInstanceInterfaceModuleRunSetMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(
            self,
        ) -> _ClimateInstanceInterfaceModule._ClimateInstanceSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._ClimateInstanceSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.ClimateInstanceClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def run(
            self,
            timeSeries: TimeSeriesClient,
            _context: contexts.ClimateInstanceRunCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.XYResultBuilder
            | readers.XYResultReader
            | dict[str, Any]
            | results_tuples.ClimateInstanceRunResultTuple
            | None
        ]: ...
        def run_context(
            self,
            context: contexts.ClimateInstanceRunCallContext,
        ) -> Awaitable[None]: ...
        def runSet(
            self,
            dataset: readers.TimeSeriesClientListReader,
            _context: contexts.RunsetCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.XYPlusResultBuilder
            | readers.XYPlusResultReader
            | dict[str, Any]
            | results_tuples.RunsetResultTuple
            | None
        ]: ...
        def runSet_context(
            self,
            context: contexts.RunsetCallContext,
        ) -> Awaitable[None]: ...

class _EnvStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _EnvSchema(_StructSchema):
        class _TimeSeriesField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _InterfaceSchema: ...

        class _SoilProfileField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_soil_soil_capnp_schemas._ProfileSchema: ...

        class _MgmtEventsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(
                    self,
                ) -> _mas_schema_management_management_capnp_schemas._EventSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _EnvStructModule._EnvSchema._MgmtEventsField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["rest"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["timeSeries"],
            ) -> _EnvStructModule._EnvSchema._TimeSeriesField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["soilProfile"],
            ) -> _EnvStructModule._EnvSchema._SoilProfileField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["mgmtEvents"],
            ) -> _EnvStructModule._EnvSchema._MgmtEventsField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _EnvStructModule._EnvSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._EnvSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        rest: common.AnyPointer | None = None,
        timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server | None = None,
        soilProfile: ProfileClient | _ProfileInterfaceModule.Server | None = None,
        mgmtEvents: builders.EventListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.EnvBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.EnvReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.EnvReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.EnvBuilder]: ...
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
    ) -> readers.EnvReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.EnvReader: ...

class _EnvInstanceInterfaceModule(
    _IdentifiableInterfaceModule,
    _PersistentInterfaceModule,
    _StoppableInterfaceModule,
):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.EnvInstanceClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
        _StoppableInterfaceModule.Server,
    ):
        def run(
            self,
            env: readers.EnvReader,
            _context: contexts.EnvInstanceRunCallContext,
            **kwargs: object,
        ) -> Awaitable[
            common.AnyPointer | results_tuples.EnvInstanceRunResultTuple | None
        ]: ...
        def run_context(
            self,
            context: contexts.EnvInstanceRunCallContext,
        ) -> Awaitable[None]: ...

class _EnvInstanceProxyInterfaceModule(_EnvInstanceInterfaceModule):
    class _UnregisterInterfaceModule(_InterfaceModule):
        class _UnregisterSchema(_InterfaceSchema):
            class _UnregisterInterfaceModuleUnregisterParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterParamSchema._Fields: ...

            class _UnregisterInterfaceModuleUnregisterResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["success"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterResultSchema._Fields: ...

            class _UnregisterInterfaceModuleUnregisterMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["unregister"],
                ) -> _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._EnvInstanceProxyUnregisterSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.UnregisterClient: ...
        class Server(_DynamicCapabilityServer):
            def unregister(
                self,
                _context: contexts.UnregisterCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | results_tuples.UnregisterResultTuple | None]: ...
            def unregister_context(
                self,
                context: contexts.UnregisterCallContext,
            ) -> Awaitable[None]: ...

    Unregister: _UnregisterInterfaceModule
    type UnregisterServer = (
        _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
    )

    class _EnvInstanceProxySchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["description"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _PersistentInterfaceModuleSaveParamSchema(_StructSchema):
            class _SealForField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_persistence_persistence_capnp_schemas._SturdyRefOwnerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["sealFor"],
                ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

        class _PersistentInterfaceModuleSaveResultSchema(_StructSchema):
            class _SturdyRefField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> (
                    _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema
                ): ...

            class _UnsaveSRField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> (
                    _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema
                ): ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["sturdyRef"],
                ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["unsaveSR"],
                ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

        class _PersistentInterfaceModuleSaveMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._PersistentInterfaceModuleSaveParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._PersistentInterfaceModuleSaveResultSchema: ...

        class _StoppableInterfaceModuleStopParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._StoppableInterfaceModuleStopParamSchema._Fields: ...

        class _StoppableInterfaceModuleStopResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["success"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._StoppableInterfaceModuleStopResultSchema._Fields: ...

        class _StoppableInterfaceModuleStopMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._StoppableInterfaceModuleStopParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._StoppableInterfaceModuleStopResultSchema: ...

        class _EnvInstanceInterfaceModuleRunParamSchema(_StructSchema):
            class _EnvField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._EnvSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["env"],
                ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._EnvInstanceInterfaceModuleRunParamSchema._EnvField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._EnvInstanceInterfaceModuleRunParamSchema._Fields: ...

        class _EnvInstanceInterfaceModuleRunResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["result"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._EnvInstanceInterfaceModuleRunResultSchema._Fields: ...

        class _EnvInstanceInterfaceModuleRunMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._EnvInstanceInterfaceModuleRunParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._EnvInstanceInterfaceModuleRunResultSchema: ...

        class _EnvInstanceProxyInterfaceModuleRegisterEnvInstanceParamSchema(
            _StructSchema,
        ):
            class _InstanceField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["instance"],
                ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._EnvInstanceProxyInterfaceModuleRegisterEnvInstanceParamSchema._InstanceField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._EnvInstanceProxyInterfaceModuleRegisterEnvInstanceParamSchema._Fields: ...

        class _EnvInstanceProxyInterfaceModuleRegisterEnvInstanceResultSchema(
            _StructSchema,
        ):
            class _UnregisterField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._EnvInstanceProxyUnregisterSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["unregister"],
                ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._EnvInstanceProxyInterfaceModuleRegisterEnvInstanceResultSchema._UnregisterField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._EnvInstanceProxyInterfaceModuleRegisterEnvInstanceResultSchema._Fields: ...

        class _EnvInstanceProxyInterfaceModuleRegisterEnvInstanceMethod(
            _InterfaceMethod,
        ):
            @property
            @override
            def param_type(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._EnvInstanceProxyInterfaceModuleRegisterEnvInstanceParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._EnvInstanceProxyInterfaceModuleRegisterEnvInstanceResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["save"],
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._PersistentInterfaceModuleSaveMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stop"],
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._StoppableInterfaceModuleStopMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["run"],
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._EnvInstanceInterfaceModuleRunMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["registerEnvInstance"],
            ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._EnvInstanceProxyInterfaceModuleRegisterEnvInstanceMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(
            self,
        ) -> _EnvInstanceProxyInterfaceModule._EnvInstanceProxySchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._EnvInstanceProxySchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.EnvInstanceProxyClient: ...
    class Server(_EnvInstanceInterfaceModule.Server):
        def registerEnvInstance(
            self,
            instance: clients.EnvInstanceClient,
            _context: contexts.RegisterenvinstanceCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
            | clients.UnregisterClient
            | results_tuples.RegisterenvinstanceResultTuple
            | None
        ]: ...
        def registerEnvInstance_context(
            self,
            context: contexts.RegisterenvinstanceCallContext,
        ) -> Awaitable[None]: ...

class _InstanceFactoryInterfaceModule(_IdentifiableInterfaceModule):
    class _InstanceFactorySchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["description"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _InstanceFactoryInterfaceModuleModelInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleModelInfoParamSchema._Fields: ...

        class _InstanceFactoryInterfaceModuleModelInfoResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["description"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleModelInfoResultSchema._Fields: ...

        class _InstanceFactoryInterfaceModuleModelInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleModelInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleModelInfoResultSchema: ...

        class _InstanceFactoryInterfaceModuleNewInstanceParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleNewInstanceParamSchema._Fields: ...

        class _InstanceFactoryInterfaceModuleNewInstanceResultSchema(_StructSchema):
            class _InstanceField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["instance"],
                ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleNewInstanceResultSchema._InstanceField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleNewInstanceResultSchema._Fields: ...

        class _InstanceFactoryInterfaceModuleNewInstanceMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleNewInstanceParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleNewInstanceResultSchema: ...

        class _InstanceFactoryInterfaceModuleNewInstancesParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["numberOfInstances"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleNewInstancesParamSchema._Fields: ...

        class _InstanceFactoryInterfaceModuleNewInstancesResultSchema(_StructSchema):
            class _InstancesField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _InterfaceSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleNewInstancesResultSchema._InstancesField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["instances"],
                ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleNewInstancesResultSchema._InstancesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleNewInstancesResultSchema._Fields: ...

        class _InstanceFactoryInterfaceModuleNewInstancesMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleNewInstancesParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleNewInstancesResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["modelInfo"],
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleModelInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["newInstance"],
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleNewInstanceMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["newInstances"],
            ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._InstanceFactoryInterfaceModuleNewInstancesMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(
            self,
        ) -> _InstanceFactoryInterfaceModule._InstanceFactorySchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._InstanceFactorySchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.InstanceFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def modelInfo(
            self,
            _context: contexts.ModelinfoCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.ModelinfoResultTuple | None]: ...
        def modelInfo_context(
            self,
            context: contexts.ModelinfoCallContext,
        ) -> Awaitable[None]: ...
        def newInstance(
            self,
            _context: contexts.NewinstanceCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _IdentifiableInterfaceModule.Server
            | IdentifiableClient
            | results_tuples.NewinstanceResultTuple
            | None
        ]: ...
        def newInstance_context(
            self,
            context: contexts.NewinstanceCallContext,
        ) -> Awaitable[None]: ...
        def newInstances(
            self,
            numberOfInstances: int,
            _context: contexts.NewinstancesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.IdentifiableClientListBuilder
            | readers.IdentifiableClientListReader
            | Sequence[Any]
            | results_tuples.NewinstancesResultTuple
            | None
        ]: ...
        def newInstances_context(
            self,
            context: contexts.NewinstancesCallContext,
        ) -> Awaitable[None]: ...
