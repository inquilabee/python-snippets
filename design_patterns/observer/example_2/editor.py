from event_manager import EventManager
from typing import Optional


class Editor:
    """The Subject/Publisher"""

    def __init__(self):
        self.events: Optional[EventManager] = EventManager()

    def open_file(self, file_path):
        # open file
        self.events.notify("open", file_path)

    def close_file(self, file_path):
        # close fle
        self.events.notify("close", file_path)

    def save_file(self, file_path):
        # save file
        self.events.notify("save", file_path)
