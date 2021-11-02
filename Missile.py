import pygame
from Object import Object

class Missile(Object):
    def __init__(self, img_path, size, velocity, interval, sfx_path):
        super().__init__(img_path, size, velocity)
        self.interval = interval
        self.sfx_path = sfx_path
        self.sfx = pygame.mixer.Sound(sfx_path)
        self.sfx.set_volume(0.1)

    def update(self, boundary):
        self.y -= self.velocity