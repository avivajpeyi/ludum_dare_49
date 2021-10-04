import pygame

from ludum_dare_49.score_manager import ScoreManager
from ludum_dare_49.screen_handler import ScreenHandler
from ludum_dare_49.ui.game_over_screen import GameOverScreen

from ludum_dare_49 import constants as const


def test_2():
    pygame.init()
    screen_mgr = ScreenHandler()
    score = ScoreManager()
    go = GameOverScreen(screen_mgr, score)
    while True:
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
                or event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
            ):
                exit()
        screen_mgr.screen.fill(pygame.Color("purple"))
        go.draw()
        pygame.display.flip()


if __name__ == "__main__":
    test_2()
