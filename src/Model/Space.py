import math
import random
from Model import Body
from Model import Vector2D


def gravitational_force(body1: Body, body2: Body, G: float = 5.0) -> Vector2D:
    """
        Calculate the gravitational force between two bodies.
    """

    displacement = body2.position - body1.position
    min_displacement = body1.size + body2.size  # Minimum distance between bodies is the sum of their radii
    direction = displacement.normalize()

    force = (body1.mass * body2.mass) / max(displacement.magnitude_squared(),
                                            min_displacement * min_displacement)  # Don't divide by zero
    return direction * G * force


class Space:
    """
        A class representing a space of bodies.
    """

    def __init__(self, width: int, height: int, num_bodies: int):
        self.width = width
        self.height = height
        self.bodies = Space.create_galaxy(width, height, num_bodies)

    @classmethod
    def create_galaxy(cls, width: int, height: int, num_bodies: int,
                      min_mass: int = 10, max_mass: int = 1000,
                      min_velocity: int = 0, max_velocity: int = 40) -> list[Body]:
        bodies = []

        for i in range(num_bodies):
            mass = random.randint(min_mass, max_mass)
            radius = math.sqrt(mass)

            position = Vector2D(random.uniform(0, width - radius), random.uniform(0, height - radius))
            velocity = Vector2D(random.uniform(min_velocity, max_velocity), random.uniform(min_velocity, max_velocity))
            bodies.append(Body(position, mass, velocity))

        return bodies

    def update(self, dt: float = 1) -> None:
        # Gravity
        for i, body in enumerate(self.bodies):
            force = Vector2D(0, 0)

            for j, other_body in enumerate(self.bodies):
                if i != j:
                    force += gravitational_force(body, other_body)

            body.acceleration = force / body.mass

        # Collision

        # Update
        for body in self.bodies:
            body.update(dt)
