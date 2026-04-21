"""Enum helper aliases for `model.capnp`."""

from typing import Literal

type StatTypeEnum = int | Literal["min", "max", "sd", "avg", "median"]
