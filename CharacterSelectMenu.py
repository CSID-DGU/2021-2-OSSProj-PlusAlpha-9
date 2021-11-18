

import pygame
import pygame_menu
from pygame_menu.baseimage import IMAGE_MODE_FILL, IMAGE_MODE_SIMPLE
from pygame_menu.locals import ALIGN_LEFT, ALIGN_RIGHT


from StageGame import StageGame
from Stage import Stage
from StageDataManager import *
from CharacterDataManager import *
from InfiniteGame import *

class CharacterSelectMenu:
    image_widget: 'pygame_menu.widgets.Image'
    item_description_widget: 'pygame_menu.widgets.Label'

    def __init__(self,screen,attr):
        # 화면 받고 화면 크기 값 받기
        self.screen = screen
        self.size = screen.get_size()
        
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
        self.menu.disable()

    #메뉴 구성하고 보이기
    def show(self):  
        #캐릭터 선택 메뉴 구성


        characters = []
        for idx in range(len(self.character_data)):
            characters.append((self.character_data[idx].name, idx))
        self.character_imgs = []
        for idx in range(len(self.character_data)):       
            default_image = pygame_menu.BaseImage(
                image_path=self.character_data[idx].img_path
            ).scale(0.5, 0.5)
            self.character_imgs.append(default_image.copy())
        
        self.character_selector = self.menu.add.selector(
            title='Character :\t',
            items=characters,
            onchange=self._on_selector_change
        )
        self.image_widget = self.menu.add.image(
            image_path=self.character_imgs[0],
            padding=(25, 0, 0, 0)  # top, right, bottom, left
        )
        self.item_description_widget = self.menu.add.label(title='')
        self.fire_rate = self.menu.add.progress_bar(
            title="FireRate",
            default=int((0.3/self.character_data[0].org_fire_interval)*100),
            progress_text_enabled = False,
            box_progress_color =(200,60,50,255)
            
        )
        self.velocity = self.menu.add.progress_bar(
            title="Mobility",
            default=int((self.character_data[0].org_velocity/25)*100),
            progress_text_enabled = False,
            box_progress_color = (50,200,50,255)
        )
        self.menu.add.button("PLAY",self.start_game)
        self.menu.add.button("BACK",self.to_menu)
        self._update_from_selection(int(self.character_selector.get_value()[0][1]))
        self.menu.mainloop(self.screen,self.check_resize)


    def start_game(self): #게임 시작 함수

        # 캐릭터 셀릭터가 선택하고 있는 데이터를 get_value 로 가져와서, 그 중 Character 객체를 [0][1]로 접근하여 할당
        selected_idx = self.character_selector.get_value()[0][1]

        #캐릭터가 열려있는지 확인
        if (self.character_data[selected_idx].is_unlocked): #캐릭터가 열려있다면

          if(isinstance(self.attr,InfiniteGame.Mode)): #인자가 난이도 모드의 객체이면 무한모드 실행
              InfiniteGame(self.character_data[selected_idx],self.attr).main()
          else: #인자가 스테이지 객체이면 스테이지 모드 실행
              StageGame(self.character_data,self.character_data[selected_idx],self.attr).main()

        else:
            print("character locked")

    #menu mainloop에서 매번 체크 실행
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
            self.size = window_size
            print(f'New menu size: {self.menu.get_size()}')

    def _on_selector_change(self, selected, value: int) -> None:
        """
        Function executed if selector changes.
        :param selected: Selector data containing text and index
        :param value: Value from the selected option
        :return: None
        """
        print('Selected data:', selected)
        self._update_from_selection(value)

    def _update_from_selection(self, selected_value, **kwargs) -> None:
        """
        Change widgets depending on index.
        :param index: Index
        :return: None
        """
        self.current = selected_value
        self.image_widget.set_image(self.character_imgs[selected_value])
        self.fire_rate.set_value(int((0.3/self.character_data[selected_value].org_fire_interval)*100))
        self.velocity.set_value(int((self.character_data[selected_value].org_velocity/25)*100))
        self.item_description_widget.set_title(self.character_data[selected_value].name)
