def dfs(start,end):
    stack = []
    stack.append(start)
    visited = [0]*(V+1)
    visited[start] = 1
    while stack:
        top = stack[-1]
        for i in range(V+1):
            if graph[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()
    return visited[end]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        a, b = map(int,input().split())
        graph[a][b] = 1

    S, G = map(int, input().split())
    if dfs(S, G):
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')