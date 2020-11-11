# print(input())
# x = input()
# y = input()
# x,y = input().split()

# print(y, x)

# a, b = input().split()
# a= int(a)

# print(type(a), b)

# a = round(float(input()),2)
# print("{0:0<4}".format(a))

# a = input()

# print(a, a, a) 

# h, m  = input().split(":")
# print("{0}:{1}".format(h,m))

# yy,mm,dd = input().split(".")

# print("{0}.{1:0>2}.{2:0>2}".format(yy,mm,dd))

# temp=input()
# temp1 = temp[0:6]
# temp2 = temp[-7:]
# print(temp1+temp2)

# data= []
# data.append(input())
# print(data[0])

# a = input()


# change = a.find(".")
# temp = a[0:change]

# temp2 = a[change+1:]

# print("{0}\n{1}".format(temp, temp2))

# temp = input()

# for i in range(0,len(temp)):
#     print("[{0}]".format(int(temp[i])*10**(len(temp)-i-1)))

# a = float(input())
# print("%f" %a)

# h,m,s = input().split(":")
# if int(m[0]) == 0 :
#     print(m[1])
# else:
#     print(m)


# yy,mm,dd = input().split(".")

# print("{2:0>2}-{1:0>2}-{0:0>4}".format(yy,mm,dd))

# a = float(input())
# print("%0.11f"%a)
  


  # 8진수로 표시하기

# a = int(input())
# print("%o" %a)

    ## 16진수로 표시하기
# a = int(input())
# print("%x".upper() %a)

## 입력받은 8진수를 10진수로 처리

# f
# 입력받은 16지ㅏㄴ수 >> 8

# a = input()
# n = int(a,16)
# print("%o"%n)

##  아스키 코드 변환!
# 
# ord  == 문자를 아스키 코드로 변환
# chr  == 코드를 문자로 변환
# 
# ex 
# print(ord("A"))
# print(chr(65))

# print(chr(int(input())))


# a, b = input().split()

# # print(a,b)

# a, b = input().split()

# print(int(a)+int(b))

# print(int(input())*-1)


## 값이 들어온다 >> 아스키 코드로 변환 +1 >>>다시 캐릭터로 변환
# temp = input()
# temp_count = ord(temp)
# print(temp_count)
# temp = chr(temp_count+1)

# # print(temp)
# a,b = input().split()
# print(int(a)//int(b))

# a = int(input())+1

# print(a)

# a, b = input().split()
# a = int(a)
# b = int(b)

# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# print("%0.2f"%round(a/b,2))

# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# d = a+b+c
# print(d)
# print(round(d/3.0,1))

# #쉬프트 연산

# a = int(input())
# print(a>>1)
# print(a>>2)
# print(a<<1)
# print(a<<2)

# a, b = input().split()

# a = int(a)
# b = int(b)

# print(a <<b)
a, b = input().split()
a = int(a)
b = int(b)
if a>b :
    print(1)
else:
    print(0)
