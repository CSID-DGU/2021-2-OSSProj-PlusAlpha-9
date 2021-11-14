import pygame
from Object import Object
from Character import Character
from Defs import *
from Effect import Effect
import time
import random

class Item(Object):
    def __init__(self, img_arr, size, velocity):
        super().__init__(img_arr[0], size, velocity, img_arr)
        self.x_inv = random.choice([True, False])
        self.y_inv = False

        self.duration = 10.0
        self.blinking_period = 4.0
        self.spawned = time.time()
        self.blink_count = 0.0

        self.inc = 0.0
        self.delay = 10.0
        self.inc_delay = 0.0
        self.anim_speed = 0.5

    def move(self, game): 
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]):
            self.on_resize(game.size)
        if self.x_inv == False:
            self.x += self.velocity
        else:
            self.x -= self.velocity
        if self.y_inv == False:
            self.y += self.velocity
        else:
            self.y -= self.velocity
        if self.x <= 0:
            self.x_inv = False
        elif self.y <= 0:
            self.y_inv = False
        elif self.x >= self.boundary[0] - self.sx:
            self.x_inv = True
        elif self.y >= self.boundary[1] - self.sy:
            self.y_inv = True
        
        self.inc += self.anim_speed
        self.inc = Utils.clamp(self.inc, 0.0, self.anim_count-1)
        if self.inc >= self.anim_count-1:
            self.inc_delay += self.anim_speed
            if self.inc_delay >= self.delay:
                self.inc = 0.0
                self.inc_delay = 0.0

        if self.is_transparent == False:
            self.img = self.anim_list[int(self.inc)]
        else:
            self.img = self.anim_trans_list[int(self.inc)]

        time_passed = time.time() - self.spawned
        time_left = self.duration - time_passed 
        if time_left > 0:
            if time_left <= self.blinking_period:
                self.blink_count += Misc.blinking_step.value
                if(self.blink_count >= Misc.blinking_speed.value):
                    if self.is_transparent == False:
                        self.img = self.anim_trans_list[int(self.inc)]
                        self.blink_count = 0.0
                        self.is_transparent = True
                    else:
                        self.img = self.anim_list[int(self.inc)]
                        self.blink_count = 0.0
                        self.is_transparent = False
        else:
            game.item_list.remove(self)

class Bomb(Item):
    def __init__(self):
        super().__init__(Images.item_bomb.value, {"x":50, "y":50 }, 5)

    def use(self, game):
        if self.is_collidable == True:
            game.character.bomb_count+=1
            self.is_collidable = False
            game.item_list.remove(self)

class Coin(Item):
    def __init__(self):
        super().__init__(Images.item_coin.value, {"x":50, "y":50 }, 5)

    def use(self, game):
        if self.is_collidable == True:
            game.score += 50
            self.is_collidable = False
            game.item_list.remove(self)

class Health(Item):
    def __init__(self):
        super().__init__(Images.item_health.value, {"x":40, "y":40 }, 5)

    def use(self, game):
        if self.is_collidable == True:
            game.life += 1
            self.is_collidable = False
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

class SpeedUp(Item):
    def __init__(self):
        super().__init__(Images.item_speedup.value, {"x":50, "y":50 }, 5)
        
    def use(self, game):
        if self.is_collidable == True:
            self.used = time.time()
            self.org_velocity = game.character.velocity
            self.org_fire_interval = game.character.fire_interval
            game.character.speed_up()
            self.is_collidable = False
            game.item_list.remove(self)