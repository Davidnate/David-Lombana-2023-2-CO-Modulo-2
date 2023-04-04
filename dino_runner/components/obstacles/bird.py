import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    BIRD_ALTITUDE = [230, 270, 320]
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super(). __init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_ALTITUDE)
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect)
        self.index += 1