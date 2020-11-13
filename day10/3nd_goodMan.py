n = input()
n = int(n)
lists =[]
for i in range(n):
    name, score = input().split()
    score = int(score)
    lists.append([name,score])


for i in range(n):
    for j in range(i+1,n):
        if lists[i][1] < lists[j][1]:
            temp = lists[i]
            lists[i] = lists[j]
            lists[j] = temp




print(lists[2][0])