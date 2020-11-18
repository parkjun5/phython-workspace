## queue == fifo 선입선출

# B F S?
C
queue = []
begin = 0
end = 0

## begin 부터 end 전까지 push

queue.append(2)
end += 1

queue.append(3)
end += 1

print(queue)
## pop

queue.pop(begin)
queue.pop(begin)
begin += 1


print(queue)