from typing import Callable

import pygame_menu

from .. import __NAME__
from ..constants import HEIGHT, WIDTH


class TitleMenu:
    def __init__(self, screen, start_game_function: Callable):
        self.screen = screen
        self.menu = self._init_menu(start_game_function)

    def _init_menu(self, start_game_function):
        menu = pygame_menu.Menu(
            __NAME__,  # game name
            WIDTH * 0.8,
            HEIGHT * 0.8,
            theme=pygame_menu.themes.THEME_DARK,
        )

        menu.add.button("Play", start_game_function)
        menu.add.button("Quit", pygame_menu.events.EXIT)
        return menu

    def update(self):
        self.menu.mainloop(self.screen)
