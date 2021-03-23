# n개의 정수로 만들어진 수열의 합을 만들자

# 연속되어야한다

# 10 -4 3 1 5 6 -35 12 21 -1

## 21 +21  33이 정답


## A 10 -4  3  1 5 6 -35 12 21 -1
## D 10  6  9 10 15 21 14 -2vs 12 33 32
# max (D)
import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
# A = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
D = [0 for _ in range(N)]

for num in range(N):
    D[num] = A[num]
    if num == 0:
        continue
    if A[num] < D[num-1] + A[num]:
        D[num]  = D[num-1] + A[num]


print(max(D))
