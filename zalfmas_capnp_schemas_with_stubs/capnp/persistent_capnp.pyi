"""This is an automatically generated stub for `persistent.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator
from contextlib import contextmanager
from io import BufferedWriter
from typing import (
    Any,
    BinaryIO,
    Generic,
    NamedTuple,
    Protocol,
    Self,
    TypeAlias,
    TypeVar,
)

Persistent_Owner = TypeVar("Persistent_Owner")
Persistent_SturdyRef = TypeVar("Persistent_SturdyRef")

class Persistent:
    SaveParamsBuilder: TypeAlias = SaveParams.Builder
    SaveParamsReader: TypeAlias = SaveParams.Reader
    class SaveParams(Generic[Persistent_Owner]):
        class Reader:
            @property
            def sealFor(self) -> Any: ...
            def as_builder(self) -> Persistent.SaveParams.Builder: ...

        class Builder:
            @property
            def sealFor(self) -> Any: ...
            @sealFor.setter
            def sealFor(self, value: Any) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Persistent.SaveParams.Builder: ...
            def copy(self) -> Persistent.SaveParams.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Persistent.SaveParams.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Persistent.SaveParams.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Persistent.SaveParams.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            sealFor: Any | None = None,
        ) -> Persistent.SaveParams.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Persistent.SaveParams.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Persistent.SaveParams.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    SaveResultsBuilder: TypeAlias = SaveResults.Builder
    SaveResultsReader: TypeAlias = SaveResults.Reader
    class SaveResults(Generic[Persistent_SturdyRef]):
        class Reader:
            @property
            def sturdyRef(self) -> Persistent_SturdyRef: ...
            def as_builder(self) -> Persistent.SaveResults.Builder: ...

        class Builder:
            @property
            def sturdyRef(self) -> Persistent_SturdyRef: ...
            @sturdyRef.setter
            def sturdyRef(self, value: Persistent_SturdyRef) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Persistent.SaveResults.Builder: ...
            def copy(self) -> Persistent.SaveResults.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Persistent.SaveResults.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Persistent.SaveResults.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Persistent.SaveResults.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            sturdyRef: Persistent_SturdyRef | None = None,
        ) -> Persistent.SaveResults.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Persistent.SaveResults.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Persistent.SaveResults.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class SaveRequest(Protocol):
        sealFor: Any
        def send(self) -> Persistent.SaveResult: ...

    class SaveResult(Awaitable[SaveResult], Protocol):
        sturdyRef: Any

    @classmethod
    def _new_client(cls, server: Persistent.Server) -> "PersistentClient": ...
    class Server(Protocol):
        class SaveResultTuple(NamedTuple):
            sturdyRef: Any

        class SaveCallContext(Protocol):
            results: Persistent.SaveResult

        def save(
            self,
            sealFor: Any,
            _context: Persistent.Server.SaveCallContext,
            **kwargs: Any,
        ) -> Awaitable[Persistent.Server.SaveResultTuple | None]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class PersistentClient(Protocol):
    def save(self, sealFor: Any | None = None) -> Persistent.SaveResult: ...
    def save_request(self, sealFor: Any | None = None) -> Persistent.SaveRequest: ...
