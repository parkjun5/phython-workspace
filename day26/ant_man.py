# [ 1 , 3 , 1, 5]
# 숫자를 선택한다.
# 인접한 곳의 숫자는 선택 불가 1번의 3를 선택시 0 , 2번 선택불가.

# N = int(input())

# supplies = list(map, int(input().split()))

# D = [1 for _ in range(N)]

# sup_array = [[supply] for supply in supplies ]

# print(sup_array)

# for i in range(N):
#     for j in range(i):
#         if supplies[i] < supplies[j]:
#             if D[j]+1 > D[i]:
#                 array[i] = array[j] +[A[i]]
#                 D[i] = D[j]+1

# # def attack_check(supplies):
#     if supplies[-1] > supplies[-2] + supplies[-3]:
#         D += supplies[-1]
#         supplies.pop()
#         supplies.pop()
#     elif supplies[-1] == supplies[-2] + supplies[-3]:
#         if supplies[-2] > supplies[-3]:



# N = int(input())

# supplies = list(map(int, (input().split())))
# # 10 20 10 30 20 50

# d = [0] * 100

# d[0]  = supplies[0]
# d[1] = max(supplies[0], supplies[1])

# for i in range(2, N):
#     d[i] = max(d[i -1], d[i-2] + supplies[i])

# print(d)



N = int(input())

d = [0]* 50

d[0] = 1

d[1 ] =3

for i in range(2, 50):
    d[i] = d[i-1] + ( 2* d[i-2])

print(d)