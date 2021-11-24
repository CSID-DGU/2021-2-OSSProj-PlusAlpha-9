import pygame
import time
from Object import Object
from Defs import *

class Effect(Object):
    def __init__(self, img_arr, size, velocity):
        super().__init__(img_arr[0], size, velocity, img_arr)
        self.occurred = time.time()
        self.duration = 7.0
        self.inc = 0.0
        self.anim_speed = 0.4

class Explosion(Effect):
    def __init__(self):
        super().__init__(Images.anim_explosion.value, Default.item.value["bomb"]["size"], 5)
    
    def move(self, game):
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]):
            self.on_resize(game.size)
        self.y += self.velocity
        self.inc += self.anim_speed
        self.inc = Utils.clamp(self.inc, 0.0, self.anim_count-1)
        self.img = self.anim_list[int(self.inc)]

        if int(self.inc) >= self.anim_count-1:
            game.effect_list.remove(self)
        else:
            for enemy in list(game.mobList):
                if self.check_crash(enemy):
                    game.mobList.remove(enemy)
                    game.score += 10