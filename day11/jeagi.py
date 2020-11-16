def fonts(num, n):
    if num > n:
        return False
    print(num)
    fonts(num+1,n)



n = input()
n = int(n)
fonts(1,n)