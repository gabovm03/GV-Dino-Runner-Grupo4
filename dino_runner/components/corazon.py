from utils.constants import HEART
from pygame.sprite import Sprite

class Heart(Sprite):
    def __init__(self):
        self.image = HEART
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect.x = 1050
        self.cloud_rect.y = 0


    def draw(self, screen):
        screen.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y))