from typing import Callable

from .base_menu import BaseMenu


class PauseMenu(BaseMenu):
    def __init__(self, screen, restart_func: Callable):
        super(PauseMenu, self).__init__(screen, "Pause")
        self.menu.add.button("Restart", restart_func)
