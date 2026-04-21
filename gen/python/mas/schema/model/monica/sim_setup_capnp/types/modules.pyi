"""Module helper types for `sim_setup.capnp`."""

from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.model.monica.sim_setup_capnp.types import builders as builders
from mas.schema.model.monica.sim_setup_capnp.types import readers as readers
from mas.schema.model.monica.sim_setup_capnp.types import schemas as schemas

class _SetupStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SetupSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["runId"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["sowingTime"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["harvestTime"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["cropId"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["simJson"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["cropJson"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["siteJson"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["startDate"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["endDate"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["groundwaterLevel"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["impenetrableLayer"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["elevation"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["slope"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["latitude"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["landcover"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["fertilization"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["nitrogenResponseOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["irrigation"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["waterDeficitResponseOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["emergenceMoistureControlOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["emergenceFloodingControlOn"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["leafExtensionModifier"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["co2"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["o3"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["fieldConditionModifier"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stageTemperatureSum"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["useVernalisationFix"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["comment"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _SetupStructModule._SetupSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SetupSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        runId: int | None = None,
        sowingTime: str | None = None,
        harvestTime: str | None = None,
        cropId: str | None = None,
        simJson: str | None = None,
        cropJson: str | None = None,
        siteJson: str | None = None,
        startDate: str | None = None,
        endDate: str | None = None,
        groundwaterLevel: bool | None = None,
        impenetrableLayer: bool | None = None,
        elevation: bool | None = None,
        slope: bool | None = None,
        latitude: bool | None = None,
        landcover: bool | None = None,
        fertilization: bool | None = None,
        nitrogenResponseOn: bool | None = None,
        irrigation: bool | None = None,
        waterDeficitResponseOn: bool | None = None,
        emergenceMoistureControlOn: bool | None = None,
        emergenceFloodingControlOn: bool | None = None,
        leafExtensionModifier: bool | None = None,
        co2: float | None = None,
        o3: float | None = None,
        fieldConditionModifier: float | None = None,
        stageTemperatureSum: str | None = None,
        useVernalisationFix: bool | None = None,
        comment: str | None = None,
        **kwargs: object,
    ) -> builders.SetupBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SetupReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SetupReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SetupBuilder]: ...
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
    ) -> readers.SetupReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SetupReader: ...
