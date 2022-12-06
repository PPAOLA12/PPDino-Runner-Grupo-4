import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_VELOCITY = 8.5
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.jump_velocity = self.JUMP_VELOCITY
        self.step_index = 0
        
        self.running = True
        self.jumping = False

    def update(self, user_input):
        if self.running:
            self.run()
        elif self.jumping:
            self.jump()
        
        if user_input[pygame.K_UP] and not self.jumping:
            self.jumping = True
            self.running = False
        elif not self.jumping:
            self.running = True

        if self.step_index >= 10:
            self.step_index = 0
    
    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.step_index += 1
    
    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_velocity *4
        print(self.dino_rect.y)
        print(self.jump_velocity)
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_rect.y = self.Y_POS
            self.jumping = False
            self.jump_velocity = self.JUMP_VELOCITY

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
