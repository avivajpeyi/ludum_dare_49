"""Module to handle the main Game Loop

To test this, run "run_ld49_game" in the CLI

"""
import random
import sys

import pygame

from . import __NAME__, asset_loader, colors
from . import constants as const
from .enemy import Enemy
from .physics import GamePhysicsHandler
from .planet import Planet
from .player import Player
from .ui import TitleMenu
from .score_manager import ScoreManager
from .custom_events import SCORE_INCREASE, GAME_OVER

PLAY_BACKGROUND_MUSIC = False


class GameWindow:
    def __init__(self):
        pygame.display.set_caption(__NAME__)
        self.screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
        if PLAY_BACKGROUND_MUSIC:
            self.play_background_music()

        self.game_is_running = False
        self.restart = True
        self.main_loop()
        self.game = None

    def play_background_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(asset_loader.filepath("sfx/music.mp3"))
        pygame.mixer.music.play(-1)  # loop the file

    def main_loop(self):
        while self.restart:
            if not self.game_is_running:
                title_screen = TitleMenu(self.screen, self.start_game)
                title_screen.update()

    def start_game(self):
        print("Start game")
        self.game = Game(self.screen)
        self.game_is_running = True
        self.game.update()
        self.restart = self.game.restart  # allow game to control execution


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.is_paused = False
        self.restart = False
        self.game_over = False
        self.clock = pygame.time.Clock()
        self.physics_handler = GamePhysicsHandler(self.screen, const.FPS)
        self.score_manger = ScoreManager()
        self.update_full_screen = False
        self.fullscreen = False

        self.init_scene()

    def init_scene(self):
        self.planet = Planet(
            size=40,
            screen=self.screen,
            color=colors.YELLOW,
            physics_handler=self.physics_handler,
        )
        for i in range(15):
            Enemy(
                x=random.randint(0, const.WIDTH),
                y=random.randint(0, const.HEIGHT),
                size=10,
                screen=self.screen,
                physics_handler=self.physics_handler,
                color=colors.RED,
            )
        for i in range(15):
            Enemy(
                x=random.randint(0, const.WIDTH),
                y=random.randint(0, const.HEIGHT),
                size=10,
                screen=self.screen,
                physics_handler=self.physics_handler,
                color=colors.BLUE,
            )
        self.player = Player(
            size=int(self.planet.size * 0.75),
            screen=self.screen,
            physics_handler=self.physics_handler,
        )

    def on_keydown(self, event):
        if event.key == pygame.K_ESCAPE:
            if self.is_paused:
                print("close pause window")  # TODO
                self.is_paused = False
            else:
                sys.exit()

        elif event.key == pygame.K_q:  # the X button on the window
            sys.exit()

        elif event.key == pygame.K_f:  # the maximise button on the window
            if not self.fullscreen:
                # Full screen needs pygame 2.0.0 for scaled. For some reason, I can't get it working ahh
                pygame.display.set_mode(
                    (const.WIDTH, const.HEIGHT),
                    pygame.FULLSCREEN | pygame.SCALED,
                )
                self.update_full_screen = True
                self.fullscreen = True
            else:
                pygame.display.set_mode((const.WIDTH, const.HEIGHT))
                self.update_full_screen = True
                self.fullscreen = False

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.on_keydown(event)

            if event == GAME_OVER:
                print("GAME OVER, BITCH")
            if event == SCORE_INCREASE:
                self.score_manger.increase_score()

    def update(self):
        while not self.game_over:
            self.process_events()

            self.screen.fill(pygame.Color("black"))

            pressed_keys = pygame.key.get_pressed()
            self.player.update(pressed_keys)

            for go in self.physics_handler.physics_game_objects:
                go.update()
            self.physics_handler.update()
            self.score_manger.draw_score_on_top_right()

            pygame.display.flip()
            self.clock.tick(const.FPS)

            # currently for debugging
            pygame.display.set_caption(
                f"fps: {self.clock.get_fps():0.2f}, "
                f"num obj: {len(self.physics_handler.physics_game_objects):02d}"
            )
