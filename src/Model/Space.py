import random
from math import sqrt
from Model.Body import Body
from Model.Vector2D import Vector2D


def gravitational_force(body1: Body, body2: Body, G: float = 0.01) -> Vector2D:
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
                      min_mass: int = 10, max_mass: int = 100,
                      min_velocity: int = 0, max_velocity: int = 0.01) -> list[Body]:
        bodies = []

        for _ in range(num_bodies):
            mass = random.randint(min_mass, max_mass)
            radius = sqrt(mass)

            position = Vector2D(random.uniform(0, width - radius), random.uniform(0, height - radius))
            velocity = Vector2D(random.uniform(min_velocity, max_velocity), random.uniform(min_velocity, max_velocity))
            bodies.append(Body(position, mass, velocity))

        return bodies
    
    def bounding_box_collision(self) -> None:
        for body in self.bodies:
            if body.position.x < 0:
                body.position.x = 0
                body.velocity.x *= -1
            elif body.position.x > self.width:
                body.position.x = self.width
                body.velocity.x *= -1

            if body.position.y < 0:
                body.position.y = 0
                body.velocity.y *= -1
            elif body.position.y > self.height:
                body.position.y = self.height
                body.velocity.y *= -1

    def bodies_are_colliding(self, body1: Body, body2: Body) -> bool:
        totSize = body1.size + body2.size
        return (body1.position - body2.position).magnitude_squared() <= totSize * totSize

    def collide_bodies(self, body1: Body, body2: Body) -> None:
        displacement = body1.position - body2.position
        d = displacement.magnitude()
        intersectionDistance = displacement * (body1.size + body2.size - d) / d  # minimum distance to make sure bodies don't overlap

        inverseMass = 1 / body1.mass
        inverseMassOther = 1 / body2.mass

        body1.position += intersectionDistance * inverseMass / (inverseMass + inverseMassOther)
        body2.position -= intersectionDistance * inverseMassOther / (inverseMass + inverseMassOther)

        vDiff = body1.velocity - body2.velocity
        if vDiff.dot(displacement.normalize()) > 0.0:
            return  # No collision as bodies are moving apart

        # Calculate the new velocities using conservation of momentum and kinetic energy (elastic collisions)
        # https://en.wikipedia.org/wiki/Elastic_collision

        displacement = body1.position - body2.position  # Update displacement as we have moved the bodies
        impulse = 2 / (body1.mass + body2.mass) * vDiff.dot(displacement) / displacement.magnitude_squared() * displacement
        body1.velocity -= impulse * body2.mass
        body2.velocity += impulse * body1.mass

    def body_collision(self) -> None:
        for i, body in enumerate(self.bodies):
            for j, other_body in enumerate(self.bodies):
                if i != j and self.bodies_are_colliding(body, other_body):
                    if self.bodies_are_colliding(body, other_body):
                        self.collide_bodies(body, other_body)

    def collision(self) -> None:
        self.bounding_box_collision()
        self.body_collision()

    def update(self, dt: float = 1) -> None:
        # Gravity
        for i, body in enumerate(self.bodies):
            force = Vector2D(0, 0)

            for j, other_body in enumerate(self.bodies):
                if i != j:
                    force += gravitational_force(body, other_body)

            body.acceleration = force / body.mass

        # Collision
        self.collision()

        # Update
        for body in self.bodies:
            body.update(dt)
