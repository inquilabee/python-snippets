from contextlib import suppress
from abc import ABC, abstractmethod


class AbstractSubscriber(ABC):
    @abstractmethod
    def update(self, context):
        pass


class AbstractPublisher(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def subscribe(self, observer: AbstractSubscriber) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def unsubscribe(self, observer: AbstractSubscriber) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify_subscribers(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class Publisher(AbstractPublisher):
    def __init__(self):
        self._subscribers: list[AbstractSubscriber] = []

    def subscribe(self, subscriber: AbstractSubscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: AbstractSubscriber):
        with suppress(ValueError):
            self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update(self)
