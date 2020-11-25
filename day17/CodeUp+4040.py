import sys


def finding(rooms, sday, eday ,index,count):
    if sday == eday:
        return 
    else:
        if str(rooms[sday])[index] =="O":
            counts[index].append(sday)
            return finding(rooms, sday+1, eday ,index,count+1)
        else:
            return  finding(rooms, sday+1, eday ,index,count)
    

n, m = map(int, sys.stdin.readline().rstrip().split())

rooms = []

for day in range( n):
    rooms.append(sys.stdin.readline().rstrip())

sday, eday = map(int, sys.stdin.readline().rstrip().split())
sday -=1
eday -=1
counts  = [[] for _ in range(m) ]


for i in range(m):
    finding(rooms, sday, eday, i, 0)
counts.sort(key = len, reverse= True)

result =0
flag = True
union = []
while flag:
    union = list(set(union)| set(counts[result]))
    for i in range(1, len(union)):
        if  int(union[i-1]) != union[i]-1:
            result +=1
    if len(union) == eday- sday:
        flag = False
        print(result)
        break
    result+=1
    for a in counts:
        uni = list(set(a)|set(union))
        for k in range(1, len(uni)):
            if  int(uni[k-1]) != uni[k]-1:
                result +=1
        if len(uni) == eday- sday:
            flag = False
            print(result)
            break
    if result >eday- sday:
        print(-1)
        break


