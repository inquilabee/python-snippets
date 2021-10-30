"""
Reference: https://sbcode.net/python/state/
"""

from abc import ABCMeta, abstractmethod
from itertools import cycle


class Context:
    """This is the object whose behavior will change"""

    def __init__(self):
        self.state_handles = [
            Started(),
            Running(),
            Finished()
        ]
        self._handle = cycle(self.state_handles)

    def request(self):
        """Each time the request is called, a new class will handle it"""

        handler = next(self._handle)
        handler()


class IState(metaclass=ABCMeta):
    """A State Interface"""

    @staticmethod
    @abstractmethod
    def __call__():
        """Set the default method"""
        pass


class Started(IState):
    """A ConcreteState Subclass"""

    @staticmethod
    def method():
        """A task of this class"""
        print("Task Started")

    __call__ = method


class Running(IState):
    """A ConcreteState Subclass"""

    @staticmethod
    def method():
        """A task of this class"""
        print("Task Running")

    __call__ = method


class Finished(IState):
    """A ConcreteState Subclass"""

    @staticmethod
    def method():
        """A task of this class"""
        print("Task Finished")

    __call__ = method


if __name__ == '__main__':
    CONTEXT = Context()
    CONTEXT.request()
    CONTEXT.request()
    CONTEXT.request()
    CONTEXT.request()
    CONTEXT.request()
    CONTEXT.request()
