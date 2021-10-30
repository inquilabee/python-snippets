from core import AbstractStrategy


class AddStrategy(AbstractStrategy):
    def execute(self, a, b):
        return a + b


class SubtractStrategy(AbstractStrategy):
    def execute(self, a, b):
        return a - b


class MultiplyStrategy(AbstractStrategy):
    def execute(self, a, b):
        return a * b
