# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# Copying instructions from other screen
import pygame

display(HTML("<style>.container { width:100% !important; }</style>"))



pygame.init()

# +
# Wrap everything in a try except loop
try:

    ### Setup static objects

    # Set up draw window
    SCREEN_SIZE = 1000
    screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])

    ### Create the triangle character here
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            """
            Initialize the player, which is a rotating triangle.
            Set the initial color, shape, and orientation.
            """
            super(Player, self).__init__()
            self.color = (255, 0, 0)
            self.theta = 0
            self.rotation_speed = 0.1
            self.center = (SCREEN_SIZE/2.0, SCREEN_SIZE/2.0)
            self.aspect_ratio = 3  # height / width of isosceles triangle
            self.scale = SCREEN_SIZE/20.0  # how big to make it
            self.relative_corners = self.get_relative_corners()

        def get_relative_corners(self):
            """
            Calculate the initial corner coordinates from the aspect ratio and scale
            """
            aspect_ratio = self.aspect_ratio
            scale = self.scale
            unscaled_coords = [(-1, 0), (1, 0), (0, aspect_ratio)]
            relative_corners = [
                [scale * coord[0], scale * coord[1]]
                for coord in unscaled_coords
            ]
            return relative_corners

        def draw(self):
            """
            Function to draw (or redraw) the triangle
            """
            coordinates = [
                [sum(coords) for coords in zip(self.center, corner)]
                for corner in self.relative_corners
            ]
            pygame.draw.polygon(screen, self.color, coordinates, 0)

        def rotate(self, pressed_keys):
            """
            Rotate the triangle a fixed amount if the relevant keys are held down
            """
            if pressed_keys[pygame.K_LEFT]:
                self.theta -= self.rotation_speed
            if pressed_keys[pygame.K_RIGHT]:
                self.theta += self.rotation_speed

        def update(self, pressed_keys):
            """
            Update the direction of the triangle in response to rotation
            """
            self.rotate(pressed_keys)
            self.relative_corners = [
                pygame.math.Vector2(p).rotate(self.theta)
                for p in self.relative_corners
            ]
            # reset theta to 0
            self.theta = 0
            self.draw()
            
    class Laser(pygame.sprite.Sprite):
        def __init__(self):
            self.color = (255, 255, 0)
            self.theta = 0
            

    # Create player Fred and place on screen
    fred = Player()
    fred.draw()

    # Render the entire screen
    pygame.display.flip()

    # Continue until user quits
    running = True
    while running:

        # Check if window should be closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    running = False

        # Make it white
        screen.fill((255, 255, 255))

        # Check for pressed keys and update player position
        pressed_keys = pygame.key.get_pressed()
        fred.update(pressed_keys)

        pygame.draw.circle(screen, (0, 0, 0), \
                           (SCREEN_SIZE/2.0, SCREEN_SIZE/2.0), SCREEN_SIZE/10.0)
        pygame.display.flip()
        
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    print(e)
    
    
pygame.quit()
# -









