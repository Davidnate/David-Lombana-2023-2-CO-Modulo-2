import pygame
import random

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.extra_life import ExtraLife
from dino_runner.components.power_ups.clock import Clock


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(150, 250)
        self.duration = random.randint(3, 5)

    def generate_power_up(self):
        power_up = random.choice([Shield, ExtraLife, Clock])()
        self.when_appears += random.randint(150, 250)
        self.power_ups.append(power_up)

    

    def update(self, game):
        if len(self.power_ups) == 0 and self.when_appears == game.score.count:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                if isinstance(power_up, ExtraLife):
                    game.life += 1
                    print("Extra life!", game.life)
                elif isinstance(power_up, Clock):
                    game.power_clock = True
                    print("clock power", game.power_clock)
                else:
                    game.player.type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        self.when_appears = random.randint(150, 250)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        self.when_appears = random.randint(150, 250)