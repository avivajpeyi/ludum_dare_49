from ludum_dare_49 import colors

from . import asset_loader

FPS = 50
SCALE = 1
REAL_WIDTH = 360
REAL_HEIGHT = 360
WIDTH = REAL_WIDTH * SCALE
HEIGHT = REAL_HEIGHT * SCALE

FONT_MAIN = asset_loader.filepath("fonts/font.ttf")
SOUND_VOLUME = 0.4

# Constants for objects
ROTATION_SPEED = 0.2
COL_TYPE1 = colors.RED
COL_TYPE2 = colors.BLUE
REFIRE_DELAY = 300  # ms
LASER_SPEED = 1000
LASER_LENGTH = 30
LASER_WIDTH = 1
ENEMY_SIZE = 10
