import pygame
from Model import Body


class BodyView:
    """
        A class representing a body view.
    """

    @classmethod
    def draw(cls, screen: pygame.Surface, body: Body, color: tuple[int, int, int] = (255, 255, 255)) -> None:
        pygame.draw.circle(screen, color, body.position, body.size)
