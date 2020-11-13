# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]

#     less_arr, equal_arr, more_arr =[], [], []

#     for num in arr:

#         if num < pivot:
#             less_arr.append(num)
#         elif num > pivot:
#             more_arr.append(num)
#         else:
#             equal_arr.append(num)

#     return quick_sort(less_arr) + equal_arr + quick_sort(more_arr)


# def binarySearch(arr,target, left, right):
#     middle_index = (left + right)//2
#     middle = arr[middle_index]
#     if target == middle:
#        return middle_index
#     elif middle > target:
#         binarySearch(arr, target, left, middle_index-1)
#     elif middle < target:
#         binarySearch(arr, target, middle_index+1 , right)

def binarySearch(array, target, left, right):
    middle_idx = (left+right)//2
    middle = array[middle_idx]
    if target == middle:
        print('{}'.format(middle_idx),end=" ")
    elif middle > target:
        binarySearch(array, target,left,middle_idx-1)
    elif middle < target:
        binarySearch(array, target,middle_idx+1,right)




n = input()
n = int(n)
lists = list(map(int,input().split()))

# sorted_list = quick_sort(lists)
sorted_list = sorted(lists)

for i in range(n):
    target = lists[i]
    binarySearch(sorted_list, target, 0, n)



