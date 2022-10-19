import pygame.display


class AppView:
    def __init__(self, width: int, height: int):
        self.surface = pygame.display.set_mode((width, height))
