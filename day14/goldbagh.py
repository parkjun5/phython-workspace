import sys
# nums = []
# lists = [i for i in range(2, 1000000)]
Max = 1000000
check = [False, False]+ [True] *(Max -1)
primes = []
count =0

for i in range(2, Max+1):
    if check[i]:
        primes.append(i)
        count += 1
        for j in range(i*2, Max+1 ,i): # i만큼 늘려준다.
            check[j] = False

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break
    for i in range(1, count):
        if check[i] is True:
            j = N - i
            if check[j] is True:
                print("{0} = {1} + {2}".format(N, i, j))
                break

# def findgold(num, list2):
#     for sosu in list2:
#         if sosu !=0:
#             for sosu2 in list2:
#                 if sosu2 !=0 and sosu2 != sosu:
#                     if num == sosu +sosu2:
#                         print("{0} = {1} + {2}".format(num, sosu, sosu2))
#                         return True
#     return False

# while True:
#     n = int(sys.stdin.readline().strip())
#     if n == 0 :
#         break
#     nums.append(n)

# for i in lists:
#     j =2
#     if list2.count(i) != 0:
#         while i*j < 1000000:
#             list2[i*j-2] = 0
#             j += 1
# list2.pop(0)

# for num in nums:
#      flag = findgold(num, list2)
#      if flag == False:
#          print("Glodbach's conjecture is wrong")
