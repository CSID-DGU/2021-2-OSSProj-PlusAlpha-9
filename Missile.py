import pygame
from pymysql import NULL
from Object import Object
from Defs import *
from pygame.math import Vector2

class Missile(Object):
    def __init__(self, img_path, size, power):
        self.boundary = pygame.display.get_surface().get_size()
        super().__init__(img_path, size, Default.character.value["missile"]["speed"])
        self.power = power

    def update(self, game):
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]):
            self.on_resize(game.size)
        self.y -= self.velocity

class TargetedMissile(Missile):
    def __init__(self, position, game, power):
        super().__init__(Images.weapon_target_missile.value, {"x":15, "y":25}, power)
        self.game = game
        self.vel = Vector2(0,0)
        self.position = Vector2(position[0]-self.sx/2, position[1]-self.sy)  # The position of the bullet.
        self.target = self.find_target(game)
        self.locked_on = True
        self.crosshair = Crosshair(self.target)
        if self.target in game.mobList:
            direction = Vector2(self.target.get_pos()) - self.position
            radius, angle = direction.as_polar()
            self.img = pygame.transform.rotozoom(self.img, -angle - 90.0, 1)
            self.vel = direction.normalize() * self.velocity
        if hasattr(game, "stage"):
            if game.stage.is_boss_stage:
                direction = Vector2(self.target.get_pos()) - self.position
                radius, angle = direction.as_polar()
                self.img = pygame.transform.rotozoom(self.img, -angle - 90.0, 1)
                self.vel = direction.normalize() * self.velocity

    def find_target(self, game):
        if hasattr(game, "stage"): 
            if game.stage.is_boss_stage:
                self.target_type = "BOSS"
                return game.boss
            elif len(game.mobList) > 0:
                targets = game.character.check_for_targets(game)
                if len(targets) > 0:
                    target = targets[0]
                    min = Utils.get_distance({"x":target.x,"y":target.y},{"x":game.character.x,"y":game.character.y}) 
                    for enemy in targets:
                        if min > Utils.get_distance({"x":enemy.x,"y":enemy.y},{"x":game.character.x,"y":game.character.y}):
                            min = Utils.get_distance({"x":enemy.x,"y":enemy.y},{"x":game.character.x,"y":game.character.y})
                            target = enemy
                    self.target_type = "MOB"
                    target.is_targeted = True
                    return target    
                else:
                    self.target_type = "NULL"
        else:
            if len(game.mobList) > 0:
                targets = game.character.check_for_targets(game)
                if len(targets) > 0:
                    target = targets[0]
                    min = Utils.get_distance({"x":target.x,"y":target.y},{"x":game.character.x,"y":game.character.y}) 
                    for enemy in targets:
                        if min > Utils.get_distance({"x":enemy.x,"y":enemy.y},{"x":game.character.x,"y":game.character.y}):
                            min = Utils.get_distance({"x":enemy.x,"y":enemy.y},{"x":game.character.x,"y":game.character.y})
                            target = enemy
                    self.target_type = "MOB"
                    target.is_targeted = True
                    return target
                else:
                    self.target_type = "NULL"

    def update(self, game):
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]):
            self.on_resize(game.size)
        if self.target_type == "BOSS":
            self.crosshair.move(game)
            direction = Vector2(self.target.get_pos()) - self.position
            self.put_img(self.img_path)
            radius, angle = direction.as_polar()
            self.vel = direction.normalize() * self.velocity
            self.img = pygame.transform.rotozoom(self.img, -angle - 90.0, 1)
        elif self.target in game.mobList:
            self.crosshair.move(game)
            direction = Vector2(self.target.get_pos()) - self.position
            self.put_img(self.img_path)
            radius, angle = direction.as_polar()
            self.vel = direction.normalize() * self.velocity
            self.img = pygame.transform.rotozoom(self.img, -angle - 90.0, 1)
        else:
            self.locked_on = False
        self.position += self.vel 
        self.x = self.position[0] 
        self.y = self.position[1]


class Crosshair(Object):
    def __init__(self, target, radius = {"x":100, "y":100}):
        super().__init__(Images.effect_crossair.value, radius, 5)
        self.target = target
    
    def move(self, game):
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]):
            self.on_resize(game.size)
        if self.target in game.mobList: 
            self.set_XY((self.target.get_pos()[0]-self.sx/2, self.target.get_pos()[1]-self.sy/2))
        elif hasattr(game, "stage"):
            if game.stage.is_boss_stage:
                self.set_XY((self.target.get_pos()[0]-self.sx/2, self.target.get_pos()[1]-self.sy/2))