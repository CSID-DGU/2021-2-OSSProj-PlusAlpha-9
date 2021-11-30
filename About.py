
from sys import argv
import pygame
import pygame_menu
from pygame_menu.locals import ALIGN_CENTER
from pygame_menu.widgets.core.widget import Widget
from Rank import *
from LeaderBoardScrollMenu import *
from pygame_menu.utils import make_surface
from Defs import *
import webbrowser

class About:
    def __init__(self,screen):
        self.size = screen.get_size()
        self.screen = screen

        self.menu_image = pygame_menu.baseimage.BaseImage(image_path=Images.about.value,drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
        self.mytheme = pygame_menu.themes.THEME_DEFAULT.copy()
        self.mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
        self.mytheme.title_close_button_cursor = pygame_menu.locals.CURSOR_HAND
        self.mytheme.title_font_color = Color.WHITE.value
        self.authors = []
        self.sources = []
        self.author_is_hidden = False
        self.source_is_hidden = False
        #self.mytheme.background_color = self.menu_image
        
        self.menu = pygame_menu.Menu('About', self.size[0], self.size[1],
                            theme=self.mytheme)

    def to_menu(self):
        self.menu.disable()

    def show(self):
        self.menu.clear()
        self.menu.add.vertical_margin(40)
        self.frame_v = self.menu.add.frame_v(500, 700, margin=(10, 0), max_height=400)

        self.frame_v.pack(self.menu.add.button("   - AUTHORS -   ", selection_effect=None), ALIGN_CENTER)
        for label in Default.about.value["authors"]:
            item = self.frame_v.pack(self.menu.add.label(label, selectable=False, font_size=20), ALIGN_CENTER)
            self.authors.append(item)
        self.frame_v.pack(self.menu.add.vertical_margin(20))
        self.frame_v.pack(self.menu.add.button("   - OPEN SOURCE -   ", selection_effect=None), ALIGN_CENTER)
        for title, val in Default.about.value["open_source"].items():
            label = self.frame_v.pack(self.menu.add.label("< "+title+" >", selectable=False, font_size=22), ALIGN_CENTER)
            self.sources.append(label)
            for key, value in val.items():
                item = self.frame_v.pack(self.menu.add.button(key, self.open_link, value, font_size=20, selection_color=Color.BLUE.value, ), ALIGN_CENTER)
                self.sources.append(item)
            self.frame_v.pack(self.menu.add.vertical_margin(20))
        
        self.menu.add.button('         back         ', self.to_menu)
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
            self.menu._current._widgets_surface = make_surface(0,0)
            self.size = window_size
            print(f'New menu size: {self.menu.get_size()}')

    def open_link(self, url):
        webbrowser.open(url, new=0, autoraise=True)