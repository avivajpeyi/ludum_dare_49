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
    planet = Planet(radius=20, screen=screen, color=colors.YELLOW)
    enemy = Enemy(
        x=5,
        y=5,
        size=5,
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
        planet.draw()
        enemy.draw()
        physics_handler.update()
        pygame.display.flip()
        clock.tick(FPS)

        print(enemy.rigid_body.position)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == "__main__":
    test_enemy()
