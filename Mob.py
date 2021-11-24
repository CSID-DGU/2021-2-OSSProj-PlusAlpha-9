import pygame
from Object import Object 
from pygame.math import Vector2
import math

class Mob(Object):
    def __init__(self, img_path, size, velocity, missile):
        super().__init__(img_path, size, velocity)
        self.missile = missile
        self.is_targeted = False
        self.direction = Vector2(1,1)
        self.rad = 1

    def move(self, boundary, game):
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]): #update when screen resized
            self.on_resize(game.size)

        self.x += self.direction.y
        self.y += self.direction.x
        self.rad+=0.05
        self.direction.from_polar((self.velocity*3,math.sin(self.rad)*70))

        if self.y >= boundary[1] - self.sy:
            game.mobList.remove(self)

        