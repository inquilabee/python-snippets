"""Composite pattern

Adapted from: https://github.com/jackdbd/design-patterns/blob/master/composite.py
"""
from contextlib import suppress

from component import Component


class MultipleParentsException(Exception):
    pass


class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = list()

    def append_child(self, child):
        """
        Extra checks to make sure that a child has only one parent component.
        """
        if child.parent and child.parent is not self:
            raise MultipleParentsException(
                f"Child {child.name} ({child.__class__.__name__}) belongs to another parent {child.parent.name}"
            )

        if child not in self.children:
            child.level = self.level + 1
            child.indentation = " " * child.level * 4
            child.parent = self
            self.children.append(child)

    def remove_child(self, child):
        with suppress(ValueError):
            self.children.remove(child)
            child.reset_component()

    def traverse(self):
        print(f"{self.indentation}{self.name}")
        [x.traverse() for x in self.children]
