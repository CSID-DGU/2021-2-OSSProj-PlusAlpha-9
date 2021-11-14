import pygame
import random
import time
import json
import pymysql
from collections import OrderedDict
from datetime import datetime
import pygame_menu 
from os import system
from InfiniteGame import InfiniteGame
from Missile import Missile
from StageGame import StageGame
from Stage import Stage
from Character import *
from Defs import *
from StageDataManager import *
from CharacterDataManager import *
from Rank import Rank
from StageSelectMenu import *
from LeaderBoardMenu import *
from DifficultySelectMenu import *

class Display:
    w_init = 1/2
    h_init = 8/9
    angle = 0
    help_scale = (0.4,0.4) 

class Utillization:
    x = 0
    y = 1

pygame.init()
infoObject = pygame.display.Info()
size = [int(infoObject.current_w*Display.w_init),int(infoObject.current_h*Display.h_init)]
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
ww, wh= pygame.display.get_surface().get_size()
Misc.org_size.value["x"] = size[0]
Misc.org_size.value["y"] = size[1]
menu_image = pygame_menu.baseimage.BaseImage(image_path='./Image/StartImage.png',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
mytheme = pygame_menu.themes.THEME_ORANGE.copy()
mytheme.background_color = menu_image 

#메인메뉴
menu = pygame_menu.Menu('PLUS ALPHA', ww,wh,theme=mytheme)

background = pygame.image.load("./Image/StartImage.png")

def show_mode():
    menu.clear()
    menu.add.button('Infinite Game',show_difficulty_select_menu)
    menu.add.button('Stage Game',show_stage_select_menu)
    menu.add.button('Back', back)
    menu.add.button('Quit', pygame_menu.events.EXIT)

def back():
    menu.clear()
    menu.add.button('Select mode', show_mode)
    menu.add.button('Help',show_help)
    menu.add.button('Rank',show_rank)
    menu.add.button('Quit', pygame_menu.events.EXIT)

def help():
    menu.clear()

def show_help():
    menu.clear()
    menu.add.button('Back',back)
    menu.add.image(image_path='./Image/howtoplay.png', angle=Display.angle, scale=Display.help_scale)

def on_resize() -> None:
    """
    Function checked if the window is resized.
    """
    window_size = surface.get_size()
    new_w, new_h = 1 * window_size[0], 1 * window_size[1]
    menu.resize(new_w, new_h)
    print(f'New menu size: {menu.get_size()}')

def show_difficulty_select_menu():
    DifficultySelectMenu(screen).show()
    

def show_stage_select_menu():
    StageSelectMenu(screen).show()

def show_rank():
    LeaderBoardMenu(screen).rank()


#메인 메뉴 구성
menu.add.button('Select mode', show_mode)
menu.add.button('Help',show_help)
menu.add.button('Rank',show_rank)
menu.add.button('Quit',pygame_menu.events.EXIT)
menu.enable()

if __name__ == '__main__':
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.VIDEORESIZE:
                # Update the surface (min size : 300,500)
                surface = pygame.display.set_mode((max(event.w,300), max(event.h,500)),
                                                  pygame.RESIZABLE)
                # Call the menu event
                on_resize()

        # Draw the menu
        surface.fill((25, 0, 50))

        menu.update(events)
        menu.draw(surface)

        pygame.display.flip()