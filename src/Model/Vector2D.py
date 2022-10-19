from pygame import Vector2


class Vector2D(Vector2):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)
