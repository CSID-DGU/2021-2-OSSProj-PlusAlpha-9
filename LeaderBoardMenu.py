
import pygame
import pygame_menu


from StageGame import StageGame
from Stage import Stage
from StageDataManager import *
from CharacterDataManager import *
from CharacterSelectMenu import *
from Rank import *

class LeaderBoardMenu:
    def __init__(self,screen):
        
        self.size = screen.get_size()
        self.screen = screen

        menu_image = pygame_menu.baseimage.BaseImage(image_path='./Image/DESERT_modified_v3.jpg',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
        mytheme = pygame_menu.themes.THEME_ORANGE.copy()
        mytheme.background_color = menu_image 
        
        self.menu = pygame_menu.Menu('-- LeaderBoard --', self.size[0], self.size[1],
                            theme=mytheme)
        self.tens = 0

    def to_menu(self):
        self.menu.disable()

    def rank(self):
        self.menu.clear()
        self.menu.add.label("   - RANKING -   ", selectable=False)
        self.menu.add.button('     current ranking     ', self.current_rank)
        self.menu.add.button('     past ranking     ', self.current_rank)
        self.menu.add.button('         back         ', self.to_menu)
        self.menu.mainloop(self.screen)

    def current_rank(self):
        self.menu.clear()
        self.menu.add.label("   - Current Rank -   ", selectable=False)
        self.menu.add.button('     easy mode     ', self.show_current_easy_rank)
        self.menu.add.button('     hard mode     ', self.show_current_hard_rank)
        self.menu.add.button('         back         ', self.rank)
        self.menu.draw(self.screen)

    # def past_rank(self):
    #     self.menu.clear()
    #     self.menu.add.label("   - Past Rank -   ", selectable=False)
    #     self.menu.add.button('     easy mode     ', current_easy_rank)
    #     self.menu.add.button('     hard mode     ', current_hard_rank)
    #     self.menu.add.button('         back         ', show_rank)

# 1. current rank 페이지화
# 2. current rank 검색 기능 추가
# 3. past rank 100위까지 자르고 정렬
# 4. 데이터베이스에 날짜 속성 추가 (서버 타임스탬프 ??)
# 5. 월 바뀔 때 데이터 갱신

    def show_current_easy_rank(self):
        self.get_current_rank('easy')

    def show_current_hard_rank(self):
        self.get_current_rank('hard')

    def get_current_rank(self, mode):
            rank = Rank()
            self.menu.clear()
            self.menu.add.image("./Image/Catus.png", angle=-10, scale=(0.15, 0.15))
            self.tens = 0

            if(mode == 'easy'):
                global easy_data
                easy_data = rank.load_data("easy")
                self.get_rank_page('easy',self.tens)

            elif(mode == 'hard'):
                self.menu.clear()
                self.menu.add.label("--Current Hard Rank--",selectable=False,font_size=30)
                self.menu.add.label("ID      Score",selectable=False, font_size=20)
                hard_data = rank.load_data("hard")
                for i in range(len(hard_data)):
                        easy_name = str(hard_data[i]['ID'])
                        easy_score = '{0:>05s}'.format(str(hard_data[i]['score']))
                        r= "#{} : ".format(i+1) + easy_name + "    " + easy_score
                        self.menu.add.label(r,selectable=False, font_size=15)
                self.menu.add.button('back', self.current_rank)
                self.menu.mainloop(self.screen)

    def get_rank_page(self, mode, tens):
        self.menu.clear()
        self.menu.add.label("--Current "+ mode +" Rank--",selectable=False,font_size=30)
        self.menu.add.label("ID      Score",selectable=False, font_size=20)
        for i in range(10):
            if(tens*10+i == len(easy_data)): break
            name = str(easy_data[tens*10+i]['ID'])
            score = '{0:>05s}'.format(str(easy_data[tens*10+i]['score']))
            r= "#{} : ".format(tens*10+i+1) + name + "    " + score
            self.menu.add.label(r,selectable=False, font_size=20)
        prev_next_frame = self.menu.add.frame_h(250, 60)
        if(tens == 0):
            prev_next_frame.pack(self.menu.add.label('  '),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add.button('>', self.get_next_rank_page),align=pygame_menu.locals.ALIGN_CENTER)
        elif(tens == len(easy_data)//10):
            prev_next_frame.pack(self.menu.add.button('<', self.get_prev_rank_page),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add.label('  '),align=pygame_menu.locals.ALIGN_CENTER)
        else:
            prev_next_frame.pack(self.menu.add.button('<', self.get_prev_rank_page),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add.button('>', self.get_next_rank_page),align=pygame_menu.locals.ALIGN_CENTER)
        self.menu.add.button('back', self.current_rank)
        self.menu.mainloop(self.screen)

    def get_next_rank_page(self):
        self.tens += 1
        self.get_rank_page('easy', self.tens)

    def get_prev_rank_page(self):
        self.tens -= 1
        self.get_rank_page('easy', self.tens)
