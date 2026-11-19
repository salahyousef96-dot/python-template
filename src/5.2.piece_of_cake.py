

def piece_of_cake(
    prices: dict[str, float],
    optionals: list[str] | None = None,
    **ingredients: float
) -> float:
    """Calculate recipe cost based on ingredient quantities in grams."""
    if optionals is None:
        optionals = []

    total_price = 0

    for ingredient, price in prices.items():
        if ingredient not in optionals:
            quantity = ingredients[ingredient]
            total_price += price * quantity / 100

    return total_price


def main():
    prices = {"chocolate": 18, "milk": 8}

    print(piece_of_cake(
        prices, chocolate=200, milk=100
    ))

    print(piece_of_cake(
        prices, optionals=["milk"], chocolate=300
    ))

    print(piece_of_cake({}))


if __name__ == "__main__":
    main()

