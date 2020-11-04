""" 표준 체중 구하는 프로그램

남 m * m *22
여 m * m *21

조건 1 표준 체중은 별도의 함수 내에서 계산
        함수 명  std_weight
        전달 값 : height , gender
조건 2 표준 체중은 소수점 둘째짜리까지 표시

출력예제
키 175cm 남자의 표준 체중은 67.38kg입니다.

"""

def std_weight(height, gender):
    height = (int(height)/100)
    if gender == "남":
       
        return height*height*22
    else: 
        return height*height*21

height = input("키를 입력해주세요 (cm)")
# gender =""
# while gender !="남"& gender !="여":
gender = input("성별을 입력해주세요 ex)남 or 여")
std_weights = round(std_weight(height,gender), 2)

print("키 {0}cm {1}의 표준 체중은 {2}입니다".format(height, gender, std_weights))