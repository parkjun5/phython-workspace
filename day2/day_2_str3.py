# # print("a"+ "b")
# # print("a", "b")

# # print("ab")

# # # 방법 1 %d 사용법
# # print("나는 %d살입니다" % 20)

# # print("나는 %s을 좋아해요" % "파이썬")

# # print("Aplle 은 %c 로 시작해요" % "A")

# # # %s >>
# # print("나는 %s살입니다" % 20)

# # print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨강"))
# # # 방법 2 
# # print("나는 {}살입니다.".format(20))

# # print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨강"))

# # print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨강"))



# #방법 3


# # print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20,color ="빨강"))


# # print("나는 {age}살이며, {color}색을 좋아해요".format(color ="빨강", age = 20))

# #방법 4 (v 3.6 이상부터 사용가능)
# # print (+f 를사용해서 변수를 사용가능해진다.
# age =20

# color = "빨강"

# # print(f"나는 {age}살이며, {color}색을 좋아해요")


# # ## 탈출 문자 \n : 줄바꿈 문자

# # print("백문이 불여일견 백견이\n불여일타")
# # # 저는 "나도 코딩"입니다./ << 목표
# # print('저도 "나도코딩" 입니다.')
# # # \ 역슬레쉬를 작성하여 그후 그전 빠음표는 사용안하는 것으로

# # print("저는 \"나도코딩\" 입니다.")

# # # \\ : 문장 내에서는 \<<하나의 역슬래쉬로

# # print("이래서 역슬레쉬를 두번 사용하는것 D:\\Users\\박세준\\Desktop\\phython workspace>")

# # # /r 는 커서를 맨앞으로 이동
# # 커서를 맨앞으로 이동하여 4자리 만큼을 Pine으로 변경
# print("Red Apple \rPine")

# # \b 백스페이스 (한 글자 삭제)
# print ("Redd\bApple")

# # \t 그저...탭

# print("Red\t aplle")


#QUIZ

# ex http://naver.com >>
# ex http://  부분은 삭제
# and . 이후 .com은 삭제 naver
# 남은 글자중 처음 세자리 nav + 글자갯수 (5) + 글자내 (e)개수 1+!로 구성

# ex naver > nav51!

site_address  ="http://youtube.com"

# progress_1 = site_address[7:-4]
progress_1 = site_address.replace("http://", "")
# 찾아서 바꿔준다 이게 더 좋다.
progress_1 = progress_1[:progress_1.find(".")]
# 마이너스를 안줘야한다 그러야지 5번쨰부터 끝까찌 삭제.


progress_3 = progress_1[:3]
progress_2 = len(progress_1) 
# e_find = progress_1.find("e") 카운트 문제
e_count = progress_1.count("e")
answer = progress_3+str(progress_2)+str(e_count)+"!"

print(f"{site_address}의 비밀번호는 {answer}입니다.")