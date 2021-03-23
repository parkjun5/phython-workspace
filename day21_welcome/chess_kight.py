data = input().split()

moves = [[-1,2],[-2,1],[1,2],[2,1],[-1,-2],[-2,-1],[1,-2],[2,-1]]

# c = ord('a')
# print(c)
count =0
for move in moves:
    data_x = ord(data[0]) +move[0]
    data_y = int(data[1])+ move[1]
    if data_x > 96 and data_x <105:
        if data_y >0 and data_y < 9:
            count += 1

print(count)
