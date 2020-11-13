badoks = [ [0 for cols in range(19)] for row in range(19)  ]

# for row_num in range(19):
#     rows = input().split()
#     for col_num in range(19):
#         badoks[row_num][col_num] = int(rows[col_num])

# n = input()
# n = int(n)

# for count in range(n):
#     x_pos, y_pos = input().split()
#     x_pos = int(x_pos)-1
#     y_pos = int(y_pos)-1

#     ## 제거 시작
#     for row_num in range(19):
#         if badoks[x_pos][row_num] == 1:
#             badoks[x_pos][row_num] =0
#         else:
#             badoks[x_pos][row_num] =1
        
#     for col_num in range(19):
#         if badoks[col_num][y_pos] == 1:
#             badoks[col_num][y_pos] =0
#         else:
#             badoks[col_num][y_pos] = 1
    


# for row_num in range(19):
#     for col_num in range(19):
#         print(badoks[row_num][col_num], end= " ")
#     print()