import math

import pygame
import pymunk

from .game_object import GameObject
from .physics import CollisionType, G, planet_gravity


class Enemy(GameObject):
    def _init_rigid_body(self) -> pymunk.Body:
        rigid_body = pymunk.Body()
        rigid_body.collision_type = CollisionType.ENEMY.value
        rigid_body.position = pymunk.Vec2d(self.x, self.y)
        rigid_body.velocity_func = planet_gravity

        # Set the enemy's velocity to put it into a circular orbit from its
        # starting position. (dampening prevents circular orbit)
        r = rigid_body.position.get_distance(self.screen_center)
        v = math.sqrt(G / r) / r
        v = v * 0.6
        vec_to_center = rigid_body.position - pymunk.Vec2d(*self.screen_center)
        rigid_body.velocity = vec_to_center.perpendicular() * v

        # Set the box's angular velocity to match its orbital period and
        # align its initial angle with its position.
        rigid_body.angular_velocity = v
        rigid_body.angle = math.atan2(
            rigid_body.position.y, rigid_body.position.x
        )

        return rigid_body

    def _init_collider(self) -> pymunk.Circle:
        col = pymunk.Circle(self.rigid_body, self.radius)
        col.mass = 10
        col.friction = 0.7
        col.damping = 0.9
        col.elasticity = 0
        if self.physics_handler.DEBUG_MODE:
            col.color = pygame.Color("red")  # colors the collider
        return col
