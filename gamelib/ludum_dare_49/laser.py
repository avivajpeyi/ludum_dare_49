import math
from typing import Optional

import numpy as np
import pygame
import pymunk

from ludum_dare_49 import colors
from ludum_dare_49.constants import LASER_LENGTH, LASER_SPEED, LASER_WIDTH

from .game_object import GameObject
from .physics import CollisionType, GamePhysicsHandler


class Laser(GameObject):
    def __init__(
        self,
        screen: pygame.Surface,
        angle: float,
        color,
        physics_handler: Optional[GamePhysicsHandler] = None,
    ):
        """
        Initialize the laser based on the current position of the player
        """
        self.screen = screen
        self.angle = angle
        self.color = color
        self.speed = LASER_SPEED
        self.r = 50  # separation from center of the sceen # TODO
        self.x = self.r * np.cos(self.angle) + self.screen_center[0]
        self.y = self.r * np.sin(self.angle) + self.screen_center[1]
        self.length = LASER_LENGTH
        self.width = LASER_WIDTH

        super().__init__(
            screen=screen,
            color=color,
            x=self.x,
            y=self.y,
            physics_handler=physics_handler,
        )

    def _init_rect(self) -> pygame.Rect:
        return pygame.Rect(
            self.x - self.width / 2,
            self.y - self.length / 2,
            self.width,
            self.length,
        )

    def _init_rigid_body(self) -> pymunk.Body:
        rigid_body = pymunk.Body()
        rigid_body.collision_type = CollisionType.LASER.value
        rigid_body.angle = self.angle + np.pi / 2
        rigid_body.velocity = [
            self.speed * np.cos(self.angle),
            self.speed * np.sin(self.angle),
        ]
        rigid_body.position = pymunk.Vec2d(self.x, self.y)
        return rigid_body

    def _init_collider(self) -> pymunk.Circle:
        col = pymunk.Segment(
            self.rigid_body,
            [0, -self.length / 2],
            [0, self.length / 2],
            self.width,
        )

        col.mass = 10000
        col.friction = 0.0
        col.damping = 0.0
        col.elasticity = 0

        return col

    def get_collider_world_bounds(self):
        p1 = self.rigid_body.local_to_world(self.collider.a)
        p2 = self.rigid_body.local_to_world(self.collider.b)
        return p1, p2

    def draw(self):
        p1, p2 = self.get_collider_world_bounds()
        pygame.draw.line(self.screen, self.color, p1, p2, self.width)

    def update(self):
        super().update()
        # If laser leaves the screen, delete it
        if self.distance_to_center > self.half_screen_diag:
            self.destroy()
