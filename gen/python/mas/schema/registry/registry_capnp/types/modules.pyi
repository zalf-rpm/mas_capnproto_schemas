"""Module helper types for `registry.capnp`."""

from collections.abc import Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceMethod,
    _InterfaceModule,
    _InterfaceSchema,
    _ListSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.common.common_capnp.types import (
    schemas as _mas_schema_common_common_capnp_schemas,
)
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.persistence.persistence_capnp.types import (
    schemas as _mas_schema_persistence_persistence_capnp_schemas,
)
from mas.schema.persistence.persistence_capnp.types.builders import VatIdBuilder
from mas.schema.persistence.persistence_capnp.types.clients import RestorerClient
from mas.schema.persistence.persistence_capnp.types.modules import (
    _RestorerInterfaceModule,
)
from mas.schema.registry.registry_capnp.types import builders as builders
from mas.schema.registry.registry_capnp.types import clients as clients
from mas.schema.registry.registry_capnp.types import contexts as contexts
from mas.schema.registry.registry_capnp.types import readers as readers
from mas.schema.registry.registry_capnp.types import schemas as schemas
from mas.schema.registry.registry_capnp.types import servers as servers
from mas.schema.registry.registry_capnp.types.results import tuples as results_tuples

class _AdminInterfaceModule(_IdentifiableInterfaceModule):
    class _AdminSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _AdminInterfaceModule._AdminSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _AdminInterfaceModuleAddCategoryParamSchema(_StructSchema):
            class _CategoryField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_common_capnp_schemas._IdInformationSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["category"],
                ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleAddCategoryParamSchema._CategoryField: ...
                @overload
                def __getitem__(self, key: Literal["upsert"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleAddCategoryParamSchema._Fields: ...

        class _AdminInterfaceModuleAddCategoryResultSchema(_StructSchema):
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
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleAddCategoryResultSchema._Fields: ...

        class _AdminInterfaceModuleAddCategoryMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleAddCategoryParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleAddCategoryResultSchema: ...

        class _AdminInterfaceModuleRemoveCategoryParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["categoryId"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["moveObjectsToCategoryId"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveCategoryParamSchema._Fields: ...

        class _AdminInterfaceModuleRemoveCategoryResultSchema(_StructSchema):
            class _RemovedObjectsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _InterfaceSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveCategoryResultSchema._RemovedObjectsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["removedObjects"],
                ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveCategoryResultSchema._RemovedObjectsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveCategoryResultSchema._Fields: ...

        class _AdminInterfaceModuleRemoveCategoryMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveCategoryParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveCategoryResultSchema: ...

        class _AdminInterfaceModuleMoveObjectsParamSchema(_StructSchema):
            class _ObjectIdsField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _ListSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["objectIds"],
                ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleMoveObjectsParamSchema._ObjectIdsField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["toCatId"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleMoveObjectsParamSchema._Fields: ...

        class _AdminInterfaceModuleMoveObjectsResultSchema(_StructSchema):
            class _MovedObjectIdsField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _ListSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["movedObjectIds"],
                ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleMoveObjectsResultSchema._MovedObjectIdsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleMoveObjectsResultSchema._Fields: ...

        class _AdminInterfaceModuleMoveObjectsMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleMoveObjectsParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleMoveObjectsResultSchema: ...

        class _AdminInterfaceModuleRemoveObjectsParamSchema(_StructSchema):
            class _ObjectIdsField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _ListSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["objectIds"],
                ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveObjectsParamSchema._ObjectIdsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveObjectsParamSchema._Fields: ...

        class _AdminInterfaceModuleRemoveObjectsResultSchema(_StructSchema):
            class _RemovedObjectsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _InterfaceSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveObjectsResultSchema._RemovedObjectsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["removedObjects"],
                ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveObjectsResultSchema._RemovedObjectsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveObjectsResultSchema._Fields: ...

        class _AdminInterfaceModuleRemoveObjectsMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveObjectsParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveObjectsResultSchema: ...

        class _AdminInterfaceModuleRegistryParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRegistryParamSchema._Fields: ...

        class _AdminInterfaceModuleRegistryResultSchema(_StructSchema):
            class _RegistryField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["registry"],
                ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRegistryResultSchema._RegistryField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRegistryResultSchema._Fields: ...

        class _AdminInterfaceModuleRegistryMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRegistryParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRegistryResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _AdminInterfaceModule._AdminSchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["addCategory"],
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleAddCategoryMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["removeCategory"],
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveCategoryMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["moveObjects"],
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleMoveObjectsMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["removeObjects"],
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRemoveObjectsMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["registry"],
            ) -> (
                _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleRegistryMethod
            ): ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(self) -> _AdminInterfaceModule._AdminSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._AdminSchema: ...
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> clients.AdminClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def addCategory(
            self,
            category: IdInformationReader,
            upsert: bool,
            _context: contexts.AddcategoryCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | results_tuples.AddcategoryResultTuple | None]: ...
        def addCategory_context(
            self,
            context: contexts.AddcategoryCallContext,
        ) -> Awaitable[None]: ...
        def removeCategory(
            self,
            categoryId: str,
            moveObjectsToCategoryId: str,
            _context: contexts.RemovecategoryCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.IdentifiableClientListBuilder
            | readers.IdentifiableClientListReader
            | Sequence[Any]
            | results_tuples.RemovecategoryResultTuple
            | None
        ]: ...
        def removeCategory_context(
            self,
            context: contexts.RemovecategoryCallContext,
        ) -> Awaitable[None]: ...
        def moveObjects(
            self,
            objectIds: readers.TextListReader,
            toCatId: str,
            _context: contexts.MoveobjectsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.TextListBuilder
            | readers.TextListReader
            | Sequence[Any]
            | results_tuples.MoveobjectsResultTuple
            | None
        ]: ...
        def moveObjects_context(
            self,
            context: contexts.MoveobjectsCallContext,
        ) -> Awaitable[None]: ...
        def removeObjects(
            self,
            objectIds: readers.TextListReader,
            _context: contexts.RemoveobjectsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.IdentifiableClientListBuilder
            | readers.IdentifiableClientListReader
            | Sequence[Any]
            | results_tuples.RemoveobjectsResultTuple
            | None
        ]: ...
        def removeObjects_context(
            self,
            context: contexts.RemoveobjectsCallContext,
        ) -> Awaitable[None]: ...
        def registry(
            self,
            _context: contexts.RegistryCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _RegistryInterfaceModule.Server
            | clients.RegistryClient
            | results_tuples.RegistryResultTuple
            | None
        ]: ...
        def registry_context(
            self,
            context: contexts.RegistryCallContext,
        ) -> Awaitable[None]: ...

class _RegistryInterfaceModule(_IdentifiableInterfaceModule):
    class _EntryStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _EntrySchema(_StructSchema):
            class _RefField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["categoryId"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["ref"],
                ) -> (
                    _RegistryInterfaceModule._EntryStructModule._EntrySchema._RefField
                ): ...
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _RegistryInterfaceModule._EntryStructModule._EntrySchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._RegistryEntrySchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            categoryId: str | None = None,
            ref: IdentifiableClient | _IdentifiableInterfaceModule.Server | None = None,
            name: str | None = None,
            id: str | None = None,
            **kwargs: object,
        ) -> builders.EntryBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.EntryBuilder]: ...
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
        ) -> readers.EntryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EntryReader: ...

    Entry: _EntryStructModule
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.RegistryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def supportedCategories(
            self,
            _context: contexts.SupportedcategoriesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.IdInformationListBuilder
            | readers.IdInformationListReader
            | Sequence[Any]
            | results_tuples.SupportedcategoriesResultTuple
            | None
        ]: ...
        def supportedCategories_context(
            self,
            context: contexts.SupportedcategoriesCallContext,
        ) -> Awaitable[None]: ...
        def categoryInfo(
            self,
            categoryId: str,
            _context: contexts.CategoryinfoCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.CategoryinfoResultTuple | None]: ...
        def categoryInfo_context(
            self,
            context: contexts.CategoryinfoCallContext,
        ) -> Awaitable[None]: ...
        def entries(
            self,
            categoryId: str,
            _context: contexts.EntriesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.EntryListBuilder
            | readers.EntryListReader
            | Sequence[Any]
            | results_tuples.EntriesResultTuple
            | None
        ]: ...
        def entries_context(
            self,
            context: contexts.EntriesCallContext,
        ) -> Awaitable[None]: ...

class _RegistrarInterfaceModule(_IdentifiableInterfaceModule):
    class _CrossDomainRestoreStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _CrossDomainRestoreSchema(_StructSchema):
            class _VatIdField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_persistence_persistence_capnp_schemas._VatIdSchema: ...

            class _RestorerField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["vatId"],
                ) -> _RegistrarInterfaceModule._CrossDomainRestoreStructModule._CrossDomainRestoreSchema._VatIdField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["restorer"],
                ) -> _RegistrarInterfaceModule._CrossDomainRestoreStructModule._CrossDomainRestoreSchema._RestorerField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _RegistrarInterfaceModule._CrossDomainRestoreStructModule._CrossDomainRestoreSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._RegistrarCrossDomainRestoreSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            vatId: VatIdBuilder | dict[str, Any] | None = None,
            restorer: RestorerClient | _RestorerInterfaceModule.Server | None = None,
            **kwargs: object,
        ) -> builders.CrossDomainRestoreBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.CrossDomainRestoreReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.CrossDomainRestoreReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.CrossDomainRestoreBuilder]: ...
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
        ) -> readers.CrossDomainRestoreReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CrossDomainRestoreReader: ...

    CrossDomainRestore: _CrossDomainRestoreStructModule
    class _RegParamsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _RegParamsSchema(_StructSchema):
            class _CapField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _XDomainField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._RegistrarCrossDomainRestoreSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["cap"],
                ) -> _RegistrarInterfaceModule._RegParamsStructModule._RegParamsSchema._CapField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["regName"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["categoryId"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["xDomain"],
                ) -> _RegistrarInterfaceModule._RegParamsStructModule._RegParamsSchema._XDomainField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _RegistrarInterfaceModule._RegParamsStructModule._RegParamsSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._RegistrarRegParamsSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            cap: IdentifiableClient | _IdentifiableInterfaceModule.Server | None = None,
            regName: str | None = None,
            categoryId: str | None = None,
            xDomain: builders.CrossDomainRestoreBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> builders.RegParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.RegParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.RegParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.RegParamsBuilder]: ...
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
        ) -> readers.RegParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.RegParamsReader: ...

    RegParams: _RegParamsStructModule
    class _UnregisterInterfaceModule(_InterfaceModule):
        class _UnregisterSchema(_InterfaceSchema):
            class _UnregisterInterfaceModuleUnregisterParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _RegistrarInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterParamSchema._Fields: ...

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
                ) -> _RegistrarInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterResultSchema._Fields: ...

            class _UnregisterInterfaceModuleUnregisterMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _RegistrarInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _RegistrarInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["unregister"],
                ) -> _RegistrarInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> _RegistrarInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._RegistrarUnregisterSchema: ...
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
    type UnregisterServer = _RegistrarInterfaceModule._UnregisterInterfaceModule.Server

    class _RegistrarSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _RegistrarInterfaceModule._RegistrarSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _RegistrarInterfaceModule._RegistrarSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _RegistrarInterfaceModule._RegistrarSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _RegistrarInterfaceModule._RegistrarSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _RegistrarInterfaceModuleRegisterParamSchema(_StructSchema):
            class _CapField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _XDomainField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._RegistrarCrossDomainRestoreSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["cap"],
                ) -> _RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterParamSchema._CapField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["regName"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["categoryId"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["xDomain"],
                ) -> _RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterParamSchema._XDomainField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterParamSchema._Fields: ...

        class _RegistrarInterfaceModuleRegisterResultSchema(_StructSchema):
            class _UnregField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._RegistrarUnregisterSchema: ...

            class _ReregSRField(_StructSchemaField):
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
                    key: Literal["unreg"],
                ) -> _RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterResultSchema._UnregField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["reregSR"],
                ) -> _RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterResultSchema._ReregSRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterResultSchema._Fields: ...

        class _RegistrarInterfaceModuleRegisterMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _RegistrarInterfaceModule._RegistrarSchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["register"],
            ) -> _RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(self) -> _RegistrarInterfaceModule._RegistrarSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._RegistrarSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.RegistrarClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def register(
            self,
            cap: IdentifiableClient,
            regName: str,
            categoryId: str,
            xDomain: readers.CrossDomainRestoreReader,
            _context: contexts.RegisterCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.RegisterResultTuple | None]: ...
        def register_context(
            self,
            context: contexts.RegisterCallContext,
        ) -> Awaitable[None]: ...
