from collections import Counter

counter = Counter(['red', 'blue', 'Black', 'red', 'green','red','blue']) 
counter.get("red")
print(counter['blue'])
print(counter['red'])
print(dict(counter))