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

# 캐릭터 스프라이트 불러오기
character= pygame.image.load("D:\\Users\\박세준\\Desktop\\phython workspace\\gameMaking\\pygame_basic\\character.png")
character_size = character.get_rect().size #이미지에서 사각형을 가져와서 크기를 구해옴
character_width  = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] ##캐릭터의 세로 크기
character_x_pos  = (screen_width / 2) - (character_width / 2) # 화면 가로 절반크기에 해당하는 곳에 위치 (가로위치) 
character_y_pos  = screen_height -character_height   ## 화면 세로크기  가장 아래에 (세로 위치)

# 좌표를 바꿔주기 위한 이동을 위한 좌표

to_x = 0
to_y = 0

## 어디선가 대기시켜야한다 동작 검사 이벤트 루프
# 이벤트 루프

running = True # 게임이 진행중인가?

while running :
    for event in pygame.event.get(): #어떤 동작을 감지해서 처리해주는 것 키보드 or 마우스
        if event.type == pygame.QUIT: ## x표 입력 창이 닫히는 이벤트가 발생하였는가?
            running = False #게임 진행중이 아니다.

        if event.type == pygame.KEYDOWN: ## 무언가 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1

        if event.type ==pygame.KEYUP:# 방향키를 떄면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        

    character_x_pos += to_x
    character_y_pos += to_y

    #가로 경계값 처리
    if character_x_pos <0:
        character_x_pos =0
    elif character_x_pos > screen_width -character_width:
        character_x_pos = screen_width - character_width
    
    # 세로 경계값 처리
    if character_y_pos <0:
        character_y_pos = 0
    elif character_y_pos > screen_height -character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0,0)) ## 배경 만들어주기  + 백그라운드와 위치 0,0

    screen.blit(character, (character_x_pos, character_y_pos ) ) #캐릭터 그려주기

    pygame.display.update() ## 게임화면을 다시그리기 계속 업데이트 해줘야한다.

# pygame 종료

pygame.quit()