

from PIL import Image


def remember_remember(file_path: str) -> str:
    """
    Decode a message using black pixel positions
    """
    message = []

    with Image.open(file_path) as source:
        image = source.convert("RGB")
        width, height = image.size

        for column in range(width):
            black_rows = [
                row
                for row in range(height)
                if image.getpixel((column, row)) == (0, 0, 0)
            ]

            if len(black_rows) != 1:
                raise ValueError(
                    f"Invalid black pixels in column {column}"
                )

            message.append(chr(black_rows[0]))

    return "".join(message)


def main():
    file_path = input("Enter image path: ")

    try:
        print(remember_remember(file_path))
    except (OSError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
