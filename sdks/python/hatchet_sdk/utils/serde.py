from dataclasses import asdict, is_dataclass
from typing import Any, TypeVar, cast, overload

from pydantic import BaseModel

T = TypeVar("T")
K = TypeVar("K")
R = TypeVar("R")


@overload
def remove_null_unicode_character(
    data: dict[K, T], replacement: str = ""
) -> dict[K, T]: ...


@overload
def remove_null_unicode_character(data: list[T], replacement: str = "") -> list[T]: ...


@overload
def remove_null_unicode_character(
    data: tuple[T, ...], replacement: str = ""
) -> tuple[T, ...]: ...


@overload
def remove_null_unicode_character(data: R, replacement: str = "") -> R: ...


def remove_null_unicode_character(
    data: dict[K, T] | list[T] | tuple[T, ...] | R, replacement: str = ""
) -> str | dict[K, T] | list[T] | tuple[T, ...] | R:
    """
    Recursively traverse a dictionary (a task's output) and remove the unicode escape sequence \\u0000 which will cause unexpected behavior in Hatchet.

    Needed as Hatchet does not support \\u0000 in task outputs

    :param data: The task output (a JSON-serializable dictionary or mapping)
    :param replacement: The string to replace \\u0000 with.

    :return: The same dictionary with all \\u0000 characters removed from strings, and nested dictionaries/lists processed recursively.
    """
    if isinstance(data, str):
        return data.replace("\u0000", replacement)

    if isinstance(data, dict):
        return {
            remove_null_unicode_character(
                cast(Any, key), replacement
            ): remove_null_unicode_character(cast(Any, value), replacement)
            for key, value in data.items()
        }

    if isinstance(data, list):
        return [
            remove_null_unicode_character(cast(Any, item), replacement) for item in data
        ]

    if isinstance(data, tuple):
        return tuple(
            remove_null_unicode_character(cast(Any, item), replacement) for item in data
        )

    return data


def contains_null_unicode_character(data: Any) -> bool:
    """
    Checks if data contains the null unicode character `\\u0000`.

    :param data: The task output (a JSON-serializable dictionary or mapping).
    :return: Whether the data contains the null unicode character.
    """
    if data is None:
        return False

    if isinstance(data, BaseModel):
        dumped = data.model_dump()
        return remove_null_unicode_character(dumped) != dumped

    if is_dataclass(data):
        dumped = asdict(data)  # type: ignore[arg-type]
        return remove_null_unicode_character(dumped) != dumped

    if isinstance(data, str | dict | list | tuple):
        return remove_null_unicode_character(data) != data

    return False
