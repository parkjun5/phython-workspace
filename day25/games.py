# import sys


col , row = map(int, (input().split()))
maps = [[ 0 for _ in range(col)] for _ in range(row) ]

# print("{0} {1}" .format(col, row))

s_x , s_y, direct = map(int, (input().split()))
lists = []
for i in range(row):
    lists.append(list(map(int,(input().split()))))
    # lists = list(map(int,(input().split() )))
    # for j, l in enumerate(lists):
    #     maps[i][j] = l
maps[s_x][s_y] = 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
cnt = 0
while True:
    if direct == 4:
        break
    
    
    t_x = s_x + dx[direct]
    t_y = s_y + dx[direct]

    if maps[t_x][t_y] ==0 and lists[t_x][t_y]:
        maps[t_x][t_y] = 1
        s_x = t_x
        s_y = t_y
        direct =0
        cnt +=1
    



    direct += 1
   

print(maps)

