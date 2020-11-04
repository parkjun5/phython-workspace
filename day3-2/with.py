# import pickle

# 피클을 활용한 기법
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))
## with 를 활용하여서 작성합니다.!
# with open("study.txt", "w" , encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어영")

with open("study.txt","r", encoding="utf8") as study_file:
    print(study_file.read(), end= "")