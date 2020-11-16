n = input()
n =int(n)
count =0
while True:
    
    if n == 1:
        print(count)
        break
    else: count+=1
    if n %3 ==0:
        n = n/3
    elif n%3 ==1:
        n -=1
    elif n % 2 ==0:
        n = n/2
    else:
        n -=1
