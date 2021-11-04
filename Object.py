import pygame
from pygame.sysfont import SysFont

class Object:
    def __init__(self, img_path, size, velocity):
        self.x =0
        self.y=0
        self.img_path = img_path
        self.put_img(img_path)
        self.sx, self.sy = size
        self.change_size(self.sx, self.sy)
        self.velocity = velocity

    def put_img(self,address):
        # png파일 일때
        # convert해줘야하는 문제가 있기때문에
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else: 
            self.img = pygame.image.load(address)
        self.sx, self.sy = self.img.get_size()

    def set_XY(self,loc):
        self.x = loc[0]
        self.y = loc[1]

    # 피사체의 그림 조정
    def change_size(self,sx,sy):
        self.img = pygame.transform.scale(self.img,(sx,sy)) # 그림의 크기를 조정한다.
        self.sx, self.sy = self.img.get_size()

    def show(self, screen):
        screen.blit(self.img,(self.x,self.y))
