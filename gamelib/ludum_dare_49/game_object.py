import math
import numpy as np
from abc import ABC
from typing import Optional, Tuple

import pygame

from .colors import WHITE
from .physics import GamePhysicsHandler


class GameObject(ABC):
    def __init__(
        self,
        size: int,
        screen: pygame.Surface,
        color=WHITE,
        # If x y init pos not provided, then we set to screen center
        x: Optional[int] = None,
        y: Optional[int] = None,
        physics_handler: Optional[GamePhysicsHandler] = None,
    ):
        self.size = size
        self.screen = screen
        self.color = color

        if x is None:
            self.x, self.y = self.screen_center
        else:
            self.x, self.y = x, y

        # PHYSICS
        self.physics_handler = physics_handler
        self.rigid_body = self._init_rigid_body()
        self.collider = self._init_collider()

        self.rect = pygame.Rect(
            self.x - size / 2, self.y - size / 2, size * 2, size * 2
        )
        if self.is_physics_object:
            physics_handler.track_object(self)

    @property
    def radius(self) -> float:
        return self.size / 2.0

    @property
    def is_physics_object(self) -> bool:
        is_obj = (
            self.rigid_body is not None
            and self.physics_handler is not None
            and self.collider is not None
        )
        return is_obj

    @property
    def screen_size(self) -> Tuple[float, float]:
        return self.screen.get_size()

    @property
    def screen_center(self) -> Tuple[float, float]:
        screen_size = self.screen_size
        return screen_size[0] / 2, screen_size[1] / 2

    @property
    def half_screen_diag(self) -> float:
        return np.sqrt(sum([x*x/4 for x in self.screen_size]))

    @property
    def distance_to_center(self):
        if self.is_physics_object:
            return self.rigid_body.position.get_distance(self.screen_center)
        else:
            ctr_x, ctr_y = self.screen_center
            x = ctr_x - self.x
            y = ctr_y - self.y
            return math.sqrt(x ** 2 + y ** 2)

    def draw(self) -> None:
        """Draws sprite in pygame window"""
        if self.is_physics_object:
            x, y = self.rigid_body.position
        else:
            x, y = self.x, self.y

        pygame.draw.circle(
            self.screen, self.color, (int(x), int(y)), self.size
        )

        if self.physics_handler.DEBUG_MODE:
            pygame.draw.rect(self.screen, pygame.Color("green"), self.rect)

    #def is_within_screen_bounds(self, buff=1):
    #    """
    #    Returns a boolean for whether the object is contained within the screen bounds.
    #    buff is an optional scaling buffer for how far outside the screen bounds the object can be
    #    """
    #    slf_x, slf_y = self.x, self.y
    #    ctr_x, ctr_y = self.screen_center
    #    scr_x, scr_y = self.screen_size
    #    half_width = scr_x/2
    #    half_height= scr_y/2

    #    # If the abs separation between the coordinate and center (in either direction) is greater than
    #    # than half the screen size in that direction (times the buffer), then return False

    #    print("is within bounds called")
    #    print("dist_x: ", abs(slf_x - ctr_x)) 
    #    print("dist_y: ", abs(slf_y - ctr_y)) 
    #    if (abs(slf_x - ctr_x) > buff*half_width) | (abs(slf_y - ctr_y) > buff*half_height):
    #        print("false")
    #        return False
    #    print('true')
    #    return True


    def update(self) -> None:
        self.draw()
        if self.is_physics_object:
            self.rect.center = self.rigid_body.position

    def destroy(self) -> None:
        """Remove from physics handler"""
        print(f"Destroy {self}")
        if self.is_physics_object:
            self.physics_handler.remove_object(self)
        del self

    def _init_rigid_body(self) -> None:
        """create a pymunk rigid body and return it"""
        return None

    def _init_collider(self) -> None:
        """create a pymunk collider and return it"""
        return None
