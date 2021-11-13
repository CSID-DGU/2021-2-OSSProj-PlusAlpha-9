

import pygame
import pygame_menu


from InfiniteGame import *
from CharacterSelectMenu import *

class DifficultySelectMenu:

    def __init__(self,screen):
        # 화면 받고 화면 크기 값 받기
        self.screen = screen
        self.size = screen.get_size()
        
        menu_image = pygame_menu.baseimage.BaseImage(image_path='./Image/StartImage.png',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
        mytheme = pygame_menu.themes.THEME_ORANGE.copy()
        mytheme.background_color = menu_image 
        
        self.menu = pygame_menu.Menu('Select Difficulty...', self.size[0], self.size[1],
                            theme=mytheme)


    def to_menu(self):
        self.menu.disable()

    #메뉴 구성하고 보이기
    def show(self):  
        #캐릭터 선택 메뉴 구성
        mode = [("EASY",InfiniteGame.EasyMode()),("HARD",InfiniteGame.HardMode())]
        self.mode_selector = self.menu.add.selector(
            title='Difficulty :\t',
            items=mode
        )
        self.mode_selector.add_self_to_kwargs()  # Callbacks will receive widget as parameter
        self.menu.add.button("Character Select ->",self.to_character_select_menu)
        self.menu.add.button("BACK",self.to_menu)
        
        
        self.menu.mainloop(self.screen)


    def to_character_select_menu(self): #캐릭터 메뉴 시작 함수
        selected_mode = self.mode_selector.get_value()[0][1]
        CharacterSelectMenu(self.screen,selected_mode).show()
