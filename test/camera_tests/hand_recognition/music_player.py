import pygame

"""
MUSIC PLAYER CLASS
Music Player Class. Contains functions to load, play, pause, adjust volume, and stop music
"""


class MusicMan(object):
    def __init__(self, file):
        print("Loading music player...")
        pygame.mixer.init()
        self.player = pygame.mixer.music
        self.song = file
        self.file = f"./music/{file}.mp3"
        self.state = None

    def load(self):
        if self.state is None:
            self.player.load(self.file)
            self.state = "loaded"

    def play(self):
        if self.state == "pause":
            self.player.unpause()
            self.state = "play"
        elif self.state in ["loaded", "stop"]:
            self.player.play()
            self.state = "play"

    def pause(self):
        if self.state == "play":
            self.player.pause()
            self.state = "pause"

    def increase_volume(self):
        if self.state is not None:
            self.player.set_volume(self.player.get_volume() - 0.02)

    def decrease_volume(self):
        if self.state is not None:
            self.player.set_volume(self.player.get_volume() + 0.02)

    def stop(self):
        if self.state == "play":
            self.player.stop()
            self.state = "stop"
