import sys
sys.setrecursionlimit(10**9)

def total(starts, n):
    if starts > n:
        return 0
    return starts+ total(starts+1, n) 
    
n = input()
n = int(n)
starts = 1
print(total(starts, n))