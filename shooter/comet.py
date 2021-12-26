import pygame
import random


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.vit = random.randint(3, 6)
        self.rect.x = random.randint(0, 1300)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event
        self.atk = 20

    def remove(self):
        self.comet_event.all_comet.remove(self)
        self.comet_event.game.sound_manager.play('tir')

        if len(self.comet_event.all_comet) == 0:
            self.comet_event.reset_percent()
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.vit

        if self.rect.y >= 550:
            self.remove()

            if len(self.comet_event.all_comet) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_player):
            self.remove()
            self.comet_event.game.player.damage(self.atk)
