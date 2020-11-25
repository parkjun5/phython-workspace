
# m = 5
# n =4
# arr = [[0] * m for _ in range(n)]

# arr[1][1] =5
# arr[2][2] =5
# arr[3][3] = 5
# for a in arr:
#     print(a)
# print()
# arr[1].insert(1, 99)
# for a in arr:
#     print(a)

# a =[1, 2, 3, 4, 5, 5, 5]
# remove_set = {3, 5}


# result = [i for i in a if i not in remove_set]


# print(result)

# strs = "HEo"
# Str2 = "LL@@@"

# print(strs+" "+Str2)


# print(strs*3)

# print(Str2[2:])


# data = dict()

# data["사과"] = "Apple"
# data["바나나"] = "Banana"
# data["코코넛"] = "coconut"

# if '사과' in data:
#     print(data)

# print(data['사과'])

# key_lists = data.keys()
# vals = data.values()




# print(key_lists, vals)


# ley = {
#     "하이" :"hi",
#     "new" : 32

# }

# print(ley)


#  집합 자료형은 중복자료 x
# 순거가 없다.

data2 = {1,1,2,23,4,4,5,2,2,5}
data = {1,2,5,3,46}
# 합집합 이거면서 이거

print(data2 | data)

# 차집함 이거가 없는 저거

print(data2 - data)

# 교집합 같은것만

print(data2& data)

data.add(99999)

print(data)

data.update([505 ,101])
print(data)
data.remove(505)
print(data)