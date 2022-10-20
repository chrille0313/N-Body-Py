import pygame
from Event.Event import Event
from Model.Vector2D import Vector2D
from Event.EventManager import EventManager
from Event.Event import Event


class Camera:
    """
    Camera class to handle all the logic related to the camera.
    This includes the position of the camera and the zoom level.
    It also handles the events related to the camera.
    """

    def __init__(self, position: Vector2D, zoom: float = 1, move_speed: float = 1, zoom_speed: float = 0.995) -> None:
        self.position = position
        self.zoom = zoom

        self.move_speed = move_speed
        self.zoom_speed = zoom_speed

        EventManager.add_listener(Event.EventType.MOVE_DOWN, self)
        EventManager.add_listener(Event.EventType.MOVE_UP, self)
        EventManager.add_listener(Event.EventType.MOVE_RIGHT, self)
        EventManager.add_listener(Event.EventType.MOVE_LEFT, self)
        EventManager.add_listener(Event.EventType.ZOOM_IN, self)
        EventManager.add_listener(Event.EventType.ZOOM_OUT, self)
        EventManager.add_listener(Event.EventType.SPACE_UPDATE, self)

    def world_space_to_camera_space(self, position: Vector2D) -> Vector2D:
        """
        Converts a world position to be relative to camera.

        :param: position: The position in world space
        :return: The position in camera space
        """

        return (position - self.position) * self.zoom

    def move(self, direction: Vector2D, dt: float = 1.0) -> None:
        """
        Moves the camera in a direction.
        
        :param: direction: The direction to move the camera
        :param: dt: Delta time
        :return: None
        """

        self.position += direction * self.move_speed * dt / self.zoom

    def zoom_in(self, dt: float = 1.0) -> None:
        """
        Zooms in the camera.

        :param: dt: Delta time
        :return: None
        """

        self.zoom /= self.zoom_speed * dt

    def zoom_out(self, dt: float = 1.0) -> None:
        """
        Zooms out the camera.

        :param: dt: Delta time
        :return: None
        """

        self.zoom *= self.zoom_speed * dt

    def on_event(self, event: Event) -> None:
        """
        Handles event when event is fetched by EventManager.

        :param event: 
        :return:
        """

        if event.type == Event.EventType.MOVE_UP:
            self.move(Vector2D(0, self.move_speed))
        if event.type == Event.EventType.MOVE_DOWN:
            self.move(Vector2D(0, -self.move_speed))
        if event.type == Event.EventType.MOVE_LEFT:
            self.move(Vector2D(-self.move_speed, 0))
        if event.type == Event.EventType.MOVE_RIGHT:
            self.move(Vector2D(self.move_speed, 0))
        if event.type == Event.EventType.ZOOM_IN:
            self.zoom_in()
        if event.type == Event.EventType.ZOOM_OUT:
            self.zoom_out()

        EventManager.post(Event(Event.EventType.CAMERA_UPDATE))
