import pygame

from ludum_dare_49 import colors
from ludum_dare_49.constants import FPS, HEIGHT, WIDTH
from ludum_dare_49.physics import GamePhysicsHandler
from ludum_dare_49.planet import Planet
from ludum_dare_49.laser import Laser


def test_laser():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    print(WIDTH, HEIGHT)

    clock = pygame.time.Clock()

    physics_handler = GamePhysicsHandler(screen, FPS)
    planet = Planet(
        size=40,
        screen=screen,
        color=colors.YELLOW,
        physics_handler=physics_handler,
    )
    laser = Laser(
        screen=screen,
        size=200,
        color=colors.YELLOW,
        x=540,
        y=540,
        physics_handler=physics_handler,
    )
    laser.draw()

    """ Many new lasers """
    #laser2 = Laser( screen=screen, size=200, color=colors.YELLOW, x=500, y=540, physics_handler=physics_handler)
    #laser2.draw()
    #laser3 = Laser( screen=screen, size=200, color=colors.YELLOW, x=540, y=600, physics_handler=physics_handler)
    #laser3.draw()
    #laser4 = Laser( screen=screen, size=200, color=colors.YELLOW, x=500, y=600, physics_handler=physics_handler)
    #laser4.draw()
    #laser5 = Laser( screen=screen, size=200, color=colors.YELLOW, x=400, y=400, physics_handler=physics_handler)
    #laser5.draw()
    #laser6 = Laser( screen=screen, size=200, color=colors.YELLOW, x=300, y=300, physics_handler=physics_handler)
    #laser6.draw()


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
        laser.draw()
        #laser2.draw()
        #laser3.draw()
        #laser4.draw()
        #laser5.draw()
        #laser6.draw()
        #player.update(pressed_keys)
        pygame.draw.circle( screen, colors.WHITE, (540, 540), 10) # just to have a thing
        physics_handler.update()
        #planet.draw()
        pygame.display.flip()
        clock.tick(FPS)


        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == "__main__":
    test_laser()
