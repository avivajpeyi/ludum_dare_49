from typing import Tuple

import numpy as np
import pygame

from . import constants as const


class ScreenHandler:
    def __init__(self):
        self.screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))

    @property
    def screen_size(self) -> Tuple[float, float]:
        return self.screen.get_size()

    @property
    def screen_center(self) -> Tuple[float, float]:
        screen_size = self.screen_size
        return screen_size[0] / 2, screen_size[1] / 2

    @property
    def half_screen_diag(self) -> float:
        return np.sqrt(sum([x * x / 4 for x in self.screen_size]))

    @property
    def screen_diag(self) -> float:
        return np.sqrt(2) * self.screen_size[0]
