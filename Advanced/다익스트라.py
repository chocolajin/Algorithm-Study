# 각 노드로 가기위한 최단경로 (최소비용) 구하기
'''
5 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''

V, E = map(int,input().split())
adj = [[0xffffff]*(V+1) for _ in range(V+1)]
for i in range(E):
    s, e, weight = map(int,input().split())
    adj[s][e] = weight

def dijkstra(start):
    # 노드들을 하나씩 선택하면서 갈 수 있는 경로가 있고
    # 비용이 더 싸면 업데이트
    # start 에서 각 노드로 가는 비용
    distance = adj[start][:]
    # 이미 선택한 정점을 표시하기위한 집합
    visited = [0]*(V+1)
    visited[start] = 1
    distance[start] = 0

    while sum(visited) <= V:
        min_idx = 0
        min_val = 0xffffffff
        for i in range(V+1):
            if not visited[i] and distance[i] < min_val:
                min_idx = i
                min_val = distance[i]
        # 최소비용을 가지는 노드를 안다
        visited[min_idx] = 1
        # 방금 선택된 노드를 거쳐서 갈 수 있는 노드들의 방문비용 확인
        for i in range(V+1):
            if not visited[i] and distance[i] > min_val + adj[min_idx][i]:
                distance[i] = min_val + adj[min_idx][i]
    return distance
result = dijkstra(0)
print(result)

