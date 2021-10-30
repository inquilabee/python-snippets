"""
Adapted from: https://github.com/faif/python-patterns/blob/master/patterns/structural/composite.py
"""

from abc import ABC, abstractmethod
from typing import List
from contextlib import suppress


class Graphic(ABC):
    @abstractmethod
    def render(self) -> None: pass


class CompositeGraphic(Graphic):
    def __init__(self) -> None:
        self.graphics: List[Graphic] = []

    def render(self) -> None:
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic: Graphic) -> None:
        if graphic not in self.graphics:
            self.graphics.append(graphic)

    def remove(self, graphic: Graphic) -> None:
        with suppress(ValueError):
            self.graphics.remove(graphic)


class Ellipse(Graphic):
    def __init__(self, name: str) -> None:
        self.name = name

    def render(self) -> None:
        print(f"Ellipse: {self.name}")


def main():
    ellipse1 = Ellipse("1")
    ellipse2 = Ellipse("2")
    ellipse3 = Ellipse("3")
    ellipse4 = Ellipse("4")

    graphic1 = CompositeGraphic()
    graphic2 = CompositeGraphic()

    graphic1.add(ellipse1)
    graphic1.add(ellipse2)
    graphic1.add(ellipse3)
    graphic2.add(ellipse4)

    graphic = CompositeGraphic()

    graphic.add(graphic1)
    graphic.add(graphic2)

    graphic.render()


if __name__ == "__main__":
    main()
