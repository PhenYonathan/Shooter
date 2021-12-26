import pygame
from game import Game
import math

pygame.init()

# clock
clock = pygame.time.Clock()
FPS = 60

# fenetre
pygame.display.set_caption("Jeu test shooter")
screen = pygame.display.set_mode((1280, 720))

background = pygame.image.load("assets/bg.jpg")

banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.33)

play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.9)
play_button_rect.y = math.ceil(screen.get_height() / 2)

game = Game()

running = True

# garder la fenetre ouverte
while running:
    # bg
    screen.blit(background, (0, -200))

    #Le jeu a commencer ?
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))
        screen.blit(banner, (banner_rect.x, 0))

    #elif game.pressed.get(pygame.K_UP) and game.player.rect.y > 400:
    #    game.player.move_saut()

    # Mise a jour de l'écran
    pygame.display.flip()

    # joueur ferme la fenetre ?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # détection du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #Saut
            if event.key == pygame.K_UP:
                game.player.move_saut()

            #Lancer de projectile
            if event.key == pygame.K_SPACE:
                game.start()

            if event.key == pygame.K_d:
                game.player.Launch_projectile()

            #if event.key == pygame.K_q:
            #    game.player.Launch_projectile_back()

            if event.key == pygame.K_UP:
                game.player.move_saut()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                game.sound_manager.play('click')

    clock.tick(FPS)

