def banary(n):
    if n <1:
        if n == 1:
            return "1"
        elif n ==0:
            return ""

    temp = n %2
    n =n//2
    return banary(n) + str(temp)
n = input()
n = int(n)

if n == 1:
    print(1)
elif n ==0:
    print(0)
else:
    print(banary(n))