


def long_cat_is_long(text: str) -> dict[str, int]:
    """
    Return a dictionary mapping unique words to their lengths.
    Remove non-letter characters and convert words to lowercase.
    """
    clean_text = "".join(
        char.lower() if char.isalpha() else " "
        for char in text
    )

    return {
        word: len(word)
        for word in clean_text.split()
    }


def main():
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is moving
    in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send
    signals here, they receive them there.
    The only difference is that there is no cat.
    """

    print(long_cat_is_long(text))


if __name__ == "__main__":
    main()
