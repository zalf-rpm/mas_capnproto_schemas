"""Module helper types for `sim_setup.capnp`."""

from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

from . import _all as _all

class _SetupStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
    ) -> _all.SetupBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SetupReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SetupReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SetupBuilder]: ...
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
    ) -> _all.SetupReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SetupReader: ...
