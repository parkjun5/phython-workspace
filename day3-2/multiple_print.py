# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10} ".format(500))
#       500 ㄷㄷ 이게 나오네
#10공간 확보 빈자리는 블랭크 +or -처리
# 양수일 때는 +로 표시, 음수 일때는 -로 표시하는 것.
# 주식같은거  음수일경우 바로 -나오지만 양수는 + 표시해줘야 뜸

# print("{0: >+10} ".format(500))
# print("{0: >-10} ".format(500))
# print("{0: >-10} ".format(-500))


# 왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0:_<10} ".format(500))
# print("{0:_<+10} ".format(500))

# 세번째 수마다 ,찍어주기
# 콤마는 살짝 특이하다 마지막에 ,를 해줘야한다.


# print("{0:+,}".format(151551515))

# # 3자리 마다 콤마를 찍어주며 부호도 붙이고 자릿수 확보
# # 돈이 많으면 행복하니까 빈자리 ^ 채워주기

# print("{0:^<+30,}".format(100000000000))

# 소수점 출력하자
## 특정 자리까지만 표시하기 f 앞에 0.~ 작성
print("{0:0.1f}".format(5/3))