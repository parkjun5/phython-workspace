import sys

strs = sys.stdin.readline().rstrip()

stack = []
count =0
index = 0
for ex in strs:
    index += 1
    if ex == "(":
        stack.append(index)
    elif ex == ")":
        #레이저 스택의 마지막 번째와 index와 1차이 나면 길이0인 레이저이다.
        if stack[-1]+1 == index:
            stack.pop()
            count += len(stack)
        else : 
            count += 1
            stack.pop()
print(count)