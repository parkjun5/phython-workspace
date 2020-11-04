# 추첨 프로그램 만들기

## 댓글작성자 중 1명은 치킨 3명은 커피


## 20명 작성 1~20

## 그냥 무작위로 추첨 중복 x

## random 모듈과 syffle과 sample 사용
## 출력예제

## 당텀자 발표 
## 치킨 :  1
## 커피 : [2,3,4]

## ㅊㅋ
from  random import *

# comments = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
 ## range = 1~ 20 까지의 값을 range로 만들어줌
comments = list(range(1,21))
 

# comments.remove(chicken)

# print(comments)
chicken = randrange(1,20)

comments.remove(chicken)

shuffle(comments)

coffs = sample(comments,3)

# comments_set = set(comments)
# comments_set.remove(chicken)

print(f"-- 당첨자 발표 --\n치킨 당첨자 : {chicken}\n커피 당첨자 :{coffs}")
print("-- 축하합니다 --")
comments2 = list(range(1,21))
shuffle(comments2)
winners = sample(comments2,4)

print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 : {0}".format(winners[1:]))