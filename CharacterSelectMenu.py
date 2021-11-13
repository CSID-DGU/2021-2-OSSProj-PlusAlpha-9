

import pygame
import pygame_menu


from StageGame import StageGame
from Stage import Stage
from StageDataManager import *
from CharacterDataManager import *
from InfiniteGame import *

class CharacterSelectMenu:

    def __init__(self,screen,stage):
        # 화면 받고 화면 크기 값 받기
        self.screen = screen
        self.size = screen.get_size()
        
        menu_image = pygame_menu.baseimage.BaseImage(image_path='./Image/StartImage.png',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
        mytheme = pygame_menu.themes.THEME_ORANGE.copy()
        mytheme.background_color = menu_image 
        
        self.menu = pygame_menu.Menu('Select Character...', self.size[0], self.size[1],
                            theme=mytheme)

        #선택된 스테이지
        self.stage =stage

        #캐릭터 데이터를 json에서 불러온다.
        self.character_data = CharacterDataManager.load()

    def to_menu(self):
        self.menu.disable()

    #메뉴 구성하고 보이기
    def show(self):  
        #캐릭터 선택 메뉴 구성
        characters = []
        for idx in range(len(self.character_data)):
            characters.append((self.character_data[idx].name, self.character_data[idx]))

        self.character_selector = self.menu.add.selector(
            title='Character :\t',
            items=characters
        )
        self.character_selector.add_self_to_kwargs()  # Callbacks will receive widget as parameter
        self.menu.add.button("PLAY",self.start_game)
        self.menu.add.button("BACK",self.to_menu)
        
        
        self.menu.mainloop(self.screen)


    def start_game(self): #게임 시작 함수

        # 캐릭터 셀릭터가 선택하고 있는 데이터를 get_value 로 가져와서, 그 중 Character 객체를 [0][1]로 접근하여 할당
        selected_character = self.character_selector.get_value()[0][1]


        if(self.stage is None ):
            if (selected_character.is_unlocked):
                InfiniteGame(selected_character).main()
            else:
                print("character locked")
            return

        if (selected_character.is_unlocked):
            StageGame(self.character_data, selected_character, self.stage).main()
        else:
            print("character locked")

