import sys

tops= []
n = int(sys.stdin.readline().rstrip())
p_pizza,p_top = map(int,sys.stdin.readline().rstrip().split())
cal_p = int(sys.stdin.readline().rstrip())

best = cal_p //p_pizza


for _ in range(n):
    tops.append(int(sys.stdin.readline().rstrip()))
tops.sort(reverse=True)

for top in tops:
    temp = (top +cal_p) //(p_pizza +p_top)
    if best > temp:
        break
    else:
        best = temp
        cal_p += top
        p_pizza += p_top

print(best)
