import math
arr = [ 0, 2, 4, 6, 8, 10, 12, 14, 16, 18 ]


def binary_search(arr, target, first, last):
    if first > last:
        return None
    truncs = (last + first)//2
    if target == arr[truncs]:
        return truncs
    elif target > arr[truncs]:
        return binary_search(arr, target, truncs+1, last)
    elif target < arr[truncs]:
        return binary_search(arr, target, first, truncs-1)
        


target = 4

answer = binary_search(arr, target, 0 , len(arr))

print(answer)