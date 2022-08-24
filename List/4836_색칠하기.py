T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = [[0] * 10 for _ in range(10)]

    case = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):

        r1, c1, r2, c2, color = case[i]

        if color == 1:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    elif arr[i][j] == 2:
                        arr[i][j] = 3

        else:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if arr[i][j] == 0:
                        arr[i][j] = 2
                    elif arr[i][j] == 1:
                        arr[i][j] = 3

    sumV = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] >= 3:
                sumV += 1

    print(f'#{tc} {sumV}')