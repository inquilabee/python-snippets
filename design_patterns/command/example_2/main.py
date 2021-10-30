"""
Adapted from: https://github.com/faif/python-patterns/blob/master/patterns/behavioral/command.py
"""

from typing import Union


class HideFileCommand:
    """
    A command to hide a file given its name
    """

    def __init__(self) -> None:
        # an array of files hidden, to undo them as needed
        self._hidden_files = []

    def execute(self, filename: str) -> None:
        print(f"hiding {filename}")
        self._hidden_files.append(filename)

    def undo(self) -> None:
        filename = self._hidden_files.pop()
        print(f"un-hiding {filename}")


class DeleteFileCommand:
    """
    A command to delete a file given its name
    """

    def __init__(self) -> None:
        # an array of deleted files, to undo them as needed
        self._deleted_files = []

    def execute(self, filename: str) -> None:
        print(f"deleting {filename}")
        self._deleted_files.append(filename)

    def undo(self) -> None:
        filename = self._deleted_files.pop()
        print(f"restoring {filename}")


class MenuItem:  # Invoker
    """
    The invoker class. Here it is items in a menu.
    """

    def __init__(self, command: Union[HideFileCommand, DeleteFileCommand]) -> None:
        self._command = command

    def on_do_press(self, filename: str) -> None:
        self._command.execute(filename)

    def on_undo_press(self) -> None:
        self._command.undo()


def main():
    delete_command = DeleteFileCommand()
    hide_command = HideFileCommand()

    menu_item_1 = MenuItem(delete_command)
    menu_item_2 = MenuItem(hide_command)

    # create a file named `test-file` to work with
    test_file_name = 'test-file'

    # deleting `test-file`
    menu_item_1.on_do_press(test_file_name)

    # restoring `test-file`
    menu_item_1.on_undo_press()

    # hiding `test-file`
    menu_item_2.on_do_press(test_file_name)

    # un-hiding `test-file`
    menu_item_2.on_undo_press()


if __name__ == "__main__":
    main()
