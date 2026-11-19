

def parsle_tongue(file_path: str) -> list[str]:
    """
    Find secret messages hidden in a binary file.
    """
    messages = []
    current_word = bytearray()

    with open(file_path, "rb") as image_file:
        while True:
            chunk = image_file.read(4096)

            if not chunk:
                break

            for byte in chunk:
                if 97 <= byte <= 122:
                    current_word.append(byte)

                elif byte == 33:
                    if len(current_word) >= 5:
                        message = current_word.decode("ascii") + "!"
                        messages.append(message)
                    current_word.clear()

                else:
                    current_word.clear()

    return messages


def main():
    file_path = input("Enter image path: ")

    try:
        messages = parsle_tongue(file_path)
        print(messages)
    except (OSError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
