
from components.obstacles.obstacle import Obstacle
import random

class Cactus(Obstacle):
    
    def __init__(self, image):
        self.size = 300
        self.typee = random.randint(0, 2)
        super().__init__(image, self.typee)
        self.image_rect.y = self.size

