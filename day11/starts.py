n = input()
n =int(n)

for i in range(n):
    if i == n-1:
        for j in range(n*2-1):
            print("*", end="")
    else:
        for j in range(n-1-i):
            print(" ", end="")
        print("*",end="")
        for k in range(i*2-1):
            print(" ",end="")
        if i != 0:
            print("*")
        else:
            print()

