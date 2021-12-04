from collections import OrderedDict
from datetime import datetime
from os import system

import pygame
import pygame_menu
import pymysql

from data.CharacterDataManager import *
from data.Defs import *
from data.Rank import Rank
from data.StageDataManager import *
from menu.About import *
from menu.DifficultySelectMenu import *
from menu.HelpMenu import HelpMenu
from menu.LeaderBoardMenu import *
from menu.StageSelectMenu import *
from object.Character import *

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
Default.game.value["size"]["x"] = size[0]
Default.game.value["size"]["y"] = size[1]
menu_image = pygame_menu.baseimage.BaseImage(image_path=Images.start.value,drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
mytheme = pygame_menu.themes.THEME_ORANGE.copy()
mytheme.background_color = menu_image 

menu = pygame_menu.Menu('PLUS ALPHA', ww,wh,theme=mytheme)

background = pygame.image.load(Images.start.value)

# 모드 선택 메뉴
def show_mode():
    menu.clear()
    menu.add.button('Infinite Game',show_difficulty_select_menu)
    menu.add.button('Stage Game',show_stage_select_menu)
    menu.add.button('Back', back)
    menu.add.button('Quit', pygame_menu.events.EXIT)

# 메인 메뉴로 돌아가기
def back():
    menu.clear()
    menu.add.button('Select mode', show_mode)
    menu.add.button('Help',show_help)
    menu.add.button('About',show_info_menu)
    menu.add.button('Rank',show_rank)
    menu.add.button('Quit', pygame_menu.events.EXIT)

# 저자 및 라이선스 정보 확인 화면 보여주기
def show_info_menu():
    About(screen).show()

# 난이도 선택 화면 보여주기
def show_difficulty_select_menu():
    DifficultySelectMenu(screen).show()

# 스테이지 선택 화면 보여주기
def show_stage_select_menu():
    StageSelectMenu(screen).show()

# 리더보드 화면 보여주기
def show_rank():
    LeaderBoardMenu(screen).rank()

# 도움말 화면 보여주기
def show_help():
    HelpMenu(screen).show()

# 메인 메뉴
menu.add.button('Select mode', show_mode)
menu.add.button('Help',show_help)
menu.add.button('About',show_info_menu)
menu.add.button('Rank',show_rank)
menu.add.button('Quit',pygame_menu.events.EXIT)
menu.enable()


if __name__ == '__main__':
    try:
        rank = Rank()
        rank.check_update()
    except:
        pass
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.VIDEORESIZE:
                pass

        if (size != screen.get_size()): #현재 사이즈와 저장된 사이즈 비교 후 다르면 변경
            changed_screen_size = screen.get_size() #변경된 사이즈
            ratio_screen_size = (changed_screen_size[0],changed_screen_size[0]*783/720) #y를 x에 비례적으로 계산
            if(ratio_screen_size[0]<320): #최소 x길이 제한
                ratio_screen_size = (494,537)
            if(ratio_screen_size[1]>783): #최대 y길이 제한
                ratio_screen_size = (720,783)
            screen = pygame.display.set_mode(ratio_screen_size,
                                                    pygame.RESIZABLE)
            window_size = screen.get_size()
            new_w, new_h = 1 * window_size[0], 1 * window_size[1]
            menu.resize(new_w, new_h)
            size = window_size
            print(f'New menu size: {menu.get_size()}')
             

        # 화면에 메뉴 그리기
        screen.fill((25, 0, 50))

        menu.update(events)
        menu.draw(screen)

        pygame.display.flip()
