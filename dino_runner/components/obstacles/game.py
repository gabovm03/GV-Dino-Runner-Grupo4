



import pygame
from utils.constants import RUNNING
import text_utils
from components.dinosaurio import Dinosaur
from components.nube import Cloud
from components.corazon import Heart
from components.obstacles.obstacle_manager import ObstacleManager
from utils.constants import CLOUD, HEART
from utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_runing = True
        self.dino = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.cloud = Cloud()
        self.heart = Heart()
        self.game_speed = 20
        self.x_pos_cloud = 700
        self.y_pos_cloud = 100
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.death_count = 0
        self.points = 0

    def run(self):
        sound = pygame.mixer.Sound("run.pp3")
        # Game loop: events - update - draw
        self.playing = True
        self.reset_attributs()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def reset_attributs(self):
        self.death_count = 0
        self.points = 0

    def excute(self):
        while self.game_runing:
            if not self.playing:
                self.show_menu()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.dino.update(user_input)
        self.obstacle_manager.update(self)
        self.heart.update(self)
        
        

    def draw(self):
        
        
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.score()
        self.dino.draw(self.screen)
        self.heart.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.cloud_run()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


    def cloud_run(self):

        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 1500
        self.x_pos_cloud -= self.game_speed


    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed +=1
        text, text_rect = text_utils.get_score_elements(self.points)
        self.screen.blit(text, text_rect)


    def show_menu(self):
        self.screen.fill((255, 255, 255))
        self.show_menu_options()
        pygame.display.update()
        self.handle_events_menu()
        #pygame.time.delay(1000)
        #self.playing = True
        #self.run()
       
    
    def handle_events_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.run()
            
            if event.type == pygame.QUIT:
                self.game_runing = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()

    def show_menu_options(self):
        message = "Welcome to Dino Runner" if self.death_count <= 0 else "GAME OVER" 
        text, text_rect = text_utils.get_center_message(message, font_size = 30)
        self.screen.blit(text, text_rect)
        pos_y = (SCREEN_HEIGHT//2) +30
        message_instruccion = "Press any key to start the game"
        text_instruction, text_instruccion_rect = text_utils.get_center_message(message_instruccion, height=pos_y)
        self.screen.blit(text_instruction, text_instruccion_rect)
        self.screen.blit(RUNNING[0], ((500), pos_y - 190))


    