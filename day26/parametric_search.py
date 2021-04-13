def cutting(ex_arr, exM ,first, end, result):
    if first > end:
        return result
    mid = (end+first) //2
    cut =0
    
    for num in ex_arr:
        if num > mid:
            cut += num -mid
    if cut < exM:
        return cutting(ex_arr, exM ,first, mid-1, result)
    else:
        
        result = mid
        return cutting(ex_arr, exM ,mid+1, end, result)



# N, M = int(input().split())
# arr = list(map, int(input().split()))
exN = 4 
exM = 41 
ex_arr= [ 19, 15, 10, 17]
result = 0
# # 0~~ 19 
# # ex_arr.sort(reverse=True)
# print(cutting(ex_arr, 0,exM, ex_arr[0]))




result = cutting(ex_arr,exM, 0, max(ex_arr), result)

print(result)