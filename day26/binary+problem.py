

def binary_se(arr, want, first, end):
    if first >= end:
        return False

    mid = (end + first)//2
    if arr[mid] == want:
        return True
    elif arr[mid] > want:
        return binary_se(arr, want, first, mid-1)
    else:
        return binary_se(arr, want ,mid+1 , end)


N = 5
arr = [8, 3, 7, 9, 2]
M = 3
wanted = [5, 7, 9]

# if want in arr wanted > Yes else: NO
arr.sort()


answers =[]
for want in wanted:
    if binary_se(arr, want, 0, len(arr)) == True:
        answers.append("yes")
    else:
        answers.append("no")
print(answers)



for wa in wanted:
    if wa in arr:
        answers.append('YES')
    else:
        answers.append('NO')
print(answers)