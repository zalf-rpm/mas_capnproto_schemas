"""Runtime placeholder module for result tuple helpers of `storage.capnp`."""

from typing import NamedTuple


class ContainerwithidResultTuple(NamedTuple):
    container: object


class ImportcontainerResultTuple(NamedTuple):
    container: object


class ListcontainersResultTuple(NamedTuple):
    containers: object


class NewcontainerResultTuple(NamedTuple):
    container: object


class RemovecontainerResultTuple(NamedTuple):
    success: object


class AddentryResultTuple(NamedTuple):
    entry: object
    success: object


class ClearResultTuple(NamedTuple):
    success: object


class DownloadentriesResultTuple(NamedTuple):
    entries: object


class ExportResultTuple(NamedTuple):
    json: object


class GetentryResultTuple(NamedTuple):
    entry: object


class ListentriesResultTuple(NamedTuple):
    entries: object


class RemoveentryResultTuple(NamedTuple):
    success: object


class GetkeyResultTuple(NamedTuple):
    key: object


class GetvalueResultTuple(NamedTuple):
    value: object
    isUnset: object


class SetvalueResultTuple(NamedTuple):
    success: object


__all__ = [
    "AddentryResultTuple",
    "ClearResultTuple",
    "ContainerwithidResultTuple",
    "DownloadentriesResultTuple",
    "ExportResultTuple",
    "GetentryResultTuple",
    "GetkeyResultTuple",
    "GetvalueResultTuple",
    "ImportcontainerResultTuple",
    "ListcontainersResultTuple",
    "ListentriesResultTuple",
    "NewcontainerResultTuple",
    "RemovecontainerResultTuple",
    "RemoveentryResultTuple",
    "SetvalueResultTuple",
]
