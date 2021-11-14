import pygame
import time
from Object import Object 
from Missile import Missile
from Defs import *
from Effect import *

class Character(Object):
    def __init__(self, name, img_path, size, velocity, 
                missile_img, missile_size, missile_velocity, missile_sfx, 
                fire_interval, min_fire_count, max_fire_count, 
                invincibility_period, is_unlocked):
        super().__init__(img_path, size, velocity)

        self.name = name
        self.last_fired = 0.0
        self.last_bomb = 0.0
        self.missiles_fired = []
        self.missile_img = missile_img
        self.missile_size = missile_size
        self.missile_velocity = missile_velocity
        self.missile_sfx_path = missile_sfx
        self.missile_sfx =  pygame.mixer.Sound(missile_sfx)
        self.missile_sfx.set_volume(0.1)

        self.org_fire_interval = fire_interval
        self.fire_interval = fire_interval
        self.min_fire_count = min_fire_count
        self.max_fire_count = max_fire_count
        self.fire_count = self.min_fire_count

        self.last_crashed = 0.0
        self.invincibility_period = invincibility_period
        self.is_unlocked = is_unlocked

        self.blink_count = 0.0

        self.is_boosted = False
        self.powerup_duration = 10.0
        self.org_velocity = velocity
        self.org_fire_interval = fire_interval
        self.bomb_interval = 1.0

        self.bomb_count = 0
        self.bomb_radius = {"x":500, "y":500}

    def update(self, game):
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]):
            self.on_resize(game.size)
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
        if key_pressed[pygame.K_a]:
            if self.bomb_count > 0:
                if time.time() - self.last_bomb > self.bomb_interval:
                    self.use_bomb(game)
                    self.bomb_count-=1
        if self.is_boosted == True:
            if time.time() - self.boosted > self.powerup_duration:
                self.velocity = self.org_velocity
                self.fire_interval = self.org_fire_interval
                self.is_boosted = False
        if self.is_collidable == False:
            time_passed = time.time() - self.last_crashed
            self.blink_count += Misc.blinking_step.value
            if game.life > 0:
                if(self.blink_count >= Misc.blinking_speed.value):
                    if(self.is_transparent == False):
                        self.img = self.img_trans
                        self.blink_count = 0.0
                        self.is_transparent = True
                    else:
                        self.img = self.img_copy
                        self.blink_count = 0.0
                        self.is_transparent = False
                if time_passed > self.invincibility_period:
                    self.is_collidable = True
                    if(self.is_transparent):
                        self.img = self.img_copy
        else:
            self.img = self.img_copy
        for missile in list(self.missiles_fired):
            missile.update(game)
            if missile.y < -missile.sy:
                if missile in self.missiles_fired:
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

    def use_bomb(self, game):
        self.last_bomb = time.time()
        explosion = Explosion(self.bomb_radius)
        player_location = {"x":self.x+(self.sx/2), "y":self.y+(self.sy/2)}
        explosion.set_XY((player_location["x"] - explosion.sx/2, player_location["y"]- explosion.sy/2))
        game.effect_list.append(explosion)

    def get_missiles_fired(self):
        return self.missiles_fired

    def speed_up(self):
        self.boosted = time.time()
        self.velocity = self.org_velocity + 5
        self.fire_interval = self.org_fire_interval/3.0
        self.is_boosted = True

    def json_dump_obj(self) -> dict:
        _data = {}
        char_dict = self.__dict__
        for key, value in char_dict.items():
            _data[key] = value
        return {
            "name": self.name,
            "img_path": self.img_path,
            "size": self.size,
            "velocity": self.org_velocity,
            "missile_img": self.missile_img,
            "missile_size": self.missile_size,
            "missile_velocity":self.missile_velocity,
            "missile_sfx":self.missile_sfx_path,
            "fire_interval": self.org_fire_interval,
            "min_fire_count": self.min_fire_count,
            "max_fire_count": self.max_fire_count,
            "invincibility_period": self.invincibility_period,
            "is_unlocked": self.is_unlocked
        }