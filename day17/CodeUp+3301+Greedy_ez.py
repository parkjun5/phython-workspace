import sys
n = int(sys.stdin.readline().rstrip())
mon = 50000
count = 0
# while mon >= 10:
#     count += n // mon
#     n = n %mon
#     if str(mon)[0] == "5":
#         mon = mon//5
#     else:
#         mon //=2


for i in range(8):
    count += n // mon
    n = n %mon
    if str(mon)[0] == "5":
        mon //= 5
    else: mon //=2
print(count)