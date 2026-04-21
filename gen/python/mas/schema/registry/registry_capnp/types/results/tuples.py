"""Runtime placeholder module for result tuple helpers of `registry.capnp`."""

# pyright: reportUnusedClass=none

from typing import NamedTuple


class AddcategoryResultTuple(NamedTuple):
    success: object


class MoveobjectsResultTuple(NamedTuple):
    movedObjectIds: object


class RegistryResultTuple(NamedTuple):
    registry: object


class RemovecategoryResultTuple(NamedTuple):
    removedObjects: object


class RemoveobjectsResultTuple(NamedTuple):
    removedObjects: object


class RegisterResultTuple(NamedTuple):
    unreg: object
    reregSR: object


class UnregisterResultTuple(NamedTuple):
    success: object


class CategoryinfoResultTuple(NamedTuple):
    id: object
    name: object
    description: object


class EntriesResultTuple(NamedTuple):
    entries: object


class SupportedcategoriesResultTuple(NamedTuple):
    cats: object


__all__ = [
    "AddcategoryResultTuple",
    "CategoryinfoResultTuple",
    "EntriesResultTuple",
    "MoveobjectsResultTuple",
    "RegisterResultTuple",
    "RegistryResultTuple",
    "RemovecategoryResultTuple",
    "RemoveobjectsResultTuple",
    "SupportedcategoriesResultTuple",
    "UnregisterResultTuple",
]
