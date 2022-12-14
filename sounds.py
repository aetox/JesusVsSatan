import pygame

class SoundsManager:
    
    def __init__(self):
        self.sounds = {
            'click' :  pygame.mixer.Sound("assets/sounds/click.ogg"),
            'game_over' : pygame.mixer.Sound("assets/sounds/game_over.ogg"),
            'meteorite' : pygame.mixer.Sound("assets/sounds/meteorite.ogg"),
            'tir' : pygame.mixer.Sound("assets/sounds/tir.ogg"),
            'scream' : pygame.mixer.Sound("assets/sounds/scream.ogg")
        }

    def play(self, name):
        self.sounds[name].play()
    
    def stop(self, name):
        self.sounds[name].stop()
    