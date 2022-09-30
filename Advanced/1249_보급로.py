import sys
sys.stdin = open('input.txt', 'r')
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c):
    queue = []
    queue.append((r, c))
    visited = [[0xffffffffffff] *N for _ in range(N)]
    visited[r][c] = 0
    while queue:
        r, c = queue.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[r][c]+data[nr][nc] < visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[r][c]+data[nr][nc]
    return visited[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, list(input()))) for _ in range(N)]
    result = bfs(0, 0)
    print(f'#{tc} {result}')