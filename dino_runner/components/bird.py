import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

from dino_runner.utils.constants import BIRD

class Bird(Sprite):

    def __init__(self):
        self.image = BIRD [0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = 400
        self.bird_rect.y = 300
        self.game_speed =  10

    def update(self):
        self.bird_rect.x -= self.game_speed
        if self.bird_rect.x < -600:
            self.bird_rect.x = SCREEN_WIDTH

    def run(self):
        pass

    def jump(self):
        pass

    def duck(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.bird_rect.x, self.bird_rect.y))
