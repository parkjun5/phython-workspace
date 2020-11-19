# 조합의 경우

# nCm의 갯수
#        n!
#   (n-m)! * m!
import sys

def collects(nums, divi):
    count =0
    while nums>= divi:
        count += nums//divi
        nums = nums//divi
    return count

n, m = map(int, sys.stdin.readline().rstrip().split())
div_5 = collects(n, 5)- collects(n-m, 5) - collects(m, 5)
div_2 = collects(n, 2)- collects(n-m, 2) - collects(m, 2)

print(min(div_5,div_2))
