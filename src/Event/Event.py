from enum import Enum, auto


class Event:
    """
        Represents an application event. Can also pass along data using args and kwargs
    """

    class EventType(Enum):
        # App events
        APP_UPDATE = auto()     # App finished one update cycle
        SPACE_UPDATE = auto()   # Space changed
        CAMERA_UPDATE = auto()  # Camera changed
        RENDER = auto()         # We should render

        # Movement
        MOVE_UP = auto()
        MOVE_DOWN = auto()
        MOVE_LEFT = auto()
        MOVE_RIGHT = auto()
        ZOOM_IN = auto()
        ZOOM_OUT = auto()

    def __init__(self, event_type, *args, **kwargs):
        self.type = event_type
        self.args = args
        self.kwargs = kwargs
