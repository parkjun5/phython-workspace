import sys
Max = 1000000
checking = [False, False] + [True] * (Max-1)
count = 0
# def making_prime(checking, count):
for i in range(2, Max-1):
    if checking[i] == True:
        # prime.append(i)
        count +=1
        for j in range(i*2, len(checking), i):
            checking[j] = False

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    temp = int(sys.stdin.readline().rstrip())
    answer = 0
    for j in range((temp//2)+1):
        if checking[j] and checking[temp-j] == True:
            answer += 1
    print(answer)