import numpy as np

import pygame
import pymunk

from ludum_dare_49 import colors
from .game_object import GameObject

### Setup static objects

# Set up draw window

### Create the triangle character here
class Player(GameObject):
    def __init__(self):
        """
        Initialize the player, which is a rotating triangle.
        Set the initial color, shape, and orientation.
        """
        super(Player, self).__init__()
        self.color = colors.RED
        self.theta = 0
        self.rotation_speed = 0.1
        self.center = (SCREEN_SIZE / 2.0, SCREEN_SIZE / 2.0)
        self.aspect_ratio = 3  # height / width of isosceles triangle
        self.scale = SCREEN_SIZE / 10.0  # how big to make it
        self.relative_corners = self.get_relative_corners()

    def _init_rigid_body(self)
        rigid_body = pymunk.Body(body_type=pymunk.Body.STATIC)

    def get_relative_corners(self):
        """
        Calculate the initial corner coordinates from the aspect ratio and scale
        """
        aspect_ratio = self.aspect_ratio
        scale = self.scale
        unscaled_coords = [(-1, 0), (1, 0), (0, aspect_ratio)]
        relative_corners = [
            [scale * coord[0], scale * coord[1]]
            for coord in unscaled_coords
        ]
        return relative_corners

    def draw(self):
        """
        Function to draw (or redraw) the triangle
        """
        coordinates = [
            [sum(coords) for coords in zip(self.center, corner)]
            for corner in self.relative_corners
        ]
        pygame.draw.polygon(screen, self.color, coordinates, 0)
        print(self.color)
        print(coordinates)

    def update(self, pressed_keys):
        """
        Update the player state depending on which keys are pressed
        """

        # If left or right arrow pressed, apply rotation
        if pressed_keys[pygame.K_LEFT] | pressed_keys[pygame.K_RIGHT]:
            self.rotate(pressed_keys)

        # If spacebar pressed, fire laser
        if pressed_keys[pygame.K_SPACE]:
            self.fire_laser()

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
        self.relative_corners = [
            pygame.math.Vector2(p).rotate(dtheta)
            for p in self.relative_corners
        ]

    def fire_laser(self):
        radius = self.aspect_ratio * self.scale
        laser = Laser(self.center, radius, self.theta)



