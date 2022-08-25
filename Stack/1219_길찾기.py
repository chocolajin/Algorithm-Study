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




#code3
def dfs2(v,visited):
    visited[v] = 1
    if v == 99:
        return 1
    #현재 노드에서 갈 수 있는 경로 찾기
    for i in range(2):
        # -1을 경로 초기값으로 잡아놓았으니.. 다른값이면 경로가 존재함
        if path[i][v] != -1 and not visited[path[i][v]]:
            if dfs2(path[i][v],visited) == 1:
                return 1
    return 0

def dfs():
    start = 0
    visited = [0]*100
    stack = [start]
    visited[start] = 1
    #스택이 비어있지 않으면, 계속 해서 경로탐색을 수행하겠다
    while stack:
        #stack의 top이 현재 위치
        # current = stack[-1]
        current = stack.pop()
        if current == 99: # 목적지에 도착할 수 있음!
            return 1
        #현재위치에서 갈수 있는 경로를 찾아주면 됩니다
        for i in range(2):
            # -1을 경로 초기값으로 잡아놓았으니.. 다른값이면 경로가 존재함
            if path[i][current] != -1 and not visited[path[i][current]]:
                #방문하기
                stack.append(path[i][current])
                visited[path[i][current]] = 1
                # break
        # else:
        #         #     stack.pop()
    # while 전체 종료 >> 탐색 종료 >> return이 안됨! >> 99번에 가는 경로를 찾지 못함
    return 0


T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    path = [[-1]*100 for _ in range(2)]
    # E*2의 길이를 가지는 data
    data = list(map(int,input().split()))
    visited = [0] * 100
    for i in range(0,E*2,2):
         # data[i]출발점, data[i+1] 도착점
        if path[0][data[i]] == -1:
            path[0][data[i]] = data[i+1]
        else:
            path[1][data[i]] = data[i + 1]

    #경로 탐색(dfs)
    # result = dfs()
    result = dfs2(0,visited)
    print(f'#{tc} {result}')
