"""Enum helper aliases for `common.capnp`."""

from typing import Literal

type StructuredTextTypeEnum = (
    int | Literal["unstructured", "json", "xml", "toml", "sturdyRef"]
)
