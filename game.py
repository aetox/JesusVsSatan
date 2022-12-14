import pygame
from player import  Player
from monster import Monster
from comet_event import CometFallEvent
from sounds import SoundsManager

#Créattion d'unne classe Game :
class Game:

    def __init__(self) :
        #définir si le jeu a commencé ou nom
        self.is_playing = False
        #groupe de joueurs
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        #evenement commete
        self.commet_event = CometFallEvent(self)
        
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()

        #mettre le score à 0 
        self.score = 0
        self.font = pygame.font.Font("assets/my_font.ttf", 25)
        

        #gerer le son
        self.manager_sound = SoundsManager()

        self.pressed ={}



    def start(self):
        self.is_playing = True
        self.manager_sound.stop('game_over')
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster() 
        self.spawn_monster() 
 

    
    def add_score(self, points = 10):
        self.score += points


    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.commet_event.all_comets = pygame.sprite.Group()
        self.player.health = 100
        self.commet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.manager_sound.play('game_over')
    
    def update(self, screen):

        #affiche le score
        score_text = self.font.render(f"Score : {self.score}",1,(255, 255, 255))
        screen.blit(score_text, (900, 20))    
        
        #applique l'image  du joueur 
        screen.blit(self.player.image, self.player.rect)

        #applique la vie du joueur :
        self.player.update_health_bar(screen)

        #on affiche la barre des commetes
        self.commet_event.update_bar(screen)

        for projectile in self.player.all_projectiles:
            projectile.move()

        #on récupere les monstres ajouté au groupe monstre

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        for comet in self.commet_event.all_comets:
            comet.fall()

        #on charge tout les projectiles présent du groupe game.player.all_projectiles

        self.player.all_projectiles.draw(screen)
    
        #affiche les monstres

        self.all_monsters.draw(screen)

        #groupe de comet
        self.commet_event.all_comets.draw(screen)


        #vérif si u joeur veeu aller à gauche ou droite
    
        #permetde se déplacer grac à la fonction move_ présent dans la class du player 
        #Game . player.rect. x < 888 permet au joueur de  ne pas sortir dess bordures, 

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x  > 0:
            self.player.move_left()

    

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):

        monster = Monster(self)
        self.all_monsters.add(monster)

