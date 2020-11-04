# 리스트 []

# 지하철 칸별로 10명, 20명, 30명

# subway1 = 10
# subway2 = 20
# subway3 = 30 lists
# subway2 = [1,2,3]
# print(subway2)
# subway = [10, 20, 30]
# bus = ["유재석", "조세호", "박명수"]
# print(bus[1])
# print(bus.index("박명수"))


# print(subway)

# # 하하 가 다음 정류ㅜ창 추가

# bus.append("하하")
# print(bus)

# # 정형돈을 유재석 / 조세ㅐ호 사이에 추가
# # 몇 번째에 누구
# bus.insert(1, "정형돈")
# print(bus)

# 지하철에서 한명씩 뒤에서 제거

# print(bus.pop())
# print(bus)

# print(bus.pop())
# print(bus)
# print(bus.pop())
# print(bus)
# print(bus.pop())
# print(bus)

# 같은 이름의 사람 몇명있는지 확인

# bus.append("유재석")
# print(bus)
# print(bus.count("유재석"))

# ## 정렬도 가능하다

# num_list= [5,4,3,2,1]

# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)

## 다양한 자료형과 함께 사용가능
num_list= [5,4,3,2,1]
mix_list = ["아녕", 1 ,True]

print(mix_list)

# 리스트의 확장

num_list.extend(mix_list)
print(num_list)