import sys
 input 과 sysstdin  의 속도차이는 어마무시하다..
stack = []
# n = int(input())
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    # mecro = input()
    mecro = sys.stdin.readline().rstrip()

    if mecro.split()[0] == "push":
        stack.append(int(mecro.split()[1]))
    elif mecro == "top":
        if len(stack) >0:
            print(stack[len(stack)-1])
        else:
            print(-1)
    elif mecro == "size":
        print(len(stack))
    elif mecro== "empty":
        print(0 if stack else 1)
    elif mecro == "pop" :
        if not stack:
            print(-1)
        else:
            print(stack.pop())