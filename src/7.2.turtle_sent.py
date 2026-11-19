

class PostOffice:

    def __init__(self, usernames: list[str]) -> None:
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(
        self,
        sender: str,
        recipient: str,
        message_body: str,
        urgent: bool = False,
        subject: str = ""
    ) -> int:
        user_box = self.boxes[recipient]
        self.message_id += 1

        message_details = {
            "id": self.message_id,
            "body": message_body,
            "sender": sender,
            "subject": subject,
            "read": False
        }

        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)

        return self.message_id

    def read_inbox(
        self,
        username: str,
        n: int | None = None
    ) -> list[dict]:
        unread = [
            message
            for message in self.boxes[username]
            if not message.get("read", False)
        ]

        if n is not None:
            if n < 0:
                raise ValueError("n cannot be negative")
            unread = unread[:n]

        for message in unread:
            message["read"] = True

        return unread

    def search_inbox(
        self,
        username: str,
        text: str
    ) -> list[dict]:
        return [
            message
            for message in self.boxes[username]
            if (
                text in message.get("subject", "")
                or text in message["body"]
            )
        ]


def turtle_sent():
    post_office = PostOffice(["Alice", "Bob"])

    post_office.send_message(
        "Alice", "Bob", "Hello Bob!", subject="Greetings"
    )
    post_office.send_message(
        "Alice", "Bob", "Python homework", subject="Homework"
    )
    post_office.send_message(
        "Alice", "Bob", "Important update", urgent=True
    )

    print(post_office.read_inbox("Bob", 2))
    print(post_office.read_inbox("Bob"))
    print(post_office.read_inbox("Bob"))
    print(post_office.search_inbox("Bob", "Python"))


if __name__ == "__main__":
    turtle_sent()
