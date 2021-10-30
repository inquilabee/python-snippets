class EventManager:
    def __init__(self):
        self._listeners = []

    def subscribe(self, event_type, listener):
        if (listener_object := (event_type, listener)) not in self._listeners:
            self._listeners.append(listener_object)

    def unsubscribe(self, event_type, listener):
        self._listeners.append((event_type, listener))

    def notify(self, event_type, data):
        for e_type, listener in self._listeners:
            if e_type == event_type:
                listener.update(data)
