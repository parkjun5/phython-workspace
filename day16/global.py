a = 0

def func():
    global a
    a +=1
    print(a)


for i in range(10):
    func()
    
