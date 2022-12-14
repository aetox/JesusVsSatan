from shutil import move
from time import gmtime
from webbrowser import get
import pygame
from game import Game
from player import Player
import math
pygame.init()

#définir une clock
clock = pygame.time.Clock()
FPS = 120

#generer la fenetree de notree jeu 

pygame.display.set_caption("JesusVsSatan")
ico = pygame.image.load("assets/player/p1.png")
pygame.display.set_icon(ico)
screen = pygame.display.set_mode((1080,720))

#importer le fond d'écran du jeu

background  = pygame.image.load('assets/bg.jpg')

#on met la bannière 

banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)


#on ajoute le bouton
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(200,75))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.6)
play_button_rect.y = math.ceil(screen.get_height()/ 1.9)

#on ajouter le boutton EXIT
exit_button = pygame.image.load('assets/exit.png')
exit_button = pygame.transform.scale(exit_button,(150,55))
exit_button_rect = exit_button.get_rect()
exit_button_rect.x = math.ceil(screen.get_width() / 2.45)
exit_button_rect.y = math.ceil(screen.get_height() / 1.55) 



#charger joueurr

game = Game()

running = True

#boucle tant que running = True

while running :

    #appliquer l'arriere plan
    screen.blit(background,(-500,-300))

    #mettre à jour l'écran

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button,(play_button_rect))
        screen.blit(exit_button,(exit_button_rect))
        screen.blit(banner,(banner_rect))

        
    pygame.display.flip()

    #si  lee joeur ferme la fentre
    for event  in pygame.event.get() :
        # que l'eveneemen est fermetue de fenetre
        if event.type == pygame.QUIT :
            running =False
            pygame.quit()

        #Détecter si un joueur lache  un touche

        elif event.type == pygame.KEYDOWN :

            game.pressed[event.key] = True

        #On va detecter si la touche espace est decter pour lancer le projectile. on le met ici afin que meme si on reste appuyé ca ne spam pas
            if event.key == pygame.K_SPACE :
                game.player.lauch_projectile()
            else : 
                game.player.reset_skin()

        elif event.type == pygame.KEYUP :

            game.pressed[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #on vérifie si on clique sur le bouton play
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé
                game.start()
                game.manager_sound.play('click')
            elif exit_button_rect.collidepoint(event.pos):
                running = False
                game.manager_sound.play('click') 
                pygame.quit()

    
    clock.tick(FPS)
          
        
