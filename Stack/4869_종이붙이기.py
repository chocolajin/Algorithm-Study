#code1

def fibo_dp(n):
    table[1] = 1
    table[2] = 3
    for i in range(3, n+1):
        table[i] = table[i-1] + table[i-2]*2
    return
table = [0]*31
fibo_dp(30)

T = int(input())
for tc in range(1,T+1):
    N= int(input())//10
    print(f'#{tc} {table[N]}')



#code2

def paper(n):
    if n >= 3 and len(memo) <= n:
        memo.append(paper(n-1)+paper(n-2)*2)
    return memo[n]
memo = [0,1,3]

T = int(input())
for tc in range(1, T+1):
    N = int(input())//10

    print(f'#{tc} {paper(N)}')