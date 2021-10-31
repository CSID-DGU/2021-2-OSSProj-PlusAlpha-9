import pygame
import time
from Object import Object 
from Missile import Missile
from Defs import *

class Character(Object):
    def __init__(self, img_path, size, velocity, missile, boundary):
        super().__init__(img_path, size, velocity)
        self.last_fired = time.time()
        self.missiles_fired = []
        self.missile = missile
        self.boundary = boundary

    def set_boundary(self, boundary):
        self.boundary = boundary

    def update(self):
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
            
    def shoot(self):
        self.last_fired = time.time()
        missile = Missile(self.missile.img_path, (self.missile.sx, self.missile.sy), self.missile.velocity, self.missile.interval, self.missile.sfx_path)
        missile.change_size(self.boundary[0]//30,self.boundary[1]//20)
        missile.sfx.play()
        missile.x = round(self.x + self.sx / 2 - missile.sx / 2) 
        missile.y = self.y - missile.sy - 1
        self.missiles_fired.append(missile)

    def get_missiles_fired(self):
        return self.missiles_fired

class Battleship(Character):
    def __init__(self, size):
        missile = Missile(Images.missile_missile2.value, (size[0]//10, size[1]//5), 20, 2.0, Sounds.sfx_weapon2.value)
        super().__init__(Images.char_battleship.value, (size[0]//9, size[1]//8), 5, missile, size)

class Speedship(Character):
    def __init__(self, size):
        missile = Missile(Images.missile_missile2.value, (size[0]//30, size[1]//20), 30, 0.5, Sounds.sfx_weapon2.value)
        super().__init__(Images.char_speedship.value, (size[0]//9, size[1]//8), 10, missile, size)

class Medship(Character):
    def __init__(self, size):
        missile = Missile(Images.missile_missile2.value, (size[0]//20, size[1]//5), 25, 1.5, Sounds.sfx_weapon2.value)
        super().__init__(Images.char_medship.value, (size[0]//7, size[1]//5), 25, missile, size)