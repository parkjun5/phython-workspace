import pygame
from random import *
##############################################################################
# 기본 초기화 부분 반드시 해야함

pygame.init() #초기화 반드시 필요하다!

# 화면 크기 설정
screen_width = 480 
screen_height = 640 

screen = pygame.display.set_mode((screen_width, screen_height)) 

#  화면 타이틀 설정
pygame.display.set_caption("Ddong rain") #게임 이름

# FPS
## 시간 처리
clock = pygame.time.Clock()
##############################################################################

# 1. 사용자 게임 초기화 (배경화면 , 게임 이미지, 좌표 ,속도 , 폰트 등등)

background = pygame.image.load("D:/Users/박세준/Desktop/phython workspace/gameMaking\pygame_basic/backs.png")

character = pygame.image.load("D:/Users/박세준/Desktop/phython workspace/gameMaking/pygame_basic/char.png")

char_size = character.get_rect().size # 캐릭터의 히트박스 
char_size_height = char_size[1]
char_size_width =  char_size[0]
char_x_pos = (screen_width/2) - (char_size_width/2)
char_y_pos =  screen_height -char_size_height-4


ddong = pygame.image.load("D:/Users/박세준/Desktop/phython workspace/gameMaking/pygame_basic/ddong.png")
ddong_size = ddong.get_rect().size # 캐릭터의 히트박스 
ddong_size_height = ddong_size[1]
ddong_size_width =  ddong_size[0]
ddong_x_pos = screen_width - ddong_size_width -randrange(0,(screen_width - ddong_size_width))
ddong_y_pos =10

ddong2 = pygame.image.load("D:/Users/박세준/Desktop/phython workspace/gameMaking/pygame_basic/ddong2.png")
ddong2_size = ddong2.get_rect().size # 캐릭터의 히트박스 
ddong2_size_height = ddong2_size[1]
ddong2_size_width =  ddong2_size[0]
ddong2_x_pos = screen_width - ddong2_size_width -randrange(0,(screen_width - ddong2_size_width))
ddong2_y_pos =10


# jumping = False
# 좌표를 바꿔주기 위한 이동을 위한 좌표

to_x = 0
to_y = 0

#이동 속도 
ddong_speed = 0.5
character_speed = 0.6


running = True 

while running :
    dt = clock.tick(60) 
    # 2 . 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    char_x_pos += to_x *dt
    ddong_y_pos += ddong_speed*dt
    ddong2_y_pos += ddong_speed*dt

    if ddong_y_pos > screen_height - ddong_size_height:
        ddong_x_pos = screen_width - ddong_size_width -randrange(0,(screen_width - ddong_size_width))
        ddong_y_pos = 5
    if ddong2_y_pos > screen_height - ddong2_size_height:
        ddong2_x_pos = screen_width - ddong2_size_width -randrange(0,(screen_width - ddong2_size_width))
        ddong2_y_pos = 5

    if char_x_pos <0:
        char_x_pos = 0
    elif char_x_pos > screen_width- char_size_width:
        char_x_pos = screen_width- char_size_width


    # 3. 게임 캐릭터 위치 정의
    # 4. 충돌 처리
    # 5. 화면에 그리기

    char_rect = character.get_rect()
    char_rect.left = char_x_pos
    char_rect.top  = char_y_pos

    ddong_rect =ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top  = ddong_y_pos

    ddong2_rect =ddong2.get_rect()
    ddong2_rect.left = ddong2_x_pos
    ddong2_rect.top  = ddong2_y_pos

    if char_rect.colliderect(ddong_rect):
        print("똥맞았어영")
        running =False
    if char_rect.colliderect(ddong2_rect):
        print("똥맞았어영")
        running =False

    screen.blit(background,(0,0))
    screen.blit(character,(char_x_pos,char_y_pos))
    screen.blit(ddong,(ddong_x_pos,ddong_y_pos))
    screen.blit(ddong2,(ddong2_x_pos,ddong2_y_pos))

    pygame.display.update() 
    

pygame.quit()