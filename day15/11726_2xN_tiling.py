# D[n]  = 2*n을 채우는 방법의 수
num = int(input())

dp = [0, 1, 3]

if num == 1:
    print(dp[1])
elif num == 2:
    print(dp[2])   
else:
    for j in range(3, num+1):
        dp.append(dp[j-1] + (2* dp[j-2]))
        
    print(dp[num]%10007)