
def pabonachi(count, n, arr):
    if count == n:
        return arr
    temp = arr[0]+ arr[1]
    arr[0] = arr[1]
    arr[1] = temp
    pabonachi(count+1, n, arr)
    return arr


arr = [1, 1]
n = input()
n = int(n)

if n>2:
    arr=pabonachi(2, n, arr)
    print(arr[1]%10009)
else:
    print(1)

