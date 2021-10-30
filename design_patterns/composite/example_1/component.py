"""Composite pattern

Adapted from: https://github.com/jackdbd/design-patterns/blob/master/composite.py
"""
from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.indentation = ""
        self.parent = None

    def reset_component(self):
        self.level = 0
        self.indentation = ""
        self.parent = None

    def detach(self):
        """Remove the bidirectional connect between parent and child.
        The children of the child stays with child."""

        if self.parent:
            self.parent.remove_child(self)

    @abstractmethod
    def traverse(self):
        """Print the name of this component and all of its children.

        Implement in Composite and Leaf
        """
        pass
