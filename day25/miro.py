N, M = map(int, input().split())

miro  = []

#미로를 만들었습니다.

for _ in range(N):
    miro.append(list(map(int, input())))

x = 0
y = 0

def miroFind(x, y, val):
    if x >= N or x < 0 or y >= M or y < 0:
        return
    
    if x == N and y == M:
        return val
    if miro[x][y] == 0:
        return
    if miro[x][y] == 1:
        miro[x][y] = val
        for mi in miro:
            print(mi)
        print()
        miroFind(x-1, y , miro[x][y]+1)
        miroFind(x, y-1 , miro[x][y]+1)
        miroFind(x+1, y , miro[x][y]+1)
        miroFind(x, y+1 , miro[x][y]+1)

    if miro[x][y]  > val :
        miro[x][y] = val
        for mi in miro:
            print(mi)
        print()
        miroFind(x-1, y , miro[x][y]+1)
        miroFind(x, y-1 , miro[x][y]+1)
        miroFind(x+1, y , miro[x][y]+1)
        miroFind(x, y+1 , miro[x][y]+1)





miroFind(x, y, miro[x][y])

print(miro[N-1][M-1])