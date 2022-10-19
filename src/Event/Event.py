from enum import Enum, auto


class Event:
    class EventType(Enum):
        APP_UPDATE = auto()
        MOVE_UP = auto()
        MOVE_DOWN = auto()
        MOVE_LEFT = auto()
        MOVE_RIGHT = auto()
        ZOOM_IN = auto()
        ZOOM_OUT = auto()
        PAUSE = auto()

    def __init__(self, event_type, *args, **kwargs):
        self.type = event_type
        self.args = args
        self.kwargs = kwargs
