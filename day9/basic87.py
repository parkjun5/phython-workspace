from random import *

# a = input()
# a = int(a)
# hap =0
# i =1
# while hap < a:
#     hap +=i
#     i+=1

# print(hap)

# a = input()
# a = int(a)
# i =0
# while i < a:
#     i +=1
#     if i%3 ==0 :
#         pass
#     else:
#         print(i, end="")

# a, d, n  = input().split()
# a = int(a)
# d = int(d)
# n = int(n)
# print(a + (n-1)*d)

# a, d, n  = input().split()
# a = int(a)
# d = int(d)
# n = int(n)
# print(a * (d**(n-1)))


# a, m, d, n  = input().split()
# a = int(a)
# m = int(m)
# d = int(d)
# n = int(n)
# # print(a * (d**(n-1)))
# x= a*m+d
# if n !=1 :
#     for n_i in range(2, n):

#         x= x*m+d
#         if n-1 == n_i:
#             print(x)
# else : 
#     print(a)


# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# days =1
# while True:
#     if days % a==0:
#         if days % b == 0:
#             if days %c  == 0:
#                 print(days)
#                 break
#     days +=1

# n = input()
# n = int(n)
# calls = input().split()
# students = []
# for i in range(1, 24):
#     temp =0
#     temp = calls.count(str(i))
#     students.append([i,temp])

# for i,j in students:
# #     print(j, end=" ") 
# n = input()
# calls = input().split()
# calls.reverse()
# for i in calls:
#     print(i, end=" ")


# for i,j in students:
#     print(j, end=" ") 

# n = input()
# calls = input().split()
# min =999
# for i in calls:
#     i = int(i)
#     if min > i:
#         min = i
# print(min)

# n = input()
# n = int(n)
# badoks = []
# for i in range(0, 20):
#     for j in range(0, 20):
#         badoks.append([i,j],0)


# # for i in range(0, 5):
# badoks = [ [0 for cols in range(19)] for row in range(19)  ]
# n = input()
# n = int(n)
# for a in range(n):
#     x, y =input().split()
#     x = int(x)-1
#     y = int(y)-1
#     badoks[x][y] =1




# for ba in badoks:
#     for b in ba:
#         print(b, end=" ")
#     print()


# badoks = [ [0 for cols in range(19)] for row in range(19)  ]

# for row in badoks:

# for row_num in range(19):
    
#     for col_num in range(19):
#         n = input()
#         n =int(n)
#         badoks[row_num][col_num] = n
#         print(badoks[row_num][col_num] , end=" ")

# badoks = [ [0 for cols in range(19)] for row in range(19)  ]

# for row_num in range(19):
#     rows = input().split()
#     for col_num in range(19):
#         badoks[row_num][col_num] = int(rows[col_num])

# n = input()
# n = int(n)

# for count in range(n):
#     x_pos, y_pos = input().split()
#     x_pos = int(x_pos)-1
#     y_pos = int(y_pos)-1

#     ## 제거 시작
#     for row_num in range(19):
#         if badoks[x_pos][row_num] == 1:
#             badoks[x_pos][row_num] =0
#         else:
#             badoks[x_pos][row_num] =1
        
#     for col_num in range(19):
#         if badoks[col_num][y_pos] == 1:
#             badoks[col_num][y_pos] =0
#         else:
#             badoks[col_num][y_pos] = 1
    


# for row_num in range(19):
#     for col_num in range(19):
#         print(badoks[row_num][col_num], end= " ")
#     print()