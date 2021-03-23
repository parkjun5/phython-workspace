import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))


D = [1 for _ in range(N)]
for i in range(1, len(D)):
    
    for j in range(i-1, -1, -1):
        if A[i] > A[j]:
            if D[i] <= D[j]:
                D[i] = D[j] +1


print(max(D))
