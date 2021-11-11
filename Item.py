import pygame
from Object import Object
from Character import Character
from Defs import *
from Effect import Effect
import math
import time

class Item(Object):
    def __init__(self, img_path, size, velocity):
        super().__init__(img_path, size, velocity)
        self.x_dir = 1
        self.y_dir = 1

        self.duration = 10.0
        self.blinking_period = 4.0
        self.spawned = time.time()
        self.blink_count = 0.0
        self.is_blinking = False

    def move(self, game): 
        self.boundary = pygame.display.get_surface().get_size()
        self.x += self.velocity * self.x_dir
        self.y += self.velocity * self.y_dir
        if self.x <= 0:
            self.x_dir = -self.x_dir
        elif self.y <= 0:
            self.y_dir = -self.y_dir
        elif self.x >= self.boundary[0] - self.sx:
            self.x_dir = -self.x_dir
        elif self.y >= self.boundary[1] - self.sy:
            self.y_dir = -self.y_dir
        time_passed = time.time() - self.spawned
        time_left = self.duration - time_passed 
        if time_left > 0:
            if time_left <= self.blinking_period:
                self.blink_count += Misc.blinking_step.value
                if(self.blink_count >= Misc.blinking_speed.value):
                    if(self.is_blinking == False):
                        self.img = self.img_trans
                        self.blink_count = 0.0
                        self.is_blinking = True
                    else:
                        self.img = self.img_copy
                        self.blink_count = 0.0
                        self.is_blinking = False
        else:
            game.item_list.remove(self)

class PowerUp(Item):
    def __init__(self):
        super().__init__(Images.item_powerup.value, {"x":50, "y":50 }, 5)

    def use(self, game):
        if self.is_collidable == True:
            fire_count = game.character.fire_count + 1
            n_min = game.character.min_fire_count
            n_max = game.character.max_fire_count
            game.character.fire_count  = max(n_min, min(fire_count, n_max)) 
            self.is_collidable = False
            game.item_list.remove(self)

class Bomb(Item):
    def __init__(self):
        super().__init__(Images.item_bomb.value, {"x":50, "y":50 }, 5)
        self.dist = 250

    def check_distance(self, enemy):
        return math.hypot((enemy.x + (enemy.sx/2)) - (self.x + (self.sx/2)), (enemy.y + (enemy.sy/2)) - (self.y + (self.sy/2))) <= float(self.dist)

    def use(self, game):
        if self.is_collidable == True:
            explosion = Effect(Images.effect_explosion.value, {"x":500, "y":500}, 2)
            explosion.set_XY((self.x- explosion.sx/2, self.y- explosion.sy/2))
            game.effect_list.append(explosion)
            for enemy in list(game.mobList):
                if self.check_distance(enemy):
                    game.mobList.remove(enemy)
            self.is_collidable = False
            game.item_list.remove(self)

