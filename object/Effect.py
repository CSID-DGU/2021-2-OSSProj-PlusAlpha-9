import time

import pygame
from data.Defs import *

from object.Object import Object


class Effect(Object):
    def __init__(self, frames, frames_trans, size, velocity, anim_id):
        super().__init__("", size, velocity, frames, frames_trans, anim_id)
        self.occurred = time.time()
        
        self.inc = 0.0
        self.anim_speed = Default.effect.value["speed"]

    def move(self, game):
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]):
            self.on_resize(game)
        self.y += self.velocity
        self.inc += self.anim_speed
        self.inc = Utils.clamp(self.inc, 0.0, self.frame_count-1)
        self.current_frame = int(self.inc)
        self.img = self.frames[int(self.inc)]
        self.update_rect((self.x, self.y))

class Explosion(Effect):
    def __init__(self, animation):
        super().__init__(animation.frames, animation.frames_trans, Default.effect.value["bomb"]["size"], Default.effect.value["velocity"], "bomb_effect")
        self.duration = Default.effect.value["bomb"]["duration"]
    
    def move(self, game):
        super().move(game)
        if int(self.inc) >= self.frame_count-1:
            game.effect_list.remove(self)
        else:
            for enemy in list(game.mobList):
                if self.check_crash(enemy):
                    enemy.destroy(game)
                    game.score += 10
            if hasattr(game, "stage"):
                if game.stage.is_boss_stage:
                    for bullet in game.enemyBullets:
                        if self.rect_collide(bullet.rect):
                            if bullet in game.enemyBullets:
                                game.enemyBullets.remove(bullet)

class Boom(Effect):
    def __init__(self, animation):
        super().__init__(animation.frames, animation.frames_trans, Default.effect.value["boom"]["size"], Default.effect.value["velocity"], "destroy_effect")
        self.duration = Default.effect.value["boom"]["duration"]
    
    def move(self, game):
        super().move(game)
        if int(self.inc) >= self.frame_count-1:
            game.effect_list.remove(self)
