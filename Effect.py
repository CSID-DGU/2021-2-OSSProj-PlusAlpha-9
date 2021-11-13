import pygame
import time
from Object import Object
from Defs import *

class Effect(Object):
    def __init__(self, img_path, size, velocity):
        super().__init__(img_path, size, velocity)
        self.occurred = time.time()
        self.duration = 7.0
        self.inc = 0.0
        self.anim_speed = 0.4

        self.animation = []
        x_scale = self.boundary[0]//self.org_boundary[0]
        y_scale = self.boundary[1]//self.org_boundary[1]
        for path in Images.anim_explosion.value:
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.scale(img,(self.size["x"]*x_scale,self.size["y"]*y_scale))
            self.animation.append(img)
        self.anim_count = len(self.animation)

    def move(self, game):
        self.y += self.velocity
        self.inc += self.anim_speed
        self.inc = Utils.clamp(self.inc, 0.0, self.anim_count-1)
        self.img = self.animation[int(self.inc)]

        if int(self.inc) >= self.anim_count-1:
            game.effect_list.remove(self)
        else:
            for enemy in list(game.mobList):
                if self.check_crash(enemy):
                    game.mobList.remove(enemy)
                    game.score += 10