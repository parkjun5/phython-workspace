def odds(a, b):
    if a > b:
        return False
    elif a % 2 ==1:
        print(a)
    odds(a+1, b)



a, b= map(int, input().split())

odds(a, b)