## sep >> 새퍼레이트 문자열 사이 ,부분을 어떻게 처리하는걸 정해준다
# 혹시 \n같은것도 되나? 되넹..

# print("Python", "Java","JavaScript", sep=" ," ,end ="?\t")
# print("무엇이 더 재미있을까요?")

# import sys

# print("Python", "Java", file= sys.stdout)
# print("Python", "Java", file= sys.stderr)
# #크게 차이가 없어보이닊지만
# ## stdout 는 표준 출력
# ## stderr 표준 에러로 나온다.

# scores ={"수학" : 0, "영어" : 50,"코딩" : 100 }
## items는 키와 밸류가 튜플로 쌍으로 나온다
# for subject, score in scores.items():
    # print(subject, score)
    # ## ljust의 의미 8자리를 확보한후 왼쪽 정렬
    # just 문법은 str만 사용가능/
    # print(subject.ljust(3), str(score).rjust(4), sep =":")

# 은행 대기 순번표
# 001, 002 ,003, 004 
# zfill >>> zero fill () 얼마만큼

# for num in range(1 , 21):
#     print("대기번호 : "+str(num).zfill(3))
# input에서 받아지는 값은 앵간해선 str이다.

answer =input("아무 값이나 입력하세요. : ")

print("입력하신 값은 "+answer+"입니다.")
