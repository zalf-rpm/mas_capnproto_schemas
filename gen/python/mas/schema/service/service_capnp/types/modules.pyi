"""Module helper types for `service.capnp`."""

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

from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.service.service_capnp.types import builders as builders
from mas.schema.service.service_capnp.types import clients as clients
from mas.schema.service.service_capnp.types import common as common
from mas.schema.service.service_capnp.types import contexts as contexts
from mas.schema.service.service_capnp.types import readers as readers
from mas.schema.service.service_capnp.types import schemas as schemas
from mas.schema.service.service_capnp.types.results import tuples as results_tuples

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

        class _AdminInterfaceModuleHeartbeatParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleHeartbeatParamSchema._Fields: ...

        class _AdminInterfaceModuleHeartbeatResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleHeartbeatResultSchema._Fields: ...

        class _AdminInterfaceModuleSetTimeoutParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["seconds"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleSetTimeoutParamSchema._Fields: ...

        class _AdminInterfaceModuleSetTimeoutResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleSetTimeoutResultSchema._Fields: ...

        class _AdminInterfaceModuleStopParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleStopParamSchema._Fields: ...

        class _AdminInterfaceModuleStopResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleStopResultSchema._Fields: ...

        class _AdminInterfaceModuleIdentitiesParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleIdentitiesParamSchema._Fields: ...

        class _AdminInterfaceModuleIdentitiesResultSchema(_StructSchema):
            class _InfosField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _StructSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleIdentitiesResultSchema._InfosField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["infos"],
                ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleIdentitiesResultSchema._InfosField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleIdentitiesResultSchema._Fields: ...

        class _AdminInterfaceModuleUpdateIdentityParamSchema(_StructSchema):
            class _NewInfoField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _StructSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["oldId"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["newInfo"],
                ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleUpdateIdentityParamSchema._NewInfoField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleUpdateIdentityParamSchema._Fields: ...

        class _AdminInterfaceModuleUpdateIdentityResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleUpdateIdentityResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _InterfaceMethod[
                _AdminInterfaceModule._AdminSchema._IdentifiableInterfaceModuleInfoParamSchema,
                _AdminInterfaceModule._AdminSchema._IdentifiableInterfaceModuleInfoResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["heartbeat"],
            ) -> _InterfaceMethod[
                _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleHeartbeatParamSchema,
                _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleHeartbeatResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["setTimeout"],
            ) -> _InterfaceMethod[
                _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleSetTimeoutParamSchema,
                _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleSetTimeoutResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stop"],
            ) -> _InterfaceMethod[
                _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleStopParamSchema,
                _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleStopResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["identities"],
            ) -> _InterfaceMethod[
                _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleIdentitiesParamSchema,
                _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleIdentitiesResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["updateIdentity"],
            ) -> _InterfaceMethod[
                _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleUpdateIdentityParamSchema,
                _AdminInterfaceModule._AdminSchema._AdminInterfaceModuleUpdateIdentityResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: str,
            ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

        @property
        @override
        def methods(self) -> _AdminInterfaceModule._AdminSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._AdminSchema: ...
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> clients.AdminClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def heartbeat(
            self,
            _context: contexts.HeartbeatCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def heartbeat_context(
            self,
            context: contexts.HeartbeatCallContext,
        ) -> Awaitable[None]: ...
        def setTimeout(
            self,
            seconds: int,
            _context: contexts.SettimeoutCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def setTimeout_context(
            self,
            context: contexts.SettimeoutCallContext,
        ) -> Awaitable[None]: ...
        def stop(
            self,
            _context: contexts.AdminStopCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def stop_context(
            self,
            context: contexts.AdminStopCallContext,
        ) -> Awaitable[None]: ...
        def identities(
            self,
            _context: contexts.IdentitiesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.IdInformationListBuilder
            | readers.IdInformationListReader
            | Sequence[Any]
            | results_tuples.IdentitiesResultTuple
            | None
        ]: ...
        def identities_context(
            self,
            context: contexts.IdentitiesCallContext,
        ) -> Awaitable[None]: ...
        def updateIdentity(
            self,
            oldId: str,
            newInfo: IdInformationReader,
            _context: contexts.UpdateidentityCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def updateIdentity_context(
            self,
            context: contexts.UpdateidentityCallContext,
        ) -> Awaitable[None]: ...

class _SimpleFactoryInterfaceModule(_IdentifiableInterfaceModule):
    class _SimpleFactorySchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _SimpleFactoryInterfaceModule._SimpleFactorySchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _SimpleFactoryInterfaceModule._SimpleFactorySchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _SimpleFactoryInterfaceModuleCreateParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _SimpleFactoryInterfaceModule._SimpleFactorySchema._SimpleFactoryInterfaceModuleCreateParamSchema._Fields: ...

        class _SimpleFactoryInterfaceModuleCreateResultSchema(_StructSchema):
            class _CapsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _InterfaceSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _SimpleFactoryInterfaceModule._SimpleFactorySchema._SimpleFactoryInterfaceModuleCreateResultSchema._CapsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["caps"],
                ) -> _SimpleFactoryInterfaceModule._SimpleFactorySchema._SimpleFactoryInterfaceModuleCreateResultSchema._CapsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _SimpleFactoryInterfaceModule._SimpleFactorySchema._SimpleFactoryInterfaceModuleCreateResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _InterfaceMethod[
                _SimpleFactoryInterfaceModule._SimpleFactorySchema._IdentifiableInterfaceModuleInfoParamSchema,
                _SimpleFactoryInterfaceModule._SimpleFactorySchema._IdentifiableInterfaceModuleInfoResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["create"],
            ) -> _InterfaceMethod[
                _SimpleFactoryInterfaceModule._SimpleFactorySchema._SimpleFactoryInterfaceModuleCreateParamSchema,
                _SimpleFactoryInterfaceModule._SimpleFactorySchema._SimpleFactoryInterfaceModuleCreateResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: str,
            ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

        @property
        @override
        def methods(
            self,
        ) -> _SimpleFactoryInterfaceModule._SimpleFactorySchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._SimpleFactorySchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.SimpleFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def create(
            self,
            _context: contexts.SimpleFactoryCreateCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.IdentifiableClientListBuilder
            | readers.IdentifiableClientListReader
            | Sequence[Any]
            | results_tuples.SimpleFactoryCreateResultTuple
            | None
        ]: ...
        def create_context(
            self,
            context: contexts.SimpleFactoryCreateCallContext,
        ) -> Awaitable[None]: ...

class _FactoryInterfaceModule(_IdentifiableInterfaceModule):
    class _CreateParamsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _CreateParamsSchema(_StructSchema):
            class _InterfaceNameToRegistrySRField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _StructSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _FactoryInterfaceModule._CreateParamsStructModule._CreateParamsSchema._InterfaceNameToRegistrySRField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["timeoutSeconds"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["interfaceNameToRegistrySR"],
                ) -> _FactoryInterfaceModule._CreateParamsStructModule._CreateParamsSchema._InterfaceNameToRegistrySRField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["msgPayload"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FactoryInterfaceModule._CreateParamsStructModule._CreateParamsSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._FactoryCreateParamsSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            timeoutSeconds: int | None = None,
            interfaceNameToRegistrySR: builders.PairListBuilder
            | dict[str, Any]
            | None = None,
            msgPayload: common.AnyPointer | None = None,
            **kwargs: object,
        ) -> builders.CreateParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.CreateParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.CreateParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.CreateParamsBuilder]: ...
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
        ) -> readers.CreateParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CreateParamsReader: ...

    CreateParams: _CreateParamsStructModule
    class _AccessInfoStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _AccessInfoSchema(_StructSchema):
            class _ServiceCapsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _InterfaceSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _FactoryInterfaceModule._AccessInfoStructModule._AccessInfoSchema._ServiceCapsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["adminCap"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["serviceCaps"],
                ) -> _FactoryInterfaceModule._AccessInfoStructModule._AccessInfoSchema._ServiceCapsField: ...
                @overload
                def __getitem__(self, key: Literal["error"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FactoryInterfaceModule._AccessInfoStructModule._AccessInfoSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._FactoryAccessInfoSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            adminCap: common.Capability | None = None,
            serviceCaps: builders.IdentifiableClientListBuilder
            | dict[str, Any]
            | None = None,
            error: str | None = None,
            **kwargs: object,
        ) -> builders.AccessInfoBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.AccessInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.AccessInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.AccessInfoBuilder]: ...
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
        ) -> readers.AccessInfoReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AccessInfoReader: ...

    AccessInfo: _AccessInfoStructModule

    class _FactorySchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _FactoryInterfaceModuleCreateParamSchema(_StructSchema):
            class _InterfaceNameToRegistrySRField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _StructSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateParamSchema._InterfaceNameToRegistrySRField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["timeoutSeconds"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["interfaceNameToRegistrySR"],
                ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateParamSchema._InterfaceNameToRegistrySRField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["msgPayload"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateParamSchema._Fields: ...

        class _FactoryInterfaceModuleCreateResultSchema(_StructSchema):
            class _ServiceCapsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _InterfaceSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateResultSchema._ServiceCapsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["adminCap"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["serviceCaps"],
                ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateResultSchema._ServiceCapsField: ...
                @overload
                def __getitem__(self, key: Literal["error"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateResultSchema._Fields: ...

        class _FactoryInterfaceModuleServiceInterfaceNamesParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleServiceInterfaceNamesParamSchema._Fields: ...

        class _FactoryInterfaceModuleServiceInterfaceNamesResultSchema(_StructSchema):
            class _NamesField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _ListSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["names"],
                ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleServiceInterfaceNamesResultSchema._NamesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleServiceInterfaceNamesResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _InterfaceMethod[
                _FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoParamSchema,
                _FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["create"],
            ) -> _InterfaceMethod[
                _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateParamSchema,
                _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["serviceInterfaceNames"],
            ) -> _InterfaceMethod[
                _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleServiceInterfaceNamesParamSchema,
                _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleServiceInterfaceNamesResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: str,
            ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

        @property
        @override
        def methods(self) -> _FactoryInterfaceModule._FactorySchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._FactorySchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.FactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def create(
            self,
            timeoutSeconds: int,
            interfaceNameToRegistrySR: readers.PairListReader,
            msgPayload: common.AnyPointer,
            _context: contexts.FactoryCreateCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.FactoryCreateResultTuple | None]: ...
        def create_context(
            self,
            context: contexts.FactoryCreateCallContext,
        ) -> Awaitable[None]: ...
        def serviceInterfaceNames(
            self,
            _context: contexts.ServiceinterfacenamesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.TextListBuilder
            | readers.TextListReader
            | Sequence[Any]
            | results_tuples.ServiceinterfacenamesResultTuple
            | None
        ]: ...
        def serviceInterfaceNames_context(
            self,
            context: contexts.ServiceinterfacenamesCallContext,
        ) -> Awaitable[None]: ...

class _StoppableInterfaceModule(_InterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.StoppableClient: ...
    class Server(_DynamicCapabilityServer):
        def stop(
            self,
            _context: contexts.StoppableStopCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | results_tuples.StoppableStopResultTuple | None]: ...
        def stop_context(
            self,
            context: contexts.StoppableStopCallContext,
        ) -> Awaitable[None]: ...
