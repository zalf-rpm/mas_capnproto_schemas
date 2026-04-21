"""Module helper types for `web_berest_data_import.capnp`."""

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

from mas.schema.model.weberest.web_berest_data_import_capnp.types import (
    clients as clients,
)
from mas.schema.model.weberest.web_berest_data_import_capnp.types import (
    contexts as contexts,
)
from mas.schema.model.weberest.web_berest_data_import_capnp.types import (
    schemas as schemas,
)
from mas.schema.model.weberest.web_berest_data_import_capnp.types.results import (
    tuples as results_tuples,
)

class _DWLABImportInterfaceModule(_InterfaceModule):
    class _DWLABImportSchema(_InterfaceSchema):
        class _DWLABImportInterfaceModuleImportDataParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["dwla"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["dwlb"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _DWLABImportInterfaceModule._DWLABImportSchema._DWLABImportInterfaceModuleImportDataParamSchema._Fields: ...

        class _DWLABImportInterfaceModuleImportDataResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["successA"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["successB"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _DWLABImportInterfaceModule._DWLABImportSchema._DWLABImportInterfaceModuleImportDataResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["importData"],
            ) -> _InterfaceMethod[
                _DWLABImportInterfaceModule._DWLABImportSchema._DWLABImportInterfaceModuleImportDataParamSchema,
                _DWLABImportInterfaceModule._DWLABImportSchema._DWLABImportInterfaceModuleImportDataResultSchema,
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
        ) -> _DWLABImportInterfaceModule._DWLABImportSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._DWLABImportSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.DWLABImportClient: ...
    class Server(_DynamicCapabilityServer):
        def importData(
            self,
            id: str,
            dwla: bytes,
            dwlb: bytes,
            _context: contexts.ImportdataCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.ImportdataResultTuple | None]: ...
        def importData_context(
            self,
            context: contexts.ImportdataCallContext,
        ) -> Awaitable[None]: ...
