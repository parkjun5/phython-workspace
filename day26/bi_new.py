# N = 26

# d = [0] * 30001

# for i in range(2, N+1):
#     d[i] = d[i-1] +1
#     if i%2 ==0:
#         d[i] = min(d[i] , d[i//2] +1)
#     if i%3 ==0:
#         d[i] = min(d[i] , d[i//3] +1)
#     if i%5 ==0:
#         d[i] = min(d[i] , d[i//5] +1)

# print(d[N])



# a = [1, 2,3, 4,5,6]

# print(a[-2-1-1])


N = 5
number =12
answer = -1
dp = []

for i in range (1,9) : 
# i = N의 개수
    #set 은 중복을 허락하지 않는다.
    set_arr = set()
    # 만들어준다.
    check_number = int(str(N)* i)
    # {N}, {NN} , {NNN}...
    #셋은 에드를 사용
    set_arr.add(check_number)
    
    for j in range(0,i-1):
    ##j 개를 사용해서 만든 값들
        for op1 in dp[j]:
            for op2 in dp[-j-1] :
                set_arr.add(op1 - op2)
                set_arr.add(op1 + op2)
                set_arr.add(op1 * op2)
                if op2 != 0:
                    set_arr.add(op1 // op2)
                    
    # if number in set_arr:
    #     answer = i
    #     break
    print(set_arr)
    dp.append(set_arr) 


    answer = -1

def DFS(n, pos, num, number, s):
    global answer
    if pos > 8:
        return
    if num == number:
        if pos < answer or answer == -1:
            #print(s)            
            answer=pos
        return

    nn=0
    for i in range(8):
        nn=nn*10+n
        DFS(n, pos+1+i, num+nn, number, s+'+')
        DFS(n, pos+1+i, num-nn, number, s+'-')
        DFS(n, pos+1+i, num*nn, number, s+'*')
        DFS(n, pos+1+i, num/nn, number, s+'/')

def solution(N, number):    
    DFS(N, 0, 0, number, '')    
    return answer
