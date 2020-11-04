# def profile(name, age, main_lang):
#     print(name,age,main_lang)
# ##함수의 파라미터를 순서 상관없이 이름으로 줘서 딱딱 줄수있다.

# profile(age =20,name ="ㅂㅂ",main_lang= "파이썬")

# profile(main_lang="자바",age=99,name= "박세준")
# ## print 뒤에 , end를 붙으면 줄을 바꾸지말고 다음 str을 출력해준다.
# def profile(name, age, lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0}\t\나이: {1}\t".format(name,age), end= " ")
#     print(lang1,lang2,lang3,lang4,lang5)

#이런 많은 수를 처리할땐 가변인자를 이용하면 좋다.
#*붙으면 가변인자를 뜻
def profile(name, age,*language):
    print("이름 : {0}\t\나이: {1}\t".format(name,age), end= " ")
    
    # print(lang for lang in language)
    for lang in language:
        print(lang , end= " " )
    print()

print("유재석", 20 ,"python","java","c","C++","c#","JavaScript")
print("박세준", 25 ,"Kotilin","Swift")


