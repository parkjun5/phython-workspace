import sys


num = int(sys.stdin.readline().rstrip())
for j in range(num):
    n = int(sys.stdin.readline().rstrip())
    dp = [1, 1, 2]
    for i in range(3, n+1):
        dp.append(dp[i-1]+dp[i-2]+ dp[i-3])

    print(dp[n])