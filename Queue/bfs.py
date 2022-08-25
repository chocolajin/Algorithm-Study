def bfs():
    #bfs는 재귀가 안됨!
    queue = [0]
    visited[0]=1
    # 노드에 방문해서,(방문하면 즉시 pop) 해당 노드에서 방문할 수 있는
    # 노드가 있으면 queue에 다 넣어주기
    # 큐가 비어있지 않으면 계속 반복
    while queue:
        front = queue.pop(0)
        print(front,end=' ')
        # if front == 목적지?:

        # 현재 노드에서 갈 수 있는 모든 경로 찾기
        for i in range(N):
            if adj[front][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = 1

V, E = map(int, input().split())
N = V + 1
adj = [[0]*N for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1
visited = [0] * N   # visited 생성
bfs()
#마지막 정점번호 6, 간선수 8
# 6 8
# 0 1
# 0 2
# 1 3
# 1 4
# 2 4
# 3 5
# 4 5
# 5 6