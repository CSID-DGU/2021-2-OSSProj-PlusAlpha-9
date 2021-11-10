import pygame
import time
from Object import Object
from Defs import Images

class Effect(Object):
    def __init__(self, img_path, size, velocity):
        super().__init__(img_path, size, velocity)
        self.occurred = time.time()
        self.duration = 3.0

    def move(self):
        self.y += self.velocity