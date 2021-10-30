from core import AbstractStrategy


class Context:
    _strategy: AbstractStrategy = None

    def __init__(self, strategy=None):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, val):
        self._strategy = val

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)
