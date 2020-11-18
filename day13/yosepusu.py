import sys

n, m= map(int,sys.stdin.readline().rstrip().split() )
yosep = []
yosep = [i for i in range(1,n+1)]
# for i in range(1,n+1):
#     yosep.append(i)
# cnt = 0
answer = []
# while  len(yosep) >0:
#     cnt += 1
#     if cnt % m ==0:
#             answer.append(str(yosep.pop(0)))
#     else:
#         yosep.append(yosep.pop(0))

temp = m-1
for i in range(n):
    if len(yosep) > temp:
        answer.append(str(yosep.pop(temp)))
        temp += m-1
    elif len(yosep) <= temp:
        temp = temp % len(yosep)
        answer.append(str(yosep.pop(temp)))
        temp += m-1

print("<%s>"%(", " .join(answer)))