a, b, c =input().split()
a = int(a)
b = int(b)
c = int(c)
list = [a,b,c]
for a in range(2):
    if list[0] > list[1]:
        temp = list [0]
        list[0]  = list[1]
        list[1] = temp
    if list[1] > list[2]:
        if list[0] > list[2]:
            temp2 =list[2]
            list[2]  = list[0]
            list[0] = temp2
        else:
            temp2 =list[2]
            list[2]  = list[1]
            list[1] = temp2 
            
for num in list:
    print(num ,end =" ")