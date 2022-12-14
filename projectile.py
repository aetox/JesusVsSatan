import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player) :
        super().__init__()
        self.velocity = 5
        self.dammage = 20
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (40, 20))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 50
        self.rect.y = player.rect.y + 110

   
    def remove(self) :
        self.player.all_projectiles.remove(self)



    def move(self) :
        self.rect.x += self.velocity

        # vérif si le projectil rentre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #retire la balle de l'écran 
            self.remove()
            #enleve la vie
            monster.damage(self.player.attack)

        #condition pour voir si le projectile sort de la fentre

        if self.rect.x > 1080 :
            self.remove()