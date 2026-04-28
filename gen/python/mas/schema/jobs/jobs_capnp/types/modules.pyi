"""Module helper types for `jobs.capnp`."""

from collections.abc import Awaitable, Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceMethod,
    _InterfaceSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.jobs.jobs_capnp.types import builders as builders
from mas.schema.jobs.jobs_capnp.types import clients as clients
from mas.schema.jobs.jobs_capnp.types import common as common
from mas.schema.jobs.jobs_capnp.types import contexts as contexts
from mas.schema.jobs.jobs_capnp.types import readers as readers
from mas.schema.jobs.jobs_capnp.types import schemas as schemas
from mas.schema.jobs.jobs_capnp.types.results import tuples as results_tuples
from mas.schema.persistence.persistence_capnp.types import (
    schemas as _mas_schema_persistence_persistence_capnp_schemas,
)
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)

class _JobStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _JobSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["data"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["noFurtherJobs"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _JobStructModule._JobSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._JobSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        data: common.AnyPointer | None = None,
        noFurtherJobs: bool | None = None,
        **kwargs: object,
    ) -> builders.JobBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.JobReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.JobReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.JobBuilder]: ...
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
    ) -> readers.JobReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.JobReader: ...

class _ServiceInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _ServiceSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

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
                ) -> _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

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
                ) -> _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["unsaveSR"],
                ) -> _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

        class _PersistentInterfaceModuleSaveMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveResultSchema: ...

        class _ServiceInterfaceModuleNextJobParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleNextJobParamSchema._Fields: ...

        class _ServiceInterfaceModuleNextJobResultSchema(_StructSchema):
            class _JobField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._JobSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["job"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleNextJobResultSchema._JobField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleNextJobResultSchema._Fields: ...

        class _ServiceInterfaceModuleNextJobMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleNextJobParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleNextJobResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["save"],
            ) -> _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nextJob"],
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleNextJobMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(self) -> _ServiceInterfaceModule._ServiceSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._ServiceSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.ServiceClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def nextJob(
            self,
            _context: contexts.NextjobCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.JobBuilder
            | readers.JobReader
            | dict[str, Any]
            | results_tuples.NextjobResultTuple
            | None
        ]: ...
        def nextJob_context(
            self,
            context: contexts.NextjobCallContext,
        ) -> Awaitable[None]: ...
