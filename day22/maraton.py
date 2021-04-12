import collections
participant = ['a', 'b', 'c', 'd', 'a','e']
ends = {'b', 'a', 'd','c'}
# for coms in ends:
#     participant.remove(coms)

# print(participant)
print(collections.Counter(participant))
print(collections.Counter(ends))
a = collections.Counter(participant) - collections.Counter(ends)
answer = list(a)[0]
print(answer)
# portfolio = [
#     ('GOOG', 100, 490.1),
#     ('IBM', 50, 91.1),
#     ('CAT', 150, 83.44),
#     ('IBM', 100, 45.23),
#     ('GOOG', 75, 572.45),
#     ('AA', 50, 23.15)
# ]



# total_shares = Counter()
# for name, shares, price in portfolio:
#     total_shares[name] += shares

# total_shares['IBM']     # 150
# print(total_shares)

# ## 합계로 처리된다.

# from collections import defaultdict
# holdings = defaultdict(list)
# for name, shares, price in portfolio:
#     holdings[name].append((shares, price))
# holdings['IBM'] # [ (50, 91.1), (100, 45.23) ]

# print(holdings)
# ## 별개의 값을 처리 된다.