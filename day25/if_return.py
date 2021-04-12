

def pabo(i):
    if i == 3:
        return i
    return i * pabo(i+1) 


print(pabo(1))