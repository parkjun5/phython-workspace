import sys

stack1 = []
stack2 = []

str_ex = sys.stdin.readline().rstrip()

N = int(sys.stdin.readline().rstrip())
for stack_str in str_ex:
    stack1.append(stack_str)

for i in range(N):
    cmd = sys.stdin.readline().rstrip()
    
    if cmd.split()[0] == "P":
        stack1.append(cmd.split()[1])
    elif cmd == "L":
        if stack1:
            stack2.append(stack1.pop())
    elif cmd == "D":
        if stack2:
            stack1.append(stack2.pop())
    elif cmd == "B":
        if stack1:
            stack1.pop()
for answer in stack1:
    print(answer, end="")
for answer in range(len(stack2)):
    print(stack2.pop(), end="")