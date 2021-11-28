import pygame
import pygame_menu
from pygame_menu.locals import ALIGN_CENTER, ALIGN_LEFT, ALIGN_RIGHT
from pygame_menu.widgets.core.widget import Widget
from Rank import *


class LeaderBoardScrollMenu:
    def __init__(self,screen):
        
        self.size = screen.get_size()
        self.screen = screen

    def to_menu(self):
        self.menu.disable()

    def get_past_rank(self, mode):
            rank = Rank()

            if(mode == 'easy'):
                easy_scroll_image = pygame_menu.baseimage.BaseImage(image_path='./Image/RankPage_scroll_easy_v1.jpg',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
                easy_scroll_theme = pygame_menu.themes.THEME_SOLARIZED.copy()
                easy_scroll_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
                easy_scroll_theme.title_close_button_cursor = pygame_menu.locals.CURSOR_HAND
                easy_scroll_theme.title_font_color = (255, 255, 255)
                easy_scroll_theme.background_color = easy_scroll_image
                self.menu = pygame_menu.Menu('', self.size[0], self.size[1],
                                    theme=easy_scroll_theme)
                self.menu.clear()
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
                hard_scroll_image = pygame_menu.baseimage.BaseImage(image_path='./Image/RankPage_scroll_hard_v1.jpg',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
                hard_scroll_theme = pygame_menu.themes.THEME_SOLARIZED.copy()
                hard_scroll_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
                hard_scroll_theme.title_close_button_cursor = pygame_menu.locals.CURSOR_HAND
                hard_scroll_theme.title_font_color = (255, 255, 255)
                hard_scroll_theme.background_color = hard_scroll_image
                self.menu = pygame_menu.Menu('', self.size[0], self.size[1],
                                    theme=hard_scroll_theme)
                self.menu.clear()
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

            self.menu.add.button('back', self.to_menu)
            #self.menu.mainloop(self.screen)
            self.menu.mainloop(self.screen,bgfun = self.check_resize)

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