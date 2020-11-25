## 매 순간 가장 큰 선택을 하는 방식


## example 거스름돈 

# N 원 나눠주는법


# import sys

# N = int(sys.stdin.readline().rstrip())

# lists = [500,100,50,10]
# ans =   [0,0,0,0]
# for i in range(4):
#     if N >= lists[i]:
#         ans[i] = N //lists[i]
#         N = N % lists[i]

# print(sum(ans))

# # import sys

# min_food = 9999
# min_drink = 9999
# for i in range(5):
#     tmp = int(sys.stdin.readline().rstrip())
#     if  i <= 2:
#         min_food = min_food if min_food < tmp else tmp
#     else:
#         min_drink = min_drink if min_drink < tmp else tmp

# print(round((min_food+min_drink)*1.1, 1))


# import sys
# N, K =map(int, sys.stdin.readline().rstrip().split())


# count = 0

# while  N != 1:
#     if N % K ==0:
#         N = N//K
#     else:
#         N -= 1
    
#     count += 1

# print(count)

# count = 0


# import sys
# N, K =map(int, sys.stdin.readline().rstrip().split())


# result = 0
# while  True:
#     target = (N//K) *K
#     result += (N- target)
#     N = target

#     if N < K:
#         break
#     result += 1
#     N //= K

# result += (N-1)

# print(result)


# import sys
# a, b =map(int, sys.stdin.readline().rstrip().split())


# count = 0

# while  a != b:
#     if abs(a - b) >=8:
#         if a- b <0:
#             a += 10
#         else:
#             a -= 10
#     elif abs(a -b) >= 3:
#         if a- b <0:
#             a += 5
#         else:
#             a -= 5
#     else:
#         if a- b <0:
#             a += 1
#         else:
#             a -= 1
#     count += 1

# print(count)



import sys
N = sys.stdin.readline().rstrip()


result = int(N[0])

for i in range(1,len(N)):
    
    n = int(N[i])

    if n <= 1 or result <= 1:
        result +=n
    else:
        result *=n
    print(result)

print(result)
