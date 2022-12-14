import pygame

class AnimateSprite(pygame.sprite.Sprite):

    #définir les choses à faire lors de la création de l'entité
    def __innit__(self, name):
        super().__init__()
        