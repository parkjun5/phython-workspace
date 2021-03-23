import sys

# ex 3 3
# ex 3 1 2 
# ex 4 1 4
# ex 2 2 2
# 이경우 3번째 열의 2가 제일 낮기때문에 2가 정답

N, M = map(int, sys.stdin.readline().rstrip().split())
lists = [[1 for _ in range(M)] for _ in range(N)]
for k in range(N):
        temp = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(len(temp)):
            lists[k][j] = temp[j]
mins = 0
cotae = 0
for i in range(N):
    
    if mins < min(lists[i]):
        cotae = i
        mins =min(lists[i])

print(cotae , mins)

