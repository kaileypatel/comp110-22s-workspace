"""Other file established in directory."""

__author__ = "730523395"

from utils import only_evens, sub, concat


def test_only_evens_01() -> None:
    """Test only evens."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_02() -> None:
    """Test only evens."""
    assert only_evens([1, 5, 3]) == []


def test_sub() -> None:
    """Test for list items."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3)


def test_concat() -> None: 
    """Test to combine all elements of list1 with list2."""
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = [4, 5, 6]
    assert concat(list_one, list_two)