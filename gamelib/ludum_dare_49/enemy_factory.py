import numpy as np
import pygame

from . import constants as const
from .enemy import Enemy
from .physics import GamePhysicsHandler


class EnemyFactory(object):
    def __init__(self, screen_handler, physics_handler):
        # TODO
        # get information about n enemies and time
        self.screen_handler = screen_handler
        self.physics_handler = physics_handler
        self.start_time = pygame.time.get_ticks()
        self.wave_number = 1
        [
            self.create_new_enemy(const.COL_TYPE1) for _ in range(10)
        ]  # first wave

    def update(self):
        duration = pygame.time.get_ticks() - self.start_time
        wave_index = int(duration / 5000)

        # Only have waves show up on odd multiples of 10
        if (wave_index % 2 == 1) & (wave_index > self.wave_number):

            # Start a new wave
            self.wave_number += 1
            print("New Wave #", self.wave_number)

            num_new_enemies = self.wave_number * 5
            [
                self.create_new_enemy(self.pick_color())
                for _ in range(num_new_enemies)
            ]  # first wave

    def pick_color(self):
        duration = pygame.time.get_ticks() - self.start_time
        if duration < 15000:  # 15s
            return const.COL_TYPE1
        else:
            return [const.COL_TYPE1, const.COL_TYPE2][np.random.choice(2)]

    def create_new_enemy(self, color):
        Enemy(
            # TODO: instantiate off screen
            x=np.random.randint(0, const.WIDTH),
            y=np.random.randint(0, const.HEIGHT),
            size=const.ENEMY_SIZE,
            screen_handler=self.screen_handler,
            physics_handler=self.physics_handler,
            color=color,
        )
