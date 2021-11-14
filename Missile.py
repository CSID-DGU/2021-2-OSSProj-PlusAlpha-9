import pygame
from Object import Object

class Missile(Object):
    def __init__(self, img_path, size, velocity, interval):
        self.boundary = pygame.display.get_surface().get_size()
        
        super().__init__(img_path, size, velocity)
        self.interval = interval

    def update(self, game):
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]):
            self.on_resize(game.size)
        self.y -= self.velocity