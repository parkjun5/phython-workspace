
## 피클?
## pickle.py라는 이름으로 파일을 작성하면 프로그램이 혼동하여 오류가 발생할수있다.
## 프로그램상의 데이터를 파일 형태로 저장해주는 것

## 이 파일로 넣은 데이터는  피클로 사용하여 다시 쓸수있다!


## write + b <<< 바이너리 타입
## 피클을 사용하기 위해서는 이 바이너리 타입을 설정하는 것이 중요하다.,
# 피클은 인코딩 안해도 댄다 개이듣ㄱ!
import pickle
profile_file = open("profile.pickle", "wb")
profile_data = {"이름":"박세준","나이": 25, "취미": ["축구", "골프", "코딩"]}
print(profile_data)
#프로필 데이터의 정보를 파일에 저장하는  피클 덤프! 
pickle.dump(profile_data, profile_file)
profile_file.close()