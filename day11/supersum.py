def supersum(a, b):
    if a ==0:
        print(b)
        return b
    for i in range(b):
        return 0+ supersum(a-1,i)

a = 1
b = 3

print(supersum(a, b))