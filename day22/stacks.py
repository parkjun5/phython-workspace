
# prices = [1, 2, 3, 2, 3]
# answer = [0 for _ in range(len(prices))]
# for i in range(len(prices)):
#     for j  in range(i+1, len(prices)):
#         answer[i] += 1
#         if prices[i] > prices[j]:
#             break


# n = 5000
# a = 0
# while n > 0:
#     if n % 2 ==0:
#         n /= 2
#     else:
#         n -= 1
#         a +=1
# print(a) 

# def make(temp, i, t):
#     if  i > len(number)-1:
#         return
#     elif len(temp) == t and temp not in answers:
#         answers.append(temp)
#         make(temp[:-1], i, t)
#     else:
        
#         for j in range(i+1, len(number)):
#             temp2 = temp + "" + number[j]
#             make(temp2, j, t)

        

# number = "12345"
# k =3
# t = len(number)- k
# answers = []
# temp = ""
# for i in range(len(number)):
#     temp = number[i]
#     make(temp, i, t)
    
# print(answers)
# answers.sort(reverse=True)
# print(answers[0])

##풀리긴 하는데 느림
#
number = [5,4,5,3,4,1]
k =2

answer = []

for (i , num) in enumerate(number):
#     # print("{0}은 번째, {1}은 값".format(i,num))
    while answer and answer[-1] < num and k > 0:
        answer.pop()
        k-=1
    answer.append(num)
answer = answer[:-k] if k > 0 else answer
print(answer)
ans = "".join(answer)

# while number: ## << mean 리스트가 채워져있어야 한다!/.
    
#     print(number)
#     number.pop()
# # print(answer)
# # print(k)
