## dictionarys 

# cabinet = {3 : "유재석",8 : "박세", 99:"ace"}

# print(cabinet[3])

# print(cabinet.get(99))

# print(cabinet.get(333))  # << 오류가 나지않는다
# # int 형 vs None 이 나와야하는데  그뒤 str을 정해줄수 있다.
# print(cabinet.get(333, "사용 가능"))
# # print(cabinet[165])  # << 오류

# # 3이라는 key가 캐비넷에 존재하는가?
# print(3 in cabinet) #True
# print(55 in cabinet) # False

cabinet = {"a-1" : "유재석","a-2" : "박세"}
# print(cabinet["a-1"])

# # print("a-2" in cabinet)
# # print("B-2" in cabinet)


# # print(cabinet)

# # cabinet["a-3"] = "ace"

# # # 새로 덮어진다.
# # cabinet["a-1"] = " newone"
# # print(cabinet)

# # # 값 없애기

# del cabinet["a-2"]
## 방 자체 삭제
# print(cabinet)

# keyt들만 출력

print(cabinet.keys())
print(cabinet.values())

print(cabinet.items())

## 폐점 

cabinet.clear()

print(cabinet)