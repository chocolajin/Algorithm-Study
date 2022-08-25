dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr,sc):

    queue = [(sr, sc, 0)]

    visited[sr][sc] = 1

    while queue:
        r, c, distance = queue.pop(0)
        if case[r][c] == 3:
            return distance-1
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0 <= nr < N and 0 <= nc < N and case[nr][nc] != 1 and not visited[nr][nc]:
                queue.append((nr, nc, distance + 1))
                visited[nr][nc] = 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    case = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if case[i][j] == 2:
                sr = i
                sc = j
                break

    print(f'#{tc} {bfs(sr, sc)}')
