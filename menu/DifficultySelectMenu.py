

import pygame
import pygame_menu
from game.InfiniteGame import *
from pygame_menu.utils import make_surface

from menu.CharacterSelectMenu import *

# 난이도 선택 메뉴
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
        self.menu.mainloop(self.screen, self.check_resize)


    def to_character_select_menu(self): #캐릭터 메뉴 시작 함수
        selected_mode = self.mode_selector.get_value()[0][1]
        CharacterSelectMenu(self.screen,selected_mode).show()
        
        
    
    # 화면 크기 조정 감지 및 비율 고정
    def check_resize(self):
        if (self.size != self.screen.get_size()): #현재 사이즈와 저장된 사이즈 비교 후 다르면 변경
            changed_screen_size = self.screen.get_size() #변경된 사이즈
            ratio_screen_size = (changed_screen_size[0],changed_screen_size[0]*783/720) #y를 x에 비례적으로 계산
            if(ratio_screen_size[0]<320): #최소 x길이 제한
                ratio_screen_size = (494,537)
            if(ratio_screen_size[1]>783): #최대 y길이 제한
                ratio_screen_size = (720,783)
            self.screen = pygame.display.set_mode(ratio_screen_size,
                                                    pygame.RESIZABLE)
            window_size = self.screen.get_size()
            new_w, new_h = 1 * window_size[0], 1 * window_size[1]
            self.menu.resize(new_w, new_h)
            self.menu.get_current().resize(new_w, new_h)
            self.size = window_size
            self.menu._current._widgets_surface = make_surface(0,0)
            print(f'New menu size: {self.menu.get_size()}')
