from abc import ABC, abstractmethod


class AbstractRoundPeg(ABC):
    @abstractmethod
    def get_radius(self): pass


class RoundPeg(AbstractRoundPeg):
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


# Incompatible Square peg
class SquarePeg:
    def __init__(self, width):
        self.width = width

    def get_width(self):
        return self.width
