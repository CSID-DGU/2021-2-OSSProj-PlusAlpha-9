import pygame
from Object import Object
from Character import Character

class Item(Object):
    def __init__(self, img_path, size, velocity):
        self.boundary = pygame.display.get_surface().get_size()
        super().__init__(img_path, (self.boundary[0]//size[0], self.boundary[1]//size[1]), velocity)
        self.x_dir = 1
        self.y_dir = 1
        

    def move(self): 
        self.boundary = pygame.display.get_surface().get_size()
        self.x += self.x_dir * self.velocity
        self.y += self.y_dir * self.velocity

        if self.x < 0:
            self.x_dir *= -1
        elif self.y < 0:
            self.y_dir *= -1
        elif self.x >= self.boundary[0] - self.sx:
            self.x_dir *= -1
        elif self.y >= self.boundary[1] - self.sy:
            self.y_dir *= -1

    def use(self, character):
        if self.is_collidable == True:
            fire_count = character.fire_count + 1
            n_min = character.min_fire_count
            n_max = character.max_fire_count
            character.fire_count  = max(n_min, min(fire_count, n_max)) 
            self.is_collidable = False