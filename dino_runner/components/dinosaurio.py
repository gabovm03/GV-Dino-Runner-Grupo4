
import pygame
from utils.constants import DUCKING, JUMPING, RUNNING
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    X_POS = 30
    Y_POS = 300
    JUMP_VEL = 8.5

    def __init__(self):
        self.dino_run_image = RUNNING
        self.dino_jump_image = JUMPING
        self.dino_duck_image = DUCKING

        self.image = self.dino_run_image[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.jump_vel = self.JUMP_VEL
        
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.dino_step = 0
    
    def update(self, input):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()


        if input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False

        elif input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False

        elif not (self.dino_jump or input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False



        if self.dino_step >= 10:
            self.dino_step = 0


    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUNNING[0] if self.dino_step < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_step +=1

    def excute(self):
        while self.game_runing:
            if not self.playing:
                self.show_menu()

    def jump(self):
        self.image = self.dino_jump_image
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def duck(self):
        
        self.image = DUCKING[0] if self.dino_step < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = 338
        self.dino_step +=1
