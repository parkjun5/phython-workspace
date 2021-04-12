from collections import deque
n , m = map(int,(input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int,(input()))))

# def findIce(x, y):
#     if x >= n or x < 0 or y >= m or y < 0:
#         return False

#     if arr[x][y] == 0:
#         arr[x][y] = 1
#         findIce(x-1, y)
#         findIce(x, y-1)
#         findIce(x+1, y)
#         findIce(x, y+1)
#         return True
#     return False

# result = 0
# for i in range(n):
#     for j in range(m):
#         if findIce(i,j) == True:
#             result +=1


def findIce(x, y, val):
    if x >= n or x < 0 or y >= m or y < 0:
        return False

    if arr[x][y] == 0:
        arr[x][y] = val
        findIce(x-1, y, val)
        findIce(x, y-1, val)
        findIce(x+1, y, val)
        findIce(x, y+1, val)
        return True
    return False

result = 0
val = 2
for i in range(n):
    for j in range(m):
        if findIce(i,j,val) == True:
            val += 1
print(val-2)

for arrs in arr:
    print(arrs)

