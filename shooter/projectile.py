import pygame


class Projectile(pygame.sprite.Sprite):
    # constructeur
    def __init__(self, player):
        super().__init__()
        self.vit = 9
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 135
        self.rect.y = player.rect.y + 80
        self.player = player
        self.image_original = self.image
        self.angle = 0

    def animation_rotate(self):
        self.angle -= 8
        self.image = pygame.transform.rotozoom(self.image_original, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove_projectile(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.vit

        for mob in self.player.game.check_collision(self, self.player.game.all_Mob):
            self.remove_projectile()
            mob.damage(self.player.atk)

        if self.rect.x > 1380:
            self.remove()

        self.animation_rotate()

    #def move_back(self):
    #    self.rect.x -= self.vit
#
    #    for mob in self.player.game.check_collision(self, self.player.game.all_Mob):
    #        self.remove_projectile()
    #        mob.damage(self.player.atk)
#
    #    if self.rect.x > -10:
    #        self.remove()
#
    #    self.animation_rotate()
