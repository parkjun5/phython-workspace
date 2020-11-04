# 집합 (set)
# 중복이 안됨 순서 x

# list의 경우 []로 설정
# set = {}로 설정
my_set = {1,2,3,3,3}

print(my_set)

java = {"유재석", "김태호", "양세형"}

python = set(["유재석", "박명수"])

# 교집합 << 자바와 파이썬 둘다 가능한 사람

print(java & python)

print(java.intersection(python))

# 합집합 자바도 할수 있거나 파이썬도 할수있는 개발자
# 순서가 없음
print(java | python)
print(java.union(python))

# 차집합 ( 자바는 할줄 알지만 파이썬는 못하는 사람)

print(java - python)

print(java.difference(python))


## python을 할줄아는 사람 증가시 >>

python.add("김태호")
print(python)


# 자바를 까먹은 사람
java.remove("김태호")
print(java)