## 순열과 조합에서 사용한다
## 순열  ABC ACB BAC CAB CBA
## 조합 AB AC BC

data = ['A', 'B', 'C']

## 순열
from itertools import permutations

result = list(permutations(data, 2))

print(result)
 
print()

## 중복 허용 모든 순열

from itertools import product

result3 = list(product(data,repeat=2))

print(result3)
print()

## 조합
from itertools import combinations

result2 = list(combinations(data, 2))

print(result2)




print()
## 중복 허용 모든 조합

from itertools import combinations_with_replacement

result4 = list(combinations_with_replacement(data,2))

print(result4)
