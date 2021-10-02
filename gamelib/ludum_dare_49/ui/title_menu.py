from typing import Callable

from .base_menu import BaseMenu


class TitleMenu(BaseMenu):
    def __init__(self, screen, start_func: Callable):
        super(TitleMenu, self).__init__(screen)
        self.menu.add.button("Play", start_func)
