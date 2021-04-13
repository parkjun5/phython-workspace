# N = int(input())
# arr = []
# for _ in range(N):
#     arr.append(int(input()))

# arr.sort( reverse= True)

# print(arr)


# N = int(input())
# arr = []
# for _ in range(N):
#     name, score = input().split()
#     arr.append([name, int(score)])

# arr.sort(key = lambda x: x[1])

# for name in arr:
#     print(name[0])

N, K = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()
B_list.sort(reverse=True)

for i in range(K):
    if A_list[i] < B_list[i]:
        A_list[i] , B_list[i] = B_list[i] , A_list[i]
    else:
        break

# result = 0
# for num in A_list:
#     result += num

# print(result)
print(sum(A_list))