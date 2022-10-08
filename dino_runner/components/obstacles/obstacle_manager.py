
import random
from components.obstacles.cactus import Cactus
from components.obstacles.bird import Bird

from utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD


class ObstacleManager():
    def __init__(self):
        self.obstacles = []


    def draw(self, screen):
        
        for obstacle in self.obstacles:
            obstacle.draw(screen)


    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_size = random.randint(0, 2)
            if cactus_size == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif cactus_size == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif cactus_size == 2:
                self.obstacles.append(Bird(BIRD))
                


        for obstacle in self.obstacles:
            obstacle.update()
            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()

            if game.dino.dino_rect.colliderect(obstacle.image_rect):
                self.obstacles.pop()
                game.death_count +=1
                if game.death_count == 5:
                    game.playing = False
                    game.excute()

    def new_method(self):
        self.size +=20
                

    