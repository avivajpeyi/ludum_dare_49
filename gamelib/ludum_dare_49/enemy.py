import math

import pygame
import pymunk

from .physics import G, GamePhysicsHandler, planet_gravity


class Enemy(object):
    def __init__(
        self,
        x: int,
        y: int,
        size: int,
        screen,
        physics_handler: GamePhysicsHandler,
        color=(0, 0, 255),
    ):
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen
        screen_size = screen.get_size()
        self.central_point = (screen_size[0] / 2, screen_size[1] / 2)
        self.color = color
        self.rigid_body = self._init_rigid_body()
        self.box_collider = self._init_render()
        self.physics_handler = physics_handler
        self.rect = pygame.Rect(x - size / 2, y - size / 2, size, size)
        physics_handler.space.add(self.rigid_body, self.box_collider)

    def _init_rigid_body(self):
        rigid_body = pymunk.Body()
        rigid_body.position = pymunk.Vec2d(self.x, self.y)
        rigid_body.velocity_func = planet_gravity

        # Set the enemy's velocity to put it into a circular orbit from its
        # starting position. (dampening prevents circular orbit)
        r = rigid_body.position.get_distance(self.central_point)
        v = math.sqrt(G / r) / r
        v = v * 0.6
        vec_to_center = rigid_body.position - pymunk.Vec2d(*self.central_point)
        rigid_body.velocity = vec_to_center.perpendicular() * v

        # Set the box's angular velocity to match its orbital period and
        # align its initial angle with its position.
        rigid_body.angular_velocity = v
        rigid_body.angle = math.atan2(
            rigid_body.position.y, rigid_body.position.x
        )
        return rigid_body

    def _init_render(self):
        r = pymunk.Poly.create_box(
            self.rigid_body, size=(self.size, self.size)
        )
        r.mass = 10
        r.friction = 0.7
        r.damping = 0.9
        r.elasticity = 0
        r.color = pygame.Color("pink")
        return r

    @property
    def distance_to_center(self):
        return self.rigid_body.position.get_distance(self.central_point)

    def destroy(self):
        """Function to kill this enemy"""

    def draw(self):
        x, y = self.rigid_body.position
        pygame.draw.circle(
            self.screen, self.color, (int(x), int(y)), self.size
        )
