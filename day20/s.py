v= [[1, 4], [3, 4], [3, 10]]

answer = [v[0][0], v[0][1]]
if answer[0] == v[1][0]:
    answer = v[2][0]
if answer[1] == v[1][1]:
    answer[1] = v[2][1]

print(answer)