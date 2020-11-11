# a, b= input().split()
# a = int(a)
# b = int(b)
# if b>=a :
#     print(1)
# else:
#     print(0)


# a, b= input().split()
# a = int(a)
# b = int(b)
# if b!=a :
#     print(1)
# else:
#     print(0)

# a = input()
# if int(a) == 0:
#     print(1)
# else:
#     print(0)

# a, b = input().split()

# if int(a) == 1 or int(b) == 1:
#     print(1)
# else:
#     print(0)

# a, b = input().split()

# if int(a) == int(b):
#     if int (a)==0:
#       print(1)
#     else:
#         print(0)
# else:
#     print(0)


# a = input()
# n = bin(~int(a))
# print(int(n,2))

# a, b = input().split()
# answer = bin(int(a) & int(b))
# print(int(answer,2))

# a, b = input().split()
# answer = bin(int(a) | int(b))
# print(int(answer,2))

# a, b = input().split()
# answer = bin(int(a) ^ int(b))
# print(int(answer,2))


# 삼항 연산자!

# 123> 457 ? 0 :1
# 파이썬의 신기한 연ㅅ나자
# a, b  =  input().split()
# print(int(a) if int(a)>int(b) else int(b))

# print(0 if 123>457 else ("두번째 ㄷㄷ" if 52 > 37 else "no"))


# a, b, c = input().split()
# a =int(a)
# b =int(b)
# c =int(c)

# print((a if a < c else c) if a < b else (b if b < c else c))

# a, b, c = input().split()
# a =int(a)
# b =int(b)
# c =int(c)

# if a % 2 ==0:
#     print("even")
# else:
#     print("odd")
# if b % 2 ==0:
#     print("even")
# else:
#     print("odd")
# if c % 2 ==0:
#     print("even")
# else:
#     print("odd")


# a = input()

# a = int(a)
# if a <0 :
#     print("minus")
#     if a % 2==0:
#         print("even")
#     else:
#         print("odd")
# else:
#     print("plus")
#     if a% 2==0:
#         print("even")
#     else:
#         print("odd")

# a = input()

# a = int(a)
# if a > 89 :
#     print("A")
# elif a > 69:
#     print("B")
# elif a > 39 :
#     print("C")
# else:
#     print("D")

# a = input()
# if   a == "A" :
#     print("best!!!")
# elif a == "B":
#     print("good!!")
# elif a == "C":
#     print("run!")
# elif a == "D":
#     print("slowly~")
# else:
#     print("what?")

# function 만들어보기!
# def function_1(value):
#     return {
#         12 : "winter",
#         1  : "winter",
#         2  : "winter",
#         3  : "spring",
#         4  : "spring",
#         5  : "spring",
#         6  : "summer",
#         7  : "summer",
#         8  : "summer",
#         9  : "fall",
#         10 : "fall",
#         11 : "fall"

#     }.get(value, -1)

# season = input()
# season = int(season)

# # print(function_1(season))
# temp = input().split()
# for a in temp:
#     if a == "0":
#         break
#     print(a)
# temp2 = input()
# temp = input().split()

# for a in temp:
#     print(a)

# n = input()
# n = int(n)
# answer = 0
# for i in range (1 , n+1):
    
#     if i % 2 ==0:
#         answer += i
# print(answer)


# strs = input().split()

# for str1 in strs:
#     print(str1)
#     if str1 =="q":
#        break

# tmp = input()
# temp = int(tmp)
# max_1 = 0
# for num in range(1,50):
#     max_1 +=num
#     if max_1 >= temp :
#         print(num)
#         break
# n = input()
# n_int = int(n,16)

# for j in range(1,16):
    
#     print("{0}*{1}={2}".format(n,str(hex(j))[2:].upper(), str(hex(n_int*j))[2:].upper() ))

# m = int(m)
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(i, j)

# range_int = input()
# range_int = int(range_int)
# for i in range(1,range_int+1):
#     if i % 3 ==0:
#         print("X" , end=" ")
#     else:
#         print(i , end=" ")

# r, g, b = input().split()

# r = int(r)
# g = int(g)
# b = int(b)
# count = 0
# for i in range(0,r):
#     for j in range(0,g):
#         for k in range(0,b):
#             print(i,j,k)
#             count +=1

# print(count)


# h,b,c,s = input().split()
# total_data =int(h)*int(b)*int(c)* int(s) /8 /1024/1024
# count = 1
# while total_data > 1024:
#     count +=1
#     total_data = total_data /1024


# if count ==1 :
#     print("{0} MB".format(round(total_data,1)))
# elif count ==2 :
#     print("{0} GB".format(round(total_data,1)))
# else:
#     print("{0} TB".format(round(total_data,1)))


w, h, b = input().split()
total_data =int(w)*int(h)* int(b) /8 /1024/1024
print("{0:0<4} MB".format(round(total_data,2)))

