import sys

N = int(sys.stdin.readline().rstrip())

def GCD(a, b):
    if b ==0:
        return a
    else:
        return GCD(b, a%b)
        


for i in range(N):
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    answer =0
    for i in range(1, nums[0]):
        for j in range(i+1, nums[0]+1):
            answer +=GCD(nums[i], nums[j])

    print(answer)
