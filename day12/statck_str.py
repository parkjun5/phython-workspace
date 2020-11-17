import sys
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    stacks = sys.stdin.readline().rstrip().split()
    for stack in stacks:
        temp = []
        for word in stack:
            temp.append(word)
        for i in range(len(temp)):
            print(temp.pop() , end="")


        print(end=" ")