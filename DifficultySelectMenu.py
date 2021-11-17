

import pygame
import pygame_menu


from InfiniteGame import *
from CharacterSelectMenu import *

class DifficultySelectMenu:

    def __init__(self,screen):
        # 화면 받고 화면 크기 값 받기
        self.screen = screen
        self.size = screen.get_size()
        self.mainloop = True
        
        menu_image = pygame_menu.baseimage.BaseImage(image_path='./Image/StartImage.png',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
        mytheme = pygame_menu.themes.THEME_ORANGE.copy()
        mytheme.background_color = menu_image 
        
        self.menu = pygame_menu.Menu('Select Difficulty...', self.size[0], self.size[1],
                            theme=mytheme)


    def to_menu(self):
        self.mainloop = False

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
        
        
        self.resizable_mainloop()


    def to_character_select_menu(self): #캐릭터 메뉴 시작 함수
        selected_mode = self.mode_selector.get_value()[0][1]
        CharacterSelectMenu(self.screen,selected_mode).show()

    
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