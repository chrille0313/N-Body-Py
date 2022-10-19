import pygame
from Event.Event import Event
from Model.Vector2D import Vector2D
from Event.EventManager import EventManager
from Event.Event import Event


class Camera:
    def __init__(self, width: int, height: int, position: Vector2D, zoom: float = 1, move_speed: float = 1, zoom_speed: float = 0.995) -> None:
        self.canvas_width = width
        self.canvas_height = height
        self.canvas = pygame.display.set_mode((self.canvas_width, self.canvas_height))

        self.position = position
        self.zoom = zoom
        self.aspect_ratio = self.canvas_width / self.canvas_height
        
        self.move_speed = move_speed
        self.zoom_speed = zoom_speed

        EventManager.add_listener(Event.EventType.MOVE_DOWN, self)
        EventManager.add_listener(Event.EventType.MOVE_UP, self)
        EventManager.add_listener(Event.EventType.MOVE_RIGHT, self)
        EventManager.add_listener(Event.EventType.MOVE_LEFT, self)
        EventManager.add_listener(Event.EventType.ZOOM_IN, self)
        EventManager.add_listener(Event.EventType.ZOOM_OUT, self)

    def world_space_to_camera_space(self, position: Vector2D) -> Vector2D:
        new_position = (position - self.position) * self.zoom
        new_position.x += self.aspect_ratio / 2
        new_position.y += 1 / 2
        new_position.y = 1 - new_position.y  # invert y axis
        
        new_position.x += self.canvas_width / 2
        new_position.y += self.canvas_height / 2

        return new_position

    def move(self, direction: Vector2D, dt: float = 1.0) -> None:
        self.position += direction * self.move_speed * dt / self.zoom

    def zoom_in(self, dt: float = 1.0) -> None:
        self.zoom /= self.zoom_speed * dt

    def zoom_out(self, dt: float = 1.0) -> None:
        self.zoom *= self.zoom_speed * dt

    def on_event(self, event):
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

    def fill(self, color):
        self.canvas.fill(color)
