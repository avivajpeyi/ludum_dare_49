import pygame

from ludum_dare_49 import colors
from ludum_dare_49.constants import FPS, HEIGHT, WIDTH
from ludum_dare_49.physics import GamePhysicsHandler
from ludum_dare_49.planet import Planet
from ludum_dare_49.player import Player


def test_player():
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
    player = Player(
        size=WIDTH / 40.0,
        screen=screen,
        physics_handler=physics_handler,
    )
    player.draw()

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
        player.run_game(pressed_keys)
        for go in physics_handler.physics_game_objects:
            go.run_game()
        physics_handler.run_game()
        planet.draw()
        pygame.display.flip()
        clock.tick(FPS)

        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == "__main__":
    test_player()
