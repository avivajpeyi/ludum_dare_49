from abc import abstractmethod

import pygame_menu

from .. import __NAME__  # game name
from ..constants import HEIGHT, WIDTH


class BaseMenu:
    def __init__(self, screen, name=__NAME__):
        self.screen = screen
        self.menu = pygame_menu.Menu(
            name,
            WIDTH * 0.5,
            HEIGHT * 0.4,
            theme=pygame_menu.themes.THEME_DARK,
        )
        self.menu.add.button("Quit", pygame_menu.events.EXIT)

    @abstractmethod
    def add_buttons_to_menu(self, *args):
        pass

    def update(self):
        self.menu.mainloop(self.screen)
