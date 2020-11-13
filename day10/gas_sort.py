n = input()
n = int(n)
lists =[]
for i in range(n):
    lists.append(list(map(int,input().split())))

for i in range(n):
    for j in range(i+1 ,n):
        if lists[i][0] > lists[j][0]:
            temp = lists[i]
            lists[i] = lists[j]
            lists[j] = temp

for [index, gas_value] in lists:
    print(index, gas_value)