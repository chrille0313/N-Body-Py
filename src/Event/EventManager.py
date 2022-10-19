import Event.Event


class EventManager:
    listeners = {}

    @classmethod
    def add_listener(cls, event_type, listener):
        if event_type not in cls.listeners:
            cls.listeners[event_type] = []

        cls.listeners[event_type].append(listener)

    @classmethod
    def remove_listener(cls, event_type, listener):
        if event_type in cls.listeners:
            cls.listeners[event_type].remove(listener)

    @classmethod
    def post(cls, event):
        if event.type in cls.listeners:
            for listener in cls.listeners[event.type]:
                listener.on_event(event)

    @classmethod
    def clear(cls):
        cls.listeners = {}
