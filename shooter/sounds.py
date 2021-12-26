import pygame


class SoundManager:
    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("assets/sounds/click.wav"),
            'game_over': pygame.mixer.Sound("assets/sounds/game_over.wav"),
            'meteorite': pygame.mixer.Sound("assets/sounds/meteorite.wav"),
            'tir': pygame.mixer.Sound("assets/sounds/tir.wav"),
        }

    def play(self, name):
        self.sounds[name].play()

