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
V, E = map(int,input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    s, e, weight = map(int,input().split())
    adj[s][e] = weight
    adj[e][s] = weight

# 프림시작
# 각 노드로 갈 수 있는 비용을 저장하는 배열
weights = [0xffffff] * (V+1)
weights[0] = 0
mst = set()
mst_V = 0

while len(mst) <= V:
    minV = 0xffffff
    min_idx = 0
    for i in range(V+1):
        if i not in mst and weights[i] < minV:
            min_idx = i
            minV = weights[i]
    # 반복문을 다 돌고 나면 최소비용으로 갈 수 있는 노드가 선택됨
    # 선택된 노드를 mst에 추가하고
    # 그 노드로 주터 다른 노드로 갈 수 있는 비요을 확인하고
    # 기존비용보다 적다면 업데이트

    mst.add(min_idx)
    mst_V += minV

    for i in range(V+1):
        if i not in mst and adj[min_idx][i] and adj[min_idx][i] < weights[i]:
            weights[i] =adj[min_idx][i]

print(mst_V)