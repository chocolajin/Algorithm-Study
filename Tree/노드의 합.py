import sys
sys.stdin = open('input.txt', 'r')

# code1
def solve(v):
    if v <=N:
        if tree[v]:
            return tree[v]
        return solve(v*2) + solve(v*2+1)
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        n,v = map(int, input().split())
        tree[n] = v
    result = solve(L)

    print(f'#{tc} {result}')

# code2
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N + 1)]
    for i in range(M):
        data = list(map(int, input().split()))
        tree[data[0]] = data[1]

    for i in range(N, 0, -1):
        if i // 2 > 0:
            tree[i // 2] += tree[i]

    print(f'#{tc} {tree[L]}')