# 간선의 가중치를 기준으로 정렬
# 가중치가 작은 간선 부터 선택
# 만약 사이클이 생기면(연결할려는 두 노드가 이미 같은 집합에 있으면) 선택하지 않겠다
'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# 리스트에 넣고 정렬하기
V, E = map(int,input().split())
graph = []
for i in range(E):
    s, e, weight = map(int,input().split())
    graph.append((s,e,weight))
# 가중치를 기준으로 정렬하기
graph = sorted(graph, key=lambda x:x[2])
# 작은것부터 하나하나 선택하기 간선은 V개 만큼

mst = set()
target = 0
parent = [x for x in range(0, V+1)]

def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent[find_set(y)] = find_set(x)

while len(mst) < V:
    # graph[target]을 선택할지말지
    # 노드 두 개가 하나의 집합에 포함되어있으면, 선택하면 사이클 생김
    # 노드 두 개가 하나의 집합에 포함되어있지 않으면 선택
    if find_set(graph[target][0]) != find_set(graph[target][1]):
        union(graph[target][0], graph[target][1])
        mst.add(graph[target])
    target += 1
print(mst)
