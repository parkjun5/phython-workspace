def colach(num):
    if num == 1:
        return
    if num % 2 ==1 :
        num = num*3+1
        colach(num)
        print(num)
    else:
        num = num//2
        colach(num)
        print(num)

num = input()
num = int(num)

colach(num)
print(num)
