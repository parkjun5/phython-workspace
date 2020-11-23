# D[N] = N을 1로 만드는 최소 연산 횟수

# 3으로 나눈다면 
# 1 + D[N //3]
# 2으로 나눈다면 
# 1 + D[N //2]
# 1으로 qisejays 
# 1 + D[N -1]
import sys
num = int(sys.stdin.readline().rstrip())
memo = [0 for i in range(num+1)]

for i in range(2, num+1):
    memo[i] = memo[i-1]+1
    temp = 9999
    temp2 = 9999
    if i %2 ==0:
        temp =memo[i//2] +1
    if i %3 ==0:
        temp2 = memo[i//3]+1
    memo[i] = min(memo[i], temp, temp2)

print(memo[num])