##파일 입출력
# "w">> write 쓰기위한 목적이다.
# score_file = open("score.txt","w",encoding="utf8")

# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)

# score_file.close()
#score_file이라는 변수를 만들고
#  w >> 덮어쓰기가 된다. a 업핸드 이어써서 덮어쓰기 x

# score_file = open("score.txt", "a", encoding="utf8")

# score_file.write("과학 : 90\n")
# score_file.write("코딩 : 100")
# score_file.close()


# new_file = open("newone.txt","a", encoding="utf8")
# new_file.write("안녕?")
# new_file.close()

# ## r 은 리딩 읽어보겠다
# score_file = open("score.txt", "r", encoding="utf8")

# ## 한번에 다읽는 방법
# print(score_file.read())
# score_file.close()


# 한줄씩 읽는 방식

# score_file = open("score.txt", "r", encoding="utf8")
# #한줄을 읽어오고 
# # 커서는 다음줄로 이동 수학 : 0값을 가져오고 그다음 영어쪽으로 커서가 간다
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# while True :
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end ="")

# score_file.close()

score_file = open("score.txt","r",encoding="utf8")
#readlines 모든 라인을 배열로 가져온다.
lines = score_file.readlines()

for line in lines:
    print(line, end="")


score_file.close()