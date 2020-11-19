import sys

def gcd_place(a, b):
    if b ==0:
        return a
    else:
        return gcd_place(b, a%b)

D_list = []
N, S = map(int, sys.stdin.readline().split())
# S == 현재 위치이다.
Dons = list(map(int, sys.stdin.readline().split()))

for don in Dons:
    D =S -don
    if D <0:
        D *=-1
    D_list.append(D)
smallest = D_list[0]
for i in range(1, len(D_list)):
    
    smallest = gcd_place(smallest, D_list[i])

print(smallest)


