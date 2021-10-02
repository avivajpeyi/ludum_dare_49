class Laser(pygame.sprite.Sprite):
    def __init__(self, origin, radius, theta):
        """
        Initialize the laser based on the current position of the player
        """
        self.color = (255, 255, 0)
        self.length = 10
        self.width = 2
        self.velocity = 1.0
        self.origin = origin
        self.radius = radius
        self.theta = theta
        self.position = self.get_position()
        self.fire()

    # def __del__(self):

    def get_position(self):
        r = self.radius
        theta = self.theta
        center = self.origin

        relative_offset = (radius * np.cos(theta), radius * np.sin(theta))
        return [sum(coords) for coords in zip(center, relative_offset)]

    # def fire(self):

    # def draw(self):
