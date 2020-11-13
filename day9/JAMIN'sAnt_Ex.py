a = 10
miro = [[0 for cols in range(a) ] for rows in range(a)]

for row in range(a):
    miro_example = input().split()
    for col in range(a):
        miro[row][col] = int(miro_example[col])
start_x, start_y = 1,1 
count =0
while count<20 :  
    if miro[start_x][start_y] ==2:
        miro[start_x][start_y] =9
        break
    if miro[start_x][start_y] ==0:
        miro[start_x][start_y] =9
 
    if miro[start_x][start_y+1] != 1:
        start_y +=1

    elif miro[start_x+1][start_y] != 1:
        start_x +=1
    count +=1

for m in miro:
    for a in m:
        print(a, end=" ")
    print()

