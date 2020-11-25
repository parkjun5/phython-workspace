
arr = [('홍길동', 50),('이순신', 37),('아무개', 74),]

def my_key(x):
    return x[1]
# 정렬 기준을 만들어 줄수있다.
# print(sorted(arr, key = my_key))

print(sorted(arr, key = lambda x : x[1]))

# print((lambda a, b: a+b) (3,7))


list1  =  [1, 2, 3, 4, 5]
list2  =  [6, 7, 8, 9, 10]


result = map(lambda a, b : a+b, list1, list2)

print(list(result))