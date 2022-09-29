#code1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w

    weights = [0xffffff] * (V + 1)
    weights[0] = 0
    mst = set()
    mst_V = 0

    while len(mst) <= V:
        minV = 0xffffff
        min_idx = 0
        for i in range(V + 1):
            if i not in mst and weights[i] < minV:
                min_idx = i
                minV = weights[i]

        mst.add(min_idx)
        mst_V += minV

        for i in range(V + 1):
            if i not in mst and adj[min_idx][i] and adj[min_idx][i] < weights[i]:
                weights[i] = adj[min_idx][i]

    print(f'#{tc} {mst_V}')
