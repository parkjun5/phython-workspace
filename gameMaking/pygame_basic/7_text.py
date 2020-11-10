import pygame

pygame.init() #초기화 반드시 필요하다!

# 화면 크기 설정

screen_width = 480 #가로 크기
screen_height = 640 #세로 게임

screen = pygame.display.set_mode((screen_width, screen_height)) #화면 크기 설정
#  화면 타이틀 설정
pygame.display.set_caption("NADO GAME") #게임 이름

# FPS
## 시간 처리
clock = pygame.time.Clock()

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

#이동 속도 
character_speed = 0.6

# 적 enemy  캐릭터!
enemy = pygame.image.load("D:\\Users\\박세준\\Desktop\\phython workspace\\gameMaking\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size #이미지에서 사각형을 가져와서 크기를 구해옴
enemy_width  = enemy_size[0] # 캐릭터의 가로크기
enemy_height =enemy_size[1] ##캐릭터의 세로 크기
enemy_x_pos  = (screen_width / 2) - (enemy_width / 2) # 화면 가로 절반크기에 해당하는 곳에 위치 (가로위치) 
enemy_y_pos  = (screen_height /2 ) - (enemy_height / 2)   ## 화면 세로크기  가장 아래에 (세로 위치)


## 어디선가 대기시켜야한다 동작 검사 이벤트 루프
# 이벤트 루프

### 폰트 정의
game_font = pygame.font.Font(None,40) # 폰트 객체를 생성 (폰트 , 크기)

# 총 시간
total_time = 10

# 시작 시간 정보

start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴


running = True # 게임이 진행중인가?

while running :
    dt = clock.tick(60) ## 게임화면의 초당 프레임수를 설정

    # 프레임 확인하기
    # print("fps : "+ str(clock.get_fps()))
    # 10fps  = 1초 동안에 10번 동작  1번에 몇만큼이동? 10! 10*10 =100
    # 20 fps = 1초 동안에 20번 동작  1번에 5만큼  5*20  == 100


    for event in pygame.event.get(): #어떤 동작을 감지해서 처리해주는 것 키보드 or 마우스
        if event.type == pygame.QUIT: ## x표 입력 창이 닫히는 이벤트가 발생하였는가?
            running = False #게임 진행중이 아니다.

        if event.type == pygame.KEYDOWN: ## 무언가 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type ==pygame.KEYUP:# 방향키를 떄면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        
    ## 프레임에 따라 속도가 변하지 않도록  dt를 곱해준다.

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

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

    ## 충돌처리를 위한 정보 업데이트
    character_rect = character.get_rect() ## 캐릭터 사각형 받아오기
    # 원래 rect는 초반 0.0 의 값을 가지기 떄문에 값을 변형시켜주는데
    # 레프트와 탑만 바꿔주면 된다.
    character_rect.left = character_x_pos
    character_rect.top =  character_y_pos
    # 적군의 현재 위치도 계속 반영해준다.
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos 

    # 캐릭터와 적군이 충돌했는지 체크
    # colliderect 내장함수는 사각형 기준으로 충돌을 확인하는 함수 확인하고자 하는
    ## 랙트를 괄호에 넣어준다
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요;;")
        running = False

    screen.blit(background, (0,0)) ## 배경 만들어주기  + 백그라운드와 위치 0,0

    screen.blit(character, (character_x_pos, character_y_pos ) ) #캐릭터 그려주기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기 
    
    ## 타이머 집어넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
     #경과 시간(ms)을 1000으로나눠서 초단위로 표시
        #render에는 무엇을, 안티알리아스 , 컬러를 정의해야한다
    timer = game_font.render(str(int(total_time -elapsed_time)), True, (255,255,255))

    screen.blit(timer,(10,10))

    if total_time - elapsed_time <=0:
        print("타임 아웃 ")
        running = False
    pygame.display.update() ## 게임화면을 다시그리기 계속 업데이트 해줘야한다.
    
#종료전에 2초 대기
pygame.time.delay(2000)
# pygame 종료

pygame.quit()