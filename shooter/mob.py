import pygame
import random
import animation


class Mob(animation.AnimateSprite):
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.pv = 100
        self.pv_max = 100
        self.atk = 0.3
        self.nb_points = 5

        self.rect = self.image.get_rect()
        self.rect.x = 1200 + random.randint(10, 400)
        self.rect.y = 540 - offset
        self.start_animation()

    def set_speed(self, speed):
        self.default_vit = speed
        self.vit = 1 + random.randint(0, self.default_vit)

    def set_nb_points(self, nbPoints):
        self.nb_points = nbPoints

    def damage(self, amount):
        self.pv -= amount

        if self.pv <= 0:
            self.rect.x = 1200 + random.randint(10, 400)
            self.vit = 1 + random.randint(0, self.default_vit)
            self.pv = self.pv_max

            # Score
            self.game.add_score(self.nb_points)

            if self.game.comet_event.is_full_loaded():
                self.game.all_Mob.remove(self)
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_pv_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.pv_max, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.pv, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.vit
        else:
            self.game.player.damage(self.atk)


class Mummy(Mob):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_nb_points(5)


class Alien(Mob):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.pv = 280
        self.pv_max = 280
        self.atk = 0.8
        self.set_speed(1)
        self.set_nb_points(15)

        self.rect.x = 1200 + random.randint(10, 400)
