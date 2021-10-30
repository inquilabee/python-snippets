import datetime
from listeners import EventListener
from editor import Editor


class LoggingListener(EventListener):
    def __init__(self, log_file, message):
        self.log_file = log_file
        self.message = message

    def update(self, filename):
        with open(self.log_file, "a+") as f:
            f.write(
                f"{datetime.datetime.now()}: {filename} {self.message} \n"
            )


class EmailListener(EventListener):

    def __init__(self, email, message):
        self.email = email
        self.message = message

    def update(self, filename):
        message = f"{self.message}: {filename}"
        print(f"Email to {self.email} with message `{message}` was sent at {datetime.datetime.now()}")


if __name__ == '__main__':
    editor = Editor()

    file_open_logger = LoggingListener(log_file="./data/open_file.log", message="file was opened")
    editor.events.subscribe("open", file_open_logger)

    file_close_logger = LoggingListener(log_file="./data/close_file.log", message="file was closed")
    editor.events.subscribe("close", file_close_logger)

    email_listener = EmailListener(email="abc@example.com", message="Someone changed the file")
    editor.events.subscribe("close", email_listener)

    editor.open_file("some_file.txt")
    editor.close_file("some_file.txt")

    editor.open_file("some_other_file.txt")
    editor.close_file("some_other_file.txt")
