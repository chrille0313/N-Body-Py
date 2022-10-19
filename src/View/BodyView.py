import pygame
from Model.Body import Body


class BodyView:
    """
        A class representing a body view.
    """

    # TODO: Fix maybe?
    max_mass = 0

    @classmethod
    def render(cls, camera, body: Body, color: tuple[int, int, int] = None) -> None:
        cls.max_mass = max(cls.max_mass, body.mass)

        color_gradient = 255 * body.mass / cls.max_mass
        color = color if color is not None else (color_gradient, 255 - color_gradient, 0)

        pygame.draw.circle(camera.canvas, color, camera.world_space_to_camera_space(body.position), body.size * camera.zoom)
