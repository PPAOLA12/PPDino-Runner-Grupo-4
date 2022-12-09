import random
import pygame
from dino_runner.components.obstacles.obtacle_manager import ObstacleManager
from dino_runner.components.obstacles.score import Score
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, CLOUD, DINO_START, ICON, RESET, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.text_utils import draw_message_components

INITIAL_GAME_SPEED = 20

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = INITIAL_GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_cloud = SCREEN_WIDTH + random.randint(800, 1000)
        self.y_cloud = random.randint(50, 100)

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.score = Score()
        self.player_heart_manager = PlayerHeartManager()
        self.death_count = 0

        self.executing = False

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.obstacle_manager.reset_obtacles()
        self.game_speed = INITIAL_GAME_SPEED
        self.score.reset_score()
        self.player_heart_manager.reset_heart_count()
        self.power_up_manager.reset_power_ups()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing =False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.score.update(self)
        self.power_up_manager.update(self.score.current_score, self.game_speed, self.player)
        self.player_heart_manager.update(self.score.current_score)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_cloud()
        self.player.draw(self.screen)
        self.player.check_power_up(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width: #la imagen paso el margen
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_cloud(self):
        cloud_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_cloud, self.y_cloud))
        self.screen.blit(CLOUD, (cloud_width + self.x_cloud, self.y_cloud))
        if self.x_cloud < -cloud_width:
            self.x_cloud = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y_cloud = random.randint(50, 100)
        self.x_cloud -= self.game_speed
    def draw_death_count(self):
        half_screen_heignt = SCREEN_HEIGHT //2
        draw_message_components(f'Your Die: {self.death_count}', self.screen, pos_y_center= half_screen_heignt+100)

    def draw_score(self):
        half_screen_heignt = SCREEN_HEIGHT //2
        draw_message_components(f'Your Score: {self.score.current_score}', self.screen, pos_y_center= half_screen_heignt+50)

    def show_menu(self):
        #Poner fondo a la pantalla
        self.screen.fill((255, 255, 255))
        #mostrar mensaje de inicio
        half_screen_width = SCREEN_WIDTH // 2 
        half_screen_heignt = SCREEN_HEIGHT //2
        #mostrar imagen como icono
        if not self.death_count:
            self.screen.blit(DINO_START, (half_screen_width-20, half_screen_heignt -140))
            draw_message_components('Pass any key to start', self.screen)
        else:
            self.screen.blit(RESET, (half_screen_width-20, half_screen_heignt -140))
            draw_message_components('Pass any key to restart', self.screen)
            self.draw_score()
            self.draw_death_count()
        #Actualizar pantalla
        pygame.display.flip()
        #manejar eventos
        self.handle_menu_events()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing =False
            elif event.type == pygame.KEYDOWN:
                self.run()