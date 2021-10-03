from ludum_dare_49.game import Game
import random

import pygame

from ludum_dare_49 import colors
from ludum_dare_49.constants import FPS, HEIGHT, WIDTH
from ludum_dare_49.enemy import Enemy
from ludum_dare_49.physics import GamePhysicsHandler
from ludum_dare_49.planet import Planet


def test_enemy():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)
    game_is_running = True
    game.update()

if __name__ == '__main__':
    test_enemy()