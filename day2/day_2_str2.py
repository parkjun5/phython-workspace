python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
# python 길이 반환
print(len(python))
## 일시적으로 만 바꿈
print(python.replace("Python" , "JAVA"))
print(python)

#문자열 사이에 n의 위치를 표시
index = python.index("n")
print(index)
# 5+1번쨰 이후부터 찾는다.
index = python.index("n",index+1)
print(index)
#>> find 의경우 없는 값일경우 -1를 반환
##하지만 index의 경우 오류를 내보낸다.

print(python.find("JAVA"))
##count == 해당 문자열이 몇번 나오는지 확인
print(python.count("ing"))
print("ji")