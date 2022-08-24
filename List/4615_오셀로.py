dr = [-1,-1,-1,0,1,1,1,0]
dc = [-1,0,1,1,1,0,-1,-1]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    board[N // 2-1][N // 2-1] = board[N // 2][N // 2] = 'W'
    board[N // 2-1][N // 2] = board[N // 2][N // 2-1] = 'B'

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
            if 0<= r+dr[d] < N and 0 <= c+dc[d]< N and board[r+dr[d]][c+dc[d]] == colorb:
                nr = r+dr[d]
                nc = c+dc[d]
                
                reverse = []
                while True:
                    if nr+dr[d] <0 or nr+dr[d] > N-1 or nc+dc[d] < 0 or nc+dc[d] > N-1 :
                        reverse =[]
                        break
                    if board[nr+dr[d]][nc+dc[d]] == 0:
                        reverse =[]
                        break
                    elif board[nr+dr[d]][nc+dc[d]] == colora:
                        reverse.append([nr,nc])
                        break

                    elif board[nr+dr[d]][nc+dc[d]] == colorb:
                        reverse.append([nr,nc])

                    nr += dr[d]
                    nc += dc[d]

                for x,y in reverse:
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
