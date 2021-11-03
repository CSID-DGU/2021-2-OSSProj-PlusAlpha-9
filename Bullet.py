import pygame
from Object import Object

from math import *
class Bullet(Object):
    def __init__(self, img_path, size, velocity, fire_loc, target_loc):
        super().__init__(img_path, size, velocity)
        if((sqrt((target_loc[0] - fire_loc[0]) ** 2 + (target_loc[1] - fire_loc[1]) ** 2)) == 0):
            self.dx=1
            self.dy=1
        else:
            self.dx = int((velocity) * (target_loc[0] - fire_loc[0]) /
                            (sqrt((target_loc[0] - fire_loc[0]) ** 2 +
                                        (target_loc[1] - fire_loc[1]) ** 2)))
            self.dy = int((velocity) * (target_loc[1] - fire_loc[1]) /
                            (sqrt((target_loc[0] - fire_loc[0]) ** 2 +
                                        (target_loc[1] - fire_loc[1]) ** 2)))

        self.x = fire_loc[0]
        self.y = fire_loc[1]

    def move(self):
        self.x += self.dx
        self.y += self.dy
        


    
