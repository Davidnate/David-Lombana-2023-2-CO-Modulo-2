import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import BIRD

class Bird(Sprite):

    def __init__(self):
        self.image = BIRD [0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = 400
        self.bird_rect.y = 300

    def update(self):
        pass

    def run(self):
        pass

    def jump(self):
        pass

    def duck(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.bird_rect.x, self.bird_rect.y))