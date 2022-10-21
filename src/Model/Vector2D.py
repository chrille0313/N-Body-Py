from pygame import Vector2


class Vector2D(Vector2):
    """
        Instead of using Vector2 directly, we inherit from it in case we want to extend it.
    """
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)
