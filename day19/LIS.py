
A = [10, 20, 10, 30 ,10, 50]
D = [1, 1, 1, 1, 1, 1]
D = [1 for _ in range(len(A))]

D[1] +=  1



for i in range(1, len(D)):
    
    for j in range(i-1, 0, -1):
        if A[i] >= A[j]:
            if D[i] <= D[j]:
                D[i] = D[j] +1
    print(D)


