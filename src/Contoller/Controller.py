import pygame


class Controller:
    @classmethod
    def get_input(cls):
        return pygame.key.get_pressed()
