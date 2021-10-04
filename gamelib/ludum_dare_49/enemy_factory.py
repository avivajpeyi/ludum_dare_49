import numpy as np
import pygame

from . import constants as const
from .enemy import Enemy
from .physics import GamePhysicsHandler


class EnemyFactory(object):
    def __init__(self, screen_handler, physics_handler):
        self.screen_handler = screen_handler
        self.physics_handler = physics_handler
        self.num_enemies = 0
        self.start_time = pygame.time.get_ticks()
        self.wave_number = 1
        [
            self.create_new_enemy(const.COL_TYPE1) for _ in range(3)
        ]  # first wave

    def update(self):
        duration = pygame.time.get_ticks() - self.start_time
        wave_index = int(duration / 2500)

        # Only have waves show up on odd multiples of 10
        if (wave_index % 2 == 1) & (wave_index > self.wave_number):

            print(f"NUM CURRENT ENEMIES {Enemy.STATIC_NUM_ENEMIES}")
            # Start a new wave
            self.wave_number += 1
            print(
                f"New Wave # {self.wave_number}, ({pygame.time.get_ticks()})"
            )

            if duration < 15000:  # 15s
                num_new_enemies = 1
            elif duration < 30000:  # 15s
                num_new_enemies = 3
            else:
                num_new_enemies = 5
            [
                self.create_new_enemy(self.pick_color())
                for _ in range(num_new_enemies)
            ]

    def pick_color(self):
        duration = pygame.time.get_ticks() - self.start_time
        if duration < 8000:  # 8s
            return const.COL_TYPE1
        else:
            return [const.COL_TYPE1, const.COL_TYPE2][np.random.choice(2)]

    def create_new_enemy(self, color):
        if const.MAX_NUM_ENEMIES_IN_GAME > Enemy.STATIC_NUM_ENEMIES:
            screen_radius = self.screen_handler.diag / 2.0
            r_draw = np.random.uniform(
                0.8 * screen_radius, screen_radius
            )  # sample between r and 2r
            theta = 2 * np.pi * np.random.rand()

            (ctr_x, ctr_y) = self.screen_handler.center

            Enemy(
                x=r_draw * np.cos(theta) + ctr_x,
                y=r_draw * np.sin(theta) + ctr_y,
                size=const.ENEMY_SIZE,
                screen_handler=self.screen_handler,
                physics_handler=self.physics_handler,
                color=color,
            )
