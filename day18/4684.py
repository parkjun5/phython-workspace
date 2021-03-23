import sys
N = int(sys.stdin.readline().rstrip())

nums = list(map(int,sys.stdin.readline().rstrip().split()))
remember =[]
no =[]

def checks(nums):
    
    for idx, num in enumerate(nums):
        if idx != N-1 and num- nums[idx+1] != -1:
            remember.append([idx, num])
        elif idx != N-1 and num- nums[idx+1] == -1:
            no.append([idx, num])
    

checks(nums)
remember.pop(0)
sorted_re = sorted(remember, key=lambda re: remember[1])

# for idx in range(len(re)):
#     nums[re[idx][0]]=(sorted_re[idx][1])

print(nums)
print(no)
diff = no[0][1] - no[0][0]
print(diff)
if diff <= 1:
    diff += 9
if diff % 2 ==0:
    print(diff//2)
    print(remember[0][0]+(diff//2)+1, remember[-1][0]+(diff//2)+1)
    print(diff//2)
else :
    print(diff -1)
    print(remember[0][0]+2, remember[-1][0]+2)
    print(1)

