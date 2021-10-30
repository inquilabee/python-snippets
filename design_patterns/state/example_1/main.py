"""
Adapted from: https://github.com/faif/python-patterns/blob/master/patterns/behavioral/state.py

A radio can toggle between an AM state and an FM state. Based on the radio's
current state, it behaves differently to various actions such as scan (i.e. play
the next song).

The concrete state objects below, AMState and FMState has access to the parent object,
that is, the Radio object these objects are a part of. Whenever there's is a toggle
from current state, the current state uses the radio object to toggle to another state.

Also, the Radio object delegates the work of toggling the state to the current state.
"""

from abc import ABC, abstractmethod


class State(ABC):
    """Base state. This is to share functionality"""

    def __init__(self):
        self.stations: list = []
        self.name: str = ""
        self.pos: int = -1

    def scan(self):
        """Scan the dial to the next station"""
        self.pos = (self.pos + 1) % len(self.stations)
        print("Scanning... Station is {} {}".format(self.stations[self.pos], self.name))

    @abstractmethod
    def toggle_am_fm(self): pass


class AMState(State):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_am_fm(self):
        print("Switching to FM")
        self.radio.state = self.radio.fm_state


class FMState(State):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_am_fm(self):
        print("Switching to AM")
        self.radio.state = self.radio.am_state


class Radio:
    """A radio.
    It has a scan button, and an AM/FM toggle switch.
    """

    def __init__(self):
        """We have an AM state and an FM state"""
        self.am_state = AMState(self)
        self.fm_state = FMState(self)
        self.state = self.am_state

    def toggle_am_fm(self):
        self.state.toggle_am_fm()

    def scan(self):
        self.state.scan()


def main():
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_am_fm] * 3 + [radio.scan] * 5

    for action in actions:
        action()


if __name__ == "__main__":
    main()
