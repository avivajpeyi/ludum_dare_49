import pygame
from test_helper import make_test_screen, should_i_quit

from ludum_dare_49.enemy import Enemy


def test_enemy(screen):
    enemy = Enemy(5, 5, 5, screen)

    enemy.draw()


if __name__ == "__main__":
    screen = make_test_screen("create_enemy")
    running = True
    while running:
        if should_i_quit():
            running = False
        test_enemy(screen)
        pygame.display.flip()
