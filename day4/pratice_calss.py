class Unit:
    def __init__(self):
        print("유닛 생성 ")

    
class Flyable :
    def __init__(self):
        print("flyable 생성자")


class FlyableUnit(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()

## 두개 이상의 부모를 둘때에는 처음의 부모만 가져올수이싿.