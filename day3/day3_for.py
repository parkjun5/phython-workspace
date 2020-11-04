## for문입니다,.!

# for waiting_no in [0,1,2,3,4]:
#     print("대기 번호 : {0}".format(waiting_no))
#파이썬에선 설마 이 시작단의 위치로 해결되나?
for waiting_no in range(1,6): # 1,2,3,4,5
    print("대기 번호 : {0}".format(waiting_no))

starbucks = ["아이언맨","토르","아이엠 그루트"]

for customs in starbucks:
        print("{0} 님 커피 나왔어요".format(customs))