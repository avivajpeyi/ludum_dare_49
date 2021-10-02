from typing import Optional

import numpy as np
import pygame
import pymunk

from ludum_dare_49 import colors

from .game_object import GameObject
from .physics import GamePhysicsHandler


### Create the triangle character here
class Player(GameObject):
    def __init__(
        self,
        size: int,
        screen: pygame.Surface,
        physics_handler: GamePhysicsHandler,
        color,
        x: Optional[int] = None,
        y: Optional[int] = None,
    ):
        # TODO: get syntax for super inits
        """
        Initialize the player, which is a rotating triangle.
        Set the initial color, shape, and orientation.
        """
        super().__init__(size, screen, physics_handler, color, x, y)
        self.theta = 0
        self.rotation_speed = 1
        self.aspect_ratio = 3  # height / width of isosceles triangle
        self.relative_vertices = self.get_relative_vertices()

    # def _init_rigid_body(self) -> pymunk.Body:
    #    rigid_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    #    #rigid_body.collision_type = CollisionType.PLANET.value
    #    rigid_body.position = pymunk.Vec2d(self.x, self.y)

    # def _init_collider(self):
    #    col = pymunk.

    def get_relative_vertices(self):
        """
        Calculate the initial vertex coordinates from the aspect ratio and size
        """
        unscaled_coords = [(-1, 0), (1, 0), (0, self.aspect_ratio)]
        relative_vertices = [
            [self.size * coord[0], self.size * coord[1]]
            for coord in unscaled_coords
        ]
        return relative_vertices

    def draw(self):
        """
        Function to draw (or redraw) the triangle
        """
        coordinates = [
            [sum(coords) for coords in zip((self.x, self.y), vertex)]
            for vertex in self.relative_vertices
        ]
        pygame.draw.polygon(self.screen, self.color, coordinates, 0)

    def update(self, pressed_keys):
        """
        Update the player state depending on which keys are pressed
        """

        # If left or right arrow pressed, apply rotation
        if pressed_keys[pygame.K_LEFT] | pressed_keys[pygame.K_RIGHT]:
            self.rotate(pressed_keys)

        # If spacebar pressed, fire laser
        # if pressed_keys[pygame.K_SPACE]:
        # self.fire_laser()

        self.draw()

    def rotate(self, pressed_keys):
        """
        Rotate the triangle a fixed amount
        """
        # Calculate change in theta
        if pressed_keys[pygame.K_RIGHT]:
            dtheta = self.rotation_speed
        if pressed_keys[pygame.K_LEFT]:
            dtheta = -self.rotation_speed

        # Update current angle
        self.theta += dtheta
        self.relative_vertices = [
            pygame.math.Vector2(p).rotate(dtheta)
            for p in self.relative_vertices
        ]

    # def fire_laser(self):
    #    radius = self.aspect_ratio * self.size
    #    laser = Laser(self.center, radius, self.theta)
