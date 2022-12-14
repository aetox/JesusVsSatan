import re
import pygame
import random

class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__()
        #image de la comete
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20,800)
        self.rect.y = - random.randint(0, 800)
        self.velocity = random.randint(3,5)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        #joue le son
        self.comet_event.game.manager_sound.play('meteorite')

        #si le nb de commete == 0 on arrete l'event

        if len(self.comet_event.all_comets) == 0:
            #remettre la barre à 0
            #reset
            self.comet_event.reset_percent()
            #spwan monstre
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
        
    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 500:
            self.remove()
            
            if len(self.comet_event.all_comets) == 0 :
                #remettre la jauge à 0
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False 

        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            self.remove()
            self.comet_event.game.player.damage(20)

