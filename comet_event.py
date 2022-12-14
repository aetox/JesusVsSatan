import pygame
from comet import Comet


class CometFallEvent:
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False

        #Groupe sprite pour les comete

        self.all_comets = pygame.sprite.Group()

    def reset_percent(self):
        self.percent = 0
    
    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_fully_loaded(self):
        return self.percent >= 100

    def meteor_fall(self):
        #range pour avoir entre 1 et 10 commete 
        for i in range(1,20):
            self.all_comets.add(Comet(self))

    
    def attempt_fall(self):
        if self.is_fully_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.reset_percent()
            self.fall_mode = True

    def update_bar(self, surface):

        self.add_percent()

        self.attempt_fall()

        #barre noir arriere plan
        pygame.draw.rect(surface,(0, 0, 0),[
            0,
            surface.get_height() - 10,
            surface.get_width(),
            10
        ]) 
        #barre rouge jaune d'event
        pygame.draw.rect(surface,(187, 11, 11),[
            0,
            surface.get_height() - 10,
            (surface.get_width() / 100 ) * self.percent,
            10
        ]) 




