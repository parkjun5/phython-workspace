def quick_sort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr)//2 ]
    lesser_arr,eqaul_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            eqaul_arr.append(num)
    return quick_sort(lesser_arr)+eqaul_arr+quick_sort(greater_arr)


arrs = [8, 1, 6, 4, 5, 2, 11 ,13, 15]
ss =quick_sort(arrs)

print(ss)