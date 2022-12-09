import pygame
from dino_runner.utils.constants import FONT_STYLE
from dino_runner.utils.text_utils import draw_message_components

class Score:
    def __init__(self):
        self.current_score = 0

    def update(self, game):
        self.current_score += 1
        if self.current_score %100 == 0:
            game.game_speed += 2

    def draw(self, screen):
        draw_message_components(f'Score: {self.current_score}', screen, pos_x_center=1000, pos_y_center=50)

    def reset_score(self):
        self.current_score = 0