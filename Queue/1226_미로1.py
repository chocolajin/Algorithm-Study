dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


for tc in range(1, 11):
    T = int(input())
    N = 16
    case = [list(map(int, input().strip())) for _ in range(N)]
    stack = []
    x, y = 1, 1
    result = 0
    stack.append((x, y))

    while stack:
        x, y = stack.pop()
        case[x][y] = 1
        for k in range(4):
            nx = x+dr[k]
            ny = y+dc[k]

            if 0 <= nx < N and 0 <= ny < N and case[nx][ny] != 1:
                if case[nx][ny] == 0:
                    stack.append((nx, ny))

                if case[nx][ny] == 3:
                    result = 1
                    break

    print(f'#{tc} {result}')