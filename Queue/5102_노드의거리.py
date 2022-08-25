def bfs(start,end, N):

    queue = []
    queue.append((start, 0))
    visited = [0] * N
    visited[start] = 1

    while queue:
        s, cnt = queue.pop(0)
        if s == end:
            return cnt
        for i in range(N):
            if graph[s][i] == 1 and not visited[i]:
                queue.append((i, cnt+1))
                visited[i] = 1
    return 0
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    N = V + 1
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int,input().split())
        graph[a][b] = 1
        graph[b][a] = 1
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S,G,N)}')