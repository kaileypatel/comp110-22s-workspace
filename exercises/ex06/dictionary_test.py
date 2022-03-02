"""Testing dictionary functions."""

__author__ = "730523395"

from dictionary import invert, favorite_color, count


def test_invert_01() -> None:
    """Test for inverted keys and values."""
    a: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(a) == {"z": "a", "y": "b", "x": "c"}


def test_invert_02() -> None:
    """Test for inverted keys and values."""
    b: dict[str, str] = {"cat": "apple"}
    assert invert(b) == {"apple": "cat"}


def test_favorite_color() -> None:
    """Test for the most common color listed in the dict."""
    c: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(c) == "blue"


def test_count() -> None:
    """Test for duplicate items in dictionary keys."""
    c: list[str] = ["hi", "okay", "hi", "whatever", "soup", "whatever"]
    assert count(c) == {"hi": 2, "okay": 1, "whatever": 2, "soup": 1}


def test_count_02() -> None:
    """Test for duplicate items in dictionary keys."""
    c: list[str] = ["boo", "howdy", "yikes", "ouch", "howdy", "howdy", "boo", "ouch", "howdy"]
    assert count(c) == {"boo": 2, "howdy": 4, "yikes": 1, "ouch": 2}