import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

D = [1 for _ in range(N)]

array = [[x] for x in A ]

# print(array)

for i in range(N):
    for j in range(i):
        if A[i]> A[j]:
            if D[j]+1 > D[i]:
                array[i] = array[j] +[A[i]]
                D[i] = D[j]+1

length = 0

flag = 0

# print(array)
# print(D)
# print(max(D))
# print(array[D.index(max(D))])
for i in range(N):
    if length < D[i]:
        flag = i
        length = D[i]

print(length)
print(*array[flag])







# def go(target):
#     if target == 0:
#         daps.append(0)
#         return 
#     daps.append(target)
    
#     target = reason[target]
    
#     return go(target)


# daps =[]
# reason = [1 for _ in range(N)]

# D = [1 for _ in range(N)]

# for i in range(1, len(D)):
    
#     for j in range(i-1, -1, -1):
#         if A[i] > A[j]:
#             if D[i] <= D[j]:
#                 D[i] = D[j]+1
#                 reason[i] = j

# target = reason[-1]
# go(target)
# re_daps = list(reversed(daps))

# print(max(D))
# for dap in re_daps:
#     print(A[dap], end=" ")
# print(max(A), end="")