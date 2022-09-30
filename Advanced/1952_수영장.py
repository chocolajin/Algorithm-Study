import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    D, M, M3, Y = map(int, input().split())
    plan = list(map(int, input().split()))
    minV = Y
    sumV = 0
    cost = [0]*13
    cost[1] = plan[0]*D
    for i in range(1, 13):
        cost[i] = cost[i-1] + min(plan[i-1]*D, M)
        if i >= 3:
            if cost[i] > cost[i-3] + M3:
                cost[i] = cost[i-3] + M3

    if cost[-1] < minV:
        minV = cost[-1]

    print(f'#{tc} {minV}')
