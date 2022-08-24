dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    case = [list(map(int,input())) for _ in range(N)]
    stack = []
    x, y = 0, 0
    result = 0
    for i in range(N):
        for j in range(N):

            if case[i][j] == 2:
                x = i
                y = j
                break
    stack.append((x, y))

    while stack:
        x,y = stack.pop()
        case[x][y] = 1
        for k in range(4):
            nx = x+dr[k]
            ny = y+dc[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if case[nx][ny] == 0:
                stack.append((nx, ny))

            if case[x+dr[k]][y+dc[k]] == 3:
                result = 1
                break
        else:
            continue

    print(f'#{tc} {result}')