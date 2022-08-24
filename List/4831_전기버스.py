T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    charge_stop = [0]*(N+1)
    for i in charge:
        charge_stop[i] += 1
    cnt = 0
    start = 0
    while True:
        end = start + K
        if end >= N:
            break
        for j in range(end, start, -1):
            if charge_stop[j] == 1:
                cnt += 1
                start = j
                break
        else:
            cnt = 0
            break
    print(f'#{tc} {cnt}')