T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    minN = 10000*M
    maxN = 0
    for i in range(N-M+1):
        cnt = 0

        for j in range(M):
            cnt += ai[i+j]

        if maxN < cnt:
            maxN = cnt
        if minN > cnt:
            minN = cnt

    result = maxN - minN
    print(f'#{tc} {result}')