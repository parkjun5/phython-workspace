## continue와 break 

absent = [2 , 5,1] # 결석
no_book = [7] #책을 두고옴

for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지 {0}번 따라와".format(student))
        break
    print("{0}번 읽어봐".format(student))


