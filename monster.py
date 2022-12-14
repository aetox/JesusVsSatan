from email.mime import image
import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.loot_amount = 20
        self.number_image = str(random.randint(1,7))
        self.image = pygame.image.load('assets/mummy' + self.number_image + '.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 540
        self.velocity = random.randint(3,5)

    def damage(self,amount):
        self.health -= amount

        if self.health <= 0 :
            self.rect.x = 1000 + random.randint(0,300)
            self.velocity = random.randint(3,5)
            self.health = 100

            #ajouter les points au score
            self.game.add_score(self.loot_amount)

            #si la barre est full on enleve les monstre
        
        if self.game.commet_event.is_fully_loaded():
            
            self.game.all_monsters.remove(self)

            self.game.commet_event.attempt_fall()

            

    def update_health_bar(self, surface):
        #on dessine notre barre de vie 
        pygame.draw.rect(surface,(60,63,60),[self.rect.x - 15, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface,(121,137,51),[self.rect.x - 15, self.rect.y - 10, self.health, 5])
        

    
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            
        else : 
            self.game.player.damage(self.attack)
            self.game.manager_sound.play('scream')
