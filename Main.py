import pygame
import random
import time
import json
from collections import OrderedDict
from datetime import datetime
import pygame_menu 
from os import system
from InfiniteGame import InfiniteGame
from StageGame import StageGame
from Stage import Stage
from Character import Character
from Defs import *
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
with open('stagedata.json') as f:
    stageData = json.load(f,object_pairs_hook=OrderedDict)

print(type(stageData))
print(list(stageData["chapter"].keys()))
for i in list(stageData["chapter"].keys()):
    print(stageData["chapter"][i].keys())

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

def startGame(selectedCh:list,selectedSt:list):
    selectedChapter = selectedCh[0]
    selectedStage = selectedSt[0]
    if(stageData["chapter"][selectedChapter][selectedStage][4]): #스테이지가 unlocked되어 있다면 실행
        print("start")
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
         ('Boss', (0))]
stageSelector = stageMenu.add.selector(
    title='Stage :\t',
    items=stages,
    # onreturn=change_background_color,  # User press "Return" button
    onchange=changeStage  # User changes value with left/right keys
)
stageSelector.add_self_to_kwargs()  # Callbacks will receive widget as parameter

stageMenu.add.button("PLAY",startGame,selectedChapter,selectedStage)
stageMenu.add.button("BACK",pygame_menu.events.BACK)


#메인 메뉴 구성
menu.add.button('Select mode', show_mode)
menu.add.button('Help',show_help)
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

            

