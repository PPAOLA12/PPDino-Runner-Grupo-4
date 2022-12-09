from dino_runner.components.player_hearts.heart import Heart

DEFAULT_HEART_COUNT=3

class PlayerHeartManager:
    def __init__(self):
        self.heart_count = DEFAULT_HEART_COUNT

    def reduce_heart_count(self):
        self.heart_count -= 1
    
    def update(self, current_score):
        if current_score % 700 == 0:
            self.heart_count += 1
        
    def draw(self, screen):
        x_position = 10
        y_position = 20

        for counter in range(self.heart_count):
            heart = Heart(x_position, y_position)
            heart.draw(screen)
            x_position += 30

    def reset_heart_count(self):
        self.heart_count = DEFAULT_HEART_COUNT
