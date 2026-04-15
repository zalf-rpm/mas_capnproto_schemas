"""Runtime placeholder module for result tuple helpers of `web_berest_data_import.capnp`."""

from typing import NamedTuple


class ImportdataResultTuple(NamedTuple):
    id: object
    successA: object
    successB: object


__all__ = ["ImportdataResultTuple"]
