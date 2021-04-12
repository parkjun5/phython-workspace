import collections

phone_book = ["119", "97674223", "1195524421"]
# answer = True
# tag = phone_book[0]
# tag_len = len(tag)
# phone_book.remove(tag)

# for phone in phone_book:
#     check = phone[:tag_len]
#     if check == tag:
#         answer = False
#         break
# print(answer)
phone_book.sort(key=str.lower,reverse=True)
print(phone_book)

l = tuple(phone_book)
for i in range(len(phone_book)-1):
    k = phone_book[i]
 
    if k.startswith(l[i+1:]): 
        break