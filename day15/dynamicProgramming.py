## top - down >>> 재귀 방식

# bottom up >> 작은문제부터 올라간다 . 반복문

memo =[0 for i in range(100)]

memo[0] = 0
memo[1] = 1

num = 10
for i in range(2, num):
    memo[i] = memo[i-1] + memo[i-2]

print(memo)

