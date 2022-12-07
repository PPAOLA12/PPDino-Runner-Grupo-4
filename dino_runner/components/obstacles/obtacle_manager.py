import random
import pygame
from dino_runner.components.obstacles.Bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.small_cactus import SmallCactus
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles: list[Obstacle] = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0,2) == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif random.randint(0,2) == 1:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0,2) == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)