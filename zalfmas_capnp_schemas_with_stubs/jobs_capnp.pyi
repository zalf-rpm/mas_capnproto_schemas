"""This is an automatically generated stub for `jobs.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator
from contextlib import contextmanager
from io import BufferedWriter
from typing import Any, BinaryIO, Generic, NamedTuple, Protocol, TypeAlias, TypeVar

from .common_capnp import Identifiable, IdentifiableClient
from .persistence_capnp import Persistent, PersistentClient

_Payload = TypeVar("_Payload")

JobBuilder: TypeAlias = Job.Builder
JobReader: TypeAlias = Job.Reader

class Job(Generic[_Payload]):
    class Reader:
        @property
        def data(self) -> _Payload: ...
        @property
        def noFurtherJobs(self) -> bool: ...
        def as_builder(self) -> Job.Builder: ...

    class Builder:
        @property
        def data(self) -> _Payload: ...
        @data.setter
        def data(self, value: _Payload) -> None: ...
        @property
        def noFurtherJobs(self) -> bool: ...
        @noFurtherJobs.setter
        def noFurtherJobs(self, value: bool) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Job.Builder: ...
        def copy(self) -> Job.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Job.Reader: ...
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
    ) -> Iterator[Job.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Job.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        data: _Payload | None = None,
        noFurtherJobs: bool | None = None,
    ) -> Job.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Job.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Job.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

class Service:
    class NextjobRequest(Protocol):
        def send(self) -> Service.NextjobResult: ...

    class NextjobResult(Awaitable[NextjobResult], Protocol):
        job: Job.Builder | Job.Reader

    @classmethod
    def _new_client(
        cls, server: Service.Server | Identifiable.Server | Persistent.Server
    ) -> ServiceClient: ...
    class Server(Identifiable.Server, Persistent.Server):
        class NextjobResultTuple(NamedTuple):
            job: Job.Builder | Job.Reader

        class NextjobCallContext(Protocol):
            params: Service.NextjobRequest
            results: Service.NextjobResult

        def nextJob(
            self, _context: Service.Server.NextjobCallContext, **kwargs: Any
        ) -> Awaitable[Service.Server.NextjobResultTuple | None]: ...
        def nextJob_context(
            self, context: Service.Server.NextjobCallContext
        ) -> Awaitable[None]: ...

class ServiceClient(IdentifiableClient, PersistentClient):
    def nextJob(self) -> Service.NextjobResult: ...
    def nextJob_request(self) -> Service.NextjobRequest: ...
