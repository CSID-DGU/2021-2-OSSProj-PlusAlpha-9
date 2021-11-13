
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
        self.menu.add.button('     past ranking     ', self.past_rank)
        self.menu.add.button('         back         ', self.to_menu)
        self.menu.mainloop(self.screen)

    def current_rank(self):
        self.menu.clear()
        self.menu.add.label("   - Current Rank -   ", selectable=False)
        self.menu.add.button('     easy mode     ', self.show_current_easy_rank)
        self.menu.add.button('     hard mode     ', self.show_current_hard_rank)
        self.menu.add.button('         back         ', self.rank)
        self.menu.draw(self.screen)

    def past_rank(self):
        self.menu.clear()
        self.menu.add.label("   - Past Rank -   ", selectable=False)
        self.menu.add.button('     easy mode     ', self.show_past_easy_rank)
        self.menu.add.button('     hard mode     ', self.show_past_hard_rank)
        self.menu.add.button('         back         ', self.rank)

# 1. current rank 페이지화 O
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
                easy_data = rank.load_data('current','easy')
                self.get_current_easy_rank_page(self.tens)

            elif(mode == 'hard'):
                global hard_data
                hard_data = rank.load_data('current','hard')
                self.get_current_hard_rank_page(self.tens)

    def get_current_easy_rank_page(self, tens):
        self.menu.clear()
        self.menu.add.label("--Current Easy Rank--",selectable=False,font_size=30)
        id_score_bar = "{:<15s}{:<30s}{:<20s}".format('Rank', 'ID', 'Score')
        self.menu.add.label(id_score_bar,selectable=False, font_size=20)
        for i in range(10):
            if(tens*10+i == len(easy_data)): break
            name = str(easy_data[tens*10+i]['ID'])
            score = '{0:>05s}'.format(str(easy_data[tens*10+i]['score']))
            r = "{:<15s}{:<30s}{:<20s}".format(str(tens*10+i+1), name, score)
            # r= "#{} : ".format(tens*10+i+1) + name + "    " + score
            self.menu.add.label(r,selectable=False, font_size=20)
        prev_next_frame = self.menu.add.frame_h(250, 60)
        if(tens == 0):
            prev_next_frame.pack(self.menu.add.label('  '),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add.button('>', self.get_next_easy_rank_page),align=pygame_menu.locals.ALIGN_CENTER)
        elif(tens == len(easy_data)//10):
            prev_next_frame.pack(self.menu.add.button('<', self.get_prev_easy_rank_page),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add.label('  '),align=pygame_menu.locals.ALIGN_CENTER)
        else:
            prev_next_frame.pack(self.menu.add.button('<', self.get_prev_easy_rank_page),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add.button('>', self.get_next_easy_rank_page),align=pygame_menu.locals.ALIGN_CENTER)
        self.menu.add.button('back', self.current_rank)
        self.menu.mainloop(self.screen)

    def get_next_easy_rank_page(self):
        self.tens += 1
        self.get_current_easy_rank_page(self.tens)

    def get_prev_easy_rank_page(self):
        self.tens -= 1
        self.get_current_easy_rank_page(self.tens)

    def get_current_hard_rank_page(self, tens):
        self.menu.clear()
        self.menu.add.label("--Current Hard Rank--",selectable=False,font_size=30)
        id_score_bar = "{:<15s}{:<30s}{:<20s}".format('Rank', 'ID', 'Score')
        self.menu.add.label(id_score_bar,selectable=False, font_size=20)
        for i in range(10):
            if(tens*10+i == len(hard_data)): break
            name = str(hard_data[tens*10+i]['ID'])
            score = '{0:>05s}'.format(str(hard_data[tens*10+i]['score']))
            r = "{:<15s}{:<30s}{:<20s}".format(str(tens*10+i+1), name, score)
            # r= "#{} : ".format(tens*10+i+1) + name + "    " + score
            self.menu.add.label(r,selectable=False, font_size=20)
        prev_next_frame = self.menu.add.frame_h(250, 60)
        if(tens == 0):
            prev_next_frame.pack(self.menu.add.label('  '),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add.button('>', self.get_next_hard_rank_page),align=pygame_menu.locals.ALIGN_CENTER)
        elif(tens == len(easy_data)//10):
            prev_next_frame.pack(self.menu.add.button('<', self.get_prev_hard_rank_page),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add.label('  '),align=pygame_menu.locals.ALIGN_CENTER)
        else:
            prev_next_frame.pack(self.menu.add.button('<', self.get_prev_hard_rank_page),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=pygame_menu.locals.ALIGN_CENTER)
            prev_next_frame.pack(self.menu.add.button('>', self.get_next_hard_rank_page),align=pygame_menu.locals.ALIGN_CENTER)
        self.menu.add.button('back', self.current_rank)
        self.menu.mainloop(self.screen)

    def get_next_hard_rank_page(self):
        self.tens += 1
        self.get_current_hard_rank_page(self.tens)

    def get_prev_hard_rank_page(self):
        self.tens -= 1
        self.get_current_hard_rank_page(self.tens)

    def show_past_easy_rank(self):
        self.get_past_rank('easy')

    def show_past_hard_rank(self):
        self.get_past_rank('hard')

    def get_past_rank(self, mode):
            rank = Rank()
            self.menu.clear()
            self.menu.add.image("./Image/Catus.png", angle=-10, scale=(0.15, 0.15))

            if(mode == 'easy'):
                past_easy_data = rank.load_data('past','easy')
                self.menu.add.label("--Past Easy Rank--",selectable=False,font_size=30)
                id_score_bar = "{:<15s}{:<30s}{:<20s}".format('Rank', 'ID', 'Score')
                self.menu.add.label(id_score_bar,selectable=False, font_size=20)
                for i in range(100):
                    if (i == len(past_easy_data)): break
                    name = str(past_easy_data[i]['ID'])
                    score = '{0:>05s}'.format(str(past_easy_data[i]['score']))
                    r = "{:<15s}{:<30s}{:<20s}".format(str(i+1), name, score)
                    # r= "#{} : ".format(tens*10+i+1) + name + "    " + scor
                    self.menu.add.label(r,selectable=False, font_size=20)

            elif(mode == 'hard'):
                past_hard_data = rank.load_data('past','hard')
                self.menu.add.label("--Past Hard Rank--",selectable=False,font_size=30)
                id_score_bar = "{:<15s}{:<30s}{:<20s}".format('Rank', 'ID', 'Score')
                self.menu.add.label(id_score_bar,selectable=False, font_size=20)
                for i in range(100):
                    if (i == len(past_hard_data)): break
                    name = str(past_hard_data[i]['ID'])
                    score = '{0:>05s}'.format(str(past_hard_data[i]['score']))
                    r = "{:<15s}{:<30s}{:<20s}".format(str(i+1), name, score)
                    # r= "#{} : ".format(tens*10+i+1) + name + "    " + scor
                    self.menu.add.label(r,selectable=False, font_size=20)

            self.menu.add.button('back', self.past_rank)
            self.menu.mainloop(self.screen)
