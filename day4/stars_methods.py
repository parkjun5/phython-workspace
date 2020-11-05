# 일반 유닛
class Unit: # 부모 클래스
    def __init__(self,name,hp ,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0} : {1}으로 이동합니다 [ 속도 :{2}]".format(self.name, \
            location, self.speed))
# 메딕 : 의무병 >>healing!
##상속!
## 상속 받을 CLASS를 ()안에 넣어준다

# 그렇다면 다중 상속은? 공중유닛 예제를 통해 배워보자

## 드랍쉬1 :: 날아다님 수송기 마린/ 파벳/ 탱꾸 수송 공격 x
class AttackUnit(Unit): #자식 클래스
    def __init__(self, name, hp, speed ,damage):
        # self.name = name
        # self.hp =hp
        # 유닛으로 값을 보내 아버지가 만들어준다.
        Unit.__init__(self,name,hp, speed)
        self.damage = damage
    
    def attact(self, location):
        print("{0} : {1} 방향을 공격을 시작합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        self.hp -=damage
        if self.hp <=0:
            print("{0} : 으아아".format(self.name))
        else :
            print("{0} : {1} 데미지를 입었습니다. [남은 체력 : {2}]"\
            .format(self.name, damage, self.hp))

# 파이어뱃 :" 공격유닛 화염방사기 .. ㄷㄷㄷ"
# firebat1 = AttackUnit("파뱃",50,16)
# ## 5시 어태땅
# firebat1.attact("5시")
# ## 공격 두번 결국 주거써..
# firebat1.damaged(25)
# firebat1.damaged(25)

# medic =Unit("메딕",100)
# print(medic.hp)

# 날수 있는 공중기능을 가진 클래스
class canfly:
    # 생성
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self,name , location):
        print("{0} : {1}으로 날아가요 [ 스피드 : {2}]".format(self.name, \
        location, self.flying_speed))

## 공중 공격 유닛 클래스
## 연산자 오버로딩
class FlyableAttackUnit(AttackUnit, canfly):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0 ,damage) # 지상 스피드느 0
        canfly.__init__(self,flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

##  밣키리 공중공격 한번에 14발 미사일

# valkyrie = FlyableAttackUnit("발키리", 200 , 6 ,5)
# valkyrie.fly(valkyrie.name, "3시")


# battleCrusier.attact("3시")

## 벌쳐 지상

# vulture = AttackUnit("벌쳐", 80 , 10 ,20)

# battlecrusier = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")

# battlecrusier.move("9시")


## 건물!
## 서플라이 디폿 : 1개 설치할때마다 유닛 8개 만들수있게해줌

class BuildingUnit(Unit):
    def __init__(self,name, hp, location):
        # Unit.__init__(self, name, hp ,0) == super
        ## 슈퍼는 self를 안보내줘도 된다. 개이득
        super().__init__(name,hp,0)
        self.location = location


#  pass ## 패쓰의 의미 일반 그냥 지나간다.
# supply_depot = BuildingUnit("서플라이 디폿",500 , "7시")


# def game_start():
#     print("새로운 게임을 시작합니다!")
# def game_over():
#     pass

# game_start()
# game_over()