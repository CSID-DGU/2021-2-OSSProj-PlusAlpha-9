import pygame
import time
from Object import Object
from Defs import *

class Effect(Object):
    def __init__(self, img_arr, size, velocity):
        super().__init__(img_arr[0], size, velocity, img_arr)
        self.occurred = time.time()
        
        self.inc = 0.0
        self.anim_speed = Default.effect.value["speed"]

    def move(self, game):
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]):
            self.on_resize(game.size)
        self.y += self.velocity
        self.inc += self.anim_speed
        self.inc = Utils.clamp(self.inc, 0.0, self.anim_count-1)
        self.img = self.anim_list[int(self.inc)]

class Explosion(Effect):
    def __init__(self):
        super().__init__(Default.effect.value["bomb"]["frames"], Default.effect.value["bomb"]["size"], Default.effect.value["velocity"])
        self.duration = Default.effect.value["bomb"]["duration"]
    
    def move(self, game):
        super().move(game)
        if int(self.inc) >= self.anim_count-1:
            game.effect_list.remove(self)
        else:
            for enemy in list(game.mobList):
                if self.check_crash(enemy):
                    enemy.destroy(game)
                    game.score += 10

class Boom(Effect):
    def __init__(self):
        super().__init__(Default.effect.value["boom"]["frames"], Default.effect.value["boom"]["size"], Default.effect.value["velocity"])
        self.duration = Default.effect.value["boom"]["duration"]
    
    def move(self, game):
        super().move(game)
        if int(self.inc) >= self.anim_count-1:
            game.effect_list.remove(self)