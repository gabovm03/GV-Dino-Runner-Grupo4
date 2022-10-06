


from utils.constants import HEART
from pygame.sprite import Sprite

class Heart(Sprite):
    def __init__(self):
        self.nheart = 0
        self.image = HEART
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect.x = 1050
        self.cloud_rect.y = 0

    def draw(self, screen):
        
        if self.nheart == 0:
            screen.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y))
            screen.blit(self.image, (1020, self.cloud_rect.y))
            screen.blit(self.image, (990, self.cloud_rect.y))
            screen.blit(self.image, (960, self.cloud_rect.y))
            screen.blit(self.image, (930, self.cloud_rect.y))
        elif self.nheart == 1:
            screen.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y))
            screen.blit(self.image, (1020, self.cloud_rect.y))
            screen.blit(self.image, (990, self.cloud_rect.y))
            screen.blit(self.image, (960, self.cloud_rect.y))
        elif self.nheart == 2:
            screen.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y))
            screen.blit(self.image, (1020, self.cloud_rect.y))
            screen.blit(self.image, (990, self.cloud_rect.y))
        elif self.nheart == 3:
            screen.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y))
            screen.blit(self.image, (1020, self.cloud_rect.y))
        elif self.nheart == 4:
            screen.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y))
        

    def update(self, game):
        if game.death_count == 0:
            self.nheart = 0
        elif game.death_count == 1:
            self.nheart = 1
        elif game.death_count == 2:
            self.nheart = 2
        elif game.death_count == 3:
            self.nheart = 3
        elif game.death_count == 4:
            self.nheart = 4
        elif game.death_count == 5:
            self.nheart = 4

        
    
    
        
