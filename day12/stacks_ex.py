import sys

N = int(sys.stdin.readline().rstrip())
## 카운트를 넣어줄꺼임.
count  = 1
stack = []
answers = []
flag = True
for i in range(N):
    temp = int(sys.stdin.readline().rstrip())
    while count  <= temp:
        stack.append(count)
        answers.append("+")
        count +=1
    # for stack_in in range(count, temp+1):
    #     stack.append(stack_in)
    #     answers.append("+")
    # if temp+1 > count:
    #     count = temp + 1
    if stack[-1] == temp:
        stack.pop()
        answers.append("-")
    else: 
        flag = False

if  flag == True:
    for ans in answers:
        print(ans)
else: print("NO")

