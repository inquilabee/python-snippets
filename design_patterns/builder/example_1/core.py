"""
Adapted from: https://github.com/faif/python-patterns/blob/master/patterns/creational/builder.py
"""

from abc import ABC, abstractmethod


class BasicBuilding(ABC):
    floor: str
    size: str

    @abstractmethod
    def build_floor(self): pass

    @abstractmethod
    def build_size(self): pass

    def __repr__(self):
        return f"Floor: {self.floor} | Size: {self.size}"


class BaseBuilding(BasicBuilding):  # noqa (for PyCharm)

    def __init__(self):
        self.build_floor()
        self.build_size()
