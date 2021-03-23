# N, K = map(int, input().split())

# D =[[0]*201 for _ in range(201)]
# mod =1000000000
# # D[K][N] = D[K-1][N-L]
# for i in range(1, 201):
#     D[i][1] = 1
#     for j in range(201):
#         for L in range(j+1):
#             D[j][i] += D[L][i-1]
#         D[j][i]%mod

# print(D[N][K]%mod)
# for i in range(N):
import sys 
N, K = map(int, sys.stdin.readline().split())
mod = 1000000000
table = [1]
table += [0] * N
for _ in range(1, K+1): 
    for idx in range(1, N+1):
         table[idx] = (table[idx] + table[idx-1])%mod
sys.stdout.write(str(table[N]))
