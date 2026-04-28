"""Module helper types for `config.capnp`."""

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

from mas.schema.config.config_capnp.types import clients as clients
from mas.schema.config.config_capnp.types import contexts as contexts
from mas.schema.config.config_capnp.types import schemas as schemas
from mas.schema.config.config_capnp.types.results import tuples as results_tuples

class _ServiceInterfaceModule(_InterfaceModule):
    class _ServiceSchema(_InterfaceSchema):
        class _ServiceInterfaceModuleNextConfigParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleNextConfigParamSchema._Fields: ...

        class _ServiceInterfaceModuleNextConfigResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["config"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["noFurtherConfigs"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleNextConfigResultSchema._Fields: ...

        class _ServiceInterfaceModuleNextConfigMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleNextConfigParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleNextConfigResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["nextConfig"],
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleNextConfigMethod: ...
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
    class Server(_DynamicCapabilityServer):
        def nextConfig(
            self,
            _context: contexts.NextconfigCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.NextconfigResultTuple | None]: ...
        def nextConfig_context(
            self,
            context: contexts.NextconfigCallContext,
        ) -> Awaitable[None]: ...
