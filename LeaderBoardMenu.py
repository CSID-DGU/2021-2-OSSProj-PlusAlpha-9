
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

    def show_current_easy_rank(self):
        self.get_current_rank('easy')

    def show_current_hard_rank(self):
        self.get_current_rank('hard')

    def get_current_rank(self, mode):
            rank = Rank()
            self.menu.clear()
            self.menu.add.image("./Image/Catus.png", angle=-10, scale=(0.15, 0.15))

            if(mode == 'easy'):
                self.menu.add.label("--Current Easy Rank--",selectable=False,font_size=30)
                self.menu.add.label("ID      Score",selectable=False, font_size=20)
                easy_data = rank.load_data("easy")
                for i in range(len(easy_data)):
                        easy_name = str(easy_data[i]['ID'])
                        easy_score = '{0:>05s}'.format(str(easy_data[i]['score']))
                        r= "#{} : ".format(i+1) + easy_name + "    " + easy_score
                        self.menu.add.label(r,selectable=False, font_size=40)
                self.menu.add.button('back', self.current_rank)
                self.menu.mainloop(self.screen)

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