from base import AbstractSubscriber
from publishers import DataPublisher


class HexViewer(AbstractSubscriber):
    def update(self, context: DataPublisher):
        print(f"Observer {self.__class__.__name__} received {context.data} from {context.name}")


class DecimalViewer(AbstractSubscriber):
    def update(self, context: DataPublisher):
        print(f"Observer {self.__class__.__name__} received {context.data} from {context.name}")
