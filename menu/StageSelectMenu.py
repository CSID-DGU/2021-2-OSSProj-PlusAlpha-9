
import pygame
import pygame_menu
from data.CharacterDataManager import *
from data.Stage import Stage
from data.StageDataManager import *
from game.StageGame import StageGame
from pygame_menu.utils import make_surface

from menu.CharacterSelectMenu import *

# 스테이지 선택 메뉴
class StageSelectMenu:

    def __init__(self,screen):
        
        self.size = screen.get_size()
        self.screen = screen

        menu_image = pygame_menu.baseimage.BaseImage(image_path='./Image/StartImage.png',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
        mytheme = pygame_menu.themes.THEME_ORANGE.copy()
        mytheme.background_color = menu_image 
        
        self.menu = pygame_menu.Menu('Select Stage...', self.size[0], self.size[1],
                            theme=mytheme)
        
        self.stage_data = StageDataManager.loadStageData()

        #initialize variables to save seleted chapter and stage.
        self.selectedChapter = [list(self.stage_data["chapter"].keys())[0]]
        self.selectedStage = ["1"]

    def to_menu(self):
        self.menu.disable()

    #Selector 위젯에는 아이템을 튜플 형태로 넣어줘야하므로 변환 함수
    def toTuple(self,str):
        return (str,str)

    #스테이지 선택화면
    def show(self):
        #스테이지 메뉴 구성
        #json에서 읽어온 스테이지 데이터에서 챕터 이름들을 가져오고 chapters에 할당
        self.chapters = list(map(self.toTuple,list(self.stage_data["chapter"].keys())))
        self.chapterSelector = self.menu.add.selector(
            title='Chapter :\t',
            items=self.chapters
        )

        self.stages = [('1', (0)),
                ('2', (0)),
                ('3', (0))]

        self.stageSelector = self.menu.add.selector(
            title='Stage :\t',
            items=self.stages
        )

        self.menu.add.button("Start",self.start_stage_game)
        self.menu.add.button("BACK",self.to_menu)

        self.menu.mainloop(self.screen,bgfun = self.check_resize)


    def start_stage_game(self):
        # 현재 selector가 선택하고 있는 항목을 get_value로 가져오고, 그것의 키를 [0][0]을 통해 가져온다.
        selected_chapter = self.chapterSelector.get_value()[0][0]
        selected_stage = self.stageSelector.get_value()[0][0]
        #스테이지 언락되었는지 확인하고, 언락되었으면 캐릭터 선택 메뉴에 스테이지 넘겨주고 실행
        if (self.check_stage_unlock(selected_chapter,selected_stage)):
            # self.menu._open(CharacterSelectMenu(self.screen,Stage(self.stage_data["chapter"][selected_chapter][selected_stage])))
            CharacterSelectMenu(self.screen,Stage(self.stage_data["chapter"][selected_chapter][selected_stage])).show()
        else:
            self.showStageLockedScreen(selected_chapter, selected_stage)
            print(selected_chapter)
            print(selected_stage)
            print("stage locked")
        

    def check_stage_unlock(self,chapter,stage): #check if the stage is unlocked when start button clicked
        self.stage_data = StageDataManager.loadStageData()
        if Stage(self.stage_data["chapter"][chapter][stage]).is_unlocked == 1 :
            return True
        return False

    # 잠긴 스테이지 선택 시 보여지는 화면
    def showStageLockedScreen(self, chapter, stage):
        self.menu.disable()
        stagelocked_theme = pygame_menu.themes.THEME_DARK.copy()
        stagelocked_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
        stagelocked_theme.title_close_button_cursor = pygame_menu.locals.CURSOR_HAND
        stagelocked_theme.title_font_color = Color.WHITE.value
        self.menu = pygame_menu.Menu(chapter+'-'+stage, self.size[0], self.size[1], # 챕터 및 스테이지 번호가 상단 바에 나타남
                            theme=stagelocked_theme)
        self.menu.add.image(Images.stage_locked.value, scale=Scales.default.value)
        self.menu.add.label("")
        self.menu.add.button('back', self.back_from_locked)
        self.menu.mainloop(self.screen,bgfun = self.check_resize)

    # 스테이지 잠긴 화면에서 돌아오기
    def back_from_locked(self):
        self.menu.disable()
        StageSelectMenu(self.screen).show()

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
            self.menu.get_current().resize(new_w,new_h)
            self.size = window_size
            print(f'New menu size: {self.menu.get_size()}')
            self.menu._current._widgets_surface = make_surface(0,0)
