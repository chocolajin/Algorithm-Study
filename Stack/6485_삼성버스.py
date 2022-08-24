T = int(input())
for tc in range(1, T+1):
    N = int(input())
    AB = [list(map(int, input().split())) for i in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]

    stop = [0]*5001

    for i in range(N):
        for j in range(AB[i][0], AB[i][1]+1):
            stop[j] += 1
    print(f'#{tc}', end=' ')
    for i in range(P):
        print(stop[C[i]], end=' ')

    print()