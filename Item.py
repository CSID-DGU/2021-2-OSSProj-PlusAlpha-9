import pygame
from Object import Object
from Character import Character
from Defs import *
from Effect import Effect
import time
import random

class Item(Object):
    def __init__(self, frames, frames_trans, anim_id):
        super().__init__("", Default.item.value["size"], Default.item.value["velocity"], frames, frames_trans, anim_id)
        self.x_inv = random.choice([True, False])
        self.y_inv = False

        self.spawned = time.time()
        self.blink_count = 0.0
        self.inc = 0.0
        self.inc_delay = 0.0

    def move(self, game): 
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]):
            self.on_resize(game)
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
        self.update_rect((self.x, self.y))
        self.inc += Default.animation.value["speed"]
        self.inc = Utils.clamp(self.inc, 0.0, self.frame_count-1)
        if self.inc >= self.frame_count-1:
            self.inc_delay += Default.animation.value["speed"]
            if self.inc_delay >= Default.animation.value["interval"]:
                self.inc = 0.0
                self.inc_delay = 0.0
        self.current_frame = int(self.inc)
        if self.is_transparent == False:
            self.img = self.frames[int(self.inc)]
        else:
            self.img = self.frames_trans[int(self.inc)]

        time_passed = time.time() - self.spawned
        time_left = Default.item.value["duration"] - time_passed 
        if time_left > 0:
            if time_left <= Default.animation.value["blink"]["duration"]:
                self.blink_count += Default.animation.value["blink"]["speed"]
                if(self.blink_count >= Default.animation.value["blink"]["frame"]):
                    if self.is_transparent == False:
                        self.img = self.frames_trans[int(self.inc)]
                        self.blink_count = 0.0
                        self.is_transparent = True
                    else:
                        self.img = self.frames[int(self.inc)]
                        self.blink_count = 0.0
                        self.is_transparent = False
        else:
            game.item_list.remove(self)

class Bomb(Item):
    def __init__(self, animation):
        super().__init__(animation.frames, animation.frames_trans, "bomb")

    def use(self, game):
        if self.is_collidable == True:
            game.character.bomb_count+=1
            self.is_collidable = False
            game.item_list.remove(self)

class Coin(Item):
    def __init__(self, animation):
        super().__init__(animation.frames, animation.frames_trans, "coin")

    def use(self, game):
        if self.is_collidable == True:
            game.score += 50
            self.is_collidable = False
            game.item_list.remove(self)

class Health(Item):
    def __init__(self, animation):
        super().__init__(animation.frames, animation.frames_trans, "health")

    def use(self, game):
        if self.is_collidable == True:
            game.life += 1
            self.is_collidable = False
            game.item_list.remove(self)

class PowerUp(Item):
    def __init__(self, animation):
        super().__init__(animation.frames, animation.frames_trans, "powerup")

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
    def __init__(self, animation):
        super().__init__(animation.frames, animation.frames_trans, "speedup")
        self.sfx = pygame.mixer.Sound(Default.item.value["speedup"]["sound"])
        self.sfx.set_volume(Default.sound.value["sfx"]["volume"])
        
    def use(self, game):
        if self.is_collidable == True:
            self.sfx.play()
            self.used = time.time()
            self.org_velocity = game.character.velocity
            self.org_fire_interval = game.character.fire_interval
            game.character.speed_up()
            self.is_collidable = False
            game.item_list.remove(self)