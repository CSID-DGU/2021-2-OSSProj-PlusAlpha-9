# Character : 이동속도, 투사체 속도, 크기, 이미지, 투사체 사운드
# stage : 목표점수, 배경이미지, 배경 사운드

# 게임 : 목숨, 시간
# 로직 : 세이브파일 변경 후 저장 필요

import time
from typing import Sized
import pygame
import random
import pygame_menu
import json
from collections import OrderedDict
from Character import Character
from Item import Item
from Boss import Boss
from Mob import Mob
from Bullet import Bullet
from Defs import *
from StageDataManager import *

class InfiniteGame:

    def __init__(self,character):
        # 1. 게임초기화 
        pygame.init()

        # 2. 게임창 옵션 설정
        infoObject = pygame.display.Info()
        title = "Infinite game"
        pygame.display.set_caption(title) # 창의 제목 표시줄 옵션
        self.size = [infoObject.current_w,infoObject.current_h]
        self.screen = pygame.display.set_mode(self.size,pygame.RESIZABLE)
        
        # 3. 게임 내 필요한 설정
        self.clock = pygame.time.Clock() # 이걸로 FPS설정함

        # 4. 게임에 필요한 객체들을 담을 배열 생성, 변수 초기화
        self.mobList = []
        self.item_list = []
        self.missileList = []
        self.character = character
        self.score = 0
        self.life = 3
        self.start_time = time.time()
        self.mob_gen_rate = 0.01
        self.item_gen_rate = 0.004
        self.mob_image = "./Image/Catus.png"
        self.background_image = "./Image/Antarctic_modified_v1.jpg"
        self.background_music = "./Sound/Rien.mp3"
        self.SB = 0

        # 4-1. 보스 스테이지를 위한 변수 초기화
        # self.isBossStage = stage.isBossStage
        # self.boss = Boss(self.size,stage.boss_image,stage.boss_bullet_image)
        self.enemyBullets =[]

        # 5. 캐릭터 위치 초기화
        self.character.set_XY((self.size[0]/2-character.sx/2,self.size[1]-character.sy))

    def main(self):
        # 메인 이벤트
        pygame.mixer.init()
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        background1_y = 0 # 배경 움직임을 위한 변수
        while self.SB==0:
            #fps 제한을 위해 한 loop에 한번 반드시 호출해야합니다.
            self.clock.tick(30)
            
            #화면 흰색으로 채우기
            self.screen.fill((255,255,255))
            # 배경 크기 변경 처리 및 그리기
            # 창크기가 바뀜에 따라 배경화면 크기 변경 필요
            background1 =  pygame.image.load(self.background_image)
            background1 = pygame.transform.scale(background1, self.size)
            background_width = background1.get_width()
            background_height = background1.get_height()
            background2 = background1.copy()
            background1_y += 2
            if background1_y > background_height:
                background1_y = 0
            self.screen.blit(background1, (0, background1_y))
            self.screen.blit(background2, (0, 0), pygame.Rect(0,background_height - background1_y,background_width,background1_y))



            # 입력 처리
            for event in pygame.event.get(): #동작을 했을때 행동을 받아오게됨
                if event.type ==pygame.QUIT:
                    self.SB=1 # SB 가 1이되면 while 문을 벗어나오게 됨
                if event.type == pygame.KEYDOWN: # 어떤 키를 눌렀을때!(키보드가 눌렸을 때)
                    '''
                    각 키가 눌러지면 플레이어 캐릭터 객체의 값 수정 (현재는 종료를 위해 왼쪽키를 종료로 둠)
                    '''
                    if event.key == pygame.K_x:
                        self.SB=1
                    if event.key == pygame.K_z: #테스트용
                        self.score += 30
                elif event.type == pygame.KEYUP: # 키를 뗐을때
                    if event.key == pygame.K_LEFT:
                        pass

            #몹을 확률적으로 발생시키기
            if(random.random()<self.mob_gen_rate):
                newMob = Mob(self.mob_image,(50,50),2,0)
                newMob.set_XY((random.randrange(0,self.size[0]),0))
                self.mobList.append(newMob)
                
            if(random.random()<self.item_gen_rate):
                new_item = Item(Images.item_powerup.value,(20,20),5)
                new_item.set_XY((random.randrange(0,self.size[0]-new_item.sx),0))
                self.item_list.append(new_item)

            #플레이어 객체 이동
            self.character.update()

            #몹 객체 이동
            for mob in self.mobList:
                mob.move(self.size,self)

            for item in self.item_list:
                item.move()

            #보스 이동
            #보스 업데이트

            # if(self.isBossStage):
            #     self.boss.draw(self.screen)
            #     self.boss.update(self.enemyBullets,self.character,self.size)
            #     self.boss.check(self.character,self)

            #     # 보스와 플레이어 충돌 감지
            #     if(self.check_crash(self.boss,self.character)):
            #         self.life -= 1

            #     #보스의 총알과 플레이어 충돌 감지
            #     for bullet in self.enemyBullets:
            #         if(bullet.check_crash(self.character)):
            #             self.life -=1
            #             self.enemyBullets.remove(bullet)

        
            #적 투사체 이동
            for bullet in self.enemyBullets:
                bullet.move(self.size,self)
                bullet.show(self.screen)

            for item in list(self.item_list):
                if(self.check_crash(self.character,item)):
                    item.use(self.character)
                    self.item_list.remove(item)

            #발사체와 몹 충돌 감지
            for missile in list(self.character.get_missiles_fired()):
                for mob in list(self.mobList):
                    if self.check_crash(missile,mob):
                        self.score += 10
                        self.character.missiles_fired.remove(missile)
                        self.mobList.remove(mob)

            #몹과 플레이어 충돌 감지
            for mob in list(self.mobList):
                if(self.check_crash(mob,self.character)):
                    if self.character.is_collidable == True:
                        self.character.last_crashed = time.time()
                        self.character.is_collidable = False
                        print("crash!")
                        self.life -= 1
                        self.mobList.remove(mob)
                   
            #화면 그리기
            #플레이어 그리기
            self.character.show(self.screen)
            
            #몹 그리기
            for mob in self.mobList:
                mob.show(self.screen)

            for item in self.item_list:
                item.show(self.screen)

            for i in self.character.get_missiles_fired():
                i.show(self.screen)
            
            #점수와 목숨 표시
            font = pygame.font.Font(Fonts.font_default.value, sum(self.size)//85)
            score_life_text = font.render("Score : {} Life: {}".format(self.score,self.life), True, (255,255,0)) # 폰트가지고 랜더링 하는데 표시할 내용, True는 글자가 잘 안깨지게 하는 거임 걍 켜두기, 글자의 색깔
            self.screen.blit(score_life_text,(10,5)) # 이미지화 한 텍스트라 이미지를 보여준다고 생각하면 됨 
            
            # 현재 흘러간 시간
            play_time = (time.time() - self.start_time)
            time_text = font.render("Time : {:.2f}".format(play_time), True, (255,255,0))
            self.screen.blit(time_text,(300,5))

            # 화면갱신
            pygame.display.flip() # 그려왔던데 화면에 업데이트가 됨


            #목숨이 0 이하면 랭킹 등록 화면
            if(self.life<1):
                self.show_ranking_register_screen()
                return

            self.update_difficulty()


        # While 빠져나오면 랭킹등록 스크린 실행
        self.show_ranking_register_screen()

    #충돌 감지 함수
    def check_crash(self,o1,o2):
        o1_mask = pygame.mask.from_surface(o1.img)
        o2_mask = pygame.mask.from_surface(o2.img)

        offset = (int(o2.x - o1.x), int(o2.y - o1.y))
        collision = o1_mask.overlap(o2_mask, offset)
        
        if collision:
            return True
        else:
            return False

    #시간 흐름에 따라 난이도 상승 (몹 생성 확률 증가)
    def update_difficulty(self):
        play_time = (time.time() - self.start_time) #게임 진행 시간


    def to_menu(self,menu):
        menu.disable()

    #랭킹 등록 화면
    def show_ranking_register_screen(self):
        menu = pygame_menu.Menu('Game Over!!', self.size[0]*0.7, self.size[1]*0.8,
                            theme=pygame_menu.themes.THEME_BLUE)
        text_input = menu.add.text_input('Name: ', default='ABC')
        menu.add.label("")
        menu.add.button('Register Ranking', self.register_ranking,text_input.get_value,self.score)
        menu.add.button('to Menu', self.to_menu,menu)
        menu.mainloop(self.screen)
        
    #랭킹 서버에 등록
    def register_ranking(self,name,score):
        print(name)
        print(score)

    
