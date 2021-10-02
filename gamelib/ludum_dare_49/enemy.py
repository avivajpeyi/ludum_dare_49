import pygame


class Enemy(object):
    def __init__(self, x: int, y: int, size: int, screen, color=(0, 0, 255)):
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen
        self.color = color

    # Method to draw object
    def draw(self):
        pygame.draw.circle(
            self.screen, self.color, (self.x, self.y), self.size
        )

    # Method to move object (special input of speedx and speedy)
    def move(self, speedx, speedy):
        self.x += speedx
        self.y += speedy
