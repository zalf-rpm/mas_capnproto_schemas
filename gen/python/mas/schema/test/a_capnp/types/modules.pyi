"""Module helper types for `a.capnp`."""

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

from mas.schema.test.a_capnp.types import clients as clients
from mas.schema.test.a_capnp.types import contexts as contexts
from mas.schema.test.a_capnp.types import schemas as schemas
from mas.schema.test.a_capnp.types.results import tuples as results_tuples

class _AInterfaceModule(_InterfaceModule):
    class _ASchema(_InterfaceSchema):
        class _AInterfaceModuleMethodParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["param"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> (
                _AInterfaceModule._ASchema._AInterfaceModuleMethodParamSchema._Fields
            ): ...

        class _AInterfaceModuleMethodResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["res"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> (
                _AInterfaceModule._ASchema._AInterfaceModuleMethodResultSchema._Fields
            ): ...

        class _AInterfaceModuleMethodMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _AInterfaceModule._ASchema._AInterfaceModuleMethodParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _AInterfaceModule._ASchema._AInterfaceModuleMethodResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["method"],
            ) -> _AInterfaceModule._ASchema._AInterfaceModuleMethodMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(self) -> _AInterfaceModule._ASchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._ASchema: ...
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> clients.AClient: ...
    class Server(_DynamicCapabilityServer):
        def method(
            self,
            param: str,
            _context: contexts.MethodCallContext,
            **kwargs: object,
        ) -> Awaitable[str | results_tuples.MethodResultTuple | None]: ...
        def method_context(
            self,
            context: contexts.MethodCallContext,
        ) -> Awaitable[None]: ...
