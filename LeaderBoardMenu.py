
import pygame
import pygame_menu
from pygame_menu.locals import ALIGN_CENTER, ALIGN_LEFT, ALIGN_RIGHT
from pygame_menu.widgets.core.widget import Widget


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
        self.menu.add.button('     rank search     ', self.show_current_rank_search)
        self.menu.add.button('         back         ', self.rank)
        self.menu.draw(self.screen)

    def past_rank(self):
        self.menu.clear()
        self.menu.add.label("   - Past Rank -   ", selectable=False)
        self.menu.add.button('     easy mode     ', self.show_past_easy_rank)
        self.menu.add.button('     hard mode     ', self.show_past_hard_rank)
        self.menu.add.button('         back         ', self.rank)

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
        if(len(easy_data) == 0):
            self.menu.add.vertical_margin(100)
            self.menu.add.label('No Ranking Information.')
            self.menu.add.vertical_margin(100)
        else:
            id_score_bar = "{:^7s}   {:^25s}   {:^5s}        {:^10s}".format('Rank', 'ID', 'Score', 'Date')
            self.menu.add.label(id_score_bar,selectable=False, font_size=20)
            for i in range(10):
                if(tens*10+i == len(easy_data)): break
                name = str(easy_data[tens*10+i]['ID'])
                score = '{0:>05s}'.format(str(easy_data[tens*10+i]['score']))
                date = str(easy_data[tens*10+i]['date'])
                # r = "{:^15s}{:^30s}{:^20s}{:^20s}".format(str(tens*10+i+1), name, score, date)
                r = "{:^7s}   {:^25s}   {:^5s}       {:^10s}".format(str(tens*10+i+1), name, score, date)
                self.menu.add.label(r,selectable=False, font_size=20)
            prev_next_frame = self.menu.add.frame_h(250, 60)
            if(tens == 0):
                prev_next_frame.pack(self.menu.add.label('  '),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add.button('>', self.get_next_easy_rank_page),align=ALIGN_CENTER)
            elif(tens == len(easy_data)//10):
                prev_next_frame.pack(self.menu.add.button('<', self.get_prev_easy_rank_page),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add.label('  '),align=ALIGN_CENTER)
            else:
                prev_next_frame.pack(self.menu.add.button('<', self.get_prev_easy_rank_page),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add.button('>', self.get_next_easy_rank_page),align=ALIGN_CENTER)
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
        if(len(hard_data) == 0):
            self.menu.add.vertical_margin(100)
            self.menu.add.label('No Ranking Information.')
            self.menu.add.vertical_margin(100)
        else:
            id_score_bar = "{:^7s}   {:^25s}   {:^5s}       {:^10s}".format('Rank', 'ID', 'Score', 'Date')
            self.menu.add.label(id_score_bar,selectable=False, font_size=20)
            for i in range(10):
                if(tens*10+i == len(hard_data)): break
                name = str(hard_data[tens*10+i]['ID'])
                score = '{0:>05s}'.format(str(hard_data[tens*10+i]['score']))
                date = str(hard_data[tens*10+i]['date'])
                r = "{:^7s}   {:^25s}   {:^5s}       {:^10s}".format(str(tens*10+i+1), name, score, date)
                self.menu.add.label(r,selectable=False, font_size=20)
            prev_next_frame = self.menu.add.frame_h(250, 60)
            if(tens == 0):
                prev_next_frame.pack(self.menu.add.label('  '),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add.button('>', self.get_next_hard_rank_page),align=ALIGN_CENTER)
            elif(tens == len(hard_data)//10):
                prev_next_frame.pack(self.menu.add.button('<', self.get_prev_hard_rank_page),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add.label('  '),align=ALIGN_CENTER)
            else:
                prev_next_frame.pack(self.menu.add.button('<', self.get_prev_hard_rank_page),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add._horizontal_margin(150),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add.button('>', self.get_next_hard_rank_page),align=ALIGN_CENTER)
        self.menu.add.button('back', self.current_rank)
        self.menu.mainloop(self.screen)

    def get_next_hard_rank_page(self):
        self.tens += 1
        self.get_current_hard_rank_page(self.tens)

    def get_prev_hard_rank_page(self):
        self.tens -= 1
        self.get_current_hard_rank_page(self.tens)

    def show_current_rank_search(self):
        self.menu.clear()
        self.menu.add.label("--Current Rank Search--",selectable=False,font_size=30)
        self.search_frame = self.menu.add.frame_v(600, 300, align=ALIGN_CENTER)
        self.search_frame.pack(self.menu.add.label('search your rank', selectable=False, font_size=20),align=ALIGN_CENTER)
        self.text_input = self.search_frame.pack(self.menu.add.text_input('ID :', maxchar=20, input_underline='_', font_size=20),align=ALIGN_CENTER)
        self.search_frame.pack(self.menu.add.vertical_margin(20))
        difficulty = [('easy', (0)), ('hard', (0))]
        self.selector = self.search_frame.pack(self.menu.add.selector(
            title = 'difficulty:\t',
            items = difficulty,
            font_size = 20
        ),align = ALIGN_CENTER)
        self.search_frame.pack(self.menu.add.vertical_margin(40))
        self.search_frame.pack(self.menu.add.button('search',self.current_rank_search_result,font_size=20), align=ALIGN_CENTER)
        self.search_frame.pack(self.menu.add.button('back', self.current_rank, font_size=20), align=ALIGN_CENTER)
        self.result_frame = self.menu.add.frame_v(500, 100, background_color = (255,255,255),align=ALIGN_CENTER)

    def get_current_rank_search_result(self, ID):
        rank = Rank()
        self.result_frame = self.menu.add.frame_v(500, 100, background_color = (255,255,255), align=ALIGN_CENTER)
        if(self.selector.get_index() == 0):
            rank_result = rank.search_data('current', 'easy', ID)
            if(rank_result == 0):
                self.result_frame.pack(self.menu.add.label('Rank not found. Please search again.',selectable=False, font_size=25), align=ALIGN_CENTER, margin=(0,20))
            else:
                self.result_frame.pack(self.menu.add.label('Rank : '+str(rank_result),selectable=False, font_size=25), align=ALIGN_CENTER, margin=(0,20))
        if(self.selector.get_index() == 1):
            rank_result = rank.search_data('current', 'hard', ID)
            if(rank_result == 0):
                self.result_frame.pack(self.menu.add.label('Rank not found. Please search again.',selectable=False, font_size=25), align=ALIGN_CENTER, margin=(0,20))
            else:
                self.result_frame.pack(self.menu.add.label('Current Rank : '+str(rank_result),selectable=False, font_size=25), align=ALIGN_CENTER, margin=(0,20))

    def current_rank_search_result(self):
        ID = self.text_input.get_value()
        self.menu.remove_widget(self.result_frame)
        self.get_current_rank_search_result(ID)

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
                if(len(past_easy_data) == 0):
                    self.menu.add.vertical_margin(100)
                    self.menu.add.label('No Ranking Information.')
                    self.menu.add.vertical_margin(100)
                else:
                    id_score_bar = "{:^7s}   {:^25s}   {:^5s}       {:^10s}".format('Rank', 'ID', 'Score', 'Date')
                    self.menu.add.label(id_score_bar,selectable=False, font_size=20)
                    for i in range(100):
                        if (i == len(past_easy_data)): break
                        name = str(past_easy_data[i]['ID'])
                        score = '{0:>05s}'.format(str(past_easy_data[i]['score']))
                        date = str(past_easy_data[i]['date'])
                        r = "{:^7s}   {:^25s}   {:^5s}       {:^10s}".format(str(i+1), name, score, date)
                        self.menu.add.label(r,selectable=False, font_size=20)

            elif(mode == 'hard'):
                past_hard_data = rank.load_data('past','hard')
                self.menu.add.label("--Past Hard Rank--",selectable=False,font_size=30)
                if(len(past_hard_data) == 0):
                    self.menu.add.vertical_margin(100)
                    self.menu.add.label('No Ranking Information.')
                    self.menu.add.vertical_margin(100)
                else:
                    id_score_bar = "{:^7s}   {:^25s}   {:^5s}       {:^10s}".format('Rank', 'ID', 'Score', 'Date')
                    self.menu.add.label(id_score_bar,selectable=False, font_size=20)
                    for i in range(100):
                        if (i == len(past_hard_data)): break
                        name = str(past_hard_data[i]['ID'])
                        score = '{0:>05s}'.format(str(past_hard_data[i]['score']))
                        date = str(past_hard_data[i]['date'])
                        r = "{:^7s}   {:^25s}   {:^5s}       {:^10s}".format(str(i+1), name, score, date)
                        self.menu.add.label(r,selectable=False, font_size=20)

            self.menu.add.button('back', self.past_rank)
            self.menu.mainloop(self.screen)
