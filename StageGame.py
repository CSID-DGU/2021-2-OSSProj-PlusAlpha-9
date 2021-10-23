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
        size = [infoObject.current_w,infoObject.current_h]
        self.screen = pygame.display.set_mode(size,pygame.RESIZABLE)
        
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
        self.pt = time.time()
        self.k=0
        self.SB = 0

    def main(self):
        # 메인 이벤트
        
        while self.SB==0:
            #fps 제한을 위해 한 loop에 한번 반드시 호출해야합니다.
            self.clock.tick(60)

            # 입력 처리
            for event in pygame.event.get(): #동작을 했을때 행동을 받아오게됨
                if event.type ==pygame.QUIT:
                    self.SB=1 # SB 가 1이되면 while 문을 벗어나오게 됨
                if event.type == pygame.KEYDOWN: # 어떤 키를 눌렀을때!(키보드가 눌렸을 때)
                    if event.key == pygame.K_LEFT: #왼쪽키 누르면 종료
                        self.SB=1

            
            now = time.time()
            if(now-self.pt>0.5):
                self.pt = now
                self.k += 1

            if self.k%2==0:
                color=self.black
            else:
                color = self.white
    
            self.screen.fill(color)
            
            # 화면갱신
            pygame.display.flip() # 그려왔던데 화면에 업데이트가 됨

        # While 빠져나오면 게임오버 스크린 실행
        self.showGameOverScreen()

     
    def showGameOverScreen(self):
        pygame.quit()

    
