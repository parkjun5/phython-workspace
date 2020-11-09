"""
대기손님의 치킨 대기 시간을 줄이고자 자동 주문 시스템을 제작하였다
시스템 코드를 확인하고 적절한 예외처리 구문을 넣어라

조건 1: 1보다 작거나 숫자가 아닌 입력밧이 들어올 때에는 ValueError 로 처리
        "잘못된 값 입력"

조건 2 : 대기 손님이 주문 할 수 있는 총 치킨량은 10마리
        치킨 소진시 소용자 정의 에러 SoldOutError 발생 프로그램 종료
        재고가 소진되어 더이상 주문을 받을수 업습니다.

raise!!!

"""
class SoldOutError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg
chicken = 10

waiting = 1

while(True):
    try:
        if chicken < 1 :
            raise SoldOutError("재고가 소진되어 더이상 주문을 받을수 업습니다.")
        print("[남은 치킨 : {0}] ".format(chicken))
        try:
             while(True):
                 order = int(input("치킨을 몇마리 주문하시겠습니까?"))
                 break
        except ValueError :
             print("잘 못 된 값 입력", end="\n\n")

    except SoldOutError as err:
        print(err)
        break
    
    if order > chicken:
        print("재료가 부족합니다 남은 치킨은 {0}입니다".format(chicken))

    else:
        print("[대기번호 : {0}], {1}마리 주문하셨습니다".format(waiting,order))
        waiting +=1
        chicken -= order




