import pygame
import pygame_menu
from pygame_menu.menu import Menu
from data.Defs import *
from data.Rank import *
from pygame_menu.locals import ALIGN_CENTER, ALIGN_LEFT, ALIGN_RIGHT
from pygame_menu.utils import make_surface
from pygame_menu.widgets.core.widget import Widget

# 스크롤 방식으로 구현된 저번 달 랭킹 메뉴
class LeaderBoardScrollMenu:
    def __init__(self,screen):
        self.size = screen.get_size()
        self.screen = screen

    # 이전 메뉴로 돌아가기
    def to_menu(self):
        self.menu.disable()

    # 지난 달 랭킹 화면
    def get_past_rank(self, mode):
            rank = Rank()
            # easy 모드로 조회한 경우
            if(mode == 'easy'):
                easy_scroll_theme = pygame_menu.themes.THEME_DEFAULT.copy()
                easy_scroll_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
                easy_scroll_theme.title_close_button_cursor = pygame_menu.locals.CURSOR_HAND
                easy_scroll_theme.title_font_color = Color.WHITE.value
                self.menu = pygame_menu.Menu('', self.size[0], self.size[1],
                                    theme=easy_scroll_theme)
                self.menu.clear()
                past_easy_data = rank.load_data('past','easy')
                self.menu.add.label("--Past Easy Rank--",selectable=False,font_size=Menus.fontsize_30.value)
                table = self.menu.add.table(table_id='my_table', font_size=Menus.fontsize_default.value)
                table.default_cell_padding = Menus.table_padding.value
                table.default_row_background_color = Color.GRAY.value
                
                if(len(past_easy_data) == 0): # 데이터가 없는 경우
                    self.menu.add.vertical_margin(Menus.margin_100.value)
                    self.menu.add.label('No Ranking Information.')
                    self.menu.add.vertical_margin(Menus.margin_100.value)
                else: # 데이터가 있는 경우, 100위 까지 테이블에 데이터 추가
                    table.add_row(['Rank', 'ID', 'Score', 'Date'],
                            cell_font=pygame_menu.font.FONT_OPEN_SANS_BOLD, cell_align=pygame_menu.locals.ALIGN_CENTER, cell_border_color=Color.GRAY.value)
                    for i in range(100):
                        if (i == len(past_easy_data)): break
                        name = str(past_easy_data[i]['ID'])
                        score = '{0:>05s}'.format(str(past_easy_data[i]['score']))
                        date = str(past_easy_data[i]['date'])
                        table.add_row([str(i+1), name, score, date], cell_align=pygame_menu.locals.ALIGN_CENTER, cell_border_color=Color.GRAY.value)

            # hard 모드로 조회한 경우
            elif(mode == 'hard'):
                hard_scroll_theme = pygame_menu.themes.THEME_DEFAULT.copy()
                hard_scroll_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
                hard_scroll_theme.title_close_button_cursor = pygame_menu.locals.CURSOR_HAND
                hard_scroll_theme.title_font_color = Color.WHITE.value
                self.menu = pygame_menu.Menu('', self.size[0], self.size[1],
                                    theme=hard_scroll_theme)
                self.menu.clear()
                past_hard_data = rank.load_data('past','hard')
                self.menu.add.label("--Past Hard Rank--",selectable=False,font_size=Menus.fontsize_30.value)
                table = self.menu.add.table(table_id='my_table_2', font_size=Menus.fontsize_default.value)
                table.default_cell_padding = Menus.table_padding.value
                table.default_row_background_color = Color.GRAY.value
                
                if(len(past_hard_data) == 0): # 데이터가 없는 경우
                    self.menu.add.vertical_margin(Menus.margin_100.value)
                    self.menu.add.label('No Ranking Information.')
                    self.menu.add.vertical_margin(Menus.margin_100.value)
                else:   # 데이터가 있는 경우, 100위 까지 테이블에 데이터 추가
                    table.add_row(['Rank', 'ID', 'Score', 'Date'],
                            cell_font=pygame_menu.font.FONT_OPEN_SANS_BOLD, cell_align=pygame_menu.locals.ALIGN_CENTER, cell_border_color=Color.GRAY.value)
                    for i in range(100):
                        if (i == len(past_hard_data)): break
                        name = str(past_hard_data[i]['ID'])
                        score = '{0:>05s}'.format(str(past_hard_data[i]['score']))
                        date = str(past_hard_data[i]['date'])
                        table.add_row([str(i+1), name, score, date], cell_align=pygame_menu.locals.ALIGN_CENTER, cell_border_color=Color.GRAY.value)

            self.menu.add.button('back', self.to_menu)
            self.menu.mainloop(self.screen,bgfun = self.check_resize)

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
            self.menu._current._widgets_surface = make_surface(0,0)
            self.size = window_size
            print(f'New menu size: {self.menu.get_size()}')
