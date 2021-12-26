import pygame
from comet import Comet
import random


class CometFallEvent:
    # compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 8
        self.game = game
        self.fall_mode = False

        self.all_comet = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent= 0

    def comet_fall(self):
        for i in range(1, random.randint(8, 18)):
            self.all_comet.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_Mob) == 0:
            self.comet_fall()
            self.fall_mode = True

    def uptade_bar(self, surface):
        self.add_percent()

        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() - 10,
            surface.get_width(),
            10
        ])
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 10,
            (surface.get_width() / 100) * self.percent,
            10
        ])
