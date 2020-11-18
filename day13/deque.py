import sys

str_exs =sys.stdin.readline().rstrip()
answer = []
reverse =[]
tag = False
temp = ""
for ex in str_exs:
    if ex == "<":
        tag = True
        for i in range(len(reverse)):
            temp = temp + reverse.pop()
        answer.append(temp)
        temp = ""
    if tag == False:
        if ex == " ":
            for i in range(len(reverse)):
                temp = temp + reverse.pop()
            temp = temp+ " "
            answer.append(temp)
            temp = ""
        else:
            reverse.append(ex)
    elif tag == True:
        temp = temp + ex
        if ex == ">":
            tag =False
            answer.append(temp)
            temp = ""

for i in range(len(reverse)):
    temp = temp + reverse.pop()
answer.append(temp)
for i in answer:
    print(i, end="")
