import random
from math import sqrt
from Model.Body import Body
from Model.Vector2D import Vector2D
from Event.EventManager import EventManager
from Event.Event import Event


def gravitational_force(body1: Body, body2: Body, G: float = 10000) -> Vector2D:
    """
        Calculate the gravitational force between two bodies
        using Newton's law of gravitational attraction.
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

        Handles looping over all the bodies performing gravity and collision calculations.
    """

    def __init__(self, width: int, height: int, num_bodies: int):
        self.width = width
        self.height = height
        self.bodies = Space.create_galaxy(width, height, num_bodies)
        self.max_mass = max(self.bodies, key=lambda body: body.mass).mass

    @classmethod
    def create_galaxy(cls, width: int, height: int, num_bodies: int,
                      min_mass: int = 10, max_mass: int = 100,
                      min_velocity: int = 0, max_velocity: int = 250) -> list[Body]:

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

    @classmethod
    def bodies_are_colliding(cls, body1: Body, body2: Body) -> bool:
        tot_size = body1.size + body2.size
        return (body1.position - body2.position).magnitude_squared() <= tot_size * tot_size

    @classmethod
    def bodies_are_moving_apart(cls, body1: Body, body2: Body) -> bool:
        return (body1.position - body2.position).dot(body1.velocity - body2.velocity) > 0

    @classmethod
    def get_intersection_vector(cls, body1: Body, body2: Body) -> Vector2D:
        """
            Get the vector required to move body1 out of body2, relative by their mass.
        """

        displacement = body1.position - body2.position
        displacement_dist = displacement.magnitude()
        intersection_vector = displacement * (body1.size + body2.size - displacement_dist) / displacement_dist  # minimum distance to make sure bodies don't overlap

        return intersection_vector * body1.mass / (body1.mass + body2.mass)

    @classmethod
    def resolve_collision(cls, body1: Body, body2: Body) -> None:
        """
            Resolve a collision between two bodies by moving them out of each other.
        """

        intersection_vector = cls.get_intersection_vector(body1, body2)
        body1.position += intersection_vector
        body2.position -= intersection_vector

    @classmethod
    def elastic_collision(cls, body1: Body, body2: Body) -> None:
        """
            Calculate new velocities between two bodies by applying an elastic collision.
            https://en.wikipedia.org/wiki/Elastic_collision
        """

        displacement = body1.position - body2.position  # Update displacement as we have moved the bodies
        v_diff = body1.velocity - body2.velocity
        impulse = 2 / (body1.mass + body2.mass) * v_diff.dot(displacement) / displacement.magnitude_squared() * displacement
        body1.velocity -= impulse * body2.mass
        body2.velocity += impulse * body1.mass

    @classmethod
    def collide_bodies(cls, body1: Body, body2: Body) -> None:
        cls.resolve_collision(body1, body2)

        if cls.bodies_are_moving_apart(body1, body2):
            return  # No collision as bodies are moving apart

        cls.elastic_collision(body1, body2)

    def body_collision(self) -> None:
        for i, body in enumerate(self.bodies):
            for j, other_body in enumerate(self.bodies):
                if i != j and self.bodies_are_colliding(body, other_body):
                    self.collide_bodies(body, other_body)

    def collision(self) -> None:
        self.bounding_box_collision()
        self.body_collision()

    def update(self, dt: float = 1) -> None:
        # Gravity
        try:
            for i, body in enumerate(self.bodies):
                force = Vector2D(0, 0)

                # Sum the force exerted by all other bodies
                for j, other_body in enumerate(self.bodies):
                    if i != j:
                        force += gravitational_force(body, other_body)

                body.acceleration = force / body.mass

            # Collision
            self.collision()

        except ZeroDivisionError:
            pass

        # Update
        for body in self.bodies:
            body.update(dt)

        EventManager.post(Event(Event.EventType.SPACE_UPDATE, dt))
