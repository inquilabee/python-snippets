from abc import ABC, abstractmethod


class AbstractStrategy(ABC):
    @abstractmethod
    def execute(self, a, b): pass
