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
from StageSelectMenu import *
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

menu_image = pygame_menu.baseimage.BaseImage(image_path='./Image/StartImage.png',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
mytheme = pygame_menu.themes.THEME_ORANGE.copy()
mytheme.background_color = menu_image 

#메인메뉴
menu = pygame_menu.Menu('MUHIRRYO GOOD', ww,wh,theme=mytheme)

background = pygame.image.load("./Image/StartImage.png")

def show_mode():
    menu.clear()
    menu.add.button('Infinite Game',show_character_select_menu)
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

score_db = pymysql.connect(
        user = 'admin',
        passwd = 'the-journey',
        # port = 3306,
        host = 'the-journey-db.cvfqry6l19ls.ap-northeast-2.rds.amazonaws.com',
        db = 'sys',
        charset = 'utf8'
        )

def show_rank():
    menu.clear()
    menu.add.label("   - RANKING -   ", selectable=False)
    menu.add.button('     current ranking     ', show_current_rank)
    menu.add.button('     past ranking     ', show_current_rank)
    menu.add.button('         back         ', back)

def show_current_rank():
    menu.clear()
    menu.add.label("   - Current Rank -   ", selectable=False)
    menu.add.button('     easy mode     ', current_easy_rank)
    menu.add.button('     hard mode     ', current_hard_rank)
    menu.add.button('         back         ', show_rank)

def current_easy_rank():                                                                                                            #easy 모드 랭킹
        menu.clear()
        menu.add.label("--Current Rank--",selectable=False,font_size=30)
        menu.add.label("ID      Score",selectable=False, font_size=20)
        easy_data = load_data("easy")
        for i in range(len(easy_data)):
                easy_name = str(easy_data[i]['ID'])
                easy_score = '{0:>05s}'.format(str(easy_data[i]['score']))
                r= "#{} : ".format(i+1) + easy_name + "    " + easy_score
                menu.add.label(r,selectable=False, font_size=15)
        menu.add.button('back', show_current_rank)
    
def current_hard_rank():                                                                                                            #easy 모드 랭킹
        menu.clear()
        menu.add.label("--Current Rank--",selectable=False,font_size=30)
        menu.add.label("ID      Score",selectable=False, font_size=20)
        easy_data = load_data("hard")
        for i in range(len(easy_data)):
                easy_name = str(easy_data[i]['ID'])
                easy_score = '{0:>05s}'.format(str(easy_data[i]['score']))
                r= "#{} : ".format(i+1) + easy_name + "    " + easy_score
                menu.add.label(r,selectable=False, font_size=15)
        menu.add.button('back', show_current_rank)

def load_data(mode):                                             #데이터 베이스에서 데이터 불러오기
        curs = score_db.cursor(pymysql.cursors.DictCursor)
        if mode == "easy":
            sql = "select * from easy_score order by score desc"
        elif mode == "hard":
            sql = "select * from hard_score order by score desc"
        curs.execute(sql)
        data = curs.fetchall()
        curs.close()
        return data

def add_data(self, ID, score):                                   #데이터 베이스에서 데이터 추가하기
    curs = self.score_db.cursor()
    sql = "INSERT INTO test_score (ID, score) VALUES (%s, %s)"
    curs.execute(sql, (ID, score))
    self.score_db.commit()
    curs.close()  

def on_resize() -> None:
    """
    Function checked if the window is resized.
    """
    window_size = surface.get_size()
    new_w, new_h = 1 * window_size[0], 1 * window_size[1]
    menu.resize(new_w, new_h)
    print(f'New menu size: {menu.get_size()}')

def show_character_select_menu():
    CharacterSelectMenu(screen,None).show()
    

def show_stage_select_menu():
    StageSelectMenu(screen).show()


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