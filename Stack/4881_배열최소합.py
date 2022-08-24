def back(i, s):
    global sumV
    if i == N:
        if s < sumV:
            sumV = s
    elif s > sumV:
        return
    else:
        for j in range(N):
            if not visit[j]:
                visit[j] = 1
                back(i+1, s+case[i][j])
                visit[j] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    case = [list(map(int,input().split())) for _ in range(N)]

    sumV = 1000
    visit = [0]*N
    back(0,0)
    print(f'#{tc} {sumV}')