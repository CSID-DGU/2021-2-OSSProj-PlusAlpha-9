import pygame
from Object import Object
from Character import Character
from Defs import *
from Effect import Effect
import time
import random

class Item(Object):
    def __init__(self, img_arr, size, velocity):
        super().__init__(img_arr[0], size, velocity)
        self.x_dir = random.choice([-1, 1])
        self.y_dir = 1

        self.duration = 10.0
        self.blinking_period = 4.0
        self.spawned = time.time()
        self.blink_count = 0.0
        self.is_blinking = False

        self.inc = 0.0
        self.delay = 10.0
        self.inc_delay = 0.0
        self.anim_speed = 0.5

        self.animation = []
        self.animation_trans = []
        x_scale = self.boundary[0]//self.org_boundary[0]
        y_scale = self.boundary[1]//self.org_boundary[1]
        for path in img_arr:
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.scale(img,(self.size["x"]*x_scale,self.size["y"]*y_scale))
            self.animation.append(img)
            img_copy = img.copy()
            img_copy.fill((255,255,255,128), None, pygame.BLEND_RGBA_MULT)
            self.animation_trans.append(img_copy)
        self.anim_count = len(self.animation)

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
        
        self.inc += self.anim_speed
        self.inc = Utils.clamp(self.inc, 0.0, self.anim_count-1)
        if self.inc >= self.anim_count-1:
            self.inc_delay += self.anim_speed
            if self.inc_delay >= self.delay:
                self.inc = 0.0
                self.inc_delay = 0.0

        if self.is_blinking == False:
            self.img = self.animation[int(self.inc)]
        else:
            self.img = self.animation_trans[int(self.inc)]

        time_passed = time.time() - self.spawned
        time_left = self.duration - time_passed 
        if time_left > 0:
            if time_left <= self.blinking_period:
                self.blink_count += Misc.blinking_step.value
                if(self.blink_count >= Misc.blinking_speed.value):
                    if self.is_blinking == False:
                        self.img = self.animation_trans[int(self.inc)]
                        self.blink_count = 0.0
                        self.is_blinking = True
                    else:
                        self.img = self.animation[int(self.inc)]
                        self.blink_count = 0.0
                        self.is_blinking = False
        else:
            game.item_list.remove(self)

class Bomb(Item):
    def __init__(self):
        super().__init__(Images.item_bomb.value, {"x":50, "y":50 }, 5)
        self.radius = {"x":500, "y":500}

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