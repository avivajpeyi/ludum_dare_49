import math
import numpy as np
from typing import Optional 

import pygame
import pymunk

from .game_object import GameObject
from .physics import CollisionType, GamePhysicsHandler
from ludum_dare_49 import colors


class Laser(GameObject):
    def __init__(self,
        screen: pygame.Surface,
        size: int,
        angle: float,
        color=colors.YELLOW,
        physics_handler: Optional[GamePhysicsHandler] = None, # TODO: this isn't really optional
    ):
        """
        Initialize the laser based on the current position of the player
        """

        # TODO: take in only the position (later, of the player) and create a vector from the center
        self.screen = screen
        self.angle = angle
        self.speed = 30
        self.r = 50 # separation from center
        self.x = self.r*np.cos(self.angle) + self.screen_center[0]
        self.y = self.r*np.sin(self.angle) + self.screen_center[1]
        self.length = 50
        self.width = 1
        #self.body = pymunk.Body()
        #self.shape = pymunk.Segment(self.body, [0, 0], [0, 50], 20)
        print(physics_handler)
        super().__init__(size=size, screen=screen, color=color, x=self.x, y=self.y, physics_handler=physics_handler)
        #self.draw()
        #self.fire()

    # TODO: Add in a destroyer if the object leaves the game screen

    # TODO: fix the laser to be rectangular not quadrilateral on rotation

    def _init_rigid_body(self) -> pymunk.Body:
        # TODO: clean this up
        rigid_body = pymunk.Body()
        rigid_body.collision_type = CollisionType.LASER.value
        rigid_body.position = pymunk.Vec2d(self.x, self.y)
        print("laser pos: ", rigid_body.position)
        velocity_direction = (rigid_body.position - pymunk.Vec2d(*self.screen_center)).normalized()
        rigid_body.velocity = self.speed* velocity_direction
        
        rigid_body.angle = math.atan2( velocity_direction[0], -velocity_direction[1])
        #rigid_body.angle = 0
        #velocity_direction = pymunk.Vec2d([0, 0], [100, 100]).normalized() # fixed vel
        #rigid_body.velocity = 50, 50
        #print("laser vel: ", rigid_body.velocity)
        # align its initial angle with its position.
        # done: change to vector of difference from center of screen

        return rigid_body

    def _init_collider(self) -> pymunk.Circle:
        col = pymunk.Segment(self.rigid_body, [0, -self.length/2], [0, self.length/2], self.width)
        #[self.length*np.cos(self.rigid_body.angle),
        #self.length*np.sin(self.rigid_body.angle)]
        col.mass = 1
        col.friction = 0.0
        col.damping = 0.0
        col.elasticity = 0
        if self.physics_handler.DEBUG_MODE:
            col.color = pygame.Color("blue")  # colors the collider
        #self.shape = pymunk.Segment(self.body, [0, 0], [0, 50], 20)
        #col = pymunk.Segk(self.rigid_body, self.radius)
        # done: Don't use a circle

        return col


    def draw(self):
        #print(self.body.velocity)
        #print(self.color)
        
        #print(dir(self.rigid_body))
        #print(dir(self.collider))
        #print(self.rigid_body.local_to_world())
        #print(self.rigid_body.position)
        #print(self.rigid_body.center_of_gravity)
        #print(self.rigid_body.local_to_world())

        #print(self.collider._shape[0])
        #p1, p2 = self.collider._shape
        p1 = self.rigid_body.local_to_world(self.collider.a)
        p2 = self.rigid_body.local_to_world(self.collider.b)
        #TODO: This is the source of the problem!
        #p1 = self.collider.a
        #p2 = self.collider.b
        #p1 = self.rigid_body.position
        #p2 = [p1[0], p1[1]+self.length]

        print("vel: ", self.rigid_body.velocity, " == pos: ", p1, p2)

        # Figure out what I can replace the 10 with here!
        pygame.draw.line(self.screen, self.color, p1, p2, self.width)
        #pygame.draw.line(self.screen, self.color, self.shape.a, self.shape.b, 10)
                
