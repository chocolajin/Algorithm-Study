#code1
def dfs(start, end):
    stack = []
    stack.append(start)
    visited = [0]*100
    visited[start] = 1
    while stack:
        top = stack[-1]
        for i in range(100):
            if graph[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()
    return visited[end]


for tc in range(1, 11):
    T, N = map(int, input().split())
    graph = [[0]*100 for _ in range(100)]
    arr = list(map(int, input().split()))

    for j in range(0, len(arr), 2):
        a = arr[j]
        b = arr[j+1]
        graph[a][b] = 1
    if dfs(0, 99):
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')



#code2
def dfs():
    start = 0
    visited = [0]*100
    stack = [start]
    visited[start] = 1
    while stack: #스택이 비어있지 않으면 계속 경로 탐색
        #스택 탑 현재 위치
        current = stack[-1]
        if current == 99:
            return 1
        # 현재위치에서 갈수있는 경로 찾기
        for i in range(2):
            #-1이 초기값이니까 다른 값이면 경로있다.
            #비지티드에 방문안했으면 간다
            #비지티드에 노드번호 넣어주기

            if path[i][current] != -1 and not visited[path[i][current]]:
                stack.append(path[i][current])
                visited[path[i][current]] = 1
                break
        else:
            stack.pop()
    return 0


T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    path = [[-1] * 100 for _ in range(2)]
    data = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        if path[0][data[i]] == -1:
            path[0][data[i]] = data[i + 1]
        else:
            path[1][data[i]] = data[i + 1]

    result = dfs()
    print(f'#{tc} {result}')