import pygame

pygame.init() #초기화 반드시 필요하다!

# 화면 크기 설정

screen_width = 480 #가로 크기
screen_height = 640 #세로 게임

screen = pygame.display.set_mode((screen_width, screen_height)) #화면 크기 설정

#  화면 타이틀 설정

pygame.display.set_caption("NADO GAME") #게임 이름

## 어디선가 대기시켜야한다 동작 검사 이벤트 루프
# 이벤트 루프

running = True # 게임이 진행중인가?

while running :
    for event in pygame.event.get(): #어떤 동작을 감지해서 처리해주는 것 키보드 or 마우스
        if event.type == pygame.QUIT: ## x표 입력 창이 닫히는 이벤트가 발생하였는가?
            running = False #게임 진행중이 아니다.


# pygame 종료

pygame.quit()