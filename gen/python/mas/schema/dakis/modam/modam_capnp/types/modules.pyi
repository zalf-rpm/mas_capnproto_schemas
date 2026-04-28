"""Module helper types for `modam.capnp`."""

from collections.abc import Awaitable
from typing import Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _InterfaceMethod,
    _InterfaceModule,
    _InterfaceSchema,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.dakis.modam.modam_capnp.types import clients as clients
from mas.schema.dakis.modam.modam_capnp.types import contexts as contexts
from mas.schema.dakis.modam.modam_capnp.types import schemas as schemas
from mas.schema.dakis.modam.modam_capnp.types.results import tuples as results_tuples

class _ModamWrapperServiceInterfaceModule(_InterfaceModule):
    class _ModamWrapperServiceSchema(_InterfaceSchema):
        class _ModamWrapperServiceInterfaceModuleRunAemModelParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["input"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ModamWrapperServiceInterfaceModule._ModamWrapperServiceSchema._ModamWrapperServiceInterfaceModuleRunAemModelParamSchema._Fields: ...

        class _ModamWrapperServiceInterfaceModuleRunAemModelResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["output"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ModamWrapperServiceInterfaceModule._ModamWrapperServiceSchema._ModamWrapperServiceInterfaceModuleRunAemModelResultSchema._Fields: ...

        class _ModamWrapperServiceInterfaceModuleRunAemModelMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ModamWrapperServiceInterfaceModule._ModamWrapperServiceSchema._ModamWrapperServiceInterfaceModuleRunAemModelParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ModamWrapperServiceInterfaceModule._ModamWrapperServiceSchema._ModamWrapperServiceInterfaceModuleRunAemModelResultSchema: ...

        class _ModamWrapperServiceInterfaceModuleRunFieldModelParamSchema(
            _StructSchema,
        ):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["input"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ModamWrapperServiceInterfaceModule._ModamWrapperServiceSchema._ModamWrapperServiceInterfaceModuleRunFieldModelParamSchema._Fields: ...

        class _ModamWrapperServiceInterfaceModuleRunFieldModelResultSchema(
            _StructSchema,
        ):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["output"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ModamWrapperServiceInterfaceModule._ModamWrapperServiceSchema._ModamWrapperServiceInterfaceModuleRunFieldModelResultSchema._Fields: ...

        class _ModamWrapperServiceInterfaceModuleRunFieldModelMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ModamWrapperServiceInterfaceModule._ModamWrapperServiceSchema._ModamWrapperServiceInterfaceModuleRunFieldModelParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ModamWrapperServiceInterfaceModule._ModamWrapperServiceSchema._ModamWrapperServiceInterfaceModuleRunFieldModelResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["runAemModel"],
            ) -> _ModamWrapperServiceInterfaceModule._ModamWrapperServiceSchema._ModamWrapperServiceInterfaceModuleRunAemModelMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["runFieldModel"],
            ) -> _ModamWrapperServiceInterfaceModule._ModamWrapperServiceSchema._ModamWrapperServiceInterfaceModuleRunFieldModelMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(
            self,
        ) -> (
            _ModamWrapperServiceInterfaceModule._ModamWrapperServiceSchema._Methods
        ): ...

    @property
    @override
    def schema(self) -> schemas._ModamWrapperServiceSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.ModamWrapperServiceClient: ...
    class Server(_DynamicCapabilityServer):
        def runAemModel(
            self,
            input: str,
            _context: contexts.RunaemmodelCallContext,
            **kwargs: object,
        ) -> Awaitable[str | results_tuples.RunaemmodelResultTuple | None]: ...
        def runAemModel_context(
            self,
            context: contexts.RunaemmodelCallContext,
        ) -> Awaitable[None]: ...
        def runFieldModel(
            self,
            input: str,
            _context: contexts.RunfieldmodelCallContext,
            **kwargs: object,
        ) -> Awaitable[str | results_tuples.RunfieldmodelResultTuple | None]: ...
        def runFieldModel_context(
            self,
            context: contexts.RunfieldmodelCallContext,
        ) -> Awaitable[None]: ...
