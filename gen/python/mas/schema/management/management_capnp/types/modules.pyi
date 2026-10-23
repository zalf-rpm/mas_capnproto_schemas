"""Module helper types for `management.capnp`."""

from collections.abc import Awaitable, Callable, Iterator, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _AsyncIoStream,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _EnumModule,
    _EnumSchema,
    _InterfaceMethod,
    _InterfaceSchema,
    _ListSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.common.common_capnp.types import (
    schemas as _mas_schema_common_common_capnp_schemas,
)
from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.common.date_capnp.types import (
    schemas as _mas_schema_common_date_capnp_schemas,
)
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.crop.crop_capnp.types import (
    schemas as _mas_schema_crop_crop_capnp_schemas,
)
from mas.schema.crop.crop_capnp.types.clients import CropClient
from mas.schema.crop.crop_capnp.types.modules import _CropInterfaceModule
from mas.schema.management.management_capnp.types import builders as builders
from mas.schema.management.management_capnp.types import clients as clients
from mas.schema.management.management_capnp.types import common as common
from mas.schema.management.management_capnp.types import contexts as contexts
from mas.schema.management.management_capnp.types import enums as enums
from mas.schema.management.management_capnp.types import readers as readers
from mas.schema.management.management_capnp.types import schemas as schemas
from mas.schema.management.management_capnp.types.results import (
    tuples as results_tuples,
)
from mas.schema.persistence.persistence_capnp.types import (
    schemas as _mas_schema_persistence_persistence_capnp_schemas,
)
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)
from mas.schema.registry.registry_capnp.types import (
    schemas as _mas_schema_registry_registry_capnp_schemas,
)
from mas.schema.registry.registry_capnp.types.modules import _RegistryInterfaceModule

class _EventTypeEnumModule(_EnumModule):
    sowing: int
    automaticSowing: int
    harvest: int
    automaticHarvest: int
    irrigation: int
    tillage: int
    organicFertilization: int
    mineralFertilization: int
    nDemandFertilization: int
    cutting: int
    setValue: int
    saveState: int

    class _EventTypeSchema(_EnumSchema): ...

class _PlantOrganEnumModule(_EnumModule):
    root: int
    leaf: int
    shoot: int
    fruit: int
    strukt: int
    sugar: int

    class _PlantOrganSchema(_EnumSchema): ...

class _EventStructModule(_StructModule):
    class _ExternalTypeEnumModule(_EnumModule):
        sowing: int
        automaticSowing: int
        harvest: int
        automaticHarvest: int
        irrigation: int
        tillage: int
        organicFertilization: int
        mineralFertilization: int
        nDemandFertilization: int
        cutting: int

        class _ExternalTypeSchema(_EnumSchema): ...

    ExternalType: _ExternalTypeEnumModule
    class _PhenoStageEnumModule(_EnumModule):
        emergence: int
        flowering: int
        anthesis: int
        maturity: int

        class _PhenoStageSchema(_EnumSchema): ...

    PhenoStage: _PhenoStageEnumModule
    class _TypeStructModule(_StructModule):
        Union: type[common._TypeModuleWhich]
        class Reader(_DynamicStructReader):
            @property
            @override
            def which(self) -> common._TypeWhich: ...

        class Builder(_DynamicStructBuilder):
            @property
            @override
            def which(self) -> common._TypeWhich: ...

        class _TypeSchema(_StructSchema):
            class _ExternalField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._EventExternalTypeEnumSchema: ...

            class _InternalField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._EventPhenoStageEnumSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["external"],
                ) -> (
                    _EventStructModule._TypeStructModule._TypeSchema._ExternalField
                ): ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["internal"],
                ) -> (
                    _EventStructModule._TypeStructModule._TypeSchema._InternalField
                ): ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _EventStructModule._TypeStructModule._TypeSchema._Fields: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            external: enums.EventExternalTypeValue
            | enums.EventExternalTypeEnum
            | None = None,
            internal: enums.EventPhenoStageValue
            | enums.EventPhenoStageEnum
            | None = None,
            **kwargs: object,
        ) -> builders.TypeBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.TypeBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.TypeReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.TypeReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.TypeBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.TypeBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.TypeReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.TypeReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.TypeReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.TypeReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.TypeReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.TypeReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.TypeReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.TypeReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.TypeReader]: ...

    Type: _TypeStructModule
    class _EventAtStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _EventAtSchema(_StructSchema):
            class _DateField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["date"],
                ) -> (
                    _EventStructModule._EventAtStructModule._EventAtSchema._DateField
                ): ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _EventStructModule._EventAtStructModule._EventAtSchema._Fields: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            date: DateBuilder | DateReader | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> builders.EventAtBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.EventAtBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.EventAtReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.EventAtReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.EventAtBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.EventAtBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventAtReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventAtReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventAtReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventAtReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventAtReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.EventAtReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.EventAtReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.EventAtReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.EventAtReader]: ...

    At: _EventAtStructModule
    class _EventBetweenStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _EventBetweenSchema(_StructSchema):
            class _EarliestField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

            class _LatestField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["earliest"],
                ) -> _EventStructModule._EventBetweenStructModule._EventBetweenSchema._EarliestField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["latest"],
                ) -> _EventStructModule._EventBetweenStructModule._EventBetweenSchema._LatestField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> (
                _EventStructModule._EventBetweenStructModule._EventBetweenSchema._Fields
            ): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            earliest: DateBuilder | DateReader | dict[str, Any] | None = None,
            latest: DateBuilder | DateReader | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> builders.EventBetweenBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.EventBetweenBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.EventBetweenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.EventBetweenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.EventBetweenBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.EventBetweenBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventBetweenReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventBetweenReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventBetweenReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventBetweenReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventBetweenReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.EventBetweenReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.EventBetweenReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.EventBetweenReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.EventBetweenReader]: ...

    Between: _EventBetweenStructModule
    class _EventAfterStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _EventAfterSchema(_StructSchema):
            class _EventField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._EventTypeSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["event"],
                ) -> _EventStructModule._EventAfterStructModule._EventAfterSchema._EventField: ...
                @overload
                def __getitem__(self, key: Literal["days"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> (
                _EventStructModule._EventAfterStructModule._EventAfterSchema._Fields
            ): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            event: builders.TypeBuilder
            | readers.TypeReader
            | dict[str, Any]
            | None = None,
            days: int | None = None,
            **kwargs: object,
        ) -> builders.EventAfterBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.EventAfterBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.EventAfterReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.EventAfterReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.EventAfterBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.EventAfterBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventAfterReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventAfterReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventAfterReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventAfterReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EventAfterReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.EventAfterReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.EventAfterReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.EventAfterReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.EventAfterReader]: ...

    After: _EventAfterStructModule
    class Reader(_DynamicStructReader):
        @property
        @override
        def which(self) -> common._EventWhich: ...

    class Builder(_DynamicStructBuilder):
        @property
        @override
        def which(self) -> common._EventWhich: ...

    class _EventSchema(_StructSchema):
        class _TypeField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._EventExternalTypeEnumSchema: ...

        class _InfoField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_common_common_capnp_schemas._IdInformationSchema: ...

        class _AtField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _StructSchema: ...

        class _BetweenField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _StructSchema: ...

        class _AfterField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _StructSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["type"],
            ) -> _EventStructModule._EventSchema._TypeField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _EventStructModule._EventSchema._InfoField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["at"],
            ) -> _EventStructModule._EventSchema._AtField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["between"],
            ) -> _EventStructModule._EventSchema._BetweenField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["after"],
            ) -> _EventStructModule._EventSchema._AfterField: ...
            @overload
            def __getitem__(self, key: Literal["params"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["runAtStartOfDay"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _EventStructModule._EventSchema._Fields: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        type: enums.EventExternalTypeValue | enums.EventExternalTypeEnum | None = None,
        info: IdInformationBuilder | IdInformationReader | dict[str, Any] | None = None,
        at: builders.EventAtBuilder
        | readers.EventAtReader
        | dict[str, Any]
        | None = None,
        between: builders.EventBetweenBuilder
        | readers.EventBetweenReader
        | dict[str, Any]
        | None = None,
        after: builders.EventAfterBuilder
        | readers.EventAfterReader
        | dict[str, Any]
        | None = None,
        params: common.AnyPointer | None = None,
        runAtStartOfDay: bool | None = None,
        **kwargs: object,
    ) -> builders.EventBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.EventBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.EventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.EventReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.EventBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.EventBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.EventReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.EventReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.EventReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.EventReader: ...
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.EventReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.EventReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.EventReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.EventReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.EventReader]: ...

class _FertilizerInterfaceModule(
    _IdentifiableInterfaceModule,
    _PersistentInterfaceModule,
):
    class _FertilizerSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _FertilizerInterfaceModule._FertilizerSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

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
                ) -> _FertilizerInterfaceModule._FertilizerSchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

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
                ) -> _FertilizerInterfaceModule._FertilizerSchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["unsaveSR"],
                ) -> _FertilizerInterfaceModule._FertilizerSchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

        class _PersistentInterfaceModuleSaveMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._PersistentInterfaceModuleSaveParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._PersistentInterfaceModuleSaveResultSchema: ...

        class _FertilizerInterfaceModuleNutrientsParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._FertilizerInterfaceModuleNutrientsParamSchema._Fields: ...

        class _FertilizerInterfaceModuleNutrientsResultSchema(_StructSchema):
            class _NutrientsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._NutrientSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _FertilizerInterfaceModule._FertilizerSchema._FertilizerInterfaceModuleNutrientsResultSchema._NutrientsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["nutrients"],
                ) -> _FertilizerInterfaceModule._FertilizerSchema._FertilizerInterfaceModuleNutrientsResultSchema._NutrientsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._FertilizerInterfaceModuleNutrientsResultSchema._Fields: ...

        class _FertilizerInterfaceModuleNutrientsMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._FertilizerInterfaceModuleNutrientsParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._FertilizerInterfaceModuleNutrientsResultSchema: ...

        class _FertilizerInterfaceModuleParametersParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._FertilizerInterfaceModuleParametersParamSchema._Fields: ...

        class _FertilizerInterfaceModuleParametersResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["params"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._FertilizerInterfaceModuleParametersResultSchema._Fields: ...

        class _FertilizerInterfaceModuleParametersMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._FertilizerInterfaceModuleParametersParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _FertilizerInterfaceModule._FertilizerSchema._FertilizerInterfaceModuleParametersResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _FertilizerInterfaceModule._FertilizerSchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["save"],
            ) -> _FertilizerInterfaceModule._FertilizerSchema._PersistentInterfaceModuleSaveMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nutrients"],
            ) -> _FertilizerInterfaceModule._FertilizerSchema._FertilizerInterfaceModuleNutrientsMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["parameters"],
            ) -> _FertilizerInterfaceModule._FertilizerSchema._FertilizerInterfaceModuleParametersMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(
            self,
        ) -> _FertilizerInterfaceModule._FertilizerSchema._Methods: ...

    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.FertilizerClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def nutrients(
            self,
            _context: contexts.NutrientsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.NutrientListBuilder
            | readers.NutrientListReader
            | Sequence[
                readers.NutrientReader | builders.NutrientBuilder | dict[str, Any]
            ]
            | results_tuples.NutrientsResultTuple
            | None
        ]: ...
        def nutrients_context(
            self,
            context: contexts.NutrientsCallContext,
        ) -> Awaitable[None]: ...
        def parameters(
            self,
            _context: contexts.ParametersCallContext,
            **kwargs: object,
        ) -> Awaitable[
            common.AnyPointer | results_tuples.ParametersResultTuple | None
        ]: ...
        def parameters_context(
            self,
            context: contexts.ParametersCallContext,
        ) -> Awaitable[None]: ...

class _NutrientStructModule(_StructModule):
    class _NameEnumModule(_EnumModule):
        urea: int
        ammonia: int
        nitrate: int
        phosphorus: int
        potassium: int
        sulfate: int
        organicC: int
        organicN: int
        organicP: int
        organicNFast: int
        organicNSlow: int

        class _NameSchema(_EnumSchema): ...

    Name: _NameEnumModule
    class _UnitEnumModule(_EnumModule):
        none: int
        fraction: int
        percent: int

        class _UnitSchema(_EnumSchema): ...

    Unit: _UnitEnumModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _NutrientSchema(_StructSchema):
        class _NutrientField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._NutrientNameEnumSchema: ...

        class _UnitField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._NutrientUnitEnumSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["nutrient"],
            ) -> _NutrientStructModule._NutrientSchema._NutrientField: ...
            @overload
            def __getitem__(self, key: Literal["value"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["unit"],
            ) -> _NutrientStructModule._NutrientSchema._UnitField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _NutrientStructModule._NutrientSchema._Fields: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        nutrient: enums.NutrientNameValue | enums.NutrientNameEnum | None = None,
        value: float | None = None,
        unit: enums.NutrientUnitValue | enums.NutrientUnitEnum | None = None,
        **kwargs: object,
    ) -> builders.NutrientBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.NutrientBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.NutrientReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.NutrientReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.NutrientBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.NutrientBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.NutrientReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.NutrientReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.NutrientReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.NutrientReader: ...
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.NutrientReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.NutrientReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.NutrientReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.NutrientReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.NutrientReader]: ...

class _ParamsStructModule(_StructModule):
    class _SowingStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _SowingSchema(_StructSchema):
            class _CropField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _mas_schema_crop_crop_capnp_schemas._CropSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["cultivar"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["plantDensity"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["crop"],
                ) -> (
                    _ParamsStructModule._SowingStructModule._SowingSchema._CropField
                ): ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ParamsStructModule._SowingStructModule._SowingSchema._Fields: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            cultivar: str | None = None,
            plantDensity: int | None = None,
            crop: CropClient | _CropInterfaceModule.Server | None = None,
            **kwargs: object,
        ) -> builders.SowingBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.SowingBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.SowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.SowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.SowingBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.SowingBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SowingReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SowingReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SowingReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SowingReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SowingReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.SowingReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.SowingReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.SowingReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.SowingReader]: ...

    Sowing: _SowingStructModule
    class _AutomaticSowingStructModule(_StructModule):
        class _AvgSoilTempStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            class _AvgSoilTempSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["soilDepthForAveraging"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["daysInSoilTempWindow"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["sowingIfAboveAvgSoilTemp"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ParamsStructModule._AutomaticSowingStructModule._AvgSoilTempStructModule._AvgSoilTempSchema._Fields: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], Any] | None = None,
                soilDepthForAveraging: float | None = None,
                daysInSoilTempWindow: int | None = None,
                sowingIfAboveAvgSoilTemp: float | None = None,
                **kwargs: object,
            ) -> builders.AvgSoilTempBuilder: ...
            @override
            def __call__(
                self,
                num_first_segment_words: int | None = None,
                **kwargs: object,
            ) -> builders.AvgSoilTempBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[readers.AvgSoilTempReader]: ...
            @overload
            def from_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                builder: Literal[False] = False,
            ) -> AbstractContextManager[readers.AvgSoilTempReader]: ...
            @overload
            def from_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[builders.AvgSoilTempBuilder]: ...
            @overload
            def from_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None,
                nesting_limit: int | None,
                builder: Literal[True],
            ) -> AbstractContextManager[builders.AvgSoilTempBuilder]: ...
            @override
            def from_bytes_packed(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.AvgSoilTempReader: ...
            @override
            def from_segments(
                self,
                segments: Sequence[Any],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.AvgSoilTempReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.AvgSoilTempReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.AvgSoilTempReader: ...
            @override
            async def read_async(
                self,
                stream: _AsyncIoStream,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.AvgSoilTempReader | None: ...
            @override
            def read_multiple(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                skip_copy: bool = False,
            ) -> Iterator[readers.AvgSoilTempReader]: ...
            @override
            def read_multiple_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                skip_copy: bool = False,
            ) -> Iterator[readers.AvgSoilTempReader]: ...
            @override
            def read_multiple_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> Iterator[readers.AvgSoilTempReader]: ...
            @override
            def read_multiple_bytes_packed(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> Iterator[readers.AvgSoilTempReader]: ...

        AvgSoilTemp: _AvgSoilTempStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _AutomaticSowingSchema(_StructSchema):
            class _AvgSoilTempField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ParamsAutomaticSowingAvgSoilTempSchema: ...

            class _SowingField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ParamsSowingSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["minTempThreshold"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["daysInTempWindow"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["minPercentASW"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["maxPercentASW"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["max3dayPrecipSum"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["maxCurrentDayPrecipSum"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["tempSumAboveBaseTemp"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["baseTemp"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["avgSoilTemp"],
                ) -> _ParamsStructModule._AutomaticSowingStructModule._AutomaticSowingSchema._AvgSoilTempField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["sowing"],
                ) -> _ParamsStructModule._AutomaticSowingStructModule._AutomaticSowingSchema._SowingField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ParamsStructModule._AutomaticSowingStructModule._AutomaticSowingSchema._Fields: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            minTempThreshold: float | None = None,
            daysInTempWindow: int | None = None,
            minPercentASW: float | None = None,
            maxPercentASW: float | None = None,
            max3dayPrecipSum: float | None = None,
            maxCurrentDayPrecipSum: float | None = None,
            tempSumAboveBaseTemp: float | None = None,
            baseTemp: float | None = None,
            avgSoilTemp: builders.AvgSoilTempBuilder
            | readers.AvgSoilTempReader
            | dict[str, Any]
            | None = None,
            sowing: builders.SowingBuilder
            | readers.SowingReader
            | dict[str, Any]
            | None = None,
            **kwargs: object,
        ) -> builders.AutomaticSowingBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.AutomaticSowingBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.AutomaticSowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.AutomaticSowingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.AutomaticSowingBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.AutomaticSowingBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AutomaticSowingReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AutomaticSowingReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AutomaticSowingReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AutomaticSowingReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AutomaticSowingReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.AutomaticSowingReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.AutomaticSowingReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.AutomaticSowingReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.AutomaticSowingReader]: ...

    AutomaticSowing: _AutomaticSowingStructModule
    class _HarvestStructModule(_StructModule):
        class _CropUsageEnumModule(_EnumModule):
            greenManure: int
            biomassProduction: int

            class _CropUsageSchema(_EnumSchema): ...

        CropUsage: _CropUsageEnumModule
        class _OptCarbonMgmtDataStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            class _OptCarbonMgmtDataSchema(_StructSchema):
                class _CropUsageField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ParamsHarvestCropUsageEnumSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["optCarbonConservation"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["cropImpactOnHumusBalance"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["cropUsage"],
                    ) -> _ParamsStructModule._HarvestStructModule._OptCarbonMgmtDataStructModule._OptCarbonMgmtDataSchema._CropUsageField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["residueHeq"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["organicFertilizerHeq"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["maxResidueRecoverFraction"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ParamsStructModule._HarvestStructModule._OptCarbonMgmtDataStructModule._OptCarbonMgmtDataSchema._Fields: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], Any] | None = None,
                optCarbonConservation: bool | None = None,
                cropImpactOnHumusBalance: float | None = None,
                cropUsage: enums.ParamsHarvestCropUsageValue
                | enums.ParamsHarvestCropUsageEnum
                | None = None,
                residueHeq: float | None = None,
                organicFertilizerHeq: float | None = None,
                maxResidueRecoverFraction: float | None = None,
                **kwargs: object,
            ) -> builders.OptCarbonMgmtDataBuilder: ...
            @override
            def __call__(
                self,
                num_first_segment_words: int | None = None,
                **kwargs: object,
            ) -> builders.OptCarbonMgmtDataBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[readers.OptCarbonMgmtDataReader]: ...
            @overload
            def from_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                builder: Literal[False] = False,
            ) -> AbstractContextManager[readers.OptCarbonMgmtDataReader]: ...
            @overload
            def from_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[builders.OptCarbonMgmtDataBuilder]: ...
            @overload
            def from_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None,
                nesting_limit: int | None,
                builder: Literal[True],
            ) -> AbstractContextManager[builders.OptCarbonMgmtDataBuilder]: ...
            @override
            def from_bytes_packed(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.OptCarbonMgmtDataReader: ...
            @override
            def from_segments(
                self,
                segments: Sequence[Any],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.OptCarbonMgmtDataReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.OptCarbonMgmtDataReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.OptCarbonMgmtDataReader: ...
            @override
            async def read_async(
                self,
                stream: _AsyncIoStream,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.OptCarbonMgmtDataReader | None: ...
            @override
            def read_multiple(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                skip_copy: bool = False,
            ) -> Iterator[readers.OptCarbonMgmtDataReader]: ...
            @override
            def read_multiple_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                skip_copy: bool = False,
            ) -> Iterator[readers.OptCarbonMgmtDataReader]: ...
            @override
            def read_multiple_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> Iterator[readers.OptCarbonMgmtDataReader]: ...
            @override
            def read_multiple_bytes_packed(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> Iterator[readers.OptCarbonMgmtDataReader]: ...

        OptCarbonMgmtData: _OptCarbonMgmtDataStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _HarvestSchema(_StructSchema):
            class _OptCarbMgmtDataField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ParamsHarvestOptCarbonMgmtDataSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["exported"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["optCarbMgmtData"],
                ) -> _ParamsStructModule._HarvestStructModule._HarvestSchema._OptCarbMgmtDataField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ParamsStructModule._HarvestStructModule._HarvestSchema._Fields: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            exported: bool | None = None,
            optCarbMgmtData: builders.OptCarbonMgmtDataBuilder
            | readers.OptCarbonMgmtDataReader
            | dict[str, Any]
            | None = None,
            **kwargs: object,
        ) -> builders.HarvestBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.HarvestBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.HarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.HarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.HarvestBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.HarvestBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.HarvestReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.HarvestReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.HarvestReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.HarvestReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.HarvestReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.HarvestReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.HarvestReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.HarvestReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.HarvestReader]: ...

    Harvest: _HarvestStructModule
    class _AutomaticHarvestStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _AutomaticHarvestSchema(_StructSchema):
            class _HarvestTimeField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._EventPhenoStageEnumSchema: ...

            class _HarvestField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ParamsHarvestSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["minPercentASW"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["maxPercentASW"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["max3dayPrecipSum"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["maxCurrentDayPrecipSum"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["harvestTime"],
                ) -> _ParamsStructModule._AutomaticHarvestStructModule._AutomaticHarvestSchema._HarvestTimeField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["harvest"],
                ) -> _ParamsStructModule._AutomaticHarvestStructModule._AutomaticHarvestSchema._HarvestField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ParamsStructModule._AutomaticHarvestStructModule._AutomaticHarvestSchema._Fields: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            minPercentASW: float | None = None,
            maxPercentASW: float | None = None,
            max3dayPrecipSum: float | None = None,
            maxCurrentDayPrecipSum: float | None = None,
            harvestTime: enums.EventPhenoStageValue
            | enums.EventPhenoStageEnum
            | None = None,
            harvest: builders.HarvestBuilder
            | readers.HarvestReader
            | dict[str, Any]
            | None = None,
            **kwargs: object,
        ) -> builders.AutomaticHarvestBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.AutomaticHarvestBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.AutomaticHarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.AutomaticHarvestReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.AutomaticHarvestBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.AutomaticHarvestBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AutomaticHarvestReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AutomaticHarvestReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AutomaticHarvestReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AutomaticHarvestReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AutomaticHarvestReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.AutomaticHarvestReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.AutomaticHarvestReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.AutomaticHarvestReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.AutomaticHarvestReader]: ...

    AutomaticHarvest: _AutomaticHarvestStructModule
    class _CuttingStructModule(_StructModule):
        class _CLEnumModule(_EnumModule):
            cut: int
            left: int

            class _CLSchema(_EnumSchema): ...

        CL: _CLEnumModule
        class _UnitEnumModule(_EnumModule):
            percentage: int
            biomass: int
            lai: int

            class _UnitSchema(_EnumSchema): ...

        Unit: _UnitEnumModule
        class _SpecStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            class _SpecSchema(_StructSchema):
                class _OrganField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._PlantOrganEnumSchema: ...

                class _UnitField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ParamsCuttingUnitEnumSchema: ...

                class _CutOrLeftField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ParamsCuttingCLEnumSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["organ"],
                    ) -> _ParamsStructModule._CuttingStructModule._SpecStructModule._SpecSchema._OrganField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["value"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["unit"],
                    ) -> _ParamsStructModule._CuttingStructModule._SpecStructModule._SpecSchema._UnitField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["cutOrLeft"],
                    ) -> _ParamsStructModule._CuttingStructModule._SpecStructModule._SpecSchema._CutOrLeftField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["exportPercentage"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ParamsStructModule._CuttingStructModule._SpecStructModule._SpecSchema._Fields: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], Any] | None = None,
                organ: enums.PlantOrganValue | enums.PlantOrganEnum | None = None,
                value: float | None = None,
                unit: enums.ParamsCuttingUnitValue
                | enums.ParamsCuttingUnitEnum
                | None = None,
                cutOrLeft: enums.ParamsCuttingCLValue
                | enums.ParamsCuttingCLEnum
                | None = None,
                exportPercentage: float | None = None,
                **kwargs: object,
            ) -> builders.SpecBuilder: ...
            @override
            def __call__(
                self,
                num_first_segment_words: int | None = None,
                **kwargs: object,
            ) -> builders.SpecBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[readers.SpecReader]: ...
            @overload
            def from_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                builder: Literal[False] = False,
            ) -> AbstractContextManager[readers.SpecReader]: ...
            @overload
            def from_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[builders.SpecBuilder]: ...
            @overload
            def from_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None,
                nesting_limit: int | None,
                builder: Literal[True],
            ) -> AbstractContextManager[builders.SpecBuilder]: ...
            @override
            def from_bytes_packed(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.SpecReader: ...
            @override
            def from_segments(
                self,
                segments: Sequence[Any],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.SpecReader: ...
            @override
            def read(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.SpecReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.SpecReader: ...
            @override
            async def read_async(
                self,
                stream: _AsyncIoStream,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.SpecReader | None: ...
            @override
            def read_multiple(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                skip_copy: bool = False,
            ) -> Iterator[readers.SpecReader]: ...
            @override
            def read_multiple_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                skip_copy: bool = False,
            ) -> Iterator[readers.SpecReader]: ...
            @override
            def read_multiple_bytes(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> Iterator[readers.SpecReader]: ...
            @override
            def read_multiple_bytes_packed(
                self,
                buf: Any,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> Iterator[readers.SpecReader]: ...

        Spec: _SpecStructModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _CuttingSchema(_StructSchema):
            class _CuttingSpecField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._ParamsCuttingSpecSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ParamsStructModule._CuttingStructModule._CuttingSchema._CuttingSpecField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["cuttingSpec"],
                ) -> _ParamsStructModule._CuttingStructModule._CuttingSchema._CuttingSpecField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["cutMaxAssimilationRatePercentage"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ParamsStructModule._CuttingStructModule._CuttingSchema._Fields: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            cuttingSpec: builders.SpecListBuilder
            | readers.SpecListReader
            | Sequence[readers.SpecReader | builders.SpecBuilder | dict[str, Any]]
            | None = None,
            cutMaxAssimilationRatePercentage: float | None = None,
            **kwargs: object,
        ) -> builders.CuttingBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.CuttingBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.CuttingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.CuttingReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.CuttingBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.CuttingBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CuttingReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CuttingReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CuttingReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CuttingReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CuttingReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.CuttingReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.CuttingReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.CuttingReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.CuttingReader]: ...

    Cutting: _CuttingStructModule
    class _MineralFertilizationStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _MineralFertilizationSchema(_StructSchema):
            class _FertilizerField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._FertilizerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["fertilizer"],
                ) -> _ParamsStructModule._MineralFertilizationStructModule._MineralFertilizationSchema._FertilizerField: ...
                @overload
                def __getitem__(self, key: Literal["amount"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ParamsStructModule._MineralFertilizationStructModule._MineralFertilizationSchema._Fields: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            fertilizer: clients.FertilizerClient
            | _FertilizerInterfaceModule.Server
            | None = None,
            amount: float | None = None,
            **kwargs: object,
        ) -> builders.MineralFertilizationBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.MineralFertilizationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.MineralFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.MineralFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.MineralFertilizationBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.MineralFertilizationBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.MineralFertilizationReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.MineralFertilizationReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.MineralFertilizationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.MineralFertilizationReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.MineralFertilizationReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.MineralFertilizationReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.MineralFertilizationReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.MineralFertilizationReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.MineralFertilizationReader]: ...

    MineralFertilization: _MineralFertilizationStructModule
    class _NDemandFertilizationStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _NDemandFertilizationSchema(_StructSchema):
            class _FertilizerField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._FertilizerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["nDemand"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["fertilizer"],
                ) -> _ParamsStructModule._NDemandFertilizationStructModule._NDemandFertilizationSchema._FertilizerField: ...
                @overload
                def __getitem__(self, key: Literal["depth"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["stage"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ParamsStructModule._NDemandFertilizationStructModule._NDemandFertilizationSchema._Fields: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            nDemand: float | None = None,
            fertilizer: clients.FertilizerClient
            | _FertilizerInterfaceModule.Server
            | None = None,
            depth: float | None = None,
            stage: int | None = None,
            **kwargs: object,
        ) -> builders.NDemandFertilizationBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.NDemandFertilizationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.NDemandFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.NDemandFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.NDemandFertilizationBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.NDemandFertilizationBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.NDemandFertilizationReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.NDemandFertilizationReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.NDemandFertilizationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.NDemandFertilizationReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.NDemandFertilizationReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.NDemandFertilizationReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.NDemandFertilizationReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.NDemandFertilizationReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.NDemandFertilizationReader]: ...

    NDemandFertilization: _NDemandFertilizationStructModule
    class _OrganicFertilizationStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _OrganicFertilizationSchema(_StructSchema):
            class _FertilizerField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._FertilizerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["fertilizer"],
                ) -> _ParamsStructModule._OrganicFertilizationStructModule._OrganicFertilizationSchema._FertilizerField: ...
                @overload
                def __getitem__(self, key: Literal["amount"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["incorporation"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ParamsStructModule._OrganicFertilizationStructModule._OrganicFertilizationSchema._Fields: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            fertilizer: clients.FertilizerClient
            | _FertilizerInterfaceModule.Server
            | None = None,
            amount: float | None = None,
            incorporation: bool | None = None,
            **kwargs: object,
        ) -> builders.OrganicFertilizationBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.OrganicFertilizationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.OrganicFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.OrganicFertilizationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.OrganicFertilizationBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.OrganicFertilizationBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.OrganicFertilizationReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.OrganicFertilizationReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.OrganicFertilizationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.OrganicFertilizationReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.OrganicFertilizationReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.OrganicFertilizationReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.OrganicFertilizationReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.OrganicFertilizationReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.OrganicFertilizationReader]: ...

    OrganicFertilization: _OrganicFertilizationStructModule
    class _TillageStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _TillageSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["depth"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ParamsStructModule._TillageStructModule._TillageSchema._Fields: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            depth: float | None = None,
            **kwargs: object,
        ) -> builders.TillageBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.TillageBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.TillageReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.TillageReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.TillageBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.TillageBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.TillageReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.TillageReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.TillageReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.TillageReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.TillageReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.TillageReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.TillageReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.TillageReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.TillageReader]: ...

    Tillage: _TillageStructModule
    class _IrrigationStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _IrrigationSchema(_StructSchema):
            class _NutrientConcentrationsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._NutrientSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ParamsStructModule._IrrigationStructModule._IrrigationSchema._NutrientConcentrationsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["amount"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["nutrientConcentrations"],
                ) -> _ParamsStructModule._IrrigationStructModule._IrrigationSchema._NutrientConcentrationsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> (
                _ParamsStructModule._IrrigationStructModule._IrrigationSchema._Fields
            ): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            amount: float | None = None,
            nutrientConcentrations: builders.NutrientListBuilder
            | readers.NutrientListReader
            | Sequence[
                readers.NutrientReader | builders.NutrientBuilder | dict[str, Any]
            ]
            | None = None,
            **kwargs: object,
        ) -> builders.IrrigationBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.IrrigationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.IrrigationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.IrrigationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.IrrigationBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.IrrigationBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.IrrigationReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.IrrigationReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.IrrigationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.IrrigationReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.IrrigationReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.IrrigationReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.IrrigationReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.IrrigationReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.IrrigationReader]: ...

    Irrigation: _IrrigationStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _ParamsSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]): ...

        @property
        @override
        def fields(self) -> _ParamsStructModule._ParamsSchema._Fields: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        **kwargs: object,
    ) -> builders.ParamsBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.ParamsBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.ParamsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.ParamsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.ParamsBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.ParamsBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.ParamsReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.ParamsReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.ParamsReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.ParamsReader: ...
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.ParamsReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.ParamsReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.ParamsReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.ParamsReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.ParamsReader]: ...

class _FertilizerServiceInterfaceModule(_RegistryInterfaceModule):
    class _FertilizerServiceSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _RegistryInterfaceModuleSupportedCategoriesParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleSupportedCategoriesParamSchema._Fields: ...

        class _RegistryInterfaceModuleSupportedCategoriesResultSchema(_StructSchema):
            class _CatsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(
                        self,
                    ) -> (
                        _mas_schema_common_common_capnp_schemas._IdInformationSchema
                    ): ...

                @property
                @override
                def schema(
                    self,
                ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleSupportedCategoriesResultSchema._CatsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["cats"],
                ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleSupportedCategoriesResultSchema._CatsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleSupportedCategoriesResultSchema._Fields: ...

        class _RegistryInterfaceModuleSupportedCategoriesMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleSupportedCategoriesParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleSupportedCategoriesResultSchema: ...

        class _RegistryInterfaceModuleCategoryInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["categoryId"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleCategoryInfoParamSchema._Fields: ...

        class _RegistryInterfaceModuleCategoryInfoResultSchema(_StructSchema):
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
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleCategoryInfoResultSchema._Fields: ...

        class _RegistryInterfaceModuleCategoryInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleCategoryInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleCategoryInfoResultSchema: ...

        class _RegistryInterfaceModuleEntriesParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["categoryId"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleEntriesParamSchema._Fields: ...

        class _RegistryInterfaceModuleEntriesResultSchema(_StructSchema):
            class _EntriesField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(
                        self,
                    ) -> (
                        _mas_schema_registry_registry_capnp_schemas._RegistryEntrySchema
                    ): ...

                @property
                @override
                def schema(
                    self,
                ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleEntriesResultSchema._EntriesField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["entries"],
                ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleEntriesResultSchema._EntriesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleEntriesResultSchema._Fields: ...

        class _RegistryInterfaceModuleEntriesMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleEntriesParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleEntriesResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["supportedCategories"],
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleSupportedCategoriesMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["categoryInfo"],
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleCategoryInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["entries"],
            ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._RegistryInterfaceModuleEntriesMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(
            self,
        ) -> _FertilizerServiceInterfaceModule._FertilizerServiceSchema._Methods: ...

    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.FertilizerServiceClient: ...
    class Server(_RegistryInterfaceModule.Server): ...

class _ServiceInterfaceModule(_IdentifiableInterfaceModule):
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

        class _ServiceInterfaceModuleManagementAtParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["lat"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["lon"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleManagementAtParamSchema._Fields: ...

        class _ServiceInterfaceModuleManagementAtResultSchema(_StructSchema):
            class _MgmtField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._EventSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleManagementAtResultSchema._MgmtField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["mgmt"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleManagementAtResultSchema._MgmtField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleManagementAtResultSchema._Fields: ...

        class _ServiceInterfaceModuleManagementAtMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleManagementAtParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleManagementAtResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["managementAt"],
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleManagementAtMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(self) -> _ServiceInterfaceModule._ServiceSchema._Methods: ...

    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.ServiceClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def managementAt(
            self,
            lat: float,
            lon: float,
            _context: contexts.ManagementatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.EventListBuilder
            | readers.EventListReader
            | Sequence[readers.EventReader | builders.EventBuilder | dict[str, Any]]
            | results_tuples.ManagementatResultTuple
            | None
        ]: ...
        def managementAt_context(
            self,
            context: contexts.ManagementatCallContext,
        ) -> Awaitable[None]: ...
