import pygame
from projectile import Projectile
import animation


# Classe joueur
class Player(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.pv = 100
        self.pv_max = 100
        self.atk = 15
        self.vit = 8
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.pv - amount > amount:
            self.pv -= amount
        else:
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_pv_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.pv_max, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.pv, 5])

    def Launch_projectile(self):
        #Nouvelle instance de projectile
        self.all_projectiles.add(Projectile(self))
        self.start_animation()
        self.game.sound_manager.play('tir')

    #def Launch_projectile_back(self):
    #    #Nouvelle instance de projectile
    #    self.all_projectiles.add(Projectile(self))
    #    self.start_animation()
    #    self.game.sound_manager.play('tir')

    def move_droite(self):
        if not self.game.check_collision(self, self.game.all_Mob):
            self.rect.x += self.vit

    def move_gauche(self):
        self.rect.x -= self.vit

    def move_saut(self):
        self.rect.y -= 100
        clock = pygame.time.Clock()
        clock.tick(500)
        self.rect.y += 100
