from itertools import zip_longest


def interleave(*iterables) -> list:
    """
    Combine elements from iterables in alternating order.
    """
    result = []
    sentinel = object()

    for group in zip_longest(*iterables, fillvalue=sentinel):
        for item in group:
            if item is not sentinel:
                result.append(item)

    return result


def main():
    print(interleave("abc", [1, 2, 3], ("!", "@", "#")))


if __name__ == "__main__":
    main()
