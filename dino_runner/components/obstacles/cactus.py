
from components.obstacles.obstacle import Obstacle
import random

from utils.constants import BIRD

from utils.constants import SMALL_CACTUS,  LARGE_CACTUS

class Cactus(Obstacle):
    
    def __init__(self, image):
        self.size = 300
        self.typee = random.randint(0, 2)
        super().__init__(image, self.typee)
        if image == SMALL_CACTUS:
            self.image_rect.y = 320
        if image == LARGE_CACTUS:
            self.image_rect.y = 300
        if image == BIRD:
            self.image_rect.y = 150
            

