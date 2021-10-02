import math
from typing import Optional

import pygame
import pymunk
import pymunk.pygame_util

from .constants import HEIGHT, WIDTH

G = 5.0e6  # phoney gravitational constant

DEBUG_MODE = True


class GamePhysicsHandler:
    def __init__(
        self, screen: pygame.Surface, update_frequency: Optional[int] = 60
    ):
        self.space = pymunk.Space()
        self.screen = screen
        self.update_frequency = update_frequency
        self.dt = 1.0 / self.update_frequency
        self.space.damping = 0.9

    def update(self):
        """Update the space for the given time step."""
        self.space.step(self.dt)


def planet_gravity(
    body: pymunk.Body, gravity: float, damping: float, dt: float
):
    """
    Gravitational acceleration is proportional to the inverse square of
    distance, and directed toward the origin. The central planet is assumed
    to be massive enough that it affects the satellites but not vice versa.

    This function is structed to be used as a pymunk.velocity_func
    http://www.pymunk.org/en/latest/pymunk.html#pymunk.Body.velocity_func
    """
    sq_dist = body.position.get_dist_sqrd((WIDTH / 2, HEIGHT / 2))
    g = (
        (body.position - pymunk.Vec2d(WIDTH / 2, HEIGHT / 2))
        * -G
        / (sq_dist * math.sqrt(sq_dist))
    )
    pymunk.Body.update_velocity(body, g, damping, dt)
