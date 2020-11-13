def quick_srt(numList):
    if len(numList) <=1:
        return numList
    pivot = numList[len(numList)//2 ]
    
    less_list, eqaul_list, more_list = [], [], []
    
    for num in numList:
        if num > pivot:
            more_list.append(num)
        elif num < pivot:
            less_list.append(num)
        else:
            eqaul_list.append(num)
    
    return quick_srt(less_list)+eqaul_list+quick_srt(more_list)


n = input()
lists =list(map(int,input().split()))
lists=quick_srt(lists)
for num in lists:
    print(num, end= " ")
