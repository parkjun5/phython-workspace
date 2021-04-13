# first is basic Fibonaci

arr = [1] * 100 

def fibo(i):
    print('f('+ str(i)+')', end =" " )
    if i == 1 or i == 2:
        return 1
    if arr[i] !=1:
        return arr[i]
    arr[i] = fibo(i-1) + fibo(i-2)
    return arr[i]
fibo(15)
# print(arr)