import sys

nums = int(sys.stdin.readline().rstrip())
answers =[]
for num in range(nums):
    stack = []
    N = sys.stdin.readline().rstrip()
    for i in N:
        if i =="(":
            stack.append(i)
        else:
            if not stack:
                stack.append(i)
                break
            else: 
                stack.pop()

    if not stack:
        answers.append("YES")
    else:
        answers.append("NO")

for answer in answers:
    print(answer)