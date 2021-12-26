import pygame
from joueur import Player
from mob import Mob, Mummy, Alien
from comet_event import CometFallEvent


#Classe jeu
from sounds import SoundManager


class Game:
    def __init__(self):
        # Commencer ?
        self.is_playing = False

        # Génération du joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)

        # Events
        self.comet_event = CometFallEvent(self)

        # Groupe de monstre
        self.all_Mob = pygame.sprite.Group()

        # Son
        self.sound_manager = SoundManager()

        # Score
        self.score = 0
        self.font = pygame.font.Font("assets/ShadowsIntoLight-Regular.ttf", 40)

        self.pressed = {}

    def add_score(self, points):
        self.score += points

    def start(self):
        self.is_playing = True
        self.spawm_Mob(Mummy)
        self.spawm_Mob(Mummy)
        self.spawm_Mob(Alien)

    def game_over(self):
        self.all_Mob = pygame.sprite.Group()
        self.player.pv = self.player.pv_max
        self.comet_event.all_comet = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')

    def update(self, screen):
        # Score
        score_txt = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_txt, (20, 20))

        # joueur
        screen.blit(self.player.image, self.player.rect)
        self.player.update_pv_bar(screen)
        self.player.update_animation()

        # Comet
        self.comet_event.uptade_bar(screen)

        # Projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        #for projectile in self.player.all_projectiles:
        #    projectile.move_back()

        for mob in self.all_Mob:
            mob.forward()
            mob.update_pv_bar(screen)
            mob.update_animation()

        for comet in self.comet_event.all_comet:
            comet.fall()

        self.player.all_projectiles.draw(screen)
        self.all_Mob.draw(screen)
        self.comet_event.all_comet.draw(screen)

        # Deplacement
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_droite()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_gauche()

    def spawm_Mob(self, mob_class_name):
        self.all_Mob.add(mob_class_name.__call__(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
