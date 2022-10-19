import pygame
from Model.Space import Space
from View.Body_View import BodyView


class GalaxyView:
    def __init__(self, width: int, height: int, space_model: Space):
        self.space_model = space_model

    def render(self, surface: pygame.surface):
        for body in self.space_model.bodies:
            BodyView.draw(surface, body)