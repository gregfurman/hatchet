from hatchet_sdk import remove_null_unicode_character
from hatchet_sdk.utils.serde import contains_null_unicode_character


def test_remove_null_unicode() -> None:
    assert remove_null_unicode_character(
        {"message": "Hello\x00World", "user": "test\0user"},
        replacement=" ",
    ) == {
        "message": "Hello World",
        "user": "test user",
    }

    assert remove_null_unicode_character(
        ["Hello\x00World", "test\0user"], replacement=" "
    ) == [
        "Hello World",
        "test user",
    ]

    assert remove_null_unicode_character(
        ("Hello\x00World", "test\0user"), replacement=" "
    ) == (
        "Hello World",
        "test user",
    )

    assert (
        remove_null_unicode_character("Hello\x00World", replacement=" ")
        == "Hello World"
    )

    assert remove_null_unicode_character(
        {"key": "value", "nested": {"inner": "text\0with\u0000"}},
        replacement=" ",
    ) == {
        "key": "value",
        "nested": {"inner": "text with "},
    }

    assert remove_null_unicode_character(1) == 1
    assert remove_null_unicode_character(None) is None
    assert remove_null_unicode_character(True) is True
    assert remove_null_unicode_character(3.14) == 3.14
    assert remove_null_unicode_character(
        {"int": 1, "float": 2.5, "string": "test\0user"},
        replacement=" ",
    ) == {"int": 1, "float": 2.5, "string": "test user"}


def test_contains_null_unicode() -> None:
    assert contains_null_unicode_character({"message": "Hello\x00World"}) is True
    assert contains_null_unicode_character({"key\x00": "value"}) is True
    assert contains_null_unicode_character(["Hello\x00World", "test"]) is True
    assert contains_null_unicode_character("Hello\x00World") is True
    assert contains_null_unicode_character({"nested": {"inner": "text\u0000"}}) is True

    assert contains_null_unicode_character({"message": "Hello World"}) is False
    assert contains_null_unicode_character(["Hello", "World"]) is False
    assert contains_null_unicode_character("Hello World") is False
    assert contains_null_unicode_character({"int": 1, "float": 2.5}) is False

    assert contains_null_unicode_character(None) is False
    assert contains_null_unicode_character(1) is False
    assert contains_null_unicode_character(3.14) is False
    assert contains_null_unicode_character(True) is False

    from pydantic import BaseModel

    class MyModel(BaseModel):
        name: str

    assert contains_null_unicode_character(MyModel(name="Hello\x00World")) is True
    assert contains_null_unicode_character(MyModel(name="Hello World")) is False

    from dataclasses import dataclass

    @dataclass
    class MyDataclass:
        name: str

    assert contains_null_unicode_character(MyDataclass(name="Hello\x00World")) is True
    assert contains_null_unicode_character(MyDataclass(name="Hello World")) is False
