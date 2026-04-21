"""Result tuple helper types for `web_berest_data_import.capnp`."""

from typing import NamedTuple

class ImportdataResultTuple(NamedTuple):
    id: str
    successA: bool
    successB: bool
