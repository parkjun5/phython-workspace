# 큐는 선입 선출 구조이다!


from collections import deque

queue = deque()

queue.append(1)
queue.append(2)

queue.append(3)
queue.append(4)

queue.append(5)
queue.append(6)

print(queue)

queue.popleft()


print(queue)
queue.popleft()


print(queue)
