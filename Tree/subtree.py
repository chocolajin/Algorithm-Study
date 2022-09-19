import sys
sys.stdin = open('input.txt', 'r')

# code1
def f(n):
    global cnt
    if n:
        cnt += 1
        f(chi1[n])
        f(chi2[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E+1
    data = list(map(int, input().split()))
    chi1 = [0]*(V+1)
    chi2 = [0]*(V+1)
    par = [0]*(V+1)
    for i in range(E):
        if chi1[data[2*i]] == 0:
            chi1[data[2*i]] = data[2*i+1]
        else:
            chi2[data[2 * i]] = data[2 * i + 1]
    cnt = 0
    f(N)
    print(f'#{tc} {cnt}')


#code2
def solve(v):
    #dfs 순회
    stack = [v]
    cnt = 0
    while stack:
        current = stack.pop()
        cnt += 1
        # 현재노드로부터 갈 수 있는 노드를 모두  스택에 푸쉬
        for i in range(2):
            if children[i][current]:
                stack.append(children[i][current])
    return cnt
#code3
def traversal(v):
    if v == 0:
        return 0
    else:
        return traversal(children[0][v]) + traversal(children[1][v]) + 1

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    children = [[0] * (E+2) for _ in range(2)]
    for i in range(E):
        if children[0][data[i*2]]:
            children[1][data[i * 2]] = data[i*2+1]
        else:
            children[0][data[i * 2]] = data[i*2+1]
    # code2
    result = solve(N)
    print(f'#{tc} {result}')
    # code3
    answer = traversal(N)
    print(f'#{tc} {answer}')

