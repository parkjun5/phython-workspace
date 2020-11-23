memory = [0 for i in range(30)]

def fibo(num):
    if num <=1:
        return num
    elif memory[num] != 0:
        return memory[num]
    else:
        memory[num] = fibo(num-1) + fibo(num-2)
        return memory[num]


print(fibo(10))
print(memory)