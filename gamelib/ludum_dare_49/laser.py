from typing import Optional

import numpy as np
import pygame
import pymunk
from ludum_dare_49 import colors

from .game_object import GameObject
from .physics import (
    CollisionType, GamePhysicsHandler
)


class Laser(GameObject):
    def __init__(
            self,
            screen: pygame.Surface,
            size: int,
            angle: float,
            color=colors.YELLOW,
            physics_handler: Optional[
                GamePhysicsHandler
            ] = None,
    ):
        """
        Initialize the laser based on the current position of the player
        """

        # TODO: take in only the position (later, of the player)
        #  and create a vector from the center
        self.screen = screen
        self.angle = angle
        self.speed = 300
        self.r = 50  # separation from center of the sceen
        self.dir_vector = self.get_direction_vector()
        self.x = self.r * self.dir_vector[0] + self.screen_center[0]
        self.y = self.r * self.dir_vector[1] + self.screen_center[1]
        self.length = 50
        self.width = 1

        super().__init__(
            size=size,
            screen=screen,
            color=color,
            x=self.x,
            y=self.y,
            physics_handler=physics_handler,
        )

    def get_direction_vector(self):
        return (np.cos(self.angle), np.sin(self.angle))

    def _init_rect(self) -> pygame.Rect:
        rect = pygame.Rect(
            self.x - self.width / 2, self.y - self.length / 2, self.width, self.length
        )
        return rect

    # TODO: Add in a destroyer if the object leaves the game screen

    # TODO: fix the laser to be rectangular not quadrilateral on rotation

    def _init_rigid_body(self) -> pymunk.Body:
        # TODO: clean this up
        rigid_body = pymunk.Body(pymunk.Body.KINEMATIC)
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

        col.mass = 1
        col.friction = 0.0
        col.damping = 0.0
        col.elasticity = 0
        col.filter = pymunk.ShapeFilter(categories= CollisionType.LASER.value)
        return col

    def get_collider_world_bounds(self):
        p1 = self.rigid_body.local_to_world((0, self.length/2))
        p2 = self.rigid_body.local_to_world((0, -self.length/2))
        return p1, p2

    def draw(self):
        p1, p2 = self.get_collider_world_bounds()
        self.rect = pygame.draw.line(self.screen, self.color, p1,p2, self.width)

    def update(self) -> None:
        self.draw()
        if self.is_physics_object:
            (x, y) = self.rigid_body.position
            self.rect.center = x, y
            self.rect.midtop = (x + self.dir_vector[0] * self.length / 2, y + self.dir_vector[1] * self.length / 2)
            self.handle_collision_with_enemy()

        super().update()
        # If laser leaves the screen, delete it
        if self.distance_to_center > self.half_screen_diag:
            self.destroy()
