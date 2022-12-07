from random import randint
from pygame import Surface
from dino_runner.components.obstacles.obstacle import Obstacle

class SmallCactus(Obstacle):
    Y_POS_SMALL_CACTUS = 325
    def __init__(self, images: list[Surface]):
        self.type = 1
        super().__init__(images, randint(0,2))
        self.rect.y = self.Y_POS_SMALL_CACTUS