#code1

def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    parent = [x for x in range(0, N + 1)]
    for i in range(M):
        x = data[i*2]
        y = data[i*2+1]
        union(x, y)

    for j in range(1, N+1):
        parent[j] = find_set(j)
    result = len(set(parent))-1

    print(f'#{tc} {result}')








#code2

def DFS(start):
    visited[start] = True  # 이미 탐색을 시작했으므로 visited에 표기

    for i in group[start]:  # 각 그룹의 인물마다 속한 그룹을 탐색
        if not visited[i]:
            DFS(i)

##############################################################################
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    form = list(map(int, input().split()))  # 신청서
    group = [[i] for i in range(N + 1)]  # 그룹 만들기, 이때, 한 사람만 있어도 그룹이므로 모두 한자리씩 넣어준다
    visited = [False] * (N + 1)  # 탐색했는지 검사하기 위한 배열
    cnt = 0  # 그룹 수

    for i in range(0, M * 2, 2):  # 신청서에 맞게 그룹에 해당 인물들을 넣는다.
        group[form[i]].append(form[i + 1])
        group[form[i + 1]].append(form[i])  # 이때, '수업에서 같은 조에 참여하고 싶은 사람끼리' 제출해서 양방향 그래프로 만든다

    for i in range(1, N + 1):  # 그룹 하나씩 검사하는 반복문
        if not visited[i]:  # 만일 방문하지 않은 그룹이라면
            cnt += 1  # 수를 추가해주고
            DFS(i)  # 탐색한다

    print(f'#{tc} {cnt}')