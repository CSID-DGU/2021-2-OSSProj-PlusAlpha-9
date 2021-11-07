import pygame
from Object import Object

class Missile(Object):
    def __init__(self, img_path, size, velocity, interval):
        self.boundary = pygame.display.get_surface().get_size()
        
        super().__init__(img_path, (self.boundary[0]//size[0], self.boundary[1]//size[1]), velocity)
        self.interval = interval

    def update(self):
        self.y -= self.velocity