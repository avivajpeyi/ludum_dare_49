import random

import pygame

from ludum_dare_49 import colors
from ludum_dare_49.constants import FPS, HEIGHT, WIDTH
from ludum_dare_49.game import Game
from ludum_dare_49.physics import GamePhysicsHandler
from ludum_dare_49.planet import Planet
from ludum_dare_49.screen_handler import ScreenHandler


def test_game_scene():
    pygame.init()
    screen = ScreenHandler()
    game = Game(screen)
    game_is_running = True
    game.run_game()


if __name__ == "__main__":
    test_game_scene()
