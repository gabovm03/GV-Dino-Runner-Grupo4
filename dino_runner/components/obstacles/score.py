import pygame


class Score:
    def _init_(self):
        self.score = 0
        
    def update (self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2

    def draw (self, screen):
        font = pygame.font.Font("freesansboldt.ttf", 30)
        text_component = font.render(f"Score: {self.score}", True, (0,0,0))
        text_rect = text_component.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text_component, text_rect)
 
    def reset_score (self): 
        self.score = 0