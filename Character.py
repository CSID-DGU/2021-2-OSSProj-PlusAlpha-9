import pygame
import time
from Object import Object 
from Missile import Missile
from Defs import *

class Character(Object):
    def __init__(self, name, img_path, size, velocity, 
                missile_img, missile_size, missile_velocity, missile_sfx, 
                fire_interval, min_fire_count, max_fire_count, 
                invincibility_period, is_unlocked):
        super().__init__(img_path, size, velocity)
        
        self.name = name
        self.last_fired = 0.0
        self.missiles_fired = []

        self.missile_img = missile_img
        self.missile_size = missile_size
        self.missile_velocity = missile_velocity
        self.missile_sfx =  pygame.mixer.Sound(missile_sfx)
        self.missile_sfx.set_volume(0.1)

        self.fire_interval = fire_interval
        self.min_fire_count = min_fire_count
        self.max_fire_count = max_fire_count
        self.fire_count = self.min_fire_count

        self.last_crashed = 0.0
        self.invincibility_period = invincibility_period
        self.is_unlocked = is_unlocked

    def update(self):
        self.boundary = pygame.display.get_surface().get_size()
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
            if time.time() - self.last_fired > self.fire_interval:
                self.shoot()
        if self.is_collidable == False:
            if time.time() - self.last_crashed > self.invincibility_period:
                self.is_collidable = True
        for missile in list(self.missiles_fired):
            missile.update()
            if missile.y < -missile.sy:
                self.missiles_fired.remove(missile)
            
    def shoot(self):
        self.last_fired = time.time()
        self.missile_sfx.play()
        for num in range(1, self.fire_count+1):
            missile = Missile(self.missile_img, self.missile_size, self.missile_velocity, self.fire_interval)
            missile.change_size()
            div_factor = self.fire_count + 1
            missile.x = round((self.x + (num * (self.sx / div_factor))) - missile.sx / 2) 
            missile.y = self.y - missile.sy - 1
            self.missiles_fired.append(missile)

    def get_missiles_fired(self):
        return self.missiles_fired