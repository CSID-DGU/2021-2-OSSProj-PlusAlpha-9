import pygame
from Object import Object
from Character import Character
from Defs import Images
import math
import time

class Item(Object):
    def __init__(self, img_path, size, velocity):
        super().__init__(img_path, size, velocity)
        self.x_dir = 1
        self.y_dir = 1

        self.duration = 10.0
        self.spawned = time.time()

    def move(self): 
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

class PowerUp(Item):
    def __init__(self):
        super().__init__(Images.item_powerup.value, {"x":50, "y":50 }, 5)

    def use(self, character):
        if self.is_collidable == True:
            fire_count = character.fire_count + 1
            n_min = character.min_fire_count
            n_max = character.max_fire_count
            character.fire_count  = max(n_min, min(fire_count, n_max)) 
            self.is_collidable = False

class Bomb(Item):
    def __init__(self):
        super().__init__(Images.item_bomb.value, {"x":50, "y":50 }, 5)
        self.dist = 250

    def check_distance(self, enemy):
        return math.hypot((enemy.x + (enemy.sx/2)) - (self.x + (self.sx/2)), (enemy.y + (enemy.sy/2)) - (self.y + (self.sy/2))) <= float(self.dist)

    def use(self, enemies):
        for enemy in list(enemies):
            if self.check_distance(enemy):
                enemies.remove(enemy)