import math
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
        physics_handler: GamePhysicsHandler,
        color=WHITE,
        # If x y init pos not provided, then we set to screen center
        x: Optional[int] = None,
        y: Optional[int] = None,
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

        if self.is_physics_object:
            physics_handler.space.add(self.rigid_body, self.collider)

    @property
    def radius(self) -> float:
        return self.size / 2.0

    @property
    def is_physics_object(self) -> bool:
        is_obj = self.rigid_body is not None
        return is_obj

    @property
    def screen_size(self) -> Tuple[float, float]:
        return self.screen.get_size()

    @property
    def screen_center(self) -> Tuple[float, float]:
        screen_size = self.screen_size
        return screen_size[0] / 2, screen_size[1] / 2

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

    def destroy(self) -> None:
        """Remove from physics handler"""
        raise NotImplementedError

    def _init_rigid_body(self) -> None:
        """create a pymunk rigid body and return it"""
        return None

    def _init_collider(self) -> None:
        """create a pymunk collider and return it"""
        return None
