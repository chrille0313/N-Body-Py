import pygame

from Model.Body import Body


class BodyView:
    """
        A class representing a body view.
    """

    @classmethod
    def render(cls, camera_view, camera, max_mass, body: Body, color: tuple[int, int, int] = None) -> None:
        color_gradient = 255 * body.mass / max_mass
        color = color if color is not None else (color_gradient, 255 - color_gradient, 0)

        camera_space = camera.world_space_to_camera_space(body.position)
        screen_space = camera_view.camera_space_to_screen_space(camera_space)

        pygame.draw.circle(camera_view.canvas, color, screen_space, body.size * camera.zoom)
