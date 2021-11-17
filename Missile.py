import pygame
from pymysql import NULL
from Object import Object
from Defs import *
from pygame.math import Vector2

class Missile(Object):
    def __init__(self, img_path, size, velocity, interval):
        self.boundary = pygame.display.get_surface().get_size()
        
        super().__init__(img_path, size, velocity)
        self.interval = interval

    def update(self, game):
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]):
            self.on_resize(game.size)
        self.y -= self.velocity

class TargetedMissile(Missile):
    def __init__(self, character, game):
        super().__init__(Images.weapon_target_missile.value, {"x":15, "y":25}, 20, 0.5)
        self.game = game
        self.vel = Vector2(0,0)
        self.position = Vector2((character.x-(self.sx/2)), (character.y - self.sy -1 ))  # The position of the bullet.
        self.target = self.find_target(game)
        if self.target in game.mobList:
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
                target = game.mobList[0]
                min = Utils.get_distance({"x":game.mobList[0].x,"y":game.mobList[0].y},{"x":game.character.x,"y":game.character.y}) 
                for enemy in game.mobList:
                    if min > Utils.get_distance({"x":enemy.x,"y":enemy.y},{"x":game.character.x,"y":game.character.y}):
                        min = Utils.get_distance({"x":enemy.x,"y":enemy.y},{"x":game.character.x,"y":game.character.y})
                        target = enemy
                self.target_type = "MOB"
                return target
        else:
            if len(game.mobList) > 0:
                target = game.mobList[0]
                min = Utils.get_distance({"x":game.mobList[0].x,"y":game.mobList[0].y},{"x":game.character.x,"y":game.character.y}) 
                for enemy in game.mobList:
                    if min > Utils.get_distance({"x":enemy.x,"y":enemy.y},{"x":game.character.x,"y":game.character.y}):
                        min = Utils.get_distance({"x":enemy.x,"y":enemy.y},{"x":game.character.x,"y":game.character.y})
                        target = enemy
                self.target_type = "MOB"
                return target

    def update(self, game):
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]):
            self.on_resize(game.size)
        if self.target_type == "BOSS":
            direction = Vector2(self.target.get_pos()) - self.position
            self.put_img(self.img_path)
            radius, angle = direction.as_polar()
            self.vel = direction.normalize() * self.velocity
            self.img = pygame.transform.rotozoom(self.img, -angle - 90.0, 1)
        elif self.target in game.mobList:
            direction = Vector2(self.target.get_pos()) - self.position
            self.put_img(self.img_path)
            radius, angle = direction.as_polar()
            self.vel = direction.normalize() * self.velocity
            self.img = pygame.transform.rotozoom(self.img, -angle - 90.0, 1)
        self.position += self.vel 
        self.x = self.position[0] 
        self.y = self.position[1]