"""Context helper types for `jobs.capnp`."""

from collections.abc import Callable
from typing import Any, Protocol

from capnp.lib.capnp import (
    _DynamicEnumField,
    _DynamicStructBuilder,
    _MessageSize,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.jobs.jobs_capnp.types.results import server as results_server

class NextjobParams(Protocol):
    _parent: Any
    is_root: bool
    @property
    def which(self) -> _DynamicEnumField: ...
    @property
    def schema(self) -> _StructSchema: ...
    @property
    def total_size(self) -> _MessageSize: ...
    def _get(self, field: str) -> Any: ...
    def _get_by_field(self, field: _StructSchemaField) -> Any: ...
    def _has(self, field: str) -> bool: ...
    def _has_by_field(self, field: _StructSchemaField) -> bool: ...
    def get_data_as_view(self, field: str) -> memoryview: ...
    def _which_str(self) -> str: ...
    def _which(self) -> _DynamicEnumField: ...
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
    ) -> _DynamicStructBuilder: ...
    def to_dict(
        self,
        verbose: bool = False,
        ordered: bool = False,
        encode_bytes_as_base64: bool = False,
    ) -> dict[str, Any]: ...

class NextjobCallContext(Protocol):
    params: NextjobParams
    @property
    def results(self) -> results_server.NextjobServerResult: ...
