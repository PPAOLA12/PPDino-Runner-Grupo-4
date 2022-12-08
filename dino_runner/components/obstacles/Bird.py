from random import randint
from pygame import Surface
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    Y_POS_BIRD = 250
    def __init__(self, images: list[Surface]):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = self.Y_POS_BIRD
        self.index = 0
    
    def update(self, game_speed, obstacles):
        super().update(game_speed, obstacles)
        game_speed = self.images
        self.images = BIRD[0] if self.index < 5 else BIRD[1]
        self.index += 1
        if self.index >= 10:
            self.index = 0

    def draw(self, screen):
        screen.blit(self.images, (self.rect.x, self.rect.y))
        
