


from components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        typee = 0
        super().__init__(image, typee)
        self.step_index = 0
        self.image_rect.y = 250

    def draw(self, screen):
        if self.step_index >= 9:
            self.step_index = 0
        screen.blit(self.image[self.step_index // 5], self.image_rect)
        self.step_index += 1