import sys

n, m = map(int, sys.stdin.readline().strip().split())

# lists = [i for i in range(2, n+1)]
# list2 = [i for i in range(m,n+1)]
# # cont = 0
# # while n >= lists[cont]*lists[cont]:
# #     i = lists[cont]
# #     for a in range(lists.index(i)+1, len(lists) ):
# #         if a % i ==0:
# #             lists.pop(lists.index(a))
# #     print(lists)
# #     cont +=1
# for i in lists:
#     j =2
#     if list2.count(i) != 0:
#         while i*j <= n:
#             list2[i*j-m] = 0
#             j += 1
#         print(i)
def isPrime(num):
    if num <2:
        return False
    else: 
        i = 2
        while i*i <=num:
            if num % i ==0:
                return False
            i += 1
        return True



for num in range(n, m+1):
    if isPrime(num): print(num)


