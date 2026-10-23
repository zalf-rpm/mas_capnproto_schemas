"""Enum helper aliases for `common.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import _DynamicEnum

class StructuredTextTypeValue(_DynamicEnum):
    @override
    def __str__(
        self,
    ) -> Literal["unstructured", "json", "xml", "toml", "sturdyRef", "csv"]: ...

type StructuredTextTypeEnum = (
    int | Literal["unstructured", "json", "xml", "toml", "sturdyRef", "csv"]
)
