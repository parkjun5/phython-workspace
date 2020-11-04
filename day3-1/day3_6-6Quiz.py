"""당신으니 코코아 서비스를 이용하는 택시기사

50명의 승객과 매칭기회가 있을때, 총 
탑승승객 수를 구하는 프로그램

1조건 승객별 소요시간 5~ 50 난수로 정해짐

조건 2 당신은 소요시간 5~ 15사이의 승객만 매칭해야함
'
예제
[O] 1번째 소요 15 '
[]  2번째 소요 50 '
[O] 3번째 소요 5 
...

[] 50번째 소요 16 '

총탑승인원 2명

"""
from random import *

total_guest = 0
for index in range(1,51):
    ox_sign = "[ ]"
    time = randrange(5,51)
    # if 5 <= time and time <= 16: # 밑에 것이 더 짧다/
    if 5 <= time <=15:
        total_guest+=1
        ox_sign = "[O]"
    print("{0} {1}번째 손님 (소요시간 : {2}분)".format(ox_sign,index,time))

print("총 탑승 승객 : {0} 분".format(total_guest))