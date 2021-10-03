import pygame

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

ROTATION_SPEED = 0.2
REFIRE_DELAY = 100  # ms
LASER_SPEED = 1000
LASER_LENGTH = 30
LASER_WIDTH = 2
ENEMY_SIZE = 10

# COLORS
COL_TYPE1 = colors.MAXIMUM_YELLOW_RED
COL_TYPE2 = colors.BLUE_SAPPHIRE
BACKGROUND_COLOR = colors.CYBER_GRAPE
PLANET_COLOR = colors.SPACE_CADET

BACKGROUND_IMAGE = asset_loader.load_image("sprites/faded_circle.png")
