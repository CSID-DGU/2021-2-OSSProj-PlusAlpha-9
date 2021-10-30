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
from StageGame import StageGame
from Stage import Stage
from Character import Character
from Defs import *
from StageDataManager import *
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
#스테이지선택메뉴
stageMenu = pygame_menu.Menu("Stage Select",ww,wh,theme=mytheme)

background = pygame.image.load("./Image/StartImage.png")

def show_mode():
    menu.clear()
    menu.add.button('Oasis',start_the_game_1)
    menu.add.button('Ice',startInfiniteGame)
    menu.add.button('StageSelect',stageMenu)
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
    # self.mytheme.widget_margin=self.widget_margin_showpage
    # menu.add_vertical_margin(self.margin_main)
    menu.add.label("   - RANKING -   ", selectable=False)
    # menu.add_vertical_margin(self.margin_show)
    menu.add.button('     test ranking     ', test_rank)
    # self.menu.add_button('     Easy mode ranking     ', self.easy_rank, font_size=self.font_main)
    # self.menu.add_button('     Hard mode ranking    ', self.hard_rank, font_size=self.font_main)
    # self.menu.add_button('     Level mode ranking    ', self.level_rank, font_size=self.font_main)
    menu.add.button('         back         ', back)

def test_rank():                                                                                                            #easy 모드 랭킹
        menu.clear()
        # self.mytheme.widget_margin=self.widget_margin_rank
        # self.menu.add_vertical_margin(self.margin_main)
        menu.add.label("--Test Rank--",selectable=False,font_size=30)
        menu.add.label("ID      Score",selectable=False, font_size=20)
        easy_data = load_data()
        if len(easy_data)>5:
            for i in range(5):
                easy_name = str(easy_data[i]['ID'])
                easy_score = '{0:>05s}'.format(str(easy_data[i]['score']))
                r= "#{} : ".format(i+1) + easy_name + "    " + easy_score
                menu.add.label(r,selectable=False, font_size=15)
        else:
            for i in range(len(easy_data)):
                easy_name = str(easy_data[i]['ID'])
                easy_score = '{0:>05s}'.format(str(easy_data[i]['score']))
                r= "#{} : ".format(i+1) + easy_name + "    " + easy_score
                menu.add.label(r,selectable=False, font_size=15)
        menu.add.button('back', back)

def load_data():                                             #데이터 베이스에서 데이터 불러오기
        pass
        curs = score_db.cursor(pymysql.cursors.DictCursor)
        # if game_mode == 'Easy':
        #     sql = "select * from easymode_score order by score desc "
        # elif game_mode == 'Hard':
        #     sql = "select * from hardmode_score order by score desc"
        # elif game_mode == 'Level':
        #     sql = "select * from levelmode_score order by level desc"
        sql = "select * from test_score order by score desc"
        curs.execute(sql)
        data = curs.fetchall()
        curs.close()
        return data

def add_data(self, ID, score):                                   #데이터 베이스에서 데이터 추가하기
    curs = self.score_db.cursor()
    # if game_mode == 'Easy':
    #     sql = "INSERT INTO easymode_score (ID, score) VALUES (%s, %s)"
    #     curs.execute(sql, (ID, score))
    # elif game_mode == 'Hard':
    #     sql = "INSERT INTO hardmode_score (ID, score) VALUES (%s, %s)"
    #     curs.execute(sql, (ID, score))
    # elif game_mode == 'Level':
    #     sql = "INSERT INTO levelmode_score (ID, level) VALUES (%s, %s)"
    #     curs.execute(sql, (ID, score))
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

def start_the_game_1():
    import Oasis

def start_the_game_2():
    import Ice

def startInfiniteGame():
    infi = InfiniteGame(1,1)
    infi.main()

def startStageGame(character,stage):
    StageGame(character,stage).main()
    
#스테이지 데이터 파일 읽어오기
stageData = StageDataManager.loadStageData()


#스테이지 메뉴 관련 함수
selectedChapter = [list(stageData["chapter"].keys())[0]]
selectedStage = ["1"]
def toTuple(str):
    return (str,str)

def change_background_color(selected_value, color, **kwargs):
    value_tuple, index = selected_value
    print('Change widget color to', value_tuple[0])  # selected_value ('Color', surface, color)
    if color == (-1, -1, -1):  # Generate a random color
        color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
    widget: 'pygame_menu.widgets.Selector' = kwargs.get('widget')
    widget.update_font({'selected_color': color})
    widget.get_selection_effect().color = color

def changeChapter(selected_value, chapterName, **kwargs):
    value_tuple, index = selected_value
    selectedChapter[0] = value_tuple[0]
    print(value_tuple)
    print(selectedChapter[0])


def changeStage(selected_value, stageNumber, **kwargs):
    value_tuple, index = selected_value
    selectedStage[0] = value_tuple[0]
    print(value_tuple)
    print(selectedStage[0])

def checkStageUnlocked(selectedCh:list,selectedSt:list):
    selectedChapter = selectedCh[0]
    selectedStage = selectedSt[0]
    stageData = StageDataManager.loadStageData()
    if(stageData["chapter"][selectedChapter][selectedStage][6]): #스테이지가 unlocked되어 있다면 실행
        startStageGame(Character(Images.character_car.value,(100,100),10,0),Stage(stageData["chapter"][selectedChapter][selectedStage]))
    else:
        print("locked")


#스테이지 메뉴 구성
chapters = list(map(toTuple,list(stageData["chapter"].keys())))
chapterSelector = stageMenu.add.selector(
    title='Chapter :\t',
    items=chapters,
    # onreturn=change_background_color,  # User press "Return" button
    onchange=changeChapter  # User changes value with left/right keys
)
chapterSelector.add_self_to_kwargs()  # Callbacks will receive widget as parameter

stages = [('1', (0)),
         ('2', (0)),
         ('3', (0))]
stageSelector = stageMenu.add.selector(
    title='Stage :\t',
    items=stages,
    # onreturn=change_background_color,  # User press "Return" button
    onchange=changeStage  # User changes value with left/right keys
)
stageSelector.add_self_to_kwargs()  # Callbacks will receive widget as parameter

stageMenu.add.button("PLAY",checkStageUnlocked,selectedChapter,selectedStage)
stageMenu.add.button("BACK",pygame_menu.events.BACK)


#메인 메뉴 구성
menu.add.button('Select mode', show_mode)
menu.add.button('Help',show_help)
menu.add.button('Rank',show_rank)
menu.add.button('Quit',pygame_menu.events.EXIT)
menu.enable()
if __name__ == '__main__':
    while True:
        surface = pygame.display.set_mode((600, 800),
                                                  pygame.RESIZABLE)
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

            

