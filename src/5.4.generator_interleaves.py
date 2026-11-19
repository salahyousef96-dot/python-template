
from itertools import zip_longest


def generator_interleaves(*iterables):
    """
    Yield elements from multiple iterables in alternating order.
    """
    sentinel = object()

    for group in zip_longest(*iterables, fillvalue=sentinel):
        for item in group:
            if item is not sentinel:
                yield item


def main():
    result = generator_interleaves(
        "abc", [1, 2, 3], ("!", "@", "#")
    )
    print(list(result))


if __name__ == "__main__":
    main()
