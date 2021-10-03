from ludum_dare_49 import colors

from . import asset_loader

FPS = 50
SCALE = 2
REAL_WIDTH = 360
REAL_HEIGHT = 360
WIDTH = REAL_WIDTH * SCALE
HEIGHT = REAL_HEIGHT * SCALE

FONT_MAIN = asset_loader.filepath("fonts/font.ttf")
SOUND_VOLUME = 0.4

# Constants for objects
ROTATION_SPEED = 0.1
COL_TYPE1 = colors.RED
COL_TYPE2 = colors.BLUE
REFIRE_DELAY = 500  # ms
LASER_SPEED = 300
LASER_LENGTH = 50
LASER_WIDTH = 1
