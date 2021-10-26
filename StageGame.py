# Character : 이동속도, 투사체 속도, 크기, 이미지, 투사체 사운드
# stage : 목표점수, 배경이미지, 배경 사운드

# 게임 : 목숨, 시간
# 로직 : 세이브파일 변경 후 저장 필요

import time
import pygame
class StageGame:

    def __init__(self,character,stage):
        # 1. 게임초기화 
        pygame.init()

        # 2. 게임창 옵션 설정
        infoObject = pygame.display.Info()
        title = "My game"
        pygame.display.set_caption(title) # 창의 제목 표시줄 옵션
        self.size = [infoObject.current_w,infoObject.current_h]
        self.screen = pygame.display.set_mode(self.size,pygame.RESIZABLE)
        
        # 3. 게임 내 필요한 설정
        self.clock = pygame.time.Clock() # 이걸로 FPS설정함
        self.black=(0,0,0) # RGB임
        self.white=(255,255,255)

        # 4. 게임에 필요한 객체들을 담을 배열 생성, 변수 초기화
        self.mob_list = []
        self.missile_list = []
        self.character = character
        self.stage = stage
        self.score = 0
        self.life = 3
        self.start_time = time.time()
        self.mob_gen_rate = 0.1
        self.k=0
        self.SB = 0

    def main(self):
        # 메인 이벤트
        
        while self.SB==0:
            #fps 제한을 위해 한 loop에 한번 반드시 호출해야합니다.
            self.clock.tick(30)

            # 입력 처리
            for event in pygame.event.get(): #동작을 했을때 행동을 받아오게됨
                if event.type ==pygame.QUIT:
                    self.SB=1 # SB 가 1이되면 while 문을 벗어나오게 됨
                if event.type == pygame.KEYDOWN: # 어떤 키를 눌렀을때!(키보드가 눌렸을 때)
                    '''
                    각 키가 눌러지면 플레이어 캐릭터 객체의 값 수정 (현재는 종료를 위해 왼쪽키를 종료로 둠)
                    '''
                    if event.key == pygame.K_LEFT:
                        self.SB=1
                    if event.key == pygame.K_RIGHT: 
                        pass
                    if event.key == pygame.K_SPACE: 
                        pass
                    if event.key == pygame.K_UP :
                        pass
                    if event.key == pygame.K_DOWN:
                        pass
                elif event.type == pygame.KEYUP: # 키를 뗐을때
                    if event.key == pygame.K_LEFT:
                        pass
                    elif event.key == pygame.K_RIGHT:
                        pass
                    elif event.key == pygame.K_SPACE:
                        pass
                    elif event.key == pygame.K_UP:
                        pass
                    elif event.key == pygame.K_DOWN:
                        pass

            

            self.screen.fill((0,0,0))

            #플레이어 객체 이동
            #self.character.move() ??

            #몹 객체 이동
            for mob in self.mob_list:
                #mob.move() ??
                pass

            #점수와 목숨 표시
            font = pygame.font.Font("./Font/DXHanlgrumStd-Regular.otf", sum(self.size)//85)
            score_life_text = font.render("Score : {} Life: {}".format(self.score,self.life), True, (255,255,0)) # 폰트가지고 랜더링 하는데 표시할 내용, True는 글자가 잘 안깨지게 하는 거임 걍 켜두기, 글자의 색깔
            self.screen.blit(score_life_text,(10,5)) # 이미지화 한 텍스트라 이미지를 보여준다고 생각하면 됨 
            
            # 현재 흘러간 시간
            playTime = (time.time() - self.start_time)
            time_text = font.render("Time : {:.2f}".format(playTime), True, (255,255,0))
            self.screen.blit(time_text,(300,5))

            # 화면갱신
            pygame.display.flip() # 그려왔던데 화면에 업데이트가 됨

        # While 빠져나오면 게임오버 스크린 실행
        self.showGameOverScreen()

     
    def showGameOverScreen(self):
        return

    
