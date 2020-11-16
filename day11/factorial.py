def factori(num,n):
    if n == num:
        return n
    return  num* factori(num+1, n)

n = input()
n = int(n)

a = factori(1, n)

print(a)