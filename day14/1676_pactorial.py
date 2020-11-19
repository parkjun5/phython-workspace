import sys

N = int(sys.stdin.readline().rstrip())

# if 100 ! 이라면 5만 찾아주면 된다. 
# 100 / 5   =20
# 20  / 5 =  4  2개 들어가는 친구들 25 / 50 75 100


count =0
while N >0:
    count+= N // 5 

    N = N//5
print(int(count))
