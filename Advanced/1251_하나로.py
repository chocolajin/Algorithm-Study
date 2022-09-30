import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    island = [0]*N

    adj = [[0] * N for _ in range(N)]

    for i in range(N):
        island[i]=(X[i], Y[i])

    for n1 in range(N):
        for n2 in range(N):
            w = (abs(island[n1][0]-island[n2][0])**2+abs(island[n1][1]-island[n2][1])**2)*E
            adj[n1][n2] = w

    weights = [0xfffffffffffffff] * N
    weights[0] = 0
    mst = set()
    mst_V = 0

    while len(mst) < N:
        minV = 0xffffffffff
        min_idx = 0
        for i in range(N):
            if i not in mst and weights[i] < minV:
                min_idx = i
                minV = weights[i]

        mst.add(min_idx)
        mst_V += minV

        for i in range(N):
            if i not in mst and adj[min_idx][i] and adj[min_idx][i] < weights[i]:
                weights[i] = adj[min_idx][i]

    print(f'#{tc} {mst_V:.0f}')
