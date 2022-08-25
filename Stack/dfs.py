#code1
# dfs를 수행하기 위해서는 graph가 필요한데
# 우리가 그래프를 표시하는 방법이 2가지 방법이 있음
# 인접행렬, 인접 리스트
# graph : dfs를 수행할 그래프, S는 시작점
N = 7   #노드의 개수
def dfs(graph,S):
    # 시작점을 stack에 넣을거에요
    stack = []
    stack.append(S)
    print(S,end=' ')
    #[1,0,0,0,1,0,0,0,0]
    visited = [0]*N
    visited[S] = 1  # 방문표시
    # DFS 순서
    # 현재노드(stack 의 top)에서 갈 수 있는 경로 확인하고,
    # while len(stack) > 0:
    while stack:
        top = stack[-1]
        # 경로가 있으면, 바로 이동,
        for i in range(N):
            if graph[top][i] == 1 and not visited[i]:
                stack.append(i) #갈수 있는 경로 찾음
                print(i, end=' ')
                visited[i] = 1
                break   #탐색종료
        # break 문이 한번도 실행 안되었을때, >>> 현재 위치에서 인접한 노드를 못찾음
        else:
            #현재 노드는 틀려먹었다... 길이없으니까..삭제
            # 없으면, 왔던 방향으로 되돌아간다.
            stack.pop()

V, E = map(int, input().split())
N = V + 1
adj = [[0]*N for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

dfs(adj,0)






#code2
def dfs(v):
    print(v)    #  v 방문
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:     # 방문하지 않은 w
            dfs(w)

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N   # visited 생성
dfs(0)
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

# adjList = [[1, 2],      # 0
#            [0, 3, 4],   # 1
#            [0, 4],      # 2
#            [1, 5],      # 3
#            [1, 2, 5],   # 4
#            [3, 4, 6],   # 5
#            [5]]         # 6





#code3
# A~G -> 0~6
# adjList = [[1, 2],      # 0
#            [0, 3, 4],   # 1
#            [0, 4],      # 2
#            [1, 5],      # 3
#            [1, 2, 5],   # 4
#            [3, 4, 6],   # 5
#            [5]]         # 6

def dfs(v, N):

    top = -1
    print(v)            # 방문
    visited[v] = 1      # 시작점 방문 표시
    #나랑 인접한 모든 노드 다 탐색해보기
    while True:
        for w in adjList[v]:        # if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0:
                top += 1            #push(v);
                stack[top] = v
                v = w               # v  w;  (w에 방문)
                print(v)  # 방문
                visited[w] = 1      # visited[w] true;
                break
        else:                       # w가 없으면
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]          # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break               # while

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N   # visited 생성
stack = [0] * N     # stack 생성
dfs(1, N)
print()




#code4
# 1. 시작점을 stack에 넣어줌
# 2. stack의 top에 있는 정점에서 인접한 노드 중, 방문하지 않은 노드 찾기
# 3.
#   3-1 : 2에 해당하는 노드를 찾았다면 방문(stack에 push)처리 후 2번 중단
#   3-2 : 2해당하는 노드를 못찾았다(경로를 못찾음)(stack pop)
# 4. 2번으로 돌아가서 반복( stack이 비어있지 않으면 계속 반복)

def dfs(graph):
    start = 0
    stack = []
    stack.append(start)
    #시작점으로 부터 dfs 수행 하기 위해서 시작점을 stack에 넣음
    #방문했던 노드는 다시 방문하지 않음!
    # 노드를 방문했음을 표시하는 배열 0 : 미방문, 1: 방문
    visited = [0] * (V+1)
    visited[start] = 1  #시작점 방문표시
    # 현재 노드에 인접하면서 방문하지 않은 노드 찾고, stack에 push
    # 경로없으면 stack에서 pop 
    # 위 과정을 stack이 비어있지 않으면 계속반복
    # python 에서 배열(stack) >> 참거짓으로 바꾸면...
    # 비어있으면 False 요소가 있으면 True
    while stack:    #요소가 있으면 계속 반복해라
        top = stack[-1] # python에서 -1 인덱스는 마지막 요소
        # top = stack.pop()  # python에서 -1 인덱스는 마지막 요소
        print(top,end=' ')
        for i in range(N):  #모든 노드 탐색
            if graph[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                break   #경로찾기 중단
        else: # break가 한번도 수행안됨(경로 찾지 못함)
            stack.pop()




#마지막 정점번호 6 V, 간선수 8 E
# 6 8
# 0 1
# 0 2
# 1 3
# 1 4
# 2 4
# 3 5
# 4 5
# 5 6
V, E = map(int, input().split())
N = V+1
graph = [ [0] * (N) for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for row in graph:
    print(row)
dfs(graph)





#code5
# 현재노드에서 방문할 수 있는 경로가 있으면 즉시 방문한다!
# v : 현재노드
def dfs(v):
    visited[v] = 1
    print(v,end=' ')
    for i in range(N):
        if graph[v][i] and not visited[i]:
            dfs(i)


#마지막 정점번호 6 V, 간선수 8 E
# 6 8
# 0 1
# 0 2
# 1 3
# 1 4
# 2 4
# 3 5
# 4 5
# 5 6
V, E = map(int, input().split())
N = V+1
graph = [ [0] * (N) for _ in range(N)]
visited = [0] * N
for _ in range(E):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(0)