import pygame
from pygame.sysfont import SysFont
from Defs import *

class Object:
    def __init__(self, img_path, size, velocity, anim_path = []):
        self.boundary = pygame.display.get_surface().get_size()
        self.org_boundary = [Default.game.value["size"]["x"],Default.game.value["size"]["y"]]
        self.x =0
        self.y=0
        self.img_path = img_path
        self.size = size
        self.sx = size["x"]
        self.sy = size["y"]
        self.velocity = velocity
        self.anim_path = anim_path
        self.is_collidable = True
        self.is_transparent = False
        if len(anim_path) > 0:
            self.anim_list = []
            self.anim_trans_list = []
            self.anim_count = len(self.anim_path)
            self.current_frame = 0 
            self.put_imgs()
        else:
            self.put_img(img_path)
            self.change_size()

    def put_img(self,address):
        # png파일 일때
        # convert해줘야하는 문제가 있기때문에
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else: 
            self.img = pygame.image.load(address)
        self.change_size()

    def put_imgs(self):
        x_scale = self.boundary[0]/self.org_boundary[0]
        y_scale = self.boundary[1]/self.org_boundary[1]
        x = int(self.size["x"]*x_scale)
        y = int(self.size["y"]*y_scale)
        for idx in range(len(self.anim_path)):
            img = pygame.image.load(self.anim_path[idx]).convert_alpha()
            img = pygame.transform.scale(img,(x,y))
            img_copy = img.copy()
            img_copy.fill((255,255,255,128), None, pygame.BLEND_RGBA_MULT)
            if len(self.anim_list) < len(self.anim_path):
                self.anim_list.append(img)
                self.anim_trans_list.append(img_copy)
            else:
                self.anim_list[idx] = img
                self.anim_trans_list[idx] = img_copy
        if self.is_transparent:
            self.img = self.anim_trans_list[self.current_frame]
        else:
            self.img = self.anim_list[self.current_frame]
        self.sx, self.sy = self.img.get_size()

    def set_XY(self,loc):
        self.x = loc[0]
        self.y = loc[1]

    # 피사체의 그림 조정
    def change_size(self):
        x_scale = self.boundary[0]/self.org_boundary[0]
        y_scale = self.boundary[1]/self.org_boundary[1]
        x = int(self.size["x"]*x_scale)
        y = int(self.size["y"]*y_scale)
        self.img = pygame.transform.scale(self.img,(x,y)) # 그림의 크기를 조정한다.
        self.img_copy = self.img.copy()
        self.img_trans = self.img.copy()
        self.img_trans.fill((255,255,255,128), None, pygame.BLEND_RGBA_MULT)
        self.sx, self.sy = self.img.get_size()
        if self.is_transparent:
            self.img = self.img_trans
        else:
            self.img = self.img_copy

    def show(self, screen):
        screen.blit(self.img,(self.x,self.y))

    #충돌 감지 함수
    def check_crash(self, o2):
        o1_mask = pygame.mask.from_surface(self.img)
        o2_mask = pygame.mask.from_surface(o2.img)

        offset = (int(o2.x - self.x), int(o2.y - self.y))
        collision = o1_mask.overlap(o2_mask, offset)
        
        if collision:
            return True
        else:
            return False

    #크기 조정 함수
    def on_resize(self, size):
        old_boundary = self.boundary
        self.boundary = size
        if len(self.anim_path) > 0:
            self.put_imgs()
        else: 
            self.put_img(self.img_path)
        self.reposition(old_boundary)

    def reposition(self, old_boundary):
        x_scale = self.x/old_boundary[0]
        y_scale = self.y/old_boundary[1]
        x = int(self.boundary[0] * x_scale)
        y = int(self.boundary[1] * y_scale)
        self.set_XY((x, y))
    
    def get_pos(self):
        return (self.x + (self.sx/2), self.y + (self.sy/2))