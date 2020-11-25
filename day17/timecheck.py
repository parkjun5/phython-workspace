import sys

N = int(sys.stdin.readline().rstrip())


# time = [[i for i in range(60) ] for _ in range(60)]
totals =0
if N <3:
    totals = (N+1)* 1575
else :
    totals = (N+1)* 1575 + 2025
count =0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) +str(j) +str(k):
                count += 1
        print(count)



print(count)