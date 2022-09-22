#code1
def sol(x,y,v):
    global max_cnt
    global min_room
    dx = [0,0,-1,1]     # 상 하 좌 우
    dy = [-1,1,0,0]
    start_v = v         # 방번호를 start_v에 저장
    cnt = 1             # 갈 수 있는 방 계산을 위한 cnt
    while True:
        num = cnt       # while문 종료를 위해 cnt값을 num에 저장
        for i in range(4):
            # 4방향 모두 검사를 함
            # 범위를 넘지 않는지 파악함
            if N-1 >= y+dy[i] >= 0 and N-1 >= x+dx[i] >= 0:
                # 범위를 넘지 않고 v+1 값이 있다면
                if room_lst[y+dy[i]][x+dx[i]] == v+1:
                    cnt += 1        # cnt + 1
                    v += 1          # v 값을 v+1로 변화
                    y += dy[i]      # y 값을 y+dy[i]
                    x += dx[i]      # x 값을 x+dx[i]
                    break
        if num == cnt:                      # cnt와 num 값이 같다면 v+1값을 찾지 못해 cnt값이 올라간 것이 아님 -> 종료 조건 만족
            if cnt > max_cnt:               # cnt 값이 max_cnt보다 크다면
                max_cnt = cnt               # max_cnt를 cnt로 바꿔줌
                min_room = start_v          # min_room(방번호) 또한 start_v로 바꿔줌
            elif cnt == max_cnt:            # cnt와 max값이 같다면 방번호가 작은 값을 넣어주면 됨
                if min_room > start_v:      # min_room이 start_v보다 크다면
                    min_room = start_v      # min_room의 값을 start_v로 바꿔줌
            break                           # while문 탈출 후 sol 함수 종료


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room_lst = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0             # 이동할 수 있는 방의 갯수
    min_room = N**2+1       # 방 번호
    for i in range(N):
        for j in range(N):
            sol(j,i,room_lst[i][j])     # 모든 방을 다 검사함
                                        # 모든 방을 다 검사한 후 min_room이 방 번호
                                        # max_cnt가 이동할 수 잇는 방을 의미함
    print(f'#{tc} {min_room} {max_cnt}')






#code
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(sr, sc):
    stack = [(sr, sc)]
    distance = 0
    while stack:
        r, c = stack.pop()
        distance += 1
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0 <= nr < N and 0 <= nc < N and room[nr][nc] == (room[r][c])+1:
                stack.append((nr, nc))

    return distance


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_distance = 0
    start_room = 0
    for i in range(N):
        for j in range(N):
            if max_distance < dfs(i, j):
                max_distance = dfs(i, j)
                start_room = room[i][j]
            if max_distance == dfs(i, j):
                if start_room > room[i][j]:
                    start_room = room[i][j]

    print(f'#{tc} {start_room} {max_distance}')
