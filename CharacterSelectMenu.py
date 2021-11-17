

import pygame
import pygame_menu


from StageGame import StageGame
from Stage import Stage
from StageDataManager import *
from CharacterDataManager import *
from InfiniteGame import *

class CharacterSelectMenu:

    def __init__(self,screen,attr):
        # 화면 받고 화면 크기 값 받기
        self.screen = screen
        self.size = screen.get_size()
        self.mainloop = True
        
        menu_image = pygame_menu.baseimage.BaseImage(image_path='./Image/StartImage.png',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
        mytheme = pygame_menu.themes.THEME_ORANGE.copy()
        mytheme.background_color = menu_image 
        
        self.menu = pygame_menu.Menu('Select Character...', self.size[0], self.size[1],
                            theme=mytheme)

        #선택된 스테이지
        self.attr =attr

        #캐릭터 데이터를 json에서 불러온다.
        self.character_data = CharacterDataManager.load()

    def to_menu(self):
        self.mainloop = False

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

        #캐릭터가 열려있는지 확인
        if (selected_character.is_unlocked): #캐릭터가 열려있다면

          if(isinstance(self.attr,InfiniteGame.Mode)): #인자가 난이도 모드의 객체이면 무한모드 실행
              InfiniteGame(selected_character,self.attr).main()
          else: #인자가 스테이지 객체이면 스테이지 모드 실행
              StageGame(self.character_data,selected_character,self.attr).main()

        else:
            print("character locked")


    def resizable_mainloop(self):
        while self.mainloop:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.VIDEORESIZE:
                    # Update the surface (min size : 300,500)
                    self.screen = pygame.display.set_mode((max(event.w,300), max(event.h,500)),
                                                    pygame.RESIZABLE)
                    
            #이전의 창크기와 다르다면 창크기가 변한것으로 인식하고 on_resize 실행
            if (self.size != self.screen.get_size()):
                self.on_resize()

            # Draw the menu
            self.menu.update(events)
            self.menu.draw(self.screen)

            pygame.display.flip()

    def on_resize(self):
        """
        Function checked if the window is resized.
        """
        window_size = self.screen.get_size()
        new_w, new_h = 1 * window_size[0], 1 * window_size[1]
        self.menu.resize(new_w, new_h)
        self.size = window_size
        print(f'New menu size: {self.menu.get_size()}')
