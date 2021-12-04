
import pygame
import pygame_menu
from data.Defs import *
from data.Rank import *
from pygame_menu.locals import ALIGN_CENTER, ALIGN_LEFT, ALIGN_RIGHT
from pygame_menu.utils import make_surface
from pygame_menu.widgets.core.widget import Widget
from menu.LeaderBoardScrollMenu import *

# 리더보드 관련 메뉴
class LeaderBoardMenu:
    def __init__(self,screen):
        self.size = screen.get_size()
        self.screen = screen
        self.mytheme = pygame_menu.themes.THEME_DEFAULT.copy()
        self.mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
        self.mytheme.title_close_button_cursor = pygame_menu.locals.CURSOR_HAND
        self.mytheme.title_font_color = Color.WHITE.value
        self.menu = pygame_menu.Menu('LeaderBoard', self.size[0], self.size[1],
                            theme=self.mytheme)
        # 페이지화를 위한 변수
        self.tens = 0

    # 메인 메뉴로 돌아가기
    def to_menu(self):
        self.menu.disable()

    # 리더보드 메인 메뉴
    def rank(self):
        self.menu.clear()
        self.menu.add.label("   - RANKING -   ", selectable=False)
        self.menu.add.button('     current ranking     ', self.current_rank)
        self.menu.add.button('     past ranking     ', self.past_rank)
        self.menu.add.button('         back         ', self.to_menu)
        self.menu.mainloop(self.screen,bgfun = self.check_resize)

    # 이번 달 랭킹 메인 메뉴
    def current_rank(self):
        self.menu.clear()
        self.menu.add.label("   - Current Rank -   ", selectable=False)
        self.menu.add.button('     easy mode     ', self.show_current_easy_rank)
        self.menu.add.button('     hard mode     ', self.show_current_hard_rank)
        self.menu.add.button('     rank search     ', self.show_current_rank_search)
        self.menu.add.button('         back         ', self.rank)

    # 저번 달 랭킹 메인 메뉴
    def past_rank(self):
        self.menu.clear()
        self.menu.add.label("   - Past Rank -   ", selectable=False)
        self.menu.add.button('     easy mode     ', self.get_past_easy_rank_from_scroll)
        self.menu.add.button('     hard mode     ', self.get_past_hard_rank_from_scroll)
        self.menu.add.button('         back         ', self.rank)

    # 이번 달 easy 모드 랭킹 보여주기
    def show_current_easy_rank(self):
        self.get_current_rank('easy')

    # 이번 달 hard 모드 랭킹 보여주기
    def show_current_hard_rank(self):
        self.get_current_rank('hard')

    # 데이터 베이스에서 이번 달 랭킹 정보 가져오기
    # mode : 난이도 (easy, hard)
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

    # 페이지화 된 이번 달 easy 모드 랭킹 보여주기
    def get_current_easy_rank_page(self, tens):
        self.menu.clear()
        self.menu.add.label("--Current Easy Rank--",selectable=False,font_size=Menus.fontsize_30.value)
        if(len(easy_data) == 0): # 데이터가 없는 경우
            self.menu.add.vertical_margin(Menus.margin_100.value)
            self.menu.add.label('No Ranking Information.\nRegister ranking for the update.')
            self.menu.add.vertical_margin(Menus.margin_100.value)
        else:   # 데이터가 있는 경우
            self.menu.add.vertical_margin(Menus.margin_40.value)
            table = self.menu.add.table(table_id='my_table', font_size=Menus.fontsize_default.value)
            table.default_cell_padding = Menus.table_padding.value
            table.default_row_background_color = Color.GRAY.value
            table.add_row(['Rank', 'ID', 'Score', 'Date'],
                            cell_font=pygame_menu.font.FONT_OPEN_SANS_BOLD, cell_align=pygame_menu.locals.ALIGN_CENTER, cell_border_color=Color.GRAY.value)
            
            for i in range(10): # 한 페이지에 10개씩 조회 가능
                if(tens*10+i == len(easy_data)): break
                name = str(easy_data[tens*10+i]['ID'])
                score = '{0:>05s}'.format(str(easy_data[tens*10+i]['score']))
                date = str(easy_data[tens*10+i]['date'])
                table.add_row([str(i+1), name, score, date], cell_align=pygame_menu.locals.ALIGN_CENTER, cell_border_color=Color.GRAY.value)
            prev_next_frame = self.menu.add.frame_h(300, 60) # 가로 300, 세로 60의 프레임 생성
            # 페이지 넘김을 위한 버튼 구성
            if(tens == 0):  # 1 페이지 일 때
                prev_next_frame.pack(self.menu.add.label('  '),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add._horizontal_margin(Menus.margin_200.value),align=ALIGN_CENTER)
                if(tens != len(easy_data)//10):  # 1 페이지가 마지막 페이지는 아닐 때
                    prev_next_frame.pack(self.menu.add.button('>', self.get_next_easy_rank_page),align=ALIGN_CENTER)
            elif(tens == len(easy_data)//10): # 마지막 페이지 일 때
                prev_next_frame.pack(self.menu.add.button('<', self.get_prev_easy_rank_page),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add._horizontal_margin(Menus.margin_200.value),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add.label('  '),align=ALIGN_CENTER)
            else:   # 1 페이지도, 마지막 페이지도 아닐 때
                prev_next_frame.pack(self.menu.add.button('<', self.get_prev_easy_rank_page),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add._horizontal_margin(Menus.margin_200.value),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add.button('>', self.get_next_easy_rank_page),align=ALIGN_CENTER)
        self.menu.add.button('back', self.current_rank)
        self.menu.mainloop(self.screen,bgfun = self.check_resize)

    # 이번 달 easy 모드 랭킹에서 다음 페이지 보기
    def get_next_easy_rank_page(self):
        self.tens += 1
        self.get_current_easy_rank_page(self.tens)

    # 이번 달 easy 모드 랭킹에서 이전 페이지 보기
    def get_prev_easy_rank_page(self):
        self.tens -= 1
        self.get_current_easy_rank_page(self.tens)

    # 페이지화 된 이번 달 hard 모드 랭킹 보여주기
    def get_current_hard_rank_page(self, tens):
        self.menu.clear()
        self.menu.add.label("--Current Hard Rank--",selectable=False,font_size=Menus.fontsize_30.value)
        if(len(hard_data) == 0): # 데이터가 없는 경우
            self.menu.add.vertical_margin(Menus.margin_100.value)
            self.menu.add.label('No Ranking Information.\nRegister ranking for the update.')
            self.menu.add.vertical_margin(Menus.margin_100.value)
        else:   # 데이터가 있는 경우
            self.menu.add.vertical_margin(Menus.margin_40.value)
            table = self.menu.add.table(table_id='my_table', font_size=Menus.fontsize_default.value)
            table.default_cell_padding = Menus.table_padding.value
            table.default_row_background_color = Color.GRAY.value
            table.add_row(['Rank', 'ID', 'Score', 'Date'],
                            cell_font=pygame_menu.font.FONT_OPEN_SANS_BOLD, cell_align=pygame_menu.locals.ALIGN_CENTER, cell_border_color=Color.GRAY.value)
          
            for i in range(10): # 한 페이지에 10개씩 조회 가능
                if(tens*10+i == len(hard_data)): break
                name = str(hard_data[tens*10+i]['ID'])
                score = '{0:>05s}'.format(str(hard_data[tens*10+i]['score']))
                date = str(hard_data[tens*10+i]['date'])
                table.add_row([str(i+1), name, score, date], cell_align=pygame_menu.locals.ALIGN_CENTER, cell_border_color=Color.GRAY.value)
            prev_next_frame = self.menu.add.frame_h(300, 60) # 가로 300, 세로 60의 프레임 생성
            # 페이지 넘김을 위한 버튼 구성
            if(tens == 0):   # 1 페이지 일 때
                prev_next_frame.pack(self.menu.add.label('  '),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add._horizontal_margin(Menus.margin_200.value),align=ALIGN_CENTER)
                if(tens != len(hard_data)//10): # 1 페이지가 마지막 페이지는 아닐 때
                    prev_next_frame.pack(self.menu.add.button('>', self.get_next_hard_rank_page),align=ALIGN_CENTER)
            elif(tens == len(hard_data)//10):   # 마지막 페이지 일 때
                prev_next_frame.pack(self.menu.add.button('<', self.get_prev_hard_rank_page),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add._horizontal_margin(Menus.margin_200.value),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add.label('  '),align=ALIGN_CENTER)
            else:   # 1 페이지도, 마지막 페이지도 아닐 때
                prev_next_frame.pack(self.menu.add.button('<', self.get_prev_hard_rank_page),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add._horizontal_margin(Menus.margin_200.value),align=ALIGN_CENTER)
                prev_next_frame.pack(self.menu.add.button('>', self.get_next_hard_rank_page),align=ALIGN_CENTER)
        self.menu.add.button('back', self.current_rank)
        self.menu.mainloop(self.screen,bgfun = self.check_resize)

    # 이번 달 hard 모드 랭킹에서 다음 페이지 보기
    def get_next_hard_rank_page(self):
        self.tens += 1
        self.get_current_hard_rank_page(self.tens)

    # 이번 달 hard 모드 랭킹에서 다음 페이지 보기
    def get_prev_hard_rank_page(self):
        self.tens -= 1
        self.get_current_hard_rank_page(self.tens)

    # 이번 달 랭킹 검색 화면
    def show_current_rank_search(self):
        self.menu.clear()
        self.menu.add.label("--Current Rank Search--",selectable=False,font_size=Menus.fontsize_30.value)
        self.menu.add.vertical_margin(Menus.margin_50.value)
        self.search_frame = self.menu.add.frame_v(600, 250, align=ALIGN_CENTER) # 가로 600, 세로 250의 프레임 생성
        self.search_frame.pack(self.menu.add.label('search your rank', selectable=False, font_size=Menus.fontsize_default.value),align=ALIGN_CENTER)
        # ID 입력
        self.text_input = self.search_frame.pack(self.menu.add.text_input('ID :', maxchar=Menus.ID_maxchar.value, input_underline='_', font_size=Menus.fontsize_default.value),align=ALIGN_CENTER)
        self.search_frame.pack(self.menu.add.vertical_margin(Menus.margin_20.value))
        # 난이도 선택
        difficulty = [('easy', (0)), ('hard', (0))]
        self.selector = self.search_frame.pack(self.menu.add.selector(
            title = 'difficulty:\t',
            items = difficulty,
            font_size = Menus.fontsize_default.value
        ),align = ALIGN_CENTER)
        self.search_frame.pack(self.menu.add.vertical_margin(Menus.margin_20.value))
        self.search_frame.pack(self.menu.add.button('search',self.current_rank_search_result,font_size=Menus.fontsize_default.value), align=ALIGN_CENTER)
        self.search_frame.pack(self.menu.add.button('back', self.current_rank, font_size=Menus.fontsize_default.value), align=ALIGN_CENTER)
        self.result_frame = self.menu.add.frame_v(500, 180, background_color = Color.GRAY.value,align=ALIGN_CENTER) # 가로 500, 세로 180의 프레임 생성
        self.result_frame.pack(self.menu.add.label('----------------------------result----------------------------',selectable=False, font_size=Menus.fontsize_default.value), align=ALIGN_CENTER, margin=Menus.ranking_search_result_margin.value)

    # 검색 결과 프레임
    def get_current_rank_search_result(self, ID):
        rank = Rank()
        self.result_frame = self.menu.add.frame_v(500, 180, background_color = Color.GRAY.value, align=ALIGN_CENTER)
        if(self.selector.get_index() == 0): # easy 모드로 검색한 경우
            rank_result = rank.search_data('current', 'easy', ID)
            if(rank_result == 0):   # 검색 결과가 없는 경우
                self.result_frame.pack(self.menu.add.label('----------------------------result----------------------------',selectable=False, font_size=Menus.fontsize_default.value), align=ALIGN_CENTER, margin=Menus.ranking_search_result_margin.value)
                self.result_frame.pack(self.menu.add.image(Images.icon_caution.value, scale=Scales.default.value), align=ALIGN_CENTER)
                self.result_frame.pack(self.menu.add.label('Rank not found. Please search again.',selectable=False, font_size=Menus.fontsize_default.value), align=ALIGN_CENTER, margin=Menus.ranking_search_result_margin.value)
            else:   # 검색 결과가 있는 경우, 현재 랭킹 알려주기
                self.result_frame.pack(self.menu.add.label('----------------------------result----------------------------',selectable=False, font_size=Menus.fontsize_default.value), align=ALIGN_CENTER, margin=Menus.ranking_search_result_margin.value)
                self.result_frame.pack(self.menu.add.image(Images.icon_award.value, scale=Scales.default.value), align=ALIGN_CENTER)
                self.result_frame.pack(self.menu.add.label('Rank : '+str(rank_result),selectable=False, font_size=Menus.fontsize_default.value), align=ALIGN_CENTER, margin=Menus.ranking_search_result_margin.value)
       
        if(self.selector.get_index() == 1): # hard 모드로 검색한 경우
            rank_result = rank.search_data('current', 'hard', ID)
            if(rank_result == 0):   # 검색 결과가 없는 경우
                self.result_frame.pack(self.menu.add.label('----------------------------result----------------------------',selectable=False, font_size=Menus.fontsize_default.value), align=ALIGN_CENTER, margin=Menus.ranking_search_result_margin.value)
                self.result_frame.pack(self.menu.add.image(Images.icon_caution.value, scale=Scales.default.value), align=ALIGN_CENTER)
                self.result_frame.pack(self.menu.add.label('Rank not found. Please search again.',selectable=False, font_size=Menus.fontsize_default.value), align=ALIGN_CENTER, margin=Menus.ranking_search_result_margin.value)
            else:   # 검색 결과가 있는 경우, 현재 랭킹 알려주기
                self.result_frame.pack(self.menu.add.label('----------------------------result----------------------------',selectable=False, font_size=Menus.fontsize_default.value), align=ALIGN_CENTER, margin=Menus.ranking_search_result_margin.value)
                self.result_frame.pack(self.menu.add.image(Images.icon_award.value, scale=Scales.default.value), align=ALIGN_CENTER)
                self.result_frame.pack(self.menu.add.label('Current Rank : '+str(rank_result),selectable=False, font_size=Menus.fontsize_default.value), align=ALIGN_CENTER, margin=Menus.ranking_search_result_margin.value)

    # 이번 달 랭킹 검색 화면에 검색 결과 프레임 반영
    def current_rank_search_result(self):
        ID = self.text_input.get_value()
        self.menu.remove_widget(self.result_frame)
        self.get_current_rank_search_result(ID)

    # 저번 달 easy 모드 랭킹 조회 화면 불러오기
    def get_past_easy_rank_from_scroll(self):
        ScrollMenu = LeaderBoardScrollMenu(self.screen)
        ScrollMenu.get_past_rank('easy')

    # 저번 달 hard 모드 랭킹 조회 화면 불러오기
    def get_past_hard_rank_from_scroll(self):
        ScrollMenu = LeaderBoardScrollMenu(self.screen)
        ScrollMenu.get_past_rank('hard')

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
