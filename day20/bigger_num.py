import sys

rules = list(map(int, sys.stdin.readline().rstrip().split()))
nums = list(map(int, sys.stdin.readline().rstrip().split()))

## ex 5 8 3 
## ex 2 4 5 4 6
## 이렇게 나왔을떄 룰의 첫자리는 갯수 둘째자리는 몇개를 더하는지
## 마지막은 연속해서 사용할수있는 갯수
## 1. 정렬하여 해결한다.
## 정렬 완료
nums.sort(reverse= 1)


# rules 3 을 지키는지 확인할 check 추가
# 정답을 넣을 count 추가

check = 0
count = 0

for _ in range(rules[1]):
    if check == rules[2]:
        check = 0
        count += nums[1]
    else:
        check += 1
        count += nums[0]

print(count)