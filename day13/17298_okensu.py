import sys
N = int(sys.stdin.readline().rstrip())
nums =list(map(int,sys.stdin.readline().rstrip().split()))
stacks = []
result = [-1 for i in range(N)]
stacks.append(0)
i =1

for i in range(N):
    # if nums[index] > nums[index-1]:
    #     result[index-1] = nums[index]
    # else:
    #     stacks.append(index-1)
    # for a in stacks:
    #     if nums[index] > nums[a]:
    #         result[a] = nums[index]
    #         stacks.pop(stacks.index(a))
    while stacks and nums[stacks[-1]] < nums[i]:
        result[stacks[-1]] = str(nums[i])
        stacks.pop()
    stacks.append(i)
    i +=1

for i in result:
    print(i, end=" ")
