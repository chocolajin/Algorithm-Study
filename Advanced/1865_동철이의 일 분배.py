#code1

def solve(idx, mulV):
    global maxV
    if mulV == 0:
        return
    if mulV < maxV:
        return
    if idx == N:
        if maxV < mulV:
            maxV = mulV
        return

    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            solve(idx + 1, mulV * arr[idx][i])
            check[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = data[i][j]/100
    maxV = 0
    check = [0] * N
    solve(0, 1)
    result = maxV*100
    print(f'#{tc} {result:.6f}')