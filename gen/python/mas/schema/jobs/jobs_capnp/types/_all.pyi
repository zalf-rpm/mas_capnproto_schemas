"""This is an automatically generated stub for `jobs.capnp`."""

from collections.abc import Awaitable, Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = (
    str
    | bytes
    | _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicListBuilder
    | _DynamicListReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class _JobStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        data: AnyPointer | None = None,
        noFurtherJobs: bool | None = None,
        **kwargs: object,
    ) -> JobBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[JobReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[JobReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[JobBuilder]: ...
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
    ) -> JobReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> JobReader: ...

class JobReader(_DynamicStructReader):
    @property
    def data(self) -> _DynamicObjectReader: ...
    @property
    def noFurtherJobs(self) -> bool: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> JobBuilder: ...

class JobBuilder(_DynamicStructBuilder):
    @property
    def data(self) -> _DynamicObjectReader: ...
    @data.setter
    def data(self, value: AnyPointer) -> None: ...
    @property
    def noFurtherJobs(self) -> bool: ...
    @noFurtherJobs.setter
    def noFurtherJobs(self, value: bool) -> None: ...
    @override
    def as_reader(self) -> JobReader: ...

Job: _JobStructModule

class _ServiceInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> ServiceClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def nextJob(
            self,
            _context: NextjobCallContext,
            **kwargs: object,
        ) -> Awaitable[
            JobBuilder | JobReader | dict[str, Any] | NextjobResultTuple | None
        ]: ...
        def nextJob_context(self, context: NextjobCallContext) -> Awaitable[None]: ...

class NextjobRequest(Protocol):
    def send(self) -> NextjobResult: ...

class NextjobResult(Awaitable[NextjobResult], Protocol):
    job: JobReader

class NextjobServerResult(_DynamicStructBuilder):
    @property
    def job(self) -> JobBuilder: ...
    @job.setter
    def job(self, value: JobBuilder | JobReader | dict[str, Any]) -> None: ...
    @overload
    def init(self, field: Literal["job"], size: int | None = None) -> JobBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class NextjobParams(Protocol): ...

class NextjobCallContext(Protocol):
    params: NextjobParams
    @property
    def results(self) -> NextjobServerResult: ...

class NextjobResultTuple(NamedTuple):
    job: JobBuilder | JobReader | dict[str, Any]

class ServiceClient(IdentifiableClient, PersistentClient):
    def nextJob(self) -> NextjobResult: ...
    def nextJob_request(self) -> NextjobRequest: ...

Service: _ServiceInterfaceModule

# Top-level type aliases for use in type annotations
ServiceServer = _ServiceInterfaceModule.Server
