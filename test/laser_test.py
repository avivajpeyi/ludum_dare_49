import numpy as np
import pygame

from ludum_dare_49 import colors
from ludum_dare_49.constants import FPS, HEIGHT, WIDTH
from ludum_dare_49.laser import Laser
from ludum_dare_49.physics import GamePhysicsHandler
from ludum_dare_49.planet import Planet


def test_laser():
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
    for ang in range(8):
        laser = Laser(
            screen=screen,
            size=66,
            color=colors.YELLOW,
            angle=ang * np.pi / 4,
            physics_handler=physics_handler,
        )
        laser.draw()

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
        pressed_keys = pygame.key.get_pressed()
        for go in physics_handler.physics_game_objects:
            go.update()
        physics_handler.update()
        planet.draw()
        pygame.display.flip()
        clock.tick(FPS)

        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == "__main__":
    test_laser()
