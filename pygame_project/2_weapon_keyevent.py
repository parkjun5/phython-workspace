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
#おはようございます。

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

#무기를 만들어 줍니다.

weapon =  pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width  = weapon_size[0]

# 무기는 한번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도

weapon_speed = 10



# 이동속도
character_speed = 5
character_to_x =0


running = True 
while running :
    dt = clock.tick(30) 


    # 2 . 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -=character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x +=character_speed
            elif event.key == pygame.K_SPACE:
                #  무기를 쏘기위해 유저의 위치를 가져온다
                weapon_x_pos = character_x_pos + (character_width/2) -(weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x =0

    character_x_pos += character_to_x 

    if character_x_pos <0 :
        character_x_pos =0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width -character_width
    
    #무기 위치 조정
    # for문에서 weapons 의 w를 하나씩 가져와준다
    # ex > 10, 200 >>> 180 , 160 , 140 스피드 만큼 쭊쭊 빠쪄깐다.
    # 500 , 200 >> 180 160 140 120
    #한번 돌때마다 20씩 줄여줘서 점점 올라가는것처럼보인다.
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons ] ## 무기 위치를 위로
    # 3. 게임 캐릭터 위치 정의
    # 4. 충돌 처리
    # 5. 화면에 그리기

    #천장에 닿은 무기 삭제
    # if w[1] 이 0보다 크다면 가져와서 리스트에 넣어줌 
    # 0보다 작은것들은 넣어지지 않아진다 .
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
    screen.blit(stage, (0, screen_height-stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))




    pygame.display.update() 
    

pygame.quit()