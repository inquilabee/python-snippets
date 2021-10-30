from base import Publisher


class DataPublisher(Publisher):
    def __init__(self, name: str = ""):
        super().__init__()
        self.name = name
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        self._data = val
        self.notify_subscribers()
