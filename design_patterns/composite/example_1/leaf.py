"""Composite pattern

Adapted from: https://github.com/jackdbd/design-patterns/blob/master/composite.py
"""
from component import Component


class Leaf(Component):
    def traverse(self):
        print(f"{self.indentation}{self.name}")
