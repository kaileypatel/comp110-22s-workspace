"""List Utility Functions."""

__author__ = "730523395"


def only_evens(x: list[int]) -> list[int]:
    """Return only the even numbers the user as inputed."""
    i: int = 0 
    result: list[int] = []
    while i < len(x):
        if x[i] % 2 == 0: 
            result.append(x[i])
        i += 1
    return result


def sub(y: list[int], start: int, end: int) -> list[int]:
    """Test for list items with the sublist using the main list items."""
    result_two: list[int] = []
    if start < 0:
        start = 0
    if end > len(y):
        end = len(y)
    if len(y) == 0 or start > len(y) or end <= 0:
        return result_two
    while start < end: 
        result_two.append(y[start])
        start += 1
    return result_two 


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Test to combine all elements of list1 with list2."""
    result_three: list[int] = list1
    for item in list2: 
        result_three.append(item)
    return result_three
