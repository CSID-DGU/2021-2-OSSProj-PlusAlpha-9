import pygame
from Object import Object 

class Mob(Object):
    def __init__(self, img_path, size, velocity, missile):
        super().__init__(img_path, size, velocity)
        self.missile = missile

    def move(self, boundary, game):
        self.y += self.velocity
        if self.y >= boundary[1] - self.sy:
            game.mobList.remove(self)