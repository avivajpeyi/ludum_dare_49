import math
from abc import ABC
from typing import Optional, Tuple

import pygame

from .colors import WHITE
from .physics import GamePhysicsHandler, CollisionType




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
        self.type = 0

        if x is None:
            self.x, self.y = self.screen_center
        else:
            self.x, self.y = x, y

        # PHYSICS
        self.physics_handler = physics_handler
        self.rigid_body = self._init_rigid_body()
        self.collider = self._init_collider()
        self.rect = self._init_rect()

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

    def update(self) -> None:
        self.draw()
        if self.is_physics_object:
            self.rect.center = self.rigid_body.position
            self.handle_collision_with_enemy()

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

    def _init_rect(self) -> pygame.Rect:
        return pygame.Rect(
            self.x - self.size / 2, self.y - self.size / 2,
            self.size * 2, self.size * 2
        )

    def handle_collision_with_enemy(self):
        if self.rigid_body.collision_type == CollisionType.ENEMY.value:
            return  # ignore enemy on enemy collisions

        collided_with_enemy = False
        collided_enemy = None

        for game_object in self.physics_handler.physics_game_objects:
            if game_object.rigid_body.collision_type == CollisionType.ENEMY.value:
                if self.rect.colliderect(game_object.rect):
                    collided_with_enemy = True
                    collided_enemy = game_object

        if collided_with_enemy:
            if self.rigid_body.collision_type == CollisionType.LASER.value:
                if self.type == collided_enemy.type:
                    print("Score +1")
                    collided_enemy.destroy()


            if self.rigid_body.collision_type == CollisionType.PLANET.value:
                # if i am planet
                print("GAME OVER, BITCH")
                collided_enemy.destroy()
                # self.destroy()
