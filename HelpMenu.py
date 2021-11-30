
import pygame
import pygame_menu
from pygame_menu.locals import ALIGN_CENTER, ALIGN_LEFT, ALIGN_RIGHT
from pygame_menu.widgets.core.widget import Widget
from Rank import *
from LeaderBoardScrollMenu import *
from pygame_menu.utils import make_surface
from Defs import *

class HelpMenu:
    def __init__(self,screen):
        self.size = screen.get_size()
        self.screen = screen

        self.mytheme = pygame_menu.themes.THEME_DEFAULT.copy()
        self.mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
        self.mytheme.title_close_button_cursor = pygame_menu.locals.CURSOR_HAND
        self.mytheme.title_font_color = Color.WHITE.value
        self.mytheme.background_color = Color.WHITE.value
        
        self.menu = pygame_menu.Menu('Help', self.size[0], self.size[1],
                            theme=self.mytheme)
        self.tens = 0

    def to_menu(self):
        self.menu.disable()

    def show(self):
        self.menu.clear()
        self.menu.add.vertical_margin(20)
        self.menu.add.label("   - HELP -   ", selectable=False)
        self.menu.add.button('     infinite game     ', self.infinite_game_1, selection_color=Color.BLACK.value)
        self.menu.add.button('     stage game     ', self.stage_game_1, selection_color=Color.BLACK.value)
        self.menu.add.button('     items     ', self.items, selection_color=Color.BLACK.value)
        self.menu.add.button('     controls     ', self.controls, selection_color=Color.BLACK.value)
        self.menu.add.button('         back         ', self.to_menu, selection_color=Color.BLACK.value)
        self.menu.mainloop(self.screen,bgfun = self.check_resize)

    def infinite_game_1(self):
        self.menu.clear()
        self.menu.add.label("1")
        self.menu.add.vertical_margin(10)
        self.menu.add.image(Images.info_infi_1.value, scale=Scales.small.value)
        self.menu.add.button('     next     ', self.infinite_game_2, selection_color=Color.BLACK.value)
        self.menu.add.button('         back         ', self.to_menu, selection_color=Color.BLACK.value)

    def infinite_game_2(self):
        self.menu.clear()
        self.menu.add.label("2")
        self.menu.add.vertical_margin(10)
        self.menu.add.image(Images.info_infi_2.value, scale=Scales.small.value)
        self.menu.add.button('     next     ', self.infinite_game_3, selection_color=Color.BLACK.value)
        self.menu.add.button('         back         ', self.infinite_game_1, selection_color=Color.BLACK.value)

    def infinite_game_3(self):
        self.menu.clear()
        self.menu.add.label("3")
        self.menu.add.vertical_margin(10)
        self.menu.add.image(Images.info_infi_3.value, scale=Scales.small.value)
        self.menu.add.button('     next     ', self.infinite_game_4, selection_color=Color.BLACK.value)
        self.menu.add.button('         back         ', self.infinite_game_2, selection_color=Color.BLACK.value)

    def infinite_game_4(self):
        self.menu.clear()
        self.menu.add.label("4")
        self.menu.add.vertical_margin(10)
        self.menu.add.image(Images.info_infi_4.value, scale=Scales.small.value)
        self.menu.add.button('     next     ', self.infinite_game_5, selection_color=Color.BLACK.value)
        self.menu.add.button('         back         ', self.infinite_game_3, selection_color=Color.BLACK.value)

    def infinite_game_5(self):
        self.menu.clear()
        self.menu.add.label("5")
        self.menu.add.vertical_margin(10)
        self.menu.add.image(Images.info_infi_5.value, scale=Scales.small.value)
        self.menu.add.button('     quit     ', self.show, selection_color=Color.BLACK.value)
        self.menu.add.button('         back         ', self.infinite_game_4, selection_color=Color.BLACK.value)

    def stage_game_1(self):
        self.menu.clear()
        self.menu.add.label("1")
        self.menu.add.vertical_margin(10)
        self.menu.add.image(Images.info_stage_1.value, scale=Scales.small.value)
        self.menu.add.button('     next     ', self.stage_game_2, selection_color=Color.BLACK.value)
        self.menu.add.button('         back         ', self.to_menu, selection_color=Color.BLACK.value)

    def stage_game_2(self):
        self.menu.clear()
        self.menu.add.label("2")
        self.menu.add.vertical_margin(10)
        self.menu.add.image(Images.info_stage_2.value, scale=Scales.small.value)
        self.menu.add.button('     next     ', self.stage_game_3, selection_color=Color.BLACK.value)
        self.menu.add.button('         back         ', self.stage_game_1, selection_color=Color.BLACK.value)

    def stage_game_3(self):
        self.menu.clear()
        self.menu.add.label("3")
        self.menu.add.vertical_margin(10)
        self.menu.add.image(Images.info_stage_3.value, scale=Scales.small.value)
        self.menu.add.button('     next     ', self.stage_game_4, selection_color=Color.BLACK.value)
        self.menu.add.button('         back         ', self.stage_game_2, selection_color=Color.BLACK.value)

    def stage_game_4(self):
        self.menu.clear()
        self.menu.add.label("4")
        self.menu.add.vertical_margin(10)
        self.menu.add.image(Images.info_stage_4.value, scale=Scales.small.value)
        self.menu.add.button('     next     ', self.stage_game_5, selection_color=Color.BLACK.value)
        self.menu.add.button('         back         ', self.stage_game_3, selection_color=Color.BLACK.value)

    def stage_game_5(self):
        self.menu.clear()
        self.menu.add.label("5")
        self.menu.add.vertical_margin(10)
        self.menu.add.image(Images.info_stage_5.value, scale=Scales.small.value)
        self.menu.add.button('     next     ', self.stage_game_6, selection_color=Color.BLACK.value)
        self.menu.add.button('         back         ', self.stage_game_4, selection_color=Color.BLACK.value)

    def stage_game_6(self):
        self.menu.clear()
        self.menu.add.label("6")
        self.menu.add.vertical_margin(10)
        self.menu.add.image(Images.info_stage_6.value, scale=Scales.small.value)
        self.menu.add.button('     quit     ', self.show, selection_color=Color.BLACK.value)
        self.menu.add.button('         back         ', self.stage_game_5, selection_color=Color.BLACK.value)

    def items(self):
        self.menu.clear()
        self.menu.add.image(Images.info_items.value, scale=Scales.tiny.value)
        self.menu.add.button('         back         ', self.show, selection_color=Color.BLACK.value)

    def controls(self):
        self.menu.clear()
        self.menu.add.image(Images.info_controls.value, scale=Scales.tiny.value)
        self.menu.add.button('         back         ', self.show, selection_color=Color.BLACK.value)

   
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