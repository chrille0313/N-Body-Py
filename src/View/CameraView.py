import pygame
from Event.Event import Event
from Event.EventManager import EventManager
from Model.Vector2D import Vector2D


class CameraView:
    """
        Camera class to handle rendering of a model.
        It is made up of a canvas with given dimensions and a model to render.
    """

    def __init__(self, width: int, height: int, camera_model) -> None:
        self.canvas_width = width
        self.canvas_height = height
        self.canvas = pygame.display.set_mode((self.canvas_width, self.canvas_height))
        self.aspect_ratio = self.canvas_width / self.canvas_height

        self.model = camera_model

        EventManager.add_listener(Event.EventType.CAMERA_UPDATE, self)

    def camera_space_to_screen_space(self, position: Vector2D) -> Vector2D:
        """
            Converts a position relative to camera, to a screen position.

            :param: position: Position relative to camera
            :return: Position in screen space
        """

        new_position = position + Vector2D(self.canvas_width / 2, self.canvas_height / 2)
        new_position.y = self.canvas_height - new_position.y  # Invert y-axis
        return new_position

    def on_event(self, event):
        if event.type == Event.EventType.CAMERA_UPDATE:
            self.canvas.fill((0, 0, 0))  # Clear the screen
            EventManager.post(Event(Event.EventType.RENDER, self.model, self))
            pygame.display.update()
