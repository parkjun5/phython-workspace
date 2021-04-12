# nums = [30, 31, 32]
# num = 34
# # 

# print(nums)
# nums.pop(2)

# nums.insert(0, 29)
# print(nums)
# for a in str(num):
#     print(a)



# for _ in range(2):
#     for i, num in enumerate(numbers):
#         if num > 9:
#             bigNums.append(num)
#             numbers.pop(i)

# # numbers.sort(reverse = True)
# # bigNums.sort(reverse = True)

# # for bigs in bigNums:
# #     for num in numbers:
# #         if str(num) == str(bigs)[0]: 
# #             for big in str(bigs):
# #                 if int(big) <int(num):
# #                     numbers.insert(i+1 , bigs)
# #                     break
# #                 elif int(big) > int(num):
# #                     if i ==0:
# #                         numbers.insert(0 , bigs)
# #                     else:
# #                         numbers.insert(i-1 , bigs)
# #                     break
        
# #     print(numbers)

# numbers = [3, 30, 34, 5, 9]	

# listss = []
# a=0
# num = list(map(str, numbers)) 
# for i,n in enumerate(num):
#     a = n*3
#     listss.append([i,a[:2]])
    
# listss.sort(key = lambda x : x[1], reverse= True)

# print(listss)
# answer = []
# for i, n in listss:
#     answer.append(str(numbers[i]))

# print(answer)

# ans = "".join(answer)
# print(ans)
# # num.sort(key = lambda x : x*3, reverse = True)


# # print(num)


# tuple_list = [('좋은하루', 0), ('niceday', 1), ('좋은하루', 5), ('good_morning', 3), ('niceday',5)]
                  
# tuple_list.sort(key=lambda x : (x[1], x[0]))  # '-'부호를 이용해서 역순으로 가능
# print(tuple_list)




number = "1924"

numbers = list(number)

print(numbers)


