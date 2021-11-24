import pygame
from Object import Object
from Character import Character
from Defs import *
from Effect import Effect
import time
import random

class Item(Object):
    def __init__(self, img_arr):
        super().__init__(img_arr[0], Default.item.value["size"], Default.item.value["speed"], img_arr)
        self.x_inv = random.choice([True, False])
        self.y_inv = False

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
        time_left = Default.item.value["duration"] - time_passed 
        if time_left > 0:
            if time_left <= Default.animation.value["blink"]["duration"]:
                self.blink_count += Default.animation.value["blink"]["speed"]
                if(self.blink_count >= Default.animation.value["blink"]["frame"]):
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
        super().__init__(Images.item_bomb.value)

    def use(self, game):
        if self.is_collidable == True:
            game.character.bomb_count+=1
            self.is_collidable = False
            game.item_list.remove(self)

class Coin(Item):
    def __init__(self):
        super().__init__(Images.item_coin.value)

    def use(self, game):
        if self.is_collidable == True:
            game.score += 50
            self.is_collidable = False
            game.item_list.remove(self)

class Health(Item):
    def __init__(self):
        super().__init__(Images.item_health.value)

    def use(self, game):
        if self.is_collidable == True:
            game.life += 1
            self.is_collidable = False
            game.item_list.remove(self)

class PowerUp(Item):
    def __init__(self):
        super().__init__(Images.item_powerup.value)

    def use(self, game):
        if self.is_collidable == True:
            fire_count = game.character.fire_count + 1
            n_min = Default.character.value["missile"]["min"]
            n_max = Default.character.value["missile"]["max"]
            if fire_count > n_max:
                game.character.auto_target = True
            game.character.fire_count  = Utils.clamp(fire_count, n_min, n_max)
            self.is_collidable = False
            game.item_list.remove(self)

class SpeedUp(Item):
    def __init__(self):
        super().__init__(Images.item_speedup.value)
        
    def use(self, game):
        if self.is_collidable == True:
            self.used = time.time()
            self.org_velocity = game.character.velocity
            self.org_fire_interval = game.character.fire_interval
            game.character.speed_up()
            self.is_collidable = False
            game.item_list.remove(self)