


from pygame.sprite import Sprite


from utils.constants import SCREEN_WIDTH
class Obstacle(Sprite):
    def __init__(self, image, typee):
        
        
        self.image = image
        self.typee = typee
        self.image_rect = self.image[self.typee].get_rect()
        self.image_rect.x = SCREEN_WIDTH
        

    def draw(self, screen):
        
        screen.blit(self.image[self.typee], self.image_rect)

    
    def update(self):
        self.image_rect.x -= 20
        
    

