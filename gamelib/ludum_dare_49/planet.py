import pygame
import pymunk

from . import colors


class Planet(object):
    def __init__(
        self, radius: int, screen: pygame.Surface, color=colors.BLACK
    ):
        screen_size = screen.get_size()
        self.x = screen_size[0] / 2
        self.y = screen_size[1] / 2
        self.radius = radius
        self.body = pymunk.Body()
        self.screen = screen
        self.color = color
        self.rect = pygame.Rect(
            self.x - radius, self.y - radius, radius * 2, radius * 2
        )

    def draw(self):
        """draw planet"""
        pygame.draw.circle(
            self.screen, self.color, self.rect.center, self.radius
        )

    def check_for_collision(self):
        """
        TODO https://stackoverflow.com/questions/65912032/pygame-how-do-i-check-if-there-is-collision-with-any-rect-in-an-array
        """
        raise NotImplementedError
