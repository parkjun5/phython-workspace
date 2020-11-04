
# 코드 작성중 글을 바꾸고 싶을때에는 \를 입력하면 된다.
# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이: {1}\t 주 사용 언어 {2}"\
#         .format(name,age,main_lang))

# profile("박",20,"파이썬")
# profile("준",25,"자바")

# 만약 전부 같은 학교 같은 반 같은 수업이라면 기본 값을 주어주어서 편하게 사용한다.


def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t 나이: {1}\t 주 사용 언어 {2}"\
        .format(name,age,main_lang))

profile("박세준")
profile("김태호")