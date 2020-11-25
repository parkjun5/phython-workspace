# 카드 N 개 구매

# 카드팩은 N가지 종류

#I번째 카드팩은 I개의 카드를 담고있고 가격은 P{I}

# 카드 N개 구매하는 비용의 최대값은?


# D(N)  = max(D(N -i) +p(i))
# 1 <= i <= N


import sys

Max = int(sys.stdin.readline().rstrip())
p = [0] +list(map(int, sys.stdin.readline().rstrip().split()))
dp = [-1 for _ in range(Max+1)]

dp[0] = 0
for idx in range(1, Max+1):

    for j in range(1, idx+1):
        if dp[idx] == -1 or dp[idx] > dp[idx-j] + p[j]:
            dp[idx] = p[j] + dp[idx-j]


sys.stdout.write(str(dp[Max]))


