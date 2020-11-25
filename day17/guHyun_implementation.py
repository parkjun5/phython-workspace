## 이차원 공간을 행렬로 구현하는 문제등

## Matrix! 행렬

# matrixs = [[(i, j) for j in range(5)] for i in range(5) ]
#     # 동  북  서  남
# dx  = [0, -1, 0, 1]
# dy  = [1, 0, -1, 0]

# x, y = 2, 2

# for i in range(4):
#     nx = x+ dx[i]
#     ny = y+ dy[i]
#     print(nx, ny)

# for ma in matrixs:
#     print(ma)
import sys
N = int(sys.stdin.readline().rstrip())

# maps = [[0 for _ in range(N) ]for _ in range(N)]

# for m in maps:
#     print(m)

# L 은 완 R 오
# U  위  D 아
x, y = 1,1
#     L  R   U  D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cmd_type = ["L","R","U","D"]

# for i in range(N):
cmds = sys.stdin.readline().rstrip().split()
move_x =0
move_y =0
for cmd in cmds:

    for i  in range(len(cmd_type)):
        if cmd  == cmd_type[i]:
            move_x = x+dx[i]
            move_y = y + dy[i]
    if 0 < move_x < N and 0 < move_y < N:
        x,y = move_x, move_y

print(x,y)

    # if cmd == "R":
    #     if y ==99:
    #         i -=1
    #         continue
    #     else: y += 1
    # elif cmd == "L":
    #     if y ==0:
    #         N += 1
            
    #     else: y-= 1
    # elif cmd == "U":
    #     if x ==0:
    #         i -=1
    #         continue
    #     else: x-= 1
    # else:
    #     if x ==99:
    #         i -=1
    #         continue
    #     else: x+= 1
    
    # for move in dx:
    #     if move != 0:
    #         x += move
    # for move in dy:
    #     if move != 0:
    #         y += move

# print(x+1, y+1)