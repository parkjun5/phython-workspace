gun = 10

def checkpoint(soldiers): #경계 근무
    ## 여기서의 gun과 밖의 gun과 다름
    # gun =20 이것이 지역변수이다.
    global gun # 전역 공간에 있는 gun으로 사용하겠다!
    gun = gun -soldiers
    print("[함수 내에서는 ] 남은총 :{0}".format(gun))
## 파라미터로 주고 하는 것이 좋은것이다.

def checkpoint_ret(gun, soldiers):
    gun = gun -soldiers
    print("[함수 내에서는 ] 남은총 :{0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
checkpoint(2)
gun = checkpoint_ret(gun,2)
print("전체 총: {0}".format(gun))
