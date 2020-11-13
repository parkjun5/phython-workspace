
# column, row = 3, 5

# array2D = [ [0 for _ in range(row)] for _ in range(column)  ]

# print(array2D)

# column, row = 3, 5

# array2D = [ [0]*row for _ in range(column)  ]

# print(array2D)



# x,y = 3,5

# array =np.ones((x,y))
# print(array)



array2D = [ [0 for col in range(10)] for row in range(10)  ]

for arr in array2D:
    for ar in arr:
        print(ar, end= " ")
    print()