import math
from typing import Optional 

import pygame
import pymunk

from .game_object import GameObject
from .physics import CollisionType, GamePhysicsHandler


class Laser(GameObject):
    def __init__(self,
        screen: pygame.Surface,
        size: int,
        color,
        x: float,
        y: float,
        physics_handler: Optional[GamePhysicsHandler] = None, # TODO: this isn't really optional
    ):
        """
        Initialize the laser based on the current position of the player
        """

        # TODO: take in only the position (later, of the player) and create a vector from the center
        self.screen = screen
        self.speed = 0.0000001
        self.body = pymunk.Body()
        self.shape = pymunk.Segment(self.body, [0, 0], [0, 50], 20)
        super().__init__(size=size, screen=screen, color=color, x=x, y=y, physics_handler=physics_handler)
        self.draw()
        #self.fire()

    #def get_shape(self):
    #    pymunk.Segment(self.body, 

    def _init_rigid_body(self) -> pymunk.Body:
        # TODO: clean this up
        rigid_body = self.body
        rigid_body.collision_type = CollisionType.LASER.value
        rigid_body.position = pymunk.Vec2d(self.x, self.y)
        print("laser pos: ", rigid_body.position)
        velocity_direction = (rigid_body.position - pymunk.Vec2d(*self.screen_center)).normalized()
        rigid_body.velocity = self.speed* velocity_direction
        print("laser vel: ", self.body.velocity)
        # align its initial angle with its position.
        # TODO: change to vector of difference from center of screen
        #rigid_body.angle = math.atan2(
        #    rigid_body.position.y, rigid_body.position.x
        #)
        rigid_body.angle = 0


        return rigid_body

    def _init_collider(self) -> pymunk.Circle:
        col = pymunk.Circle(self.rigid_body, self.radius)
        # TODO: Don't use a circle
        col.mass = 0
        col.friction = 0.9
        col.damping = 0.0
        col.elasticity = 0
        if self.physics_handler.DEBUG_MODE:
            col.color = pygame.Color("blue")  # colors the collider
        return col


    def draw(self):
        #print(self.body.velocity)
        #print(self.color)
        
        p1 = self.body.local_to_world(self.shape.a)
        p2 = self.body.local_to_world(self.shape.b)
        #TODO: This is the source of the problem!
        #p1 = self.shape.a
        #p2 = self.shape.b
        print("vel: ", self.body.velocity, " == pos: ", p1, p2)

        # Figure out what I can replace the 10 with here!
        pygame.draw.line(self.screen, self.color, p1, p2, 10)
        pygame.draw.line(self.screen, self.color, self.shape.a, self.shape.b, 10)
                

    #def update(self):



    # def __del__(self):

    #def get_position(self):
    #    r = self.radius
    #    theta = self.theta
    #    center = self.origin

    #    relative_offset = (radius * np.cos(theta), radius * np.sin(theta))
    #    return [sum(coords) for coords in zip(center, relative_offset)]

    # def fire(self):

