import pygame
import time
from Object import Object 
from Missile import Missile
from Defs import *

class Character(Object):
    def __init__(self, img_path, size, velocity, missile_img, missile_size, missile_velocity, fire_interval, missile_sfx, boundary):
        super().__init__(img_path, size, velocity)
        self.last_fired = time.time()
        self.missiles_fired = []
        self.missiles_to_be_del = []
        
        self.missile_img = missile_img
        self.missile_size = missile_size
        self.missile_velocity = missile_velocity
        self.fire_interval = fire_interval
        self.missile_sfx = missile_sfx

        self.boundary = boundary

    def set_boundary(self, boundary):
        self.boundary = boundary

    def update(self):
        self.missiles_to_be_del = []
        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.x -= self.velocity
            if self.x < 0:
                self.x = 0
        if key_pressed[pygame.K_RIGHT]:
            self.x += self.velocity
            if self.x >= self.boundary[0] - self.sx:
                self.x = self.boundary[0] - self.sx
        if key_pressed[pygame.K_UP]:
            self.y -= self.velocity
            if self.y < 0:
                self.y = 0
        if key_pressed[pygame.K_DOWN]:
            self.y += self.velocity
            if self.y >= self.boundary[1] - self.sy:
                self.y = self.boundary[1] - self.sy
        if key_pressed[pygame.K_SPACE]:
            if(time.time() - self.last_fired > 0.5):
                self.shoot()
        for idx in range(len(self.missiles_fired)):
            self.missiles_fired[idx].update(self.boundary)
            if self.missiles_fired[idx].y < -self.missiles_fired[idx].sy:
                self.missiles_to_be_del.append(idx)
            
    def shoot(self):
        self.last_fired = time.time()
        missile = Missile(self.missile_img, self.missile_size, self.missile_velocity, self.fire_interval, self.missile_sfx)
        missile.change_size(self.boundary[0]//30,self.boundary[1]//20)
        missile.sfx.play()
        missile.x = round(self.x + self.sx / 2 - missile.sx / 2) 
        missile.y = self.y - missile.sy - 1
        self.missiles_fired.append(missile)

    def get_missiles_fired(self):
        return self.missiles_fired

class Battleship(Character):
    def __init__(self, size):
        super().__init__(Images.char_battleship.value, (size[0]//9, size[1]//8), 5, Images.missile_missile2.value, (size[0]//10, size[1]//5), 20, 2.0, Sounds.sfx_weapon2.value, size)

class Speedship(Character):
    def __init__(self, size):
        super().__init__(Images.char_speedship.value, (size[0]//9, size[1]//8), 10, Images.missile_missile2.value, (size[0]//10, size[1]//5), 20, 2.0, Sounds.sfx_weapon2.value, size)

class Medship(Character):
    def __init__(self, size):
        super().__init__(Images.char_medship.value, (size[0]//7, size[1]//5), 25, Images.missile_missile2.value, (size[0]//10, size[1]//5), 20, 2.0, Sounds.sfx_weapon2.value, size)