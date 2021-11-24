import pygame
import time
from Object import Object 
from Missile import *
from Defs import *
from Effect import *

class Character(Object):
    def __init__(self, name, img_path, velocity, 
                missile_img, missile_size, missile_sfx, missile_power,
                fire_interval,
                is_unlocked):
        super().__init__(img_path, Default.character.value["size"], velocity)

        self.name = name
        self.last_fired = 0.0
        self.last_bomb = 0.0
        self.missiles_fired = []
        self.missile_img = missile_img
        self.missile_size = missile_size
        self.missile_power = missile_power
        self.missile_sfx_path = missile_sfx
        self.missile_sfx =  pygame.mixer.Sound(missile_sfx)
        self.missile_sfx.set_volume(Default.character.value["missile"]["volume"])

        self.org_fire_interval = fire_interval
        self.fire_interval = fire_interval
        self.fire_count = Default.character.value["missile"]["min"]

        self.last_crashed = 0.0
        self.is_unlocked = is_unlocked

        self.blink_count = 0.0

        self.is_boosted = False
        self.org_velocity = velocity
        self.org_fire_interval = fire_interval

        self.bomb_count = 0

        self.auto_target = False

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
                if self.auto_target:
                    self.shoot_targeted(game)
        if key_pressed[pygame.K_a]:
            if self.bomb_count > 0:
                if time.time() - self.last_bomb > Default.item.value["bomb"]["interval"]:
                    self.use_bomb(game)
                    self.bomb_count-=1
        if self.is_boosted == True:
            if time.time() - self.boosted > Default.item.value["powerup"]["duration"]:
                self.velocity = self.org_velocity
                self.fire_interval = self.org_fire_interval
                self.is_boosted = False
        if self.is_collidable == False:
            time_passed = time.time() - self.last_crashed
            self.blink_count += Default.animation.value["blink"]["speed"]
            if game.life > 0:
                if(self.blink_count >= Default.animation.value["blink"]["frame"]):
                    if(self.is_transparent == False):
                        self.img = self.img_trans
                        self.blink_count = 0.0
                        self.is_transparent = True
                    else:
                        self.img = self.img_copy
                        self.blink_count = 0.0
                        self.is_transparent = False
                if time_passed > Default.character.value["invincible_period"]:
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
            missile = Missile(self.missile_img, self.missile_size, self.missile_power)
            missile.change_size()
            div_factor = self.fire_count + 1
            missile.x = round((self.x + (num * (self.sx / div_factor))) - missile.sx / 2) 
            missile.y = self.y - missile.sy
            self.missiles_fired.append(missile)

    def shoot_targeted(self, game):
        targets = self.check_for_targets(game)
        if len(targets) > 0:
            x = round(self.x + (self.sx / 2)) 
            y = self.y
            missile = TargetedMissile((x,y), game, self.missile_power)
            self.missiles_fired.append(missile)
        elif hasattr(game, "stage"):
            if game.stage.is_boss_stage:
                x = round(self.x + (self.sx / 2)) 
                y = self.y
                missile = TargetedMissile((x,y), game)
                self.missiles_fired.append(missile)

    def check_for_targets(self, game):
        targets = []
        for enemy in game.mobList:
            if enemy.is_targeted == False:
                targets.append(enemy)
        return targets

    def use_bomb(self, game):
        self.last_bomb = time.time()
        explosion = Explosion()
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
            "velocity": self.org_velocity,
            "missile_img": self.missile_img,
            "missile_size": self.missile_size,
            "missile_sfx": self.missile_sfx_path,
            "missile_power": self.missile_power,
            "fire_interval": self.org_fire_interval,
            "is_unlocked": self.is_unlocked
        }