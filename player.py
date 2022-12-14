import pygame
from monster import Monster
from projectile import Projectile


#Création d'une première classe  qui reeprésente le joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 40
        self.velocity = 5
        self.shooting = False
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player/p2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 460

    def reset_skin(self):
        self.image = pygame.image.load('assets/player/p2.png')

    def damage(self,amount):
        if self.health - amount > amount :
            self.health -= amount
        else:
            self.game.game_over()
    
    def update_health_bar(self, surface):
        #on dessine notre barre de vie 
        pygame.draw.rect(surface,(60,63,60),[self.rect.x + 5 , self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface,(121,137,51),[self.rect.x + 5 , self.rect.y - 10, self.health, 5])
        

    def lauch_projectile(self):
        #on ajoute les projectiles dans le groupe all_projectile
        self.all_projectiles.add(Projectile(self))
        
        #le player prend le skin du tirreur 
        self.image = pygame.image.load('assets/player/p3.png')
        self.game.manager_sound.play('tir')


    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity 

    def move_left(self):
        self.rect.x -= self.velocity
    