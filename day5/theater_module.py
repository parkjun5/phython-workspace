# 일반 가격

def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people*10000))


def price_morning(people):
    print("{0}명의 조조할인 가격은 {1}원 입니다.".format(people, people*6000))

def price_soldier(people):
    print("{0}명의 구닌 할인 가격은 {1}원 입니다.".format(people, people*4000))
