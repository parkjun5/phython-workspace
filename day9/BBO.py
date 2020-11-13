row, col = input().split()
row =int(row)
col = int(col)
board = [ [0 for cols in range(col)] for rows in range(row)  ]

counts = input()
counts = int(counts)

for count in range(counts):
    # l은 막대의 길이. d는 방향 0이면 가로 1이면 ㅔㅅ로, xy는 좌표
    l, d, x, y = input().split()
    l = int(l)
    d = int(d)
    x = int(x)-1
    y = int(y)-1
    if   d == 0:# 가로 방향
        for making in range(0,l):
            if y+making >= col :
                break
            board[x][y+making] = 1
    elif d ==1: ## 세로 방향
        for making in range(0,l):
            if x+making >= row :
                break
            board[x+making][y] =1

for rows in range(row):
    for cols in range(col):
        print(board[rows][cols], end=" ")
    print()


