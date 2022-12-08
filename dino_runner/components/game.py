import pygame
from dino_runner.components.obstacles.obtacle_manager import ObstacleManager
from dino_runner.components.obstacles.score import Score
from dino_runner.utils.constants import BG, DINO_START, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
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
        self.obstacle_manager.reset_obtacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()

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

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
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
    
    def text_message(self, text, x_pos, y_pos):
        font = pygame.font.Font(FONT_STYLE, 40)
        message = font.render(text, True, (0, 0, 0))
        message_rect  = message.get_rect()
        message_rect.center = ( x_pos, y_pos)
        self.screen.blit(message, message_rect)

    def draw_death_count(self):
        text = f'You Die: {self.death_count}'
        x_pos = SCREEN_WIDTH // 2 
        half_screen_heignt = SCREEN_HEIGHT //2
        y_pos = half_screen_heignt + 100
        self.text_message(text, x_pos, y_pos)

    def draw_score(self):
        text = f'Your Score: {self.score}'
        x_pos = SCREEN_WIDTH // 2 
        half_screen_heignt = SCREEN_HEIGHT //2
        y_pos = half_screen_heignt + 50
        self.text_message(text, x_pos, y_pos)

    def show_menu(self):
        #Poner fondo a la pantalla
        self.screen.fill((255, 255, 255))
        #mostrar mensaje de inicio
        half_screen_width = SCREEN_WIDTH // 2 
        half_screen_heignt = SCREEN_HEIGHT //2
        #mostrar imagen como icono
        self.screen.blit(DINO_START, (half_screen_width-20, half_screen_heignt -140))
        if not self.death_count:
            text = 'Pass any key to start'
            self.text_message(text, half_screen_width, half_screen_heignt)
        else:
            text = 'Pass any key to restart'
            self.text_message(text, half_screen_width, half_screen_heignt)
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