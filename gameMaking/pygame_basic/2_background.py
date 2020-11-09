import pygame

pygame.init() #초기화 반드시 필요하다!

# 화면 크기 설정

screen_width = 480 #가로 크기
screen_height = 640 #세로 게임

screen = pygame.display.set_mode((screen_width, screen_height)) #화면 크기 설정
#  화면 타이틀 설정

pygame.display.set_caption("NADO GAME") #게임 이름
# 배경 이미지 불러오기

background = pygame.image.load("D:\\Users\\박세준\\Desktop\\phython workspace\\gameMaking\\pygame_basic\\background.png")

## 어디선가 대기시켜야한다 동작 검사 이벤트 루프
# 이벤트 루프

running = True # 게임이 진행중인가?

while running :
    for event in pygame.event.get(): #어떤 동작을 감지해서 처리해주는 것 키보드 or 마우스
        if event.type == pygame.QUIT: ## x표 입력 창이 닫히는 이벤트가 발생하였는가?
            running = False #게임 진행중이 아니다.

    # screen.blit(background, (0,0)) ## 배경 만들어주기  + 백그라운드와 위치 0,0
    screen.fill((0,0,255)) ## rgb 값으로 색 채워주기
    pygame.display.update() ## 게임화면을 다시그리기 계속 업데이트 해줘야한다.

# pygame 종료

pygame.quit()