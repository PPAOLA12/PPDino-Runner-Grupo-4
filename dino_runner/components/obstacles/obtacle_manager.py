import random
import pygame
from dino_runner.components.obstacles.Bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.small_cactus import SmallCactus
from dino_runner.components.player_hearts.heart import Heart
from dino_runner.utils.constants import BIRD, GAME_OVER, LARGE_CACTUS, SCREEN_HEIGHT, SCREEN_WIDTH, SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def update(self, game):
        if len(self.obstacles) == 0:
            random_elec = random.randint(0,2)
            if random_elec == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif random_elec == 1:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random_elec == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if not game.player.shield:
                if game.player.dino_rect.colliderect(obstacle.rect):
                    game.player_heart_manager.reduce_heart_count()
                    if game.player_heart_manager.heart_count > 0:
                        self.obstacles.pop()
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
            elif not game.player.hammer:
                if game.player.dino_rect.colliderect(obstacle.rect):
                    self.obstacles.pop()


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obtacles(self):
        self.obstacles = []