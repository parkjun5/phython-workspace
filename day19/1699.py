# N 이 주어줬을때 제곱수로 표현하기

#ex 11 = 3*3 + 1*1 + 1*1

N = int(input())
D = [i for i in range(N+1)]
for i in range(1,N+1):
    for j in range(i):
        if j*j > i:
            break
        if D[i] > D[i-j*j]+1:
            D[i] =D[i-j*j]+1

print(D[N])