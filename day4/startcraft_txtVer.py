from random import *

class Unit: # 부모 클래스
    def __init__(self,name,hp ,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))
    
    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0} : {1}으로 이동합니다 [ 속도 :{2}]".format(self.name, \
            location, self.speed))

    def damaged(self, damage):
        self.hp -=damage
        if self.hp <=0:
            print("{0} : 으아아".format(self.name))
        else :
            print("{0} : {1} 데미지를 입었습니다. [남은 체력 : {2}]"\
            .format(self.name, damage, self.hp))

class AttackUnit(Unit): 

    def __init__(self, name, hp, speed ,damage):
        Unit.__init__(self,name,hp, speed)
        self.damage = damage
    
    def attact(self, location):
        print("{0} : {1} 방향을 공격을 시작합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage))


### 마린의 자체 클래스
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    # 일정기간동안 이속 + 공속 증가  체력 10감소 
    def stimpack(self):
        if self.hp >10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10감소) ".format(self.name))
        else: 
            print("{0} : 체력이 부족합니다...".format(self.name))

## 사즈모드 ;

# 이속 0가 되며 더 높은 공격력 가져진다.
class Tank(AttackUnit):

    seize_developed = False # 시즈 개발 여부

    def __init__(self):
        super().__init__("탱크",150 ,2 ,35)
        self.seize_mode =False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        #현재 시즈모드가 아닐때 > 시즈
        if self.seize_mode ==False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *=2
            self.seize_mode ==True

        #현재 시즈모드일때
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /=2
            self.seize_mode == False




class canfly:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self,name , location):
        print("{0} : {1}으로 날아가요 [ 스피드 : {2}]".format(self.name, \
        location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, canfly):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0 ,damage) # 지상 스피드느 0
        canfly.__init__(self,flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)



class Wraith(FlyableAttackUnit):

    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80 , 20, 5)
        self.clocked = False #클로킹 해제새ㅏㅇ태..

    def clocking(self):

        ## 클로킹 상태
        if self.clocked == True:
            print("{0} : 해제합니다".format(self.name))
            self.clocked = False
            ##ㅠ해제
        else:
            print("{0} : 클로킹중....".format(self.name))
            self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

game_start()
## 마 3
m1 = Marine()
m2 = Marine()
m3 = Marine()
##탱2
t1 = Tank()
t2 = Tank()
#레 1
w1 = Wraith()

#유닛 일괄 괄리

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

##전군 이동

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed =True
print("[알림] 탱크 시지모드 업그레이드 완료")

## 공격 모드 준비 (마린 스팀팩 탱크 시즈 레이스 클로킹)
## isinstance << 이것이 어떤 객체인지 확인하는 것 특정인스턴스인것을 확인

for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()


for unit in attack_units:
    unit.attact("1시")


for unit in attack_units:
    unit.damaged(randint(5,50))

game_over()

