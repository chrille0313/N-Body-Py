from enum import Enum


class Event:
    class EventType(Enum):
        GAME_UPDATE = 0

    def __init__(self, event_type, **kwargs):
        self.type = event_type
        self.kwargs = kwargs
