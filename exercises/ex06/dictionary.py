"""Creating dictionary functions."""

__author__ = "730523395"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values and making sure keys do not repeat."""
    result: dict[str, str] = {}
    for key in a:
        inv_key = a[key]
        result[inv_key] = key
        i: int = 0 
        for key_two in a:
            if inv_key == a[key_two]:
                i += 1
                if i > 1:
                    raise KeyError("inverted values/keys have been repeated.")
        result[inv_key] = key
    return result


def favorite_color(b: dict[str, str]) -> str:
    """Returns the most common color in the dictionary."""
    result: dict[str, int] = {}
    blank: list[str] = []

    for key in b:
        new = b[key]
        blank.append(new)
        result[new] = 0
        for key_two in b:
            if new == b[key_two]:
                result[new] += 1

    common_color: str = blank[0]

    for key_three in result:
        z = result[key_three]
        for key_four in result:
            if result[key_four] > z:
                common_color = key_four

    return common_color


def count(c: list[str]) -> dict[str, int]:
    """Counts how many times a certain item is repeated in the list and returns as a dictionary."""
    built_result: dict[str, int] = {}
    for item in c:
        new = item
        built_result[item] = 0 
        for item_two in c:
            if item_two == new:
                built_result[item] += 1
            # else:
            #     built_result[new] = 1

    return built_result