import pygame
import os 
##############################################################################
# 기본 초기화 부분 반드시 해야함

pygame.init() #초기화 반드시 필요하다!

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height)) 

#  화면 타이틀 설정
pygame.display.set_caption("New Pang") #게임 이름

# FPS
## 시간 처리
clock = pygame.time.Clock()
##############################################################################

# 1. 사용자 게임 초기화 (배경화면 , 게임 이미지, 좌표 ,속도 , 폰트 등등)

##위치를 우선 설정해준다.
current_path =  os.path.dirname(__file__) ## 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")

## 배경 만들기 
background =pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 처리

stage =pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지 높이 위에 캐릭터를 두기위해


# 캐릭터 만들기

character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos =  screen_height -stage_height - character_height

running = True 
while running :
    dt = clock.tick(30) 


    # 2 . 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    # 3. 게임 캐릭터 위치 정의
    # 4. 충돌 처리
    # 5. 화면에 그리기



    screen.blit(background,(0,0))
    screen.blit(stage, (0, screen_height-stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() 
    

pygame.quit()