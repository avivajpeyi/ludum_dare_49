import math
from enum import Enum
from typing import Optional

import pygame
import pymunk
import pymunk.pygame_util

from .constants import HEIGHT, WIDTH
from .screen_handler import ScreenHandler

G = 5.0e6  # phoney gravitational constant

DEBUG_PHYSICS = False


class CollisionType(Enum):
    ENEMY = 1
    PLANET = 2
    LASER = 3


class GamePhysicsHandler:
    def __init__(
        self, screen_handler: ScreenHandler, update_frequency: Optional[int] = 60
    ):
        self.space = pymunk.Space()
        self.screen_handler = screen_handler
        self.update_frequency = update_frequency
        self.dt = 1.0 / self.update_frequency
        # self.space.damping = 0.9
        self.physics_game_objects = []

        self.DEBUG_MODE = DEBUG_PHYSICS
        if self.DEBUG_MODE:
            self.draw_options = pymunk.pygame_util.DrawOptions(self.screen_handler.screen)

    def update(self):
        """Update the space for the given time step."""
        if DEBUG_PHYSICS:
            self.space.debug_draw(self.draw_options)
        self.space.step(self.dt)

    def track_object(self, game_object):
        self.space.add(game_object.rigid_body, game_object.collider)
        self.physics_game_objects.append(game_object)

    def remove_object(self, game_object):
        self.space.remove(game_object.rigid_body, game_object.collider)
        self.physics_game_objects.remove(game_object)  # THIS MAY NOT WORK


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
