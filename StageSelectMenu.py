
import pygame
import pygame_menu


from StageGame import StageGame
from Stage import Stage
from StageDataManager import *
from CharacterDataManager import *
from CharacterSelectMenu import *

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

        self.menu.mainloop(self.screen)

    def print_var(self):
        print(self.stageSelector.get_value())
        print(self.chapterSelector.get_value())

    def start_stage_game(self):
        # 현재 selector가 선택하고 있는 항목을 get_value로 가져오고, 그것의 키를 [0][0]을 통해 가져온다.
        selected_chapter = self.chapterSelector.get_value()[0][0]
        selected_stage = self.stageSelector.get_value()[0][0]
        #스테이지 언락되었는지 확인하고, 언락되었으면 캐릭터 선택 메뉴에 스테이지 넘겨주고 실행
        if (self.check_stage_unlock(selected_chapter,selected_stage)):
            CharacterSelectMenu(self.screen,Stage(self.stage_data["chapter"][selected_chapter][selected_stage])).show()
        else:
            print("stage locked")
        

    def check_stage_unlock(self,chapter,stage):
        if Stage(self.stage_data["chapter"][chapter][stage]).is_unlocked == 1 :
            return True
        return False