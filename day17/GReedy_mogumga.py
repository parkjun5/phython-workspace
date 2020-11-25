import sys

N = int(sys.stdin.readline().rstrip())

lists = list(map(int, sys.stdin.readline().rstrip().split()))
lists.sort()
# count = 0
# result = 0
# for  i in range(1,N+1):
#     for j in range(len(lists)):
#         if lists[j] == i:
#             pops.append(j)
#         if len(pops) ==i:
#             for k in pops:
#                 lists[k] =0
#             count +=1
#             pops.clear()
    
# print(count)

count = 0
result = 0

for i in lists:
    count +=1
    if count >= i:
        result +=1
        count =0
print(result)
