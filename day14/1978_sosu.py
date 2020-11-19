import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int,(sys.stdin.readline().rstrip().split())))

count = 0
for num in nums:
    flag = True
    if num <2:
        continue
    else:
        i = 2
        while i*i <= num:
            if num % i ==0:
                flag = False
            i += 1
    if flag == True:
        count += 1
print(count)