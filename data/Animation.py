import pygame

from data.Defs import *


class AnimationManager():
    def __init__(self):
        self.animations = {
            "bomb_effect": BombEffectAnim(),
            "destroy_effect": DestroyEffectAnim(),
            "bomb": BombAnim(),
            "powerup": PowerupAnim(),
            "speedup": SpeedupAnim(),
            "coin": CoinAnim(),
            "health": HealthAnim()
        }

    def on_resize(self, game):
        for key, value in self.animations.items():
            value.on_resize(game)

class Animation():
    def __init__(self, frame_paths, size):
        self.boundary = pygame.display.get_surface().get_size()
        self.org_boundary = [Default.game.value["size"]["x"],Default.game.value["size"]["y"]]
        self.frame_paths = frame_paths
        self.size = size
        self.load_frames()

    def load_frames(self):
        self.frames = []
        self.frames_trans = []
        x_scale = self.boundary[0]/self.org_boundary[0]
        y_scale = self.boundary[1]/self.org_boundary[1]
        x = int(self.size["x"]*x_scale)
        y = int(self.size["y"]*y_scale)
        for idx in range(len(self.frame_paths)):
            img = pygame.image.load(self.frame_paths[idx]).convert_alpha()
            img = pygame.transform.scale(img,(x,y))
            img_copy = img.copy()
            img_copy.fill(Color.TRANSPARENT.value, None, pygame.BLEND_RGBA_MULT)
            self.frames.append(img)
            self.frames_trans.append(img_copy)

    def on_resize(self, game):
        self.boundary = game.size
        self.load_frames()

class BombEffectAnim(Animation):
    def __init__(self):
        super().__init__(Default.effect.value["bomb"]["frames"], Default.effect.value["bomb"]["size"])

class DestroyEffectAnim(Animation):
    def __init__(self):
        super().__init__(Default.effect.value["boom"]["frames"], Default.effect.value["boom"]["size"])

class BombAnim(Animation):
    def __init__(self):
        super().__init__(Default.item.value["bomb"]["frames"], Default.item.value["size"])

class PowerupAnim(Animation):
    def __init__(self):
        super().__init__(Default.item.value["powerup"]["frames"], Default.item.value["size"])

class SpeedupAnim(Animation):
    def __init__(self):
        super().__init__(Default.item.value["speedup"]["frames"], Default.item.value["size"])

class HealthAnim(Animation):
    def __init__(self):
        super().__init__(Default.item.value["health"]["frames"], Default.item.value["size"])

class CoinAnim(Animation):
    def __init__(self):
        super().__init__(Default.item.value["coin"]["frames"], Default.item.value["size"])
