arr = [5,8,4,3,1,7,10,2,9]

#선 택 정 렬


# for i, num in enumerate(arr):


#     k = i
#     for j in range(i, len(arr)):
#         if arr[j] < arr[k]:
#             k = j
#     # 스왑 ㄷㄷ
#     arr[i], arr[k]  = arr[k], arr[i]

#     print(arr)


# for i, num in enumerate(arr):
#     for j in range(0, i):
#         if arr[j] > arr[i]:
#             arr[i], arr[j] = arr[j] , arr[i]

# print(arr)


## alcuEK..ㄷㄷ

def pythons_quickSORT(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]

    left_arr = [x for x in tail if x <= pivot]
    right_arr = [x for x in tail if x > pivot]

    return pythons_quickSORT(left_arr) + [pivot] +pythons_quickSORT(right_arr)



print(pythons_quickSORT(arr))


## 정수형 + 제한된 리스트에서 사용가능한 것

cnt_arr = [0] * (max(arr)+1)

# for i in range(len(arr)):
#     cnt_arr[arr[i]] += 1
for num in arr:
    cnt_arr[num] += 1


for i in range(len(cnt_arr)):
    for j in range(cnt_arr[i]):
        print(i , end = " ")