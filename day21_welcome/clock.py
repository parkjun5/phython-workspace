import sys

N = int(sys.stdin.readline().rstrip())

# non = (15*60)+ (45 *15)
# threes = (60*60) 
# dap = 0
# if N > 3:
#     dap = non*N + threes
# else:
#     dap = non*(N+1)
# print(dap)

count =0

for i in range(N+1):
    for j in range(60):
        for h in range(60):
            if '3' in str(i) +str(j)+ str(h):
                count += 1
print(count)