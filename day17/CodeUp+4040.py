import sys


def finding(rooms, sday, eday ,index,count):
    if sday == eday:
        return 
    else:
        if str(rooms[sday])[index] =="O":
            counts[index].append(sday)
            return finding(rooms, sday+1, eday ,index,count+1)
        else:
            return  finding(rooms, sday+1, eday ,index,count)
    

n, m = map(int, sys.stdin.readline().rstrip().split())

rooms = []

for day in range( n):
    rooms.append(sys.stdin.readline().rstrip())

sday, eday = map(int, sys.stdin.readline().rstrip().split(" "))
# sday -=1
# eday -=1
# counts  = [[] for _ in range(m) ]

# 이 제로 리스트는 예약이 불가능한 날을 판별한다.
zeros = [0]*m

def new_check(day_data):
    result = [0]*m
# enumerate 는 배열의 값과 인덱스 값을 튜플로 만들어준다
# ex 1 2 3 4 5
#  (0, 1) (1, 2) (2, 3) (3, 4) (4, 5)
    for idx, ox in enumerate(day_data):
        if ox =="O": result[idx] = 1
    if result == zeros : return -1
    return result

def check_max_day(room):
    move = -1

    check_list = [0] * m

    for day_data in rooms:
        #오늘 날짜의 값
        if check_list != zeros:
            for idx, r in enumerate(check_list):
                if r ==1 and day_data[idx] =="X": check_list[idx] =0

        if check_list == zeros:
            move += 1
            check_list = new_check(day_data)
            if check_list == -1 : return -1

    return move



rooms = rooms[sday-1: eday-1]

print(check_max_day(rooms))







# for i in range(m):
#     finding(rooms, sday, eday, i, 0)
# counts.sort(key = len, reverse= True)

# result =0
# flag = True
# union = []
# while flag:
#     if result >= m:
#         print(-1)
#         break
#     union = list(set(union)| set(counts[result]))
#     for i in range(1, len(union)):
#         if  int(union[i-1]) != union[i]-1:
#             result +=1
#     if len(union) == eday- sday:
#         flag = False
#         print(result)
#         break
#     result+=1
#     for a in counts:
#         uni = list(set(a)|set(union))
#         print(uni)
#         for k in range(1, len(uni)):
#             if  int(uni[k-1]) != uni[k]-1:
#                 result +=1
#         if len(uni) == eday- sday:
#             flag = False
#             print(result)
#             break
    

