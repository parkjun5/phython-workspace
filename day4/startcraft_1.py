# ## 떼란

# # 매린

# name = "마린"

# hp = 40

# damage =5

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력은{0}, 공격력은{1}\n".format(hp,damage))

# # 탱크 : 공격유닛 일반 시즈

# tank_name = "탱크"
# tank_hp =150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력은{0}, 공격력은{1}\n".format(tank_hp,tank_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다 [공격력 :{2}]".format( \
#          name, location, damage)) 

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)

# ##if tank +1 이라면 
# tank2_name = "탱크"
# tank2_hp =150
# tank2_damage = 35

# attack(tank2_name,"1시",tank2_damage)

# ## 매번 만드는게 어려워서 클래스로 해준다.!

## 맴버 변수라 카면 self 의 네임, hp damage 등등을 포함
class Unit: 
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.  name))
        print("체력은{0}, 공격력은{1}\n".format(self.hp,self.damage),end="")
        print("클래스 내부에서 작성...")

## 셀프를 제외한 나머지를 작성
marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)
# marine2 = Unit("마린",5)<< 오류가 나온다/


#__init__ 생성자() 생성할때 자동으로 생성되는 부분.
# class에서 생성되는 애들을 객체라 학고
## 탱크와 마린은 인스턴스라 한다.


# 레이쓰 : 공중유닛 비행긱 클로킹가능 

wraith1 =Unit("레이쓰",80 ,5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인트 컨트롤 : 상대방 유닛을 내것으로 만드는 것 (빼앗음)
wraith2 = Unit("레이스",80,5)
wraith2.clocking =True

## if wraith .cloking을 확인하려 하면 해당 변수가 없어서 오류가 나온다.
if wraith2.clocking == True:
    print("{0}는 현재 클로킹 중입니다.".format(wraith2.name))