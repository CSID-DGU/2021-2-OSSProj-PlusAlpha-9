
import pygame
import pygame_menu
from pygame_menu.locals import ALIGN_CENTER, ALIGN_LEFT, ALIGN_RIGHT
from pygame_menu.widgets.core.widget import Widget
from Rank import *
from LeaderBoardScrollMenu import *

class LeaderBoardMenu:
    def __init__(self,screen):
        self.size = screen.get_size()
        self.screen = screen

        self.menu_image = pygame_menu.baseimage.BaseImage(image_path='./Image/RankPage_v2.jpg',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
        self.mytheme = pygame_menu.themes.THEME_SOLARIZED.copy()
        self.mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        self.mytheme.title_close_button_cursor = pygame_menu.locals.CURSOR_HAND
        self.mytheme.title_font_color = (255, 255, 255)
        self.mytheme.background_color = self.menu_image
        
        self.menu = pygame_menu.Menu('', self.size[0], self.size[1],
                            theme=self.mytheme)
        self.tens = 0

    def to_menu(self):
        self.menu.disable()

    def rank(self):
        self.menu.clear()
        self.menu.add.vertical_margin(80)
        self.menu.add.label("   - RANKING -   ", selectable=False)
        self.menu.add.button('     current ranking     ', self.current_rank)
        self.menu.add.button('     past ranking     ', self.past_rank)
        self.menu.add.button('         back         ', self.to_menu)
        #self.menu.mainloop(self.screen)
        self.menu.mainloop(self.screen,bgfun = self.check_resize)

    def current_rank(self):
        self.menu.clear()
        self.menu.add.vertical_margin(80)
        self.menu.add.label("   - Current Rank -   ", selectable=False)
        self.menu.add.button('     easy mode     ', self.show_current_easy_rank)
        self.menu.add.button('     hard mode     ', self.show_current_hard_rank)
        self.menu.add.button('     rank search     ', self.show_current_rank_search)
        self.menu.add.button('         back         ', self.rank)

    def past_rank(self):
        self.menu.clear()
        self.menu.add.vertical_margin(80)
        self.menu.add.label("   - Past Rank -   ", selectable=False)
        self.menu.add.button('     easy mode     ', self.get_past_easy_rank_from_scroll)
        self.menu.add.button('     hard mode     ', self.get_past_hard_rank_from_scroll)
        self.menu.add.button('         back         ', self.rank)

    def show_current_easy_rank(self):
        self.get_current_rank('easy')

    def show_current_hard_rank(self):
        self.get_current_rank('hard')

    def get_current_rank(self, mode):
            rank = Rank()
            self.menu.clear()
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
        self.menu.add.vertical_margin(100)
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
        #self.menu.mainloop(self.screen)
        self.menu.mainloop(self.screen,bgfun = self.check_resize)

    def get_next_easy_rank_page(self):
        self.tens += 1
        self.get_current_easy_rank_page(self.tens)

    def get_prev_easy_rank_page(self):
        self.tens -= 1
        self.get_current_easy_rank_page(self.tens)

    def get_current_hard_rank_page(self, tens):
        self.menu.clear()
        self.menu.add.vertical_margin(100)
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
        #self.menu.mainloop(self.screen)
        self.menu.mainloop(self.screen,bgfun = self.check_resize)

    def get_next_hard_rank_page(self):
        self.tens += 1
        self.get_current_hard_rank_page(self.tens)

    def get_prev_hard_rank_page(self):
        self.tens -= 1
        self.get_current_hard_rank_page(self.tens)

    def show_current_rank_search(self):
        self.menu.clear()
        self.menu.add.vertical_margin(100)
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
        self.result_frame = self.menu.add.frame_v(500, 180, background_color = (254,254,237),align=ALIGN_CENTER)
        self.result_frame.pack(self.menu.add.label('----------------------result-------------------------',selectable=False, font_size=25), align=ALIGN_CENTER, margin=(0,20))

    def get_current_rank_search_result(self, ID):
        rank = Rank()
        self.result_frame = self.menu.add.frame_v(500, 180, background_color = (254,254,237), align=ALIGN_CENTER)
        if(self.selector.get_index() == 0):
            rank_result = rank.search_data('current', 'easy', ID)
            if(rank_result == 0):
                self.result_frame.pack(self.menu.add.label('----------------------result-------------------------',selectable=False, font_size=25), align=ALIGN_CENTER, margin=(0,20))
                self.result_frame.pack(self.menu.add.label('Rank not found. Please search again.',selectable=False, font_size=25), align=ALIGN_CENTER, margin=(0,20))
            else:
                self.result_frame.pack(self.menu.add.label('----------------------result-------------------------',selectable=False, font_size=25), align=ALIGN_CENTER, margin=(0,20))
                self.result_frame.pack(self.menu.add.label('Rank : '+str(rank_result),selectable=False, font_size=25), align=ALIGN_CENTER, margin=(0,20))
        if(self.selector.get_index() == 1):
            rank_result = rank.search_data('current', 'hard', ID)
            if(rank_result == 0):
                self.result_frame.pack(self.menu.add.label('----------------------result-------------------------',selectable=False, font_size=25), align=ALIGN_CENTER, margin=(0,20))
                self.result_frame.pack(self.menu.add.label('Rank not found. Please search again.',selectable=False, font_size=25), align=ALIGN_CENTER, margin=(0,20))
            else:
                self.result_frame.pack(self.menu.add.label('----------------------result-------------------------',selectable=False, font_size=25), align=ALIGN_CENTER, margin=(0,20))
                self.result_frame.pack(self.menu.add.label('Current Rank : '+str(rank_result),selectable=False, font_size=25), align=ALIGN_CENTER, margin=(0,20))

    def current_rank_search_result(self):
        ID = self.text_input.get_value()
        self.menu.remove_widget(self.result_frame)
        self.get_current_rank_search_result(ID)

    def get_past_easy_rank_from_scroll(self):
        ScrollMenu = LeaderBoardScrollMenu(self.screen)
        ScrollMenu.get_past_rank('easy')

    def get_past_hard_rank_from_scroll(self):
        ScrollMenu = LeaderBoardScrollMenu(self.screen)
        ScrollMenu.get_past_rank('hard')

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