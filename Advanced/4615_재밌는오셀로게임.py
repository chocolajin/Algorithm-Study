#code1
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 'W'
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 'B'

    for i in range(M):
        r, c, color = map(int, input().split())
        r -= 1
        c -= 1
        if color == 1:
            colora = 'B'
            colorb = 'W'
        else:
            colora = 'W'
            colorb = 'B'

        board[r][c] = colora

        for d in range(8):
            if 0 <= r + dr[d] < N and 0 <= c + dc[d] < N and board[r + dr[d]][c + dc[d]] == colorb:
                nr = r + dr[d]
                nc = c + dc[d]

                reverse = []
                while True:
                    if nr + dr[d] < 0 or nr + dr[d] > N - 1 or nc + dc[d] < 0 or nc + dc[d] > N - 1:
                        reverse = []
                        break
                    if board[nr + dr[d]][nc + dc[d]] == 0:
                        reverse = []
                        break
                    elif board[nr + dr[d]][nc + dc[d]] == colora:
                        reverse.append([nr, nc])
                        break

                    elif board[nr + dr[d]][nc + dc[d]] == colorb:
                        reverse.append([nr, nc])

                    nr += dr[d]
                    nc += dc[d]

                for x, y in reverse:
                    board[x][y] = colora

            else:
                continue
    cntB = 0
    cntW = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'B':
                cntB += 1
            elif board[i][j] == 'W':
                cntW += 1
    print(f'#{tc} {cntB} {cntW}')






#code2
# 보드는 4*4, 6*6, 8*8

# 첫 줄에 테스트 케이스 T
T = int(input())
for tc in range(1,T+1):
    # 한변의 길이 N, 플레이어가 돌을 놓는 횟수 M
    N, M = map(int,input().split())
    # M줄에는 돌을 놓을 위치와 돌의 색
    # 1이면 흑, 2이면 백
    board = [[0] * (N+1) for _ in range(N+1)]
    board[N // 2 - 1][N // 2 - 1], board[N // 2][N // 2] = 2, 2
    board[N // 2 - 1][N // 2], board[N // 2][N // 2 - 1] = 1, 1
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]
    move = 0
    for i in range(M):
        r, c, player = map(int, input().split())
        board[r][c] = player
        x, y = r, c
        for j in range(8):
            move = j
            nr = r + dr[move]
            nc = c + dc[move]
            while 0<= r < N+1 and 0<= c < N+1 and board[nr][nc] != 0:
                if board[nr][nc] != board[r][c]:
                    while True:
                        nr = r + dr[move]
                        nc = c + dc[move]
                        r, c = nr, nc
                else:
                    while r != x and c != y:
                        r -= move
                        c -= move
                        board[nr][nc] = player
                if r == x and c == y:
                    break

    print(board)