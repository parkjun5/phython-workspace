m, n = map(int,input().split())
stus =[] 
scores =[]
for i in range(m):
    name, score = input().split()
    score= int(score)
    scores.append(score)
    stus.append([name, score])

sorted_scores = sorted(scores)
sorted_scores.reverse()
for i in range(n):
    for j in range(m):
        if sorted_scores[i] == stus[j][1]:
            print(stus[j][0])
            del stus[j]
            break