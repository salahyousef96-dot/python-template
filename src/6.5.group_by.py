

from collections.abc import Callable, Iterable
from typing import Any


def group_by(
    func: Callable,
    iterable: Iterable
) -> dict[Any, list]:
    """
    Group elements according to the result of a function.
    """
    result = {}

    for item in iterable:
        key = func(item)

        if key not in result:
            result[key] = []

        result[key].append(item)

    return result


def main():
    words = ["hi", "bye", "yo", "try"]
    print(group_by(len, words))


if __name__ == "__main__":
    main()
