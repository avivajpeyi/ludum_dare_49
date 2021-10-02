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

    clock = pygame.time.Clock()

    physics_handler = GamePhysicsHandler(screen, FPS)
    planet = Planet(
        size=40,
        screen=screen,
        color=colors.YELLOW,
        physics_handler=physics_handler,
    )

    for i in range(30):
        Enemy(
            x=random.randint(0, WIDTH),
            y=random.randint(0, HEIGHT),
            size=10,
            screen=screen,
            physics_handler=physics_handler,
            color=colors.RED,
        )

    while True:
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
                or event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
            ):
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pygame.image.save(screen, "planet.png")

        # 'planet' in the center of screen
        screen.fill(pygame.Color("black"))
        planet.check_for_collision_with_enemy()
        for go in physics_handler.physics_game_objects:
            go.update()
        physics_handler.update()

        pygame.display.flip()
        clock.tick(FPS)

        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == "__main__":
    test_enemy()
