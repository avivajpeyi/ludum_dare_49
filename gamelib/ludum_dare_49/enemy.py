import math

import pygame
import pymunk

from .game_object import GameObject
from .physics import CollisionType, G, planet_gravity
from ludum_dare_49.constants import COL_TYPE1


class Enemy(GameObject):
    def _init_rigid_body(self) -> pymunk.Body:
        rigid_body = pymunk.Body(pymunk.Body.KINEMATIC)

        rigid_body.collision_type = CollisionType.ENEMY.value
        rigid_body.position = pymunk.Vec2d(self.x, self.y)
        rigid_body.velocity_func = planet_gravity

        # Set the enemy's velocity to put it into a circular orbit from its
        # starting position. (dampening prevents circular orbit)
        r = rigid_body.position.get_distance(self.screen_center)
        v = math.sqrt(G / r) / r
        # v = v * 0.6
        # Reverse direction for enemies with COLOR1
        if self.color == COL_TYPE1:
            v *= -1 
        vec_to_center = rigid_body.position - pymunk.Vec2d(*self.screen_center)
        # Aim the enemy randomly between the circular orbit and directed at the player
        rigid_body.velocity = pygame.math.Vector2(
                                    v* vec_to_center.perpendicular()
                              ).rotate_rad(2*np.pi*np.random.rand())

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
        col.elasticity = 1
        col.filter = pymunk.ShapeFilter(categories=CollisionType.ENEMY.value)
        if self.physics_handler.DEBUG_MODE:
            col.color = pygame.Color("white")  # colors the collider
        return col

    def update(self):
        super().update()
        # If enemy leaves (twice the distance to) the screen, delete it
        if self.screen.distance_to_center > 2 * self.screen.half_screen_diag:
            self.destroy()
