from math import sqrt
from Model import Vector2D


class Body:
    """
        A class representing a body in space.
    """

    def __init__(self, position: Vector2D,
                 mass: int,
                 velocity: Vector2D = Vector2D(0, 0),
                 acceleration: Vector2D = Vector2D(0, 0)):
        self.position = position
        self.mass = mass
        self.velocity = velocity
        self.acceleration = acceleration

    @property
    def size(self) -> float:
        return sqrt(self.mass)

    def update(self, dt: float = 1) -> None:
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        self.acceleration *= 0
